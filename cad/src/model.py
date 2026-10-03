"""CanalRung parametric model (build123d), TRL 3, constructable design (CNR-DDR-002).

Run from the repo root:
    python cad/src/model.py            build, print part masses, export STEP and STL
    python cad/src/model.py --check    constructability checks only (touch, clear, no overlap)

The model has two parts:
  * the bank station: a galvanised steel post set in a concrete footing, a forged eye nut on an
    M16 through bolt (with a crush tube inside the post) as the ladder anchor, an aluminium
    mounting plate and two square U-bolts that clamp a bought storage box to the post, a post
    cap, decals and a rescue knife;
  * the ladder: 13 aluminium tube rungs at 335 mm pitch with closed-cell foam float sleeves,
    nylon rope bushes and plastic end caps, HDPE wall stand-off blocks on rungs 3, 6, 9 and 12,
    two 10.5 mm low-stretch kernmantle side ropes with an overhand stopper knot under every
    rung end and a seizing above it, screw links at the top and bottom, a soft throw weight
    and two edge protector sleeves.

World axes (deployed scene): the canal runs along Y. X is across the canal: the bank is X >= 0,
the coping edge is the line X = 0, Z = 0, and the lined wall falls toward -X at 1.5:1 (H:V).
Z is up; the bank top is Z = 0. The ladder lies down the wall on its stand-offs.

Ladder axes (local, used for making and for the hanging assembly): X along the rungs, Z up the
ladder (rung 1, the top rung, on Z = 0), Y toward the wall. CONCEPT, NOT FOR FABRICATION until
the TRL 4 proof loads are done.
"""
from __future__ import annotations

import math
import sys
from dataclasses import dataclass, field
from pathlib import Path

from build123d import (Axis, Box, Compound, Cylinder, Location, Plane, Polygon, Pos, Rot, Sphere,
                       Torus, Vector, export_step, export_stl, extrude)

ROOT = Path(__file__).resolve().parents[2]

PARAMS = dict(
    # ladder
    n_rungs=13, pitch=335.0, rope_pitch=320.0,          # rope centre to rope centre across the ladder
    rung_len=360.0, rung_od=28.6, rung_wall=1.65,       # 6061-T6, 1-1/8 in x 0.065 in
    bush_id=12.0, bush_od=16.0, bush_len=29.0, flange_od=22.0, flange_t=2.0,
    rope_d=10.5, knot_r=13.0, seize_len=20.0, seize_t=1.5,
    foam_od=50.0, foam_len=294.0, foam_len_so=260.0,
    so_rungs=(3, 6, 9, 12), so_t=16.0, so_back=20.0, so_depth=95.0, so_h=40.0, so_nose_h=24.0, so_bolt_x=140.0,
    cap_head=2.0, cap_shank=10.0,
    tail=280.0,                                          # bottom rung axis to the bottom screw link
    weight_d=70.0, weight_len=140.0, weight_kg=0.5,
    link_major=20.0, link_wire=5.0,
    # site and station
    slope_h=1.5, water_drop=2000.0, water_depth=1000.0, rung1_s=150.0,
    post_x=1000.0, post_w=60.0, post_t=3.0, post_len=2100.0, post_embed=900.0,
    footing_d=400.0, footing_depth=1000.0,
    eye_z=250.0, bolt_d=16.0, bolt_len=90.0, crush_od=21.3, crush_t=2.0,
    plate=(4.0, 400.0, 300.0), plate_z0=480.0,
    ubolt_d=8.0, ubolt_z=(560.0, 720.0), ubolt_leg=84.0,
    box=(450.0, 650.0, 360.0), box_t=4.0, box_z0=450.0, lid_t=12.0, notch=(30.0, 25.0),
)

DENSITY = {"al": 2.70e-6, "steel": 7.85e-6, "hdpe": 0.95e-6, "nylon": 1.14e-6, "xlpe": 0.033e-6,
           "pp": 0.91e-6, "concrete": 2.3e-6}   # kg per mm3
ROPE_KG_M = 0.068      # 10.5 mm EN 1891 type A kernmantle, typical catalogue mass per metre

# BOM line numbers follow the build order (bom/bom.csv)
BOM = {
    "post": (1, "Post, galvanised steel 60 x 60 x 3 SHS, 2,100 long"),
    "footing": (2, "Concrete footing, 400 dia x 1,000 deep"),
    "crush": (3, "Crush tube, steel 21.3 x 2.0, 57 long"),
    "bolt": (4, "Anchor bolt M16 x 90, grade 8.8, washers"),
    "eyenut": (5, "Forged eye nut M16 (ladder anchor)"),
    "plate": (6, "Box mounting plate, aluminium 4 mm"),
    "ubolts": (7, "Square U-bolts M8 for 60 mm tube (2)"),
    "box": (8, "Storage box, 70 L, drilled, with lid"),
    "boxfix": (9, "Box fixings: fender washers and nyloc nuts"),
    "cap": (10, "Post cap"),
    "decals": (11, "Decals and tamper tag"),
    "knife": (12, "Rescue knife in a sheath"),
    "rungs": (13, "Rungs, aluminium tube 28.6 x 1.65 (13)"),
    "foam": (14, "Float sleeves, closed-cell foam (13)"),
    "blocks": (15, "Wall stand-off blocks, HDPE (8)"),
    "sobolts": (16, "Stand-off bolts M5 x 50 (8)"),
    "bushes": (17, "Rope bushes, nylon, flanged (26)"),
    "caps": (18, "Rung end caps (26)"),
    "ropes": (19, "Side ropes, 10.5 mm kernmantle, with knots (2)"),
    "seizings": (20, "Seizings above each rung end (26)"),
    "links": (21, "Screw links, 10 mm (2)"),
    "weight": (22, "Soft throw weight, 0.5 kg"),
    "protectors": (23, "Edge protector sleeves (2)"),
}


# ------------------------------------------------------------------ helpers
def box(x0, x1, y0, y1, z0, z1):
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def cyl_x(x0, x1, r, y=0.0, z=0.0):
    return Pos((x0 + x1) / 2, y, z) * Rot(0, 90, 0) * Cylinder(r, abs(x1 - x0))


def cyl_y(y0, y1, r, x=0.0, z=0.0):
    return Pos(x, (y0 + y1) / 2, z) * Rot(90, 0, 0) * Cylinder(r, abs(y1 - y0))


def cyl_z(z0, z1, r, x=0.0, y=0.0):
    return Pos(x, y, (z0 + z1) / 2) * Cylinder(r, abs(z1 - z0))


def cyl_between(p0, p1, r):
    a, b = Vector(*p0), Vector(*p1)
    v = b - a
    return Location(Plane(origin=(a + b) * 0.5, z_dir=v.normalized())) * Cylinder(r, v.length)


def comp(shapes):
    shapes = [s for s in shapes if s is not None]
    return Compound(shapes)


def derived(P=PARAMS):
    """Numbers the drawings, calculations and build plan use."""
    H = P["slope_h"]
    k = math.hypot(H, 1.0)
    d = (-H / k, 0.0, -1.0 / k)              # down the wall
    n = (-1.0 / k, 0.0, H / k)               # out of the wall, into the canal
    ro = P["rung_od"] / 2
    off = P["so_depth"]                       # rung axis to the wall
    O = tuple(P["rung1_s"] * d[i] + off * n[i] for i in range(3))
    span = (P["n_rungs"] - 1) * P["pitch"]
    zs = [-(k_ - 1) * P["pitch"] for k_ in range(1, P["n_rungs"] + 1)]
    wall_to_foam = off - P["foam_od"] / 2
    clear_w = P["rope_pitch"] - P["flange_od"]
    return dict(d=d, n=n, O=O, span=span, zs=zs, ro=ro, ri=ro - P["rung_wall"], wall_to_foam=wall_to_foam,
                clear_w=clear_w, slope_deg=math.degrees(math.atan(1 / H)),
                post_face=P["post_x"] - P["post_w"] / 2, post_back=P["post_x"] + P["post_w"] / 2,
                eye_cx=P["post_x"] - P["post_w"] / 2 - 4 - 26 - 25, box_front=P["post_x"] - P["post_w"] / 2 - P["plate"][0] - P["box"][0])


def ladder_frame(P=PARAMS):
    D = derived(P)
    return Location(Plane(origin=D["O"], x_dir=(0, -1, 0), z_dir=tuple(-c for c in D["d"])))


def to_world(local_pt, P=PARAMS):
    D = derived(P)
    x, y, z = local_pt
    up = tuple(-c for c in D["d"])
    tw = (-D["n"][0], 0.0, -D["n"][2])         # local +Y, toward the wall
    return tuple(D["O"][i] + x * (0, -1, 0)[i] + y * tw[i] + z * up[i] for i in range(3))


# ------------------------------------------------------------------ ladder parts (local frame)
def rung_tube(k, P=PARAMS):
    D = derived(P)
    z = D["zs"][k - 1]
    L, hx = P["rung_len"], P["rope_pitch"] / 2
    t = cyl_x(-L / 2, L / 2, D["ro"], z=z) - cyl_x(-L / 2, L / 2, D["ri"], z=z)
    for sx in (-1, 1):
        t -= cyl_z(z - 20, z + 20, P["bush_od"] / 2, x=sx * hx)
        if k in P["so_rungs"]:
            t -= cyl_z(z - 20, z + 20, 2.65, x=sx * P["so_bolt_x"])
    return t


def bush(k, sx, P=PARAMS):
    D = derived(P)
    z = D["zs"][k - 1]
    x = sx * P["rope_pitch"] / 2
    zb = z - D["ro"]
    top = zb + P["bush_len"]
    sleeve = cyl_z(zb, top, P["bush_od"] / 2, x=x) - cyl_z(zb - 1, top + 1, P["bush_id"] / 2, x=x)
    fl = cyl_z(zb - P["flange_t"], zb, P["flange_od"] / 2, x=x) - cyl_z(zb - 3, zb + 1, P["bush_id"] / 2, x=x)
    return sleeve + fl


def end_cap(k, sx, P=PARAMS):
    D = derived(P)
    z = D["zs"][k - 1]
    xe = sx * P["rung_len"] / 2
    head = cyl_x(xe, xe + sx * P["cap_head"], D["ro"], z=z)
    shank = cyl_x(xe - sx * P["cap_shank"], xe, D["ri"], z=z)
    return head + shank


def foam(k, P=PARAMS):
    D = derived(P)
    z = D["zs"][k - 1]
    L = P["foam_len_so"] if k in P["so_rungs"] else P["foam_len"]
    return cyl_x(-L / 2, L / 2, P["foam_od"] / 2, z=z) - cyl_x(-L / 2, L / 2, D["ro"], z=z)


def block_profile_solid(P=PARAMS):
    """Stand-off block, at the origin: X across the 16 mm thickness, Y toward the wall, Z up."""
    b, dpt, h, nh = P["so_back"], P["so_depth"], P["so_h"] / 2, P["so_nose_h"] / 2
    pts = [(-b, -h), (35, -h), (dpt, -nh), (dpt, nh), (35, h), (-b, h)]
    prof = Plane.YZ * Polygon(*pts, align=None)
    s = extrude(prof, amount=P["so_t"])          # along +X from X = 0
    s -= cyl_x(-1, P["so_t"] + 1, P["rung_od"] / 2 + 0.1)
    s -= cyl_z(-30, 30, 2.65, x=P["so_t"] / 2)
    return s


def block(k, sx, P=PARAMS):
    D = derived(P)
    z = D["zs"][k - 1]
    x0 = P["so_bolt_x"] - P["so_t"] / 2
    s = Pos(x0, 0, z) * block_profile_solid(P)
    return s if sx > 0 else s.mirror(Plane.YZ)


def so_bolt(k, sx, P=PARAMS):
    D = derived(P)
    z, x = D["zs"][k - 1], sx * P["so_bolt_x"]
    h = P["so_h"] / 2
    return comp([cyl_z(z - h - 9, z + h + 1, 2.5, x=x),                  # shank, 50 long
                 cyl_z(z + h, z + h + 1, 5.0, x=x), cyl_z(z + h + 1, z + h + 4.5, 4.0, x=x),   # washer, head
                 cyl_z(z - h - 1, z - h, 5.0, x=x), cyl_z(z - h - 6, z - h - 1, 4.6, x=x)])    # washer, nyloc nut


def knot_z(k, P=PARAMS):
    D = derived(P)
    # the knot sits up into the bush bore until it bears on the rim of the 12 mm hole
    return D["zs"][k - 1] - D["ro"] - P["flange_t"] - math.sqrt(P["knot_r"] ** 2 - (P["bush_id"] / 2) ** 2)


def seizing(k, sx, P=PARAMS):
    D = derived(P)
    z0 = D["zs"][k - 1] - D["ro"] + P["bush_len"]
    x, r = sx * P["rope_pitch"] / 2, P["rope_d"] / 2
    return cyl_z(z0, z0 + P["seize_len"], r + P["seize_t"], x=x) - cyl_z(z0 - 1, z0 + P["seize_len"] + 1, r, x=x)


def rope_local(sx, top_z, P=PARAMS, hang=False):
    """One side rope in the local frame from top_z down to the bottom link, with its stopper knots.
    hang=True adds the top lead to a link 700 mm above rung 1 (the ladder hung from a beam)."""
    D = derived(P)
    x, r = sx * P["rope_pitch"] / 2, P["rope_d"] / 2
    zl = D["zs"][-1]
    kz = knot_z(P["n_rungs"], P)
    bot = (sx * 8.0, 0.0, zl - P["tail"] + P["link_major"] - 2)
    pieces = [cyl_z(kz, top_z, r, x=x),
              cyl_between((x, 0, kz), (bot[0] + sx * 10, 0, bot[2] + 40), r),
              Pos(bot[0] + sx * 10, 0, bot[2] + 40) * Sphere(P["knot_r"]),     # figure-eight loop knot
              cyl_between((bot[0] + sx * 10, 0, bot[2] + 40), bot, r)]
    pieces += [Pos(x, 0, knot_z(k, P)) * Sphere(P["knot_r"]) for k in range(1, P["n_rungs"] + 1)]
    if hang:
        tl = (sx * 8.0, 0.0, 700.0 - P["link_major"] + 2)
        pieces += [cyl_between((x, 0, top_z), (tl[0] + sx * 10, 0, tl[2] - 40), r),
                   Pos(tl[0] + sx * 10, 0, tl[2] - 40) * Sphere(P["knot_r"]),
                   cyl_between((tl[0] + sx * 10, 0, tl[2] - 40), tl, r)]
    return comp(pieces)


def link(center, axis="Y", P=PARAMS):
    """Screw link drawn as a ring of 10 mm wire. axis: the ring's axis."""
    t = Torus(P["link_major"], P["link_wire"])
    rot = {"Y": Rot(90, 0, 0), "X": Rot(0, 90, 0), "Z": Rot(0, 0, 0)}[axis]
    return Pos(*center) * rot * t


def throw_weight(P=PARAMS):
    D = derived(P)
    zl = D["zs"][-1] - P["tail"] - P["link_major"]
    r, L = P["weight_d"] / 2, P["weight_len"]
    top = zl - 22
    body = cyl_z(top - L + r, top - r, r) + Pos(0, 0, top - r) * Sphere(r) + Pos(0, 0, top - L + r) * Sphere(r)
    loop = box(-12.5, 12.5, -1, 1, top - 4, zl + P["link_wire"] + 2) - box(-9, 9, -2, 2, top - 1, zl + P["link_wire"])
    return body + loop


def ladder_local(P=PARAMS, hang=True):
    """Every ladder component in the local frame, keyed like BOM. hang: ropes run up to a top link."""
    D = derived(P)
    ks = range(1, P["n_rungs"] + 1)
    out = {
        "rungs": comp([rung_tube(k, P) for k in ks]),
        "bushes": comp([bush(k, s, P) for k in ks for s in (-1, 1)]),
        "caps": comp([end_cap(k, s, P) for k in ks for s in (-1, 1)]),
        "foam": comp([foam(k, P) for k in ks]),
        "blocks": comp([block(k, s, P) for k in P["so_rungs"] for s in (-1, 1)]),
        "sobolts": comp([so_bolt(k, s, P) for k in P["so_rungs"] for s in (-1, 1)]),
        "seizings": comp([seizing(k, s, P) for k in ks for s in (-1, 1)]),
        "weight": throw_weight(P),
    }
    top_z = 40.0 if not hang else D["ro"] + P["bush_len"] + P["seize_len"] + 10
    out["ropes"] = comp([rope_local(s, top_z, P, hang=hang) for s in (-1, 1)])
    zl = D["zs"][-1] - P["tail"]
    links = [link((0, 0, zl), "Y", P)]
    if hang:
        links.append(link((0, 0, 700.0), "Y", P))
    out["links"] = comp(links)
    return out


# ------------------------------------------------------------------ station parts (world frame)
def post(P=PARAMS):
    x, w, t = P["post_x"], P["post_w"], P["post_t"]
    z0, z1 = -P["post_embed"], P["post_len"] - P["post_embed"]
    s = box(x - w / 2, x + w / 2, -w / 2, w / 2, z0, z1) - box(x - w / 2 + t, x + w / 2 - t, -w / 2 + t, w / 2 - t, z0 - 1, z1 + 1)
    s -= cyl_x(x - w, x, 8.75, z=P["eye_z"])                    # 17.5 mm in the canal-side wall
    s -= cyl_x(x, x + w, 10.75, z=P["eye_z"])                   # 21.5 mm in the back wall, for the crush tube
    return s


def crush_tube(P=PARAMS):
    x, w, t = P["post_x"], P["post_w"], P["post_t"]
    a, b = x - w / 2 + t, x + w / 2                              # front wall inside face to back face, 57 mm
    return cyl_x(a, b, P["crush_od"] / 2, z=P["eye_z"]) - cyl_x(a - 1, b + 1, P["crush_od"] / 2 - P["crush_t"], z=P["eye_z"])


def footing(P=PARAMS):
    x, w = P["post_x"], P["post_w"]
    f = cyl_z(-P["footing_depth"], 0, P["footing_d"] / 2, x=x)
    return f - box(x - w / 2, x + w / 2, -w / 2, w / 2, -P["post_embed"], 1)


def anchor_bolt(P=PARAMS):
    D = derived(P)
    z, xf, xb = P["eye_z"], D["post_face"], D["post_back"]
    return comp([cyl_x(xb + 4 + 10 - P["bolt_len"], xb + 4, P["bolt_d"] / 2, z=z),     # shank
                 cyl_x(xb + 4, xb + 14, 13.0, z=z),                                  # head
                 cyl_x(xb, xb + 4, 25.0, z=z) - cyl_x(xb - 1, xb + 5, 8.6, z=z),    # back washer 50 OD
                 cyl_x(xf - 3, xf, 15.0, z=z) - cyl_x(xf - 4, xf + 1, 8.6, z=z)])    # front washer 30 OD


def eye_nut(P=PARAMS):
    D = derived(P)
    z, xf = P["eye_z"], D["post_face"] - 3
    collar = cyl_x(xf - 26, xf, 16.0, z=z) - cyl_x(xf - 27, xf + 1, P["bolt_d"] / 2, z=z)
    ring = Pos(D["eye_cx"], 0, z) * Rot(90, 0, 0) * Torus(22.0, 7.0)
    return collar + ring


def mount_plate(P=PARAMS):
    D = derived(P)
    t, w, h = P["plate"]
    xf = D["post_face"]
    s = box(xf - t, xf, -w / 2, w / 2, P["plate_z0"], P["plate_z0"] + h)
    for z in P["ubolt_z"]:
        for y in (-34.0, 34.0):
            s -= cyl_x(xf - t - 1, xf + 1, 4.5, y=y, z=z)
    return s


def ubolts(P=PARAMS):
    D = derived(P)
    xr = D["post_back"] + P["ubolt_d"] / 2
    r = P["ubolt_d"] / 2
    out = []
    for z in P["ubolt_z"]:
        for y in (-34.0, 34.0):
            out.append(cyl_x(xr - P["ubolt_leg"], xr, r, y=y, z=z))
            out.append(Pos(xr, y, z) * Sphere(r))
        out.append(cyl_y(-34, 34, r, x=xr, z=z))
    return comp(out)


def storage_box(P=PARAMS, lid=True):
    D = derived(P)
    dx, wy, hz = P["box"]
    t, z0 = P["box_t"], P["box_z0"]
    xb = D["post_face"] - P["plate"][0]
    xf = xb - dx
    s = box(xf, xb, -wy / 2, wy / 2, z0, z0 + hz) - box(xf + t, xb - t, -wy / 2 + t, wy / 2 - t, z0 + t, z0 + hz + 1)
    nw, nd = P["notch"]
    s -= box(xf - 1, xf + t + 1, -nw / 2, nw / 2, z0 + hz - nd, z0 + hz + 1)
    for z in P["ubolt_z"]:
        for y in (-34.0, 34.0):
            s -= cyl_x(xb - t - 1, xb + 1, 4.5, y=y, z=z)
    for xx in (xf + 40, xb - 40):
        for y in (-wy / 2 + 40, wy / 2 - 40):
            s -= cyl_z(z0 - 1, z0 + t + 1, 4.0, x=xx, y=y)
    if not lid:
        return s
    return s + box_lid(P)


def box_lid(P=PARAMS):
    D = derived(P)
    dx, wy, hz = P["box"]
    xb = D["post_face"] - P["plate"][0]
    return box(xb - dx - 5, xb, -wy / 2 - 5, wy / 2 + 5, P["box_z0"] + hz, P["box_z0"] + hz + P["lid_t"])


def box_fixings(P=PARAMS):
    D = derived(P)
    xi = D["post_face"] - P["plate"][0] - P["box_t"]
    out = []
    for z in P["ubolt_z"]:
        for y in (-34.0, 34.0):
            out.append(cyl_x(xi - 1.5, xi, 15.0, y=y, z=z) - cyl_x(xi - 2, xi + 1, 4.3, y=y, z=z))
            out.append(cyl_x(xi - 9.5, xi - 1.5, 6.5, y=y, z=z) - cyl_x(xi - 10, xi - 1, 4.0, y=y, z=z))
    return comp(out)


def post_cap(P=PARAMS):
    x, w, t = P["post_x"], P["post_w"], P["post_t"]
    ztop = P["post_len"] - P["post_embed"]
    return box(x - w / 2 - 0.5, x + w / 2 + 0.5, -w / 2 - 0.5, w / 2 + 0.5, ztop, ztop + 8) + \
        box(x - w / 2 + t, x + w / 2 - t, -w / 2 + t, w / 2 - t, ztop - 15, ztop)


def decals(P=PARAMS):
    D = derived(P)
    z0, hz = P["box_z0"], P["box"][2]
    xf = D["box_front"]
    top = z0 + hz + P["lid_t"]
    lid_decal = box(xf + 40, xf + 360, -230, 230, top, top + 0.5)
    front = box(xf - 0.5, xf, -250, 250, z0 + 140, z0 + 290)
    tag = box(xf - 0.5, xf, 200, 230, z0 + hz - 40, z0 + hz - 10)
    return comp([lid_decal, front, tag])


def knife(P=PARAMS):
    D = derived(P)
    zt = P["box_z0"] + P["box"][2]
    xf = D["box_front"]
    return box(xf + 80, xf + 300, 250, 290, zt - 18, zt)


# ------------------------------------------------------------------ deployed ladder (world frame)
def top_lead(P=PARAMS):
    """Both ropes from just above rung 1 over the coping to the top link on the eye nut, and the
    edge protector sleeves where they cross the coping."""
    D = derived(P)
    r = P["rope_d"] / 2
    lk = (D["eye_cx"] - P["link_major"], 0.0, P["eye_z"])          # top link centre (ring axis Z)
    ropes, prot = [], []
    for sx in (-1, 1):
        a = to_world((sx * P["rope_pitch"] / 2, 0, 40.0), P)
        e = (-2.0, -sx * 130.0, 5.5)
        kn = (lk[0] - P["link_major"] - 30, -sx * 8.0, lk[2])
        end = (lk[0] - P["link_major"] + 2, -sx * 6.0, lk[2])
        ropes += [cyl_between(a, e, r), Pos(*e) * Sphere(r), cyl_between(e, kn, r), Pos(*kn) * Sphere(P["knot_r"]),
                  cyl_between(kn, end, r)]
        for p_from, p_to in ((e, a), (e, kn)):
            v = Vector(*p_to) - Vector(*p_from)
            q = Vector(*p_from) + v.normalized() * 250
            prot.append(cyl_between(p_from, tuple(q), 12.0) - cyl_between(p_from, tuple(q), r))
    return comp(ropes), comp(prot), link(lk, "Z", P)


@dataclass
class Comp:
    key: str
    bom: int
    name: str
    shape: object
    made: str = "buy"
    extra: dict = field(default_factory=dict)


def station(P=PARAMS):
    f = {"post": post(P), "crush": crush_tube(P), "footing": footing(P), "bolt": anchor_bolt(P), "eyenut": eye_nut(P),
         "plate": mount_plate(P), "ubolts": ubolts(P), "box": storage_box(P), "boxfix": box_fixings(P),
         "cap": post_cap(P), "decals": decals(P), "knife": knife(P)}
    return f


def deployed_ladder(P=PARAMS):
    loc = ladder_frame(P)
    L = ladder_local(P, hang=False)
    out = {k: loc * v for k, v in L.items() if k != "links"}
    lead, prot, toplink = top_lead(P)
    out["ropes"] = comp([out["ropes"], lead])
    D = derived(P)
    out["links"] = comp([toplink, loc * link((0, 0, D["zs"][-1] - P["tail"]), "Y", P)])
    out["protectors"] = prot
    return out


def simple_parts(P=PARAMS):
    """Light set for orthographic projection at small scale (general arrangement, concept sheet):
    the main parts, with the ropes drawn as plain lines of rope and the small parts (bushes, end
    caps, knots, seizings, fixings, decals, knife) left out because they do not show at 1:50."""
    st, dl = station(P), deployed_ladder(P)
    r = P["rope_d"] / 2
    D = derived(P)
    lines = []
    for sx in (-1, 1):
        x = sx * P["rope_pitch"] / 2
        a = to_world((x, 0, 40.0), P)
        b = to_world((x, 0, D["zs"][-1] - 40), P)
        c = to_world((sx * 8.0, 0, D["zs"][-1] - P["tail"] + P["link_major"]), P)
        e = (-2.0, -sx * 130.0, 5.5)
        k = (D["eye_cx"] - 2 * P["link_major"] + 2, -sx * 6.0, P["eye_z"])
        lines += [cyl_between(a, b, r), cyl_between(b, c, r), cyl_between(a, e, r), cyl_between(e, k, r)]
    keep = {k: st[k] for k in ("post", "footing", "eyenut", "plate", "box", "cap")}
    keep.update({k: dl[k] for k in ("rungs", "foam", "blocks", "links", "weight", "protectors")})
    keep["ropes"] = comp(lines)
    return keep


MADE = {"post": "cut, drill, touch up", "crush": "cut", "footing": "cast", "plate": "cut, drill", "box": "bought, drilled",
        "rungs": "cut, drill", "foam": "cut", "blocks": "cut, drill", "ropes": "cut, mark, knot"}


def components(P=PARAMS):
    """Every component of the deployed station, in build order (BOM order)."""
    parts = {**station(P), **deployed_ladder(P)}
    return [Comp(k, BOM[k][0], BOM[k][1], parts[k], MADE.get(k, "buy")) for k in BOM]


def site(P=PARAMS, yw=450.0):
    """Context: bank top, concrete lining and the water, for pictures only (not built)."""
    H, drop, dep = P["slope_h"], P["water_drop"], P["water_depth"]
    toe_z = -(drop + dep)
    toe_x = toe_z * H
    bed_x = toe_x - 600
    bank = box(0, 1500, -yw, yw, -100, 0)
    lin = Plane.XZ * Polygon((0, 0), (toe_x, toe_z), (bed_x, toe_z), (bed_x, toe_z - 100),
                             (toe_x - 60, toe_z - 100), (-60, -100), (0, -100), align=None)
    lining = extrude(lin, amount=yw, both=True)
    wx = -drop * H
    wat = Plane.XZ * Polygon((wx, -drop), (toe_x, toe_z), (bed_x, toe_z), (bed_x, -drop), align=None)
    water = extrude(wat, amount=yw, both=True)
    return {"bank": bank, "lining": lining, "water": water}


# ------------------------------------------------------------------ masses and checks
def masses(P=PARAMS):
    """Ladder masses in kg (everything that leaves the box when the ladder is thrown)."""
    L = ladder_local(P, hang=False)
    D = derived(P)
    rope_len = rope_cut_length(P)
    m = {"rungs": L["rungs"].volume * DENSITY["al"],
         "bushes": L["bushes"].volume * DENSITY["nylon"],
         "caps": 26 * 0.004,                                     # bought hollow plugs, catalogue mass
         "foam": L["foam"].volume * DENSITY["xlpe"],
         "blocks": L["blocks"].volume * DENSITY["hdpe"],
         "sobolts": 8 * 0.010,
         "ropes": 2 * rope_len / 1000 * ROPE_KG_M,
         "seizings": 0.02,
         "links": 2 * 0.06,
         "weight": P["weight_kg"] + 0.03,
         "protectors": 2 * 0.08}
    m["total"] = sum(m.values())
    return m


def rope_cut_length(P=PARAMS):
    """Cut length of one side rope (mm): top lead, rung section with knots, tail, two loop knots."""
    D = derived(P)
    a = Vector(*to_world((P["rope_pitch"] / 2, 0, 40.0), P))
    e = Vector(-2.0, -130.0, 5.5)
    k = Vector(D["eye_cx"] - 2 * P["link_major"] - 30, -8.0, P["eye_z"])
    lead = (a - e).length + (e - k).length + 30
    section = 40 + D["span"] + P["n_rungs"] * 100.0            # 100 mm of rope in each overhand stopper knot
    tail = P["tail"] + 40
    loops = 2 * 600.0                                           # figure-eight on a bight with tail, each end
    return lead + section + tail + loops


CHECKS = []


def _pairs(P=PARAMS):
    """(a, b, relation, limit): 'touch' means they must meet (gap <= limit mm, no overlap beyond
    a press fit); 'clear' means at least limit mm apart."""
    ks = range(1, P["n_rungs"] + 1)
    D = derived(P)
    out = []
    for k in ks:
        for s in (-1, 1):
            out.append((f"rung {k} tube", rung_tube(k, P), f"bush {k}{'LR'[s > 0]}", bush(k, s, P), "touch", 0.2))
            out.append((f"bush {k}{'LR'[s > 0]}", bush(k, s, P), f"knot {k}{'LR'[s > 0]}",
                        Pos(s * P["rope_pitch"] / 2, 0, knot_z(k, P)) * Sphere(P["knot_r"]), "touch", 0.2))
            out.append((f"bush {k}{'LR'[s > 0]}", bush(k, s, P), f"seizing {k}{'LR'[s > 0]}", seizing(k, s, P), "touch", 0.2))
            out.append((f"rung {k} tube", rung_tube(k, P), f"end cap {k}{'LR'[s > 0]}", end_cap(k, s, P), "touch", 0.2))
            out.append((f"rope {'LR'[s > 0]}", cyl_z(knot_z(k, P), D["zs"][k - 1] + 60, P["rope_d"] / 2, x=s * P["rope_pitch"] / 2),
                        f"rung {k} tube", rung_tube(k, P), "clear", 2.0))
            out.append((f"end cap {k}{'LR'[s > 0]}", end_cap(k, s, P), f"bush {k}{'LR'[s > 0]}", bush(k, s, P), "clear", 1.0))
            out.append((f"foam {k}", foam(k, P), f"bush {k}{'LR'[s > 0]}", bush(k, s, P), "clear", 1.0))
        out.append((f"rung {k} tube", rung_tube(k, P), f"foam {k}", foam(k, P), "touch", 0.2))
    for k in P["so_rungs"]:
        for s in (-1, 1):
            out.append((f"block {k}{'LR'[s > 0]}", block(k, s, P), f"rung {k} tube", rung_tube(k, P), "touch", 0.2))
            out.append((f"block {k}{'LR'[s > 0]}", block(k, s, P), f"stand-off bolt {k}{'LR'[s > 0]}", so_bolt(k, s, P), "touch", 0.2))
            out.append((f"block {k}{'LR'[s > 0]}", block(k, s, P), f"foam {k}", foam(k, P), "clear", 1.0))
            out.append((f"block {k}{'LR'[s > 0]}", block(k, s, P), f"bush {k}{'LR'[s > 0]}", bush(k, s, P), "clear", 0.5))
    st = station(P)
    out += [("post", st["post"], "crush tube", st["crush"], "touch", 0.2),
            ("post", st["post"], "footing", st["footing"], "touch", 0.2),
            ("anchor bolt", st["bolt"], "post", st["post"], "touch", 0.2),
            ("anchor bolt washers", st["bolt"], "crush tube end", st["crush"], "touch", 0.2),
            ("anchor bolt shank", cyl_x(D["post_back"] + 14 - P["bolt_len"], D["post_back"] + 4, P["bolt_d"] / 2, z=P["eye_z"]),
             "crush tube bore", st["crush"], "clear", 0.5),
            ("eye nut", st["eyenut"], "anchor bolt", st["bolt"], "touch", 0.2),
            ("mounting plate", st["plate"], "post", st["post"], "touch", 0.2),
            ("U-bolts", st["ubolts"], "post", st["post"], "touch", 0.2),
            ("U-bolts", st["ubolts"], "mounting plate", st["plate"], "touch", 0.6),
            ("storage box", st["box"], "mounting plate", st["plate"], "touch", 0.2),
            ("storage box", st["box"], "box fixings", st["boxfix"], "touch", 0.2),
            ("storage box", st["box"], "eye nut", st["eyenut"], "clear", 100.0),
            ("post cap", st["cap"], "post", st["post"], "touch", 0.2),
            ("knife", st["knife"], "storage box", st["box"], "touch", 0.2)]
    dl = deployed_ladder(P)
    _, _, toplink = top_lead(P)
    out += [("top link", toplink, "eye nut", st["eyenut"], "clear", 3.0),
            ("deployed ladder ropes", dl["ropes"], "storage box", st["box"], "clear", 100.0),
            ("deployed ladder rungs", dl["rungs"], "bank and lining", site(P)["lining"], "clear", 20.0),
            ("stand-off blocks", dl["blocks"], "bank and lining", site(P)["lining"], "touch", 0.5)]
    return out


def check(P=PARAMS, verbose=True):
    fails = 0
    rows = _pairs(P)
    for an, a, bn, b, rel, lim in rows:
        try:
            ov = (a & b).volume
        except Exception:
            ov = 0.0
        gap = a.distance_to(b)
        if rel == "touch":
            ok = gap <= lim and ov < 0.05 * min(a.volume, b.volume) + 1.0
        else:
            ok = gap >= lim and ov < 1e-3
        fails += not ok
        if verbose and not ok:
            print(f"FAIL {rel:5s} {an} / {bn}: gap {gap:.2f} mm, overlap {ov:.1f} mm3 (limit {lim})")
    if verbose:
        print(f"{len(rows) - fails} of {len(rows)} constructability checks pass")
    return fails, len(rows)


def export(P=PARAMS):
    step, stl = ROOT / "cad/step", ROOT / "cad/stl"
    step.mkdir(parents=True, exist_ok=True)
    stl.mkdir(parents=True, exist_ok=True)
    cs = components(P)
    export_step(Compound([c.shape for c in cs]), str(step / "canalrung-assembly.step"))
    L = ladder_local(P, hang=True)
    export_step(Compound(list(L.values())), str(step / "canalrung-ladder.step"))
    st = station(P)
    singles = {"post": st["post"], "mounting-plate": st["plate"], "rung": rung_tube(3, P),
               "standoff-block": block_profile_solid(P), "crush-tube": crush_tube(P)}
    for name, s in singles.items():
        export_step(s, str(step / f"{name}.step"))
        export_stl(s, str(stl / f"{name}.stl"), tolerance=0.2, angular_tolerance=0.3)
    print("exported STEP and STL")


if __name__ == "__main__":
    if "--check" in sys.argv:
        f, n = check()
        sys.exit(1 if f else 0)
    D = derived()
    m = masses()
    print(f"rung section {D['span']:.0f} mm, slope {D['slope_deg']:.1f} deg, rope cut length {rope_cut_length():.0f} mm each")
    for k, v in m.items():
        print(f"  {k:12s} {v:6.3f} kg")
    check()
    export()
