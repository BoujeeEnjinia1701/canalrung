#!/usr/bin/env python3
"""CanalRung STEM check (CNR-STM-001, STANDARDS section 20): first-order screen of every physical, chemical,
biological and mathematical claim, for option A (the current design) and the added options B and C.

Run from the repo root:  python docs/04-calcs/stem_check.py     (writes docs/04-calcs/stem_results.csv)

Every number is computed here from the model parameters (cad/src/model.py, cad/src/cnr_opts.py) and handbook
constants, independently of docs/04-calcs/sizing.py (the calculation note CNR-CAL-001), so the two can disagree and
show a mistake. A check is a screen; it never replaces the calculation note.
"""
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from stem_check import Check, limits, PLAUSIBLE  # noqa: E402
import model as M  # noqa: E402

P = M.PARAMS
G, RHO_W = 9.81, 1000.0
FY_AL, FY_STEEL = 240.0, 235.0           # MPa, 6061-T6 drawn tube minimum yield; S235
ALLOW = 2 / 3                            # share of yield allowed under the design load (CNR-REQ-001)
CLIMBER = 100.0 * G * 1.5                # N, 100 kg adult with a dynamic factor of 1.5
TARGET_N = 4500.0                        # N, anchor target
c = Check()


def tube_z(do, wall):
    di = do - 2 * wall
    return math.pi * (do ** 4 - di ** 4) / (32 * do)        # mm3


def rhs_z(b, h, t):
    return (b * h ** 3 - (b - 2 * t) * (h - 2 * t) ** 3) / (6 * h)      # mm3, about the axis across b


# ------------------------------------------------------------------ option A: thrown rope ladder on a bank post
span = P["rope_pitch"]
sig = CLIMBER * span / 4 / tube_z(P["rung_od"], P["rung_wall"])
c.claim("S1", "A: a 28.6 x 1.65 mm 6061-T6 rung carries the 1.47 kN climber load (100 kg x 1.5) at mid-span", "Physics", "Strength of materials",
        "Simply supported beam, M = F L / 4; hollow circular section modulus; 6061-T6 yield 240 MPa",
        round(sig, 1), FY_AL * ALLOW, "MPa", closed_by="CNR-CAL-001 D1")

foam_vol = math.pi / 4 * (P["foam_od"] ** 2 - P["rung_od"] ** 2) * P["foam_len"]          # mm3 of closed-cell foam
tube_vol = math.pi / 4 * (P["rung_od"] ** 2 - (P["rung_od"] - 2 * P["rung_wall"]) ** 2) * P["rung_len"]
lift = RHO_W * foam_vol * 1e-9 - 0.033e-6 * foam_vol - (2.7e-6 - RHO_W * 1e-9) * tube_vol
c.claim("S2", "A: each foam-sleeved rung floats with at least 0.15 kg of spare lift (before the rope share)", "Physics", "Fluid statics",
        "Archimedes: foam displaces water, bore floods through the rope holes, aluminium wall sinks",
        round(lift, 3), 0.15, "kg", rule="above", margin=0.0, closed_by="CNR-CAL-001 C1 (with the rope and fittings share)")

rope_n = 18.0 * 0.60 * 0.85 * 2
c.claim("S3", "A: two wet 9 mm EN 1891 type B ropes with stopper knots hold four times the 4.5 kN anchor target (equal sharing; after the 20 percent ageing allowance of R8 the figure is 14.7 kN, a factor of 3.3)", "Engineering and technology",
        "Rope and knots", "Catalogue minimum breaking strength 18 kN x knot efficiency 0.60 x wet 0.85 (to be proof-loaded)",
        round(rope_n, 2), 4 * TARGET_N / 1000, "kN", rule="above", margin=0.1, closed_by="CNR-CAL-001 E1")


def broms(gamma, D, L, e, phi=30.0):
    kp = math.tan(math.radians(45 + phi / 2)) ** 2
    return 0.5 * gamma * D * L ** 3 * kp / (e + L)            # kN, short rigid free-head pile in cohesionless soil


e = P["eye_z"] / 1000
hu_d = broms(18.0, P["footing_d"] / 1000, P["footing_depth"] / 1000, e)
hu_s = broms(8.0, P["footing_d"] / 1000, P["footing_depth"] / 1000, e)
c.cited("S4", "A: the 500 x 1,200 mm footing holds 1.5 x 4.5 kN in drained granular soil", "Physics", "Geotechnics",
        "Broms (1964) short rigid pile, cohesionless soil, free head: Hu = 0.5 g D L^3 Kp / (e + L); g 18 kN/m3, phi 30 deg",
        f"{hu_d:.1f} kN against 6.75 kN on level ground; the post is 1.0 m behind a 1.5:1 lined slope, so the passive wedge is cut and a slope-crest "
        "reduction applies that CNR-CAL-001 does not include (independent review, finding 1)", PLAUSIBLE)
c.cited("S5", "A: the same footing holds 1.5 x 4.5 kN in saturated soil", "Physics", "Geotechnics",
        "Broms (1964) with submerged unit weight 8 kN/m3",
        f"{hu_s:.1f} kN against 6.75 kN on level ground, only 7 percent over; the slope-crest reduction is not applied, so the margin may not exist "
        "(independent review, finding 1); site pull test", PLAUSIBLE)

drag = 0.5 * RHO_W * 0.35 * 2.0 ** 2
c.claim("S6", "A: a person holding on in a 2 m/s current, plus climbing, loads the anchor to less than 4.5 kN", "Physics", "Fluid mechanics",
        "Drag F = 0.5 rho Cd A v^2 (Cd A 0.35 m2) plus 1.47 kN climbing on a vertical wall", round((drag + CLIMBER) / 1000, 2),
        TARGET_N / 1000, "kN", closed_by="CNR-CAL-001 F3, F4")

run = math.hypot(P["water_drop"] * P["slope_h"], P["water_drop"]) - P["rung1_s"]          # slope length to the water, less the top offset along the slope
need = run + 1 * P["pitch"]
c.claim("S7", "A: the 4,020 mm rung section reaches the water on the 1.5:1 design slope with two rungs in it", "Mathematics", "Geometry",
        "Slope length to the water line from the coping, less the top offset, plus one more pitch", round(need),
        (P["n_rungs"] - 1) * P["pitch"], "mm", closed_by="CNR-CAL-001 A3")

m_throw, d_throw = 4.27, 3.0
v = math.sqrt(d_throw * G)                                   # 45 degree launch, level
ke = 0.5 * m_throw * v ** 2
c.claim("S8", "A: one adult throws the 4.27 kg ladder (as thrown) the 3 m to the water", "Physics", "Mechanics",
        "Projectile range v^2/g at 45 deg; kinetic energy 0.5 m v^2 against 300 W peak over 0.3 s (limits.HUMAN_PEAK_W)",
        round(ke, 1), limits.HUMAN_PEAK_W * 0.3, "J", margin=0.4)

c.claim("S9", "A: a nylon rope bush takes the full 1.47 kN of a foot at one rung end on a 2 mm contact band (CNR-CAL-001 uses 750 N per end)", "Engineering and technology", "Strength of materials",
        "Flange bearing stress, F over a 2 mm contact band (a quarter of the 22 mm flange ring), against water-saturated nylon (PA6) yield taken as 35 MPa (dry about 50 MPa; class values, datasheet to cite)",
        round(1470 / (0.25 * math.pi / 4 * (22 ** 2 - 16 ** 2)), 1), 35.0, "MPa", margin=0.1, closed_by="CNR-CAL-001 D3 (750 N per end); proof load at TRL 4")

c.cited("S10", "A: ropes, rungs and foam keep 80 percent of strength after 2 years of outdoor storage", "Chemistry", "Polymer ageing",
        "Polyester and polyamide lose strength under UV; the opaque UV-stabilised box limits exposure to use and inspection",
        "Consistent with the literature on UV ageing of rope; the retained strength is a test result, not a calculation",
        PLAUSIBLE)
c.cited("S11", "A: an aluminium mounting plate clamped on a galvanised steel post does not corrode through in 2 years", "Chemistry", "Corrosion",
        "Zinc and aluminium sit close together in the galvanic series in neutral water, so the couple is weak; the plate sits behind an HDPE box",
        "No calculation; plausible, to watch at TRL 4 (RSK failure mode F8)", PLAUSIBLE)
c.cited("S12", "A: a person in 5 to 30 C water can grip and climb a 335 mm rung pitch in under 60 s", "Biology", "Human physiology",
        "Cold-water immersion reduces grip strength and coordination within minutes; 6 rungs at about 5 s each is 30 s for a fit adult, much more for a child or a cold person",
        "A supervised tank trial is the only real check (TRL 4); no fix is possible on paper", PLAUSIBLE)

# ------------------------------------------------------------------ option B: coping-hook folding ladder
span_b = 375.0                                         # mm, bolt to bolt across the stiles
sig_first = CLIMBER * span_b / 4 / tube_z(25.4, 1.6)
sig_b = CLIMBER * span_b / 4 / tube_z(25.4, 3.2)
c.claim("S13", "B: a 25.4 x 3.2 mm 6061-T6 rung carries a 1.5 kN climber load at mid-span (the first design used a 1.6 mm wall: "
        f"{sig_first:.0f} MPa, {sig_first / FY_AL:.2f} of yield, a fail; fixed to 3.2 mm, same outside diameter)", "Physics",
        "Strength of materials", "Simply supported beam, M = F L / 4; hollow circular section; 6061-T6 yield 240 MPa",
        round(sig_b, 1), FY_AL * ALLOW, "MPa", closed_by="DEC fix under the 2026-10-23 instruction; not in CNR-CAL-001")

span_pad = 1.8                                          # m, between wall pads
w_n = CLIMBER * math.cos(math.atan(1 / P["slope_h"]))   # wall-normal part of the load, N
sig_s = w_n * span_pad / 4 / 2 * 1000 / rhs_z(25, 45, 2)
c.claim("S14", "B: each RHS 25 x 45 x 2 stile bridges 1.8 m between wall pads under a climber", "Physics", "Strength of materials",
        "Point load at mid-span, shared by two stiles, strong axis of the 45 mm depth", round(sig_s, 1), FY_AL * ALLOW, "MPa",
        closed_by="")
c.cited("S15", "B: the 10 mm lanyard holds the along-slope part of a climber (0.82 kN) with a factor of 4", "Engineering and technology", "Rope and knots",
        "A catalogue breaking strength for the 10 mm rope is not cited (to assess); if it matches the 9 mm rope of S3 (9.2 kN with knots, wet) the factor is 11",
        "Unknown until a datasheet is cited; the vertical-wall case (1.6 kN) is not checked", PLAUSIBLE)
bearing_mid = (CLIMBER * span_pad / 4 / 2) / 0.176 / (5.0 * 2.0)    # N/mm2: splice couple over 176 mm bolt spacing, 5 mm x 2 mm wall
bearing = 0.375 * bearing_mid                           # splice on the wall pad: continuous-beam support moment 3 P L / 32 against P L / 4
c.claim("S16", "B: the splice sleeve bolts pass the stile bending moment by bearing on a 2 mm wall (the first design put the splice at "
        f"mid-span: {bearing_mid:.0f} MPa, a fail; fixed by moving the splice onto the wall pad)", "Physics", "Strength of materials",
        "Support moment of a stile continuous over the pad 3 P L / 32; couple over two M5 bolts 176 mm apart; bearing area 5 mm x 2 mm wall; 6061-T6 yield 240 MPa",
        round(bearing, 1), FY_AL * ALLOW, "MPa", margin=0.25, closed_by="DEC fix under the 2026-10-23 instruction; not in CNR-CAL-001")
c.cited("S17", "B: one adult carries and lowers the 10.6 kg ladder over the coping", "Biology", "Human factors",
        "Mass against the 23 kg load constant of the NIOSH lifting equation (ideal case); lowering a 4.7 m ladder at arm's length over an edge counts for much less",
        "10.6 kg is under half of the load constant, but the cantilever when lowering is a lever of about 1 m", PLAUSIBLE)

# ------------------------------------------------------------------ option C: post winch with a floating rescue sling
theta = math.atan(1 / P["slope_h"])
T = 100 * G * (math.sin(theta) + 0.5 * math.cos(theta))     # N, hauling 100 kg up a wet 1.5:1 wall, friction 0.5
v_haul = 2 * math.pi * 0.034 / 5                            # m/s, one handle turn in 5 s on a 34 mm drum radius: 0.043 m/s
eff = 0.85                                                  # drum, sheave and bush losses (screening value)
power = T * v_haul / eff
t_haul = 4.2 / v_haul
c.claim("S18", f"C: one adult hand-cranks a 100 kg person up the wall at 0.043 m/s ({t_haul:.0f} s for 4.2 m; handle force about 150 N)", "Physics", "Mechanics",
        "Tension T = m g (sin a + mu cos a), mu 0.5 wet clothing on concrete; power T v / efficiency 0.85 against sustained human output (limits.HUMAN_SUSTAINED_W)",
        round(power, 1), limits.HUMAN_SUSTAINED_W, "W", margin=0.4, closed_by="")
Zb = (60 * 100 ** 3 - 52 * 92 ** 3) / (6 * 100)
fv = T * 1.182
sig_boom = fv * 1430 / Zb
c.claim("S19", "C: the RHS 100 x 60 x 4 boom carries the sheave reaction 1.43 m from the post", "Physics", "Strength of materials",
        "Sheave resultant T x |sum of the two rope directions| = 1.2 T; moment on the boom root; S235", round(sig_boom, 1), FY_STEEL * ALLOW, "MPa",
        closed_by="")
Zp = (100 ** 4 - 92 ** 4) / (6 * 100)
m_post = fv * 1.43 + 0.277 * T * 1.9
mu_ground = 0.5 * 18.0 * 0.6 * 1.2 ** 3 * math.tan(math.radians(60)) ** 2 * 1000      # N m, rigid pile moment limit (e large)
c.claim("S20", "C: the 600 x 1,200 mm footing resists the overturning moment of the boom", "Physics", "Geotechnics",
        "Broms limit moment 0.5 g D L^3 Kp at a large load height, against 1.5 x the moment at ground level (g 18 kN/m3, phi 30 deg)",
        round(1.5 * m_post), round(mu_ground), "N m", closed_by="")
v_collar = 2 * math.pi ** 2 * 270 * 55 ** 2 * 1e-6          # litres
c.claim("S21", "C: the float collar (torus of 270 mm major radius and 55 mm minor radius) displaces enough water to support a clothed adult; head-up stability is not checked", "Physics", "Fluid statics",
        "Torus volume 2 pi^2 R r^2 displaces water; an adult's negative buoyancy is taken as 5 kg (screening value, to be confirmed)",
        round(v_collar, 1), 5.0 * 2, "kg", rule="above", closed_by="")
c.cited("S22", "C: the 8 mm rescue rope holds the 1.0 kN haul with a factor of 5", "Engineering and technology", "Rope and knots",
        "A catalogue minimum breaking strength for 8 mm low-stretch kernmantle rope is not yet cited (to assess); 8 mm is below the 9 mm that CNR-DDR-003 judged the minimum for A",
        "Unknown until a datasheet is cited", PLAUSIBLE)

c.cited("S23", "A: the forged M16 eye nut holds the 4.5 kN with a factor of 1.5 at the real pull angle", "Engineering and technology", "Strength of materials",
        "DIN 582 class working load limit 700 kg applies in line with the thread; the rope pulls the eye 14 to 34 degrees off the bolt axis down the slope and across the canal, where a rating is lower (value to cite)",
        "In line the factor is 1.53; off axis it is not shown (independent review, finding 6); fix proposed to Amish (CNR-DEC-001)", PLAUSIBLE)

if __name__ == "__main__":
    state = c.write()
    sys.exit(1 if state == "fail" else 0)
