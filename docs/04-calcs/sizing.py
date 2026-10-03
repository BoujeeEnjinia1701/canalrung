"""CanalRung sizing calculations (CNR-CAL-001).

Run from the repo root:  python docs/04-calcs/sizing.py
Every figure in docs/04-calcs/01-sizing.md is printed here with a tag in brackets ([A1], [B2] ...).
Geometry and part volumes come from cad/src/model.py; prices from bom/bom.csv; the value-engineering
target from project.yaml. First-principles estimates for a paper proof of concept, not a
certification of rescue equipment.
"""
import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "cad" / "src"))
import yaml  # noqa: E402
import model as M  # noqa: E402

P, D = M.PARAMS, M.derived()
G = 9.81
RHO_W = 1000.0          # kg/m3, fresh water
OUT = []


def out(tag, text, value=None):
    OUT.append((tag, text, value))
    print(f"[{tag}] {text}")


# ------------------------------------------------------------ assumptions
CLIMBER_KG = 100.0       # heavy adult, clothed and wet
DYN = 1.5                # dynamic factor for climbing and grabbing
RUNG_PROOF_N = 1500.0    # R4 rung target, point load at mid-span
SYSTEM_N = 4500.0        # R4 and R6 anchor target
FY_AL = 240.0            # MPa, 6061-T6 drawn tube, minimum yield
FY_POST = 235.0          # MPa, S235 hollow section
ROPE_MBS = 22.0          # kN, EN 1891 type A minimum
KNOT_EFF = 0.60          # overhand stopper knot, strength retained (literature range 0.55 to 0.65)
WET_EFF = 0.85           # wet polyamide; polyester retains more
EDGE_EFF = 0.50          # rope over a 10 mm coping edge without protection, worst case
EYE_WLL = 700.0          # kg, DIN 582 M16 in line with the thread
LINK_WLL = 1000.0        # kg, 10 mm screw link
V_FLOW = 2.0             # m/s, design surface current
CDA_PERSON = 0.35        # m2, adult holding a rung, broadside to the current
SOIL = dict(gamma=18.0, phi=30.0, gamma_sat=8.0)   # kN/m3, degrees; drained bank and saturated case

# ------------------------------------------------------------ A. reach and climbing geometry (R1, R5)
sin_a = math.sin(math.atan(1 / P["slope_h"]))
s = [P["rung1_s"] + (k - 1) * P["pitch"] for k in range(1, P["n_rungs"] + 1)]
out("A1", f"Rung section, rung 1 to rung {P['n_rungs']}: {D['span']:,.0f} mm at {P['pitch']:.0f} mm pitch; {P['n_rungs']} rungs")
out("A2", f"Design slope 1.5:1 (H:V) is {D['slope_deg']:.1f} deg; rung 1 lies {P['rung1_s']:.0f} mm down the wall from the coping")
depth_slope = [x * sin_a for x in s]
wet_slope = sum(1 for z in depth_slope if z >= P["water_drop"])
out("A3", f"1.5:1 slope, water {P['water_drop']:,.0f} mm below the coping: bottom rung {depth_slope[-1]:,.0f} mm below the coping "
          f"({depth_slope[-1] - P['water_drop']:.0f} mm below the water line); {wet_slope} rungs at or below the water line, "
          f"rung {P['n_rungs'] - wet_slope} {P['water_drop'] - depth_slope[-wet_slope - 1]:.0f} mm above it")
max_slope_drop = s[-2] * sin_a
out("A4", f"Deepest water on a 1.5:1 slope with two rungs still at or below the water line: {max_slope_drop:,.0f} mm below the coping")
wet_vert = sum(1 for z in s if z >= 3000.0)
out("A5", f"Vertical wall, water 3,000 mm below the coping: bottom rung {s[-1] - 3000:,.0f} mm below the water line; {wet_vert} rungs at or below it; "
          f"deepest water with two rungs at or below it: {s[-2]:,.0f} mm")
out("A6", f"Clear width between rope bushes {D['clear_w']:.0f} mm; rung pitch {P['pitch']:.0f} mm; "
          f"hand clearance behind the float sleeve at a stand-off rung {D['wall_to_foam']:.0f} mm")

# ------------------------------------------------------------ B. mass (R2)
m = M.masses()
rope_cut = M.rope_cut_length()
out("B1", f"Side rope cut length {rope_cut / 1000:.2f} m each ({2 * rope_cut / 1000:.2f} m in all) at {M.ROPE_KG_M * 1000:.0f} g/m")
for k_ in ("rungs", "foam", "bushes", "caps", "blocks", "sobolts", "ropes", "seizings", "links", "weight", "protectors"):
    out("B2", f"  {k_:11s} {m[k_]:.3f} kg")
out("B3", f"Ladder as thrown (everything that leaves the box): {m['total']:.2f} kg against the 4.0 kg target of R2 "
          f"({m['total'] - 4.0:+.2f} kg)")
alt = m["rungs"] * (math.pi * (25.4 ** 2 - (25.4 - 2 * 1.65) ** 2) / 4) / (math.pi * (P['rung_od'] ** 2 - (P['rung_od'] - 2 * P['rung_wall']) ** 2) / 4)
out("B4", f"Saving with 25.4 x 1.65 mm rungs instead: {m['rungs'] - alt:.2f} kg (rejected: see D2)")

# ------------------------------------------------------------ C. buoyancy (R3)
L = M.ladder_local(P, hang=False)
n = P["n_rungs"]
v_tube = L["rungs"].volume / n
m_tube = v_tube * M.DENSITY["al"]
v_foam_plain = math.pi / 4 * (P["foam_od"] ** 2 - P["rung_od"] ** 2) * P["foam_len"]
v_foam_so = math.pi / 4 * (P["foam_od"] ** 2 - P["rung_od"] ** 2) * P["foam_len_so"]
v_bush, v_cap = L["bushes"].volume / (2 * n), L["caps"].volume / (2 * n)
v_blk = L["blocks"].volume / 8
rope_share = (2 * (P["pitch"] + 100.0)) / 1000 * M.ROPE_KG_M          # kg of rope per rung, knots included
rope_sub = rope_share * (1 - 1 / 1.38)                                # polyester, the denser fibre


def net(v_foam, so):
    up = v_foam * 1e-6 * (1 - 33 / 1000)                              # foam lift less its own mass, kg
    down = (m_tube - v_tube * 1e-6) + 2 * (v_bush * M.DENSITY["nylon"] - v_bush * 1e-6) \
        + 2 * (v_cap * M.DENSITY["nylon"] - v_cap * 1e-6) + rope_sub
    if so:
        down += 2 * (v_blk * M.DENSITY["hdpe"] - v_blk * 1e-6) + 2 * (0.010 * (1 - 1 / 7.9))
    return up - down


nb_plain, nb_so = net(v_foam_plain, False), net(v_foam_so, True)
out("C1", f"Net buoyancy per rung with its share of rope: plain rung {nb_plain:.3f} kg, stand-off rung {nb_so:.3f} kg (target at least 0.15 kg)")
w_sub = P["weight_kg"] * (1 - 1 / 7.85) + 0.03 * 0.2
bottom3 = 2 * nb_plain + nb_so                                       # rungs 11 and 13 plain, 12 stand-off
out("C2", f"Throw weight in water {w_sub:.3f} kg; bottom three rungs lift {bottom3:.3f} kg, factor {bottom3 / w_sub:.2f} (target at least 1.5)")
out("C3", f"Whole ladder in water: {9 * nb_plain + 4 * nb_so - w_sub:.2f} kg of spare lift; it floats with the weight hanging below")

# ------------------------------------------------------------ D. rung strength (R4)
do, di = P["rung_od"], P["rung_od"] - 2 * P["rung_wall"]
Z = math.pi * (do ** 4 - di ** 4) / (32 * do)
span = P["rope_pitch"]
Mmax = RUNG_PROOF_N * span / 4
sig = Mmax / Z
out("D1", f"Rung tube {do} x {P['rung_wall']} mm 6061-T6: section modulus {Z:.0f} mm3; 1.5 kN at mid-span over {span:.0f} mm gives "
          f"{Mmax / 1000:.0f} N m and {sig:.0f} MPa, {sig / FY_AL:.2f} of the {FY_AL:.0f} MPa minimum yield (target at most 0.67)")
do2, di2 = 25.4, 25.4 - 3.3
Z2 = math.pi * (do2 ** 4 - di2 ** 4) / (32 * do2)
out("D2", f"Lighter 25.4 x 1.65 mm tube: {Mmax / Z2:.0f} MPa, {Mmax / Z2 / FY_AL:.2f} of yield (over the 0.67 limit, so not used)")
end_load = RUNG_PROOF_N / 2
bear = end_load / (P["flange_od"] * 2.0)
out("D3", f"Each rung end puts {end_load:.0f} N through the bush flange onto the knot; nylon flange bearing about {bear:.0f} MPa on a 2 mm contact band (nylon yields at about 50 MPa)")
mu, Nn = 0.3, CLIMBER_KG * G * DYN * math.cos(math.atan(1 / P['slope_h'])) / 2
T = mu * Nn * P["so_depth"] / 1000
Fb = T / (2 * D["ro"] / 1000)
out("D4", f"Stand-off block on a 1.5:1 slope: wall force {Nn:.0f} N per block (whole climber on one rung), friction torque {T:.1f} N m, "
          f"{Fb:.0f} N across the M5 bolt (two shear planes, capacity about 6 kN each)")

# ------------------------------------------------------------ E. ropes, knots and links (R4)
per_rope = ROPE_MBS * KNOT_EFF * WET_EFF
both = 2 * per_rope
out("E1", f"One side rope with a stopper knot, wet: {ROPE_MBS:.0f} x {KNOT_EFF} x {WET_EFF} = {per_rope:.1f} kN; both ropes {both:.1f} kN; "
          f"factor {both / (SYSTEM_N / 1000):.1f} on the 4.5 kN target (target at least 4)")
out("E2", f"Over an unprotected 10 mm coping edge as well: {both * EDGE_EFF:.1f} kN for both ropes; the edge protectors keep the rope off the edge")
out("E3", f"Screw links: working load limit {LINK_WLL:,.0f} kg = {LINK_WLL * G / 1000:.1f} kN, {LINK_WLL * G / SYSTEM_N:.2f} times the 4.5 kN target")

# ------------------------------------------------------------ F. loads in use
W = CLIMBER_KG * G * DYN
out("F1", f"Design climber {CLIMBER_KG:.0f} kg with a {DYN} dynamic factor: {W / 1000:.2f} kN")
along = W * sin_a
out("F2", f"On the 1.5:1 slope the ropes carry the part along the wall, {along / 1000:.2f} kN (friction on the wall ignored); "
          f"on a vertical wall the whole {W / 1000:.2f} kN")
drag = 0.5 * RHO_W * V_FLOW ** 2 * CDA_PERSON
rdrag = 3 * 0.5 * RHO_W * V_FLOW ** 2 * 1.2 * (P["foam_od"] / 1000) * (P["foam_len"] / 1000)
out("F3", f"Person holding a rung in a {V_FLOW} m/s current: drag {drag:.0f} N on the person and {rdrag:.0f} N on three rungs (Cd x A {CDA_PERSON} m2, rung Cd 1.2)")
worst = W + drag + rdrag + m["total"] * G
out("F4", f"Upper bound on the anchor (climbing a vertical wall and the full current drag together): {worst / 1000:.2f} kN, "
          f"{SYSTEM_N / worst:.2f} times inside the 4.5 kN target")

# ------------------------------------------------------------ G. anchor: eye nut, bolt, post and footing (R6)
out("G1", f"Eye nut M16 working load limit {EYE_WLL:.0f} kg in line = {EYE_WLL * G / 1000:.2f} kN, {EYE_WLL * G / SYSTEM_N:.2f} times the target")
As = 157.0
out("G2", f"M16 grade 8.8 bolt: proof load {As * 600 / 1000:.0f} kN; post wall under the 50 mm washer, punching capacity {math.pi * 50 * 3 * 0.6 * FY_POST / 1000:.0f} kN")
wp, tp = P["post_w"], P["post_t"]
Ipost = (wp ** 4 - (wp - 2 * tp) ** 4) / 12
Zpost = Ipost / (wp / 2)
Mpost = SYSTEM_N * P["eye_z"] / 1000
out("G3", f"Post 60 x 60 x 3: section modulus {Zpost:,.0f} mm3; 4.5 kN at {P['eye_z']:.0f} mm gives {Mpost:.0f} N m and "
          f"{Mpost * 1000 / Zpost:.0f} MPa, {Mpost * 1000 / Zpost / FY_POST:.2f} of yield")


def broms(gamma, Dm, Lm, e, phi):
    kp = math.tan(math.radians(45 + phi / 2)) ** 2
    return 0.5 * gamma * Dm * Lm ** 3 * kp / (e + Lm)


Df, Lf, e = P["footing_d"] / 1000, P["footing_depth"] / 1000, P["eye_z"] / 1000
Hu = broms(SOIL["gamma"], Df, Lf, e, SOIL["phi"])
out("G4", f"Footing {P['footing_d']:.0f} dia x {P['footing_depth']:,.0f} deep, short rigid pile (Broms), drained medium dense granular soil "
          f"(unit weight {SOIL['gamma']:.0f} kN/m3, 30 deg): ultimate {Hu:.1f} kN, factor {Hu / (SYSTEM_N / 1000):.2f} on the target (target at least 1.5)")
Hs = broms(SOIL["gamma_sat"], Df, Lf, e, SOIL["phi"])
Hs2 = broms(SOIL["gamma_sat"], 0.5, 1.2, e, SOIL["phi"])
out("G5", f"Same footing in saturated soil (submerged unit weight {SOIL['gamma_sat']:.0f} kN/m3): {Hs:.1f} kN, factor {Hs / 4.5:.2f}: not enough; "
          f"a 500 dia x 1,200 deep footing gives {Hs2:.1f} kN, factor {Hs2 / 4.5:.2f}")
vol = math.pi / 4 * Df ** 2 * Lf - (wp / 1000) ** 2 * P["post_embed"] / 1000
out("G6", f"Concrete in the standard footing {vol:.3f} m3, about {vol * 2300 / 25 + 0.5:.0f} bags of 25 kg")

# ------------------------------------------------------------ H. deployment, storage and safety (R7, R8, R10)
steps = [("lift the lid", 2), ("take the throw weight and the top of the folded ladder", 4),
         ("throw upstream of the person", 4), ("let the ladder pay out down the wall", 5)]
out("H1", "Deploy time estimate: " + "; ".join(f"{a} {b} s" for a, b in steps) + f"; total {sum(b for _, b in steps)} s (target under 30 s; to be timed)")
out("H2", "UV: ropes, rungs and foam live in an opaque UV-stabilised box and see daylight only when used or inspected")
out("H3", "Nothing hard is thrown: the throw weight is a soft shot pouch; rung ends are capped and holes bushed; a blunt-tip knife is kept in the lid")

# ------------------------------------------------------------ I. cost (R9)
pm = yaml.safe_load((ROOT / "project.yaml").read_text())
rows = list(csv.DictReader((ROOT / "bom/bom.csv").open()))
cost = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in rows)
station = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in rows if int(r["item"].split()[0]) <= 10 or int(r["item"].split()[0]) >= 22)
tgt = float(pm["budget_usd"])
out("I1", f"Value-engineering target: USD {tgt:,.0f}. Estimated cost of the constructable design: USD {cost:,.2f} "
          f"(USD {abs(cost - tgt):,.2f} {'over' if cost > tgt else 'under'} the target)")
out("I2", f"Station (post, footing, anchor, box, decals, knife, consumables) USD {station:,.2f}; ladder USD {cost - station:,.2f}")

# ------------------------------------------------------------ results table
print()
print("Requirement results (CNR-REQ-001)")
res = [
    ("R1", "met on paper", f"4,020 mm rung section; slopes to {max_slope_drop / 1000:.1f} m, vertical walls to {s[-2] / 1000:.1f} m"),
    ("R2", "not met (mass)", f"{m['total']:.2f} kg against 4.0 kg; throw accuracy needs trials"),
    ("R3", "met on paper", f"{nb_plain:.2f} and {nb_so:.2f} kg per rung; bottom three rungs {bottom3 / w_sub:.1f} x the weight"),
    ("R4", "met on paper", f"rung {sig / FY_AL:.2f} of yield; ropes {both:.1f} kN wet with knots"),
    ("R5", "met by design; climb time needs trials", f"{D['clear_w']:.0f} mm clear, {P['pitch']:.0f} mm pitch, {D['wall_to_foam']:.0f} mm hand room"),
    ("R6", "met on paper in drained soil", f"footing factor {Hu / 4.5:.2f}; eye nut {EYE_WLL * G / SYSTEM_N:.2f}"),
    ("R7", "not verifiable at TRL 3", f"estimate {sum(b for _, b in steps)} s"),
    ("R8", "met by design; to confirm by test", "stored in an opaque box"),
    ("R9", "over the value-engineering target", f"USD {cost:,.2f} against USD {tgt:,.0f}"),
    ("R10", "met by design", "soft weight, capped ends, knife"),
]
for r in res:
    print(f"  {r[0]:4s} {r[1]:40s} {r[2]}")
with (Path(__file__).parent / "results.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["tag", "text"])
    for t, x, _ in OUT:
        w.writerow([t, x])
