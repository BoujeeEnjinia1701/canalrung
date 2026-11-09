"""CanalRung concept options B and C at detail level D3 (kit 1.9, CNR-DDR-004).

Option B, the coping-hook folding ladder: a rigid two-piece aluminium ladder that is lowered over the coping and
hangs on the wall on rubber pads; a lanyard to the station's eye nut stops it sliding down. Option C, the post winch:
a hand winch on a bank post hauls a floating rescue sling up the wall over a boom sheave. Both stand in the same canal
as option A. Drawn with the coping edge at Z = 0 and lifted onto the ground by cnr_geom.lift(), like option A.
"""
from __future__ import annotations

import math

from build123d import Box, Circle, Cylinder, Location, Plane, Polygon, Pos, RectangleRounded, Rot, Sketch, Sphere, Torus, Vector, extrude

import cad_parts as cp
import model as M
from cnr_geom import prism_z, bead_xy, bead_xz, box, comp, cyl_between, cyl_x, cyl_y, cyl_z, lift, to_yz


def _adder(out, default_group):
    def add(name, shape, material, kind, bom=None, group=None, color=None):
        out.append(cp.part(name, lift(shape), material, kind=kind, bom=None, group=group or default_group, color=color))
    return add


def _annulus(od, id_, t):
    return extrude(Sketch() + Circle(od / 2) - Circle(id_ / 2), t)


def _bolt_along(axis_sign, shape, x, y, z):
    """Place a hex_bolt_set (joint top face at 0, head up, joint toward -Z) so its axis lies along X or Y.
    axis_sign: 'x-' head on the -X side, 'x+' head on the +X side, 'y-' head on the -Y side."""
    rot = {"x-": Rot(0, -90, 0), "x+": Rot(0, 90, 0), "y-": Rot(90, 0, 0)}[axis_sign]
    return Pos(x, y, z) * rot * shape


def _bolt_set(d, grip):
    return comp([s for _, s in cp.hex_bolt_set(d, grip)])


# ====================================================================== option B
def parts_B(P):
    PB = dict(P, footing_d=350.0, footing_depth=900.0, post_len=2100.0, post_embed=800.0)
    D = M.derived(PB)
    out = []
    add = _adder(out, "station")
    M._post_anchor(PB, add)
    xf, x = D["post_face"], PB["post_x"]
    # ---- ladder hangers (two J hooks on plates, welded, clamped to the post by square U-bolts)
    for zc in (600.0, 1100.0):
        n = int(zc)
        holes = [(y, 0.0, 9.0) for y in (-34.0, 34.0)]
        plate = Pos(xf - 4, 0, zc) * to_yz(cp.sheet(100, 180, 4, holes=holes, r_corner=8.0))
        add(f"Hanger plate {n}", plate, "aluminium", "made")
        prof = [(xf - 10, zc - 60), (xf - 4, zc - 60), (xf - 4, zc + 66), (xf - 84, zc + 66), (xf - 84, zc + 100),
                (xf - 90, zc + 100), (xf - 90, zc + 60), (xf - 10, zc + 60)]
        hook = cp.break_edges(bead_xz(prof, -15, 15), 1.0)
        add(f"Hanger hook {n}", hook, "galvanised", "made")
        add(f"Hook weld {n}", bead_xz([(xf - 4, zc - 60), (xf - 9, zc - 60), (xf - 4, zc - 65)], -15, 15), "mild_steel", "weld")
        xr, r = D["post_back"] + 4.0, 4.0
        ub = comp([cyl_x(xr - 84, xr, r, y=y, z=zc) for y in (-34.0, 34.0)] + [Pos(xr, y, zc) * Sphere(r) for y in (-34.0, 34.0)] +
                  [cyl_y(-34, 34, r, x=xr, z=zc)])
        add(f"Square U-bolt M8 {n}", ub, "zinc_plated", "bought")
        for y in (-34.0, 34.0):
            xi = xf - 4
            add(f"Fender washer M8 {n}{'+-'[y < 0]}", Pos(xi - 1.5, y, zc) * Rot(0, 90, 0) * _annulus(30, 8.4, 1.5), "stainless", "fastener")
            add(f"Nyloc nut M8 {n}{'+-'[y < 0]}", Pos(xi - 1.5 - 6.8, y, zc) * Rot(0, 90, 0) * cp.hex_nut(8), "stainless", "fastener")
    # ---- ladder (local frame: X across, Z up the ladder, Y toward the wall)
    d, nrm = D["d"], D["n"]
    s1, off = 200.0, 74.5
    origin = tuple(s1 * d[i] + off * nrm[i] for i in range(3))
    loc = Location(Plane(origin=origin, x_dir=(0, -1, 0), z_dir=tuple(-c for c in d)))
    XC = 187.5
    rung_z = [110.0] + [-(k - 1) * 300.0 for k in range(1, 15)]            # index 0 is the top (lanyard) bar
    names = ["Top bar"] + [f"Rung {k}" for k in range(1, 15)]
    splice_z = (-2162.0, -2338.0)     # on the middle wall pad (z -2250), where the stile bending moment is smallest (STM S16)
    secs = {"upper": (150.0, -2250.0), "lower": (-2250.0, -4050.0)}
    ladd = _adder(out, "ladder")
    for sec, (zt, zb) in secs.items():
        for sx in (-1, 1):
            xc = sx * XC
            st = Pos(xc, 0, zb) * cp.rhs(25, 45, 2, zt - zb)
            for z in rung_z:
                if zb + 1 < z < zt - 1:
                    st = st - cyl_x(xc - 13, xc + 13, 12.75, z=z) - cyl_y(-23, 23, 2.75, x=xc, z=z)
            for z in splice_z:
                if zb < z < zt:
                    st = st - cyl_x(xc - 13, xc + 13, 2.75, z=z)
            ladd(f"Stile {sec} {M._lr(sx)}, RHS 25 x 45 x 2", loc * st, "aluminium", "made")
    for nm, z in zip(names, rung_z):
        tube = Pos(-200, 0, z) * Rot(0, 90, 0) * cp.round_tube(25.4, 3.2, 400)
        for sx in (-1, 1):
            tube = tube - cyl_y(-14, 14, 2.75, x=sx * XC, z=z)
        ladd(f"{nm}, tube 25.4 x 3.2 x 400", loc * tube, "aluminium", "made")
        for sx in (-1, 1):
            ladd(f"M5 bolt set, {nm} {M._lr(sx)}", loc * _bolt_along("y-", _bolt_set(5, 45), sx * XC, -22.5, z), "stainless", "fastener")
    for sx in (-1, 1):
        xc = sx * XC
        sl = Pos(xc, 0, -2350) * cp.rhs(20.6, 40.6, 1.5, 200)
        for z in splice_z:
            sl = sl - cyl_x(xc - 11, xc + 11, 2.75, z=z)
        ladd(f"Splice sleeve {M._lr(sx)}", loc * sl, "aluminium", "made")
        for z in splice_z:
            ax = "x-" if sx < 0 else "x+"
            ladd(f"M5 splice bolt set {M._lr(sx)} z{int(-z)}", loc * _bolt_along(ax, _bolt_set(5, 25), sx * 200.0, 0, z), "stainless", "fastener")
        for zc in (-450.0, -2250.0, -3750.0):
            pad = cp.break_edges(Pos(xc, 48.5, zc) * Box(25, 52, 60), 3.0)
            ladd(f"Wall pad {M._lr(sx)} z{int(-zc)}", loc * pad, "epdm", "bought")
        for zc, up in ((150.0, 1), (-4050.0, -1)):
            plate = Pos(xc, 0, zc if up > 0 else zc - 3) * extrude(RectangleRounded(25, 45, 4), 3)
            ins = Pos(xc, 0, zc - 15 if up > 0 else zc) * (extrude(RectangleRounded(20.6, 40.6, 2), 15) -
                                                          extrude(RectangleRounded(16.6, 36.6, 1), 15))
            ladd(f"Stile end cap {M._lr(sx)} {'top' if up > 0 else 'foot'}", loc * (plate + ins), "epdm", "bought")
    # ---- lanyard: ring round the top bar, 10 mm rope over the coping to the eye nut link
    lk = (D["eye_cx"] - PB["link_major"], 0.0, PB["eye_z"])
    ring = loc * M.screw_link((0, 0, 110.0), "X", PB)
    a = (loc * Pos(0, 0, 140.2)).position
    pts = [(a.X - 2, a.Y, a.Z), (-2.0, 0.0, 14.0), (lk[0] - PB["link_major"] + 2, 0.0, lk[2])]
    rope = cp.rope(pts, 10.0)
    ladd("Lanyard rope 10 mm", rope, "rope", "bought", color="#DC2626")
    ladd("Screw link, top bar", ring, "zinc_plated", "bought")
    ladd("Screw link, eye nut", M.screw_link(lk, "Z", PB) - rope, "zinc_plated", "bought")
    return out


# ====================================================================== option C
def parts_C(P):
    PC = dict(P, footing_d=600.0, footing_depth=1200.0, post_len=3100.0, post_embed=1100.0, post_w=100.0, post_t=4.0)
    out = []
    add = _adder(out, "station")
    x, w, t = PC["post_x"], 100.0, 4.0
    xf, xb = x - w / 2, x + w / 2                      # post canal face 950, back face 1050
    z0, ztop = -1100.0, 2000.0
    post = Pos(x, 0, z0) * cp.shs(w, t, 3100.0)
    # winch mounting holes (M12, 14 mm) at y = +-30, z = 1000 and 1300; boom welded to the canal face
    mount = [(y, z) for y in (-30.0, 30.0) for z in (1000.0, 1300.0)]
    for y, z in mount:
        post = post - cyl_x(xf - 1, xb + 1, 7.0, y=y, z=z)
    add("Post, SHS 100 x 100 x 4", post, "galvanised", "made")
    solid = Pos(x, 0, z0) * extrude(RectangleRounded(w, w, 2 * t), 3100.0)
    add("Concrete footing 600 dia x 1,200", cyl_z(-1200.0, 0, 300.0, x=x) - solid, "concrete", "made")
    cap = (Pos(x, 0, ztop) * extrude(RectangleRounded(w + 1, w + 1, 7), 8) +
           Pos(x, 0, ztop - 15) * (extrude(RectangleRounded(w - 2 * t - 0.4, w - 2 * t - 0.4, 6), 15) -
                                   extrude(RectangleRounded(w - 2 * t - 4.4, w - 2 * t - 4.4, 3), 15)))
    add("Post cap", cap, "hdpe_black", "bought")
    # ---- boom: RHS 100 x 60 x 4 from the post face out over the coping, centre line at 1,900
    bz, bx0 = 1900.0, -550.0
    boom = Pos(bx0, 0, bz) * Rot(0, 90, 0) * cp.rhs(100, 60, 4, xf - bx0)
    add("Boom, RHS 100 x 60 x 4 x 1,500", boom, "galvanised", "made")
    add("Boom cap plate", Pos(bx0 - 4, 0, bz) * to_yz(cp.sheet(60, 100, 4, r_corner=4.0)), "galvanised", "made")
    for sgn, name in ((1, "top"), (-1, "bottom")):
        zc = bz + sgn * 50
        pts = [(xf, zc), (xf - 8, zc), (xf, zc + sgn * 8)]
        add(f"Boom weld, {name}", bead_xz(pts, -30, 30), "mild_steel", "weld")
    # ---- sheave block under the boom end: two cheek plates, a 100 mm sheave, spacers and an M12 axle
    sx, sz = -480.0, 1790.0

    def xz_plate(cx, cz, w_, h_, t_, y_face, holes=(), r=8.0):
        """Plate in the XZ plane, thickness from y_face to y_face + t_."""
        return Pos(cx, y_face + t_, cz) * Rot(90, 0, 0) * cp.sheet(w_, h_, t_, holes=list(holes), r_corner=r)

    for yf, nm in ((-24.0, "near"), (18.0, "far")):
        add(f"Sheave cheek plate, {nm}", xz_plate(sx, sz - 5, 110, 130, 6, yf, [(0, 5.0, 13.0)], 10.0), "galvanised", "made")
    add("Sheave 100 mm", Pos(sx, 0, sz) * Rot(90, 0, 0) * cp.pulley(100, 20, 12.0), "cast_aluminium", "bought")
    for y1, nm in ((-10.0, "near"), (18.0, "far")):
        add(f"Sheave spacer bush, {nm}", Pos(sx, y1, sz) * Rot(90, 0, 0) * cp.bush(20, 12.2, 8), "hdpe_black", "bought")
    add("M12 axle bolt set (sheave)", Pos(sx, -24.0, sz) * Rot(90, 0, 0) * _bolt_set(12, 48), "zinc_plated", "fastener")
    # ---- hand winch on the post face: base plate, two side plates, drum, shaft, ratchet, pawl, crank
    wx, wz = 870.0, 1150.0
    base = Pos(xf - 8, 0, 1150) * to_yz(cp.sheet(180, 360, 8, holes=[(y, z - 1150, 14.0) for y, z in mount], r_corner=10.0))
    add("Winch base plate 8 mm", base, "painted_steel", "made")
    for y, z in mount:
        add(f"M12 mount bolt set y{int(y)} z{int(z)}", _bolt_along("x-", _bolt_set(12, 108), xf - 8, y, z), "zinc_plated", "fastener")
    for yf, nm in ((-66.0, "near"), (60.0, "far")):
        add(f"Winch side plate, {nm}", xz_plate(862, wz, 160, 200, 6, yf, [(8, 0, 26.0)], 8.0), "painted_steel", "made")
    for xy, nm in (([(942, -66), (936, -66), (942, -72)], "near out"), ([(942, -60), (936, -60), (942, -54)], "near in"),
                   ([(942, 60), (936, 60), (942, 54)], "far in"), ([(942, 66), (936, 66), (942, 72)], "far out")):
        add(f"Side plate weld, {nm}", bead_xy(xy, 1050.0, 1250.0), "mild_steel", "weld")
    add("Winch shaft 20 mm", Pos(wx, 104.0, wz) * Rot(90, 0, 0) * cp.round_bar(20, 176, 1.0) - Pos(wx, 96.0, wz) * Rot(0, 90, 0) * Cylinder(3.4, 30), "mild_steel", "made")
    add("Shaft collar", Pos(wx, -66.0, wz) * Rot(90, 0, 0) * _annulus(36, 20.0, 6), "mild_steel", "made")
    for y1, nm in ((-60.0, "near"), (66.0, "far")):
        add(f"Bearing bush, {nm}", Pos(wx, y1, wz) * Rot(90, 0, 0) * cp.bush(26, 20.2, 6), "hdpe_black", "bought")
    add("Drum tube 60 x 4", Pos(wx, 54.0, wz) * Rot(90, 0, 0) * cp.round_tube(60, 4, 108), "mild_steel", "made")
    for y1, nm in ((-54.0, "near"), (60.0, "far")):
        add(f"Drum flange, {nm}", Pos(wx, y1, wz) * Rot(90, 0, 0) * _annulus(128, 20.0, 6), "mild_steel", "made")
    # ratchet wheel (20 teeth) and pawl
    pts = []
    for i in range(20):
        a0 = math.radians(i * 18)
        pts += [(50 * math.cos(a0), 50 * math.sin(a0)), (44 * math.cos(a0 + math.radians(2)), 44 * math.sin(a0 + math.radians(2)))]
    wheel = prism_z(pts, 0, 10) - Cylinder(10.0, 30)
    add("Ratchet wheel", Pos(wx, 76.0, wz) * Rot(90, 0, 0) * wheel, "mild_steel", "made")
    ta = math.radians(95)
    tip = (wx + 47.0 * math.cos(ta), wz + 47.0 * math.sin(ta))
    pa = math.radians(112)
    piv = (wx + 78.0 * math.cos(pa), wz + 78.0 * math.sin(pa))
    vx, vz = piv[0] - tip[0], piv[1] - tip[1]
    ln = math.hypot(vx, vz)
    nx, nz = -vz / ln, vx / ln
    pawl = prism_z([(tip[0], tip[1]), (piv[0] + 8 * nx, piv[1] + 8 * nz), (piv[0] - 8 * nx, piv[1] - 8 * nz)], 0, 6) + Pos(piv[0], piv[1], 3) * Cylinder(11.0, 6)
    pawl = pawl - Pos(piv[0], piv[1], 0) * Cylinder(4.2, 20)
    add("Pawl", Pos(0, 72.0, 0) * Rot(90, 0, 0) * pawl, "mild_steel", "made")
    add("Pawl pivot stud 8 mm", Pos(piv[0], 66.0, piv[1]) * Rot(-90, 0, 0) * cp.round_bar(8, 16.4, 0.6), "stainless", "fastener")
    add("Pawl pivot washer", Pos(piv[0], 73.6, piv[1]) * Rot(90, 0, 0) * cp.washer(8), "stainless", "fastener")
    add("Pawl pivot nyloc nut M8", Pos(piv[0], 80.4, piv[1]) * Rot(90, 0, 0) * cp.hex_nut(8), "stainless", "fastener")
    # crank arm, handle pin and grip
    add("Crank arm 40 x 8", Pos(wx, 86.0, wz - 105) * Rot(90, 0, 0) * cp.sheet(40, 250, 8, holes=[(0, 105.0, 20.2), (0, -105.0, 10.2)], r_corner=12.0),
        "painted_steel", "made")
    add("Handle pin 10 mm", Pos(wx, 205.0, wz - 210) * Rot(90, 0, 0) * cp.round_bar(10, 127, 0.8), "mild_steel", "made")
    add("Handle grip", Pos(wx, 200.0, wz - 210) * Rot(90, 0, 0) * cp.bush(32, 10.2, 110), "epdm", "bought")
    add("Shaft washer", Pos(wx, 89.0, wz) * Rot(90, 0, 0) * _annulus(37, 21.6, 3), "zinc_plated", "fastener")
    add("Shaft split pin", Pos(wx, 96.0, wz) * cp.split_pin(20), "stainless", "fastener")
    # ---- rope: drum, over the sheave, down to the sling
    r = 4.0
    P0 = (wx, wz + 34.0)
    rho = 49.6
    dx_, dz_ = P0[0] - sx, P0[1] - sz
    Ld = math.hypot(dx_, dz_)
    th = math.degrees(math.atan2(dz_, dx_)) + math.degrees(math.acos(rho / Ld))
    n_arc = 12
    pulley_arc = [(sx + rho * math.cos(math.radians(th + (180 - th) * i / n_arc)), 0.0,
                   sz + rho * math.sin(math.radians(th + (180 - th) * i / n_arc))) for i in range(n_arc + 1)]
    sling_c = (-3350.0, 0.0, -1960.0)
    ring_c = (-3350.0, 0.0, -1700.0)
    rope_pts = [(P0[0], 0.0, P0[1])] + pulley_arc + [(ring_c[0], 0.0, ring_c[2] + 36.0 + r + 0.2)]
    add("Rescue rope 8 mm", cp.rope(rope_pts, 8.0), "rope", "bought", color="#DC2626")
    # ---- floating rescue sling
    add("Sling float collar", Pos(*sling_c) * Torus(270.0, 55.0), "insulated_white", "bought", color="#F97316")
    add("Lift ring", Pos(*ring_c) * Rot(90, 0, 0) * Torus(30.0, 6.0), "zinc_plated", "bought")
    for sy in (-1, 1):
        add(f"Sling strap {M._lr(sy)}", cp.rope([(ring_c[0] + sy * 43.2, 0.0, ring_c[2]), (sling_c[0], sy * 270.0, sling_c[2] + 55.0 + 7.2)], 14.0),
            "canvas", "bought", color="#0F766E")
    return out


def parts(option, P):
    return {"B": parts_B, "C": parts_C}[option](P)
