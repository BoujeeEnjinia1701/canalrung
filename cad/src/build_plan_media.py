"""CanalRung prototype build plan pictures (CNR-BLD-001, STANDARDS section 18).

Run from the repo root (one group per process on a small machine):
    python cad/src/build_plan_media.py overview
    python cad/src/build_plan_media.py sheets [101 102 ...]
    python cad/src/build_plan_media.py joints [1 2 ...]
    python cad/src/build_plan_media.py steps [1 2 ...]
Every picture is drawn from cad/src/model.py, so the pictures and the model never disagree:
    docs/05-build-plan/overview.png        every component pulled apart, numbered in build order
    cad/drawings/CNR-DWG-101 to 109        making sketches for the made components
    docs/05-build-plan/joint-NN.png        close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png         one picture per assembly step
The ladder pictures use a short ladder of 4 rungs (rung 3 a stand-off rung) built from the same
model, so the parts stay large enough to read; the real ladder has 13. Station pictures use the
world axes of model.py (canal along Y, bank X >= 0); ladder pictures use the ladder's own axes
(rungs along X, up the ladder Z, wall side +Y). BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
from build123d import Compound, Pos, Rot, Torus  # noqa: E402
import model as M  # noqa: E402
from model import box, comp, cyl_z, cyl_x, cyl_between  # noqa: E402

OUT = ROOT / "docs" / "05-build-plan"
DWG = ROOT / "cad" / "drawings"
DATE = "2026-10-03"
P = M.PARAMS
D = M.derived()
P4 = dict(P, n_rungs=4, so_rungs=(3,))
D4 = M.derived(P4)
C = {"post": "#9CA3AF", "crush": "#0EA5E9", "footing": "#D6D3D1", "bolt": "#374151", "eyenut": "#B45309",
     "plate": "#94A3B8", "ubolts": "#4B5563", "box": "#EAB308", "boxfix": "#111827", "cap": "#1F2937",
     "rungs": "#A1A1AA", "bushes": "#E7E5E4", "caps": "#111827", "foam": "#F97316", "blocks": "#374151",
     "sobolts": "#6B7280", "ropes": "#DC2626", "seizings": "#111827", "links": "#52525B", "weight": "#16A34A",
     "protectors": "#0F766E", "decals": "#1D4ED8", "knife": "#111827", "site": "#E7E5E4"}


def part(name, shape, key, explode=(0, 0, 0), alpha=1.0):
    return Part(name, shape, C[key], None, tuple(explode), alpha)


def win(shape, x0, x1, y0, y1, z0, z1):
    """The part of a shape inside a box (for close-ups)."""
    w = box(x0, x1, y0, y1, z0, z1)
    try:
        sols = list(shape.solids()) or [shape]
    except Exception:
        sols = [shape]
    kept = []
    for s_ in sols:
        bb = s_.bounding_box()
        if bb.max.X < x0 or bb.min.X > x1 or bb.max.Y < y0 or bb.min.Y > y1 or bb.max.Z < z0 or bb.min.Z > z1:
            continue
        r = s_ & w
        if r is not None and r.volume > 1e-3:
            kept.append(r)
    return Compound(kept) if kept else None


# ------------------------------------------------------------------ the short ladder, hanging (local axes)
def ladder4():
    L = M.ladder_local(P4, hang=True)
    ks = range(1, 5)
    L["caps_l"] = comp([M.end_cap(k, -1, P4) for k in ks])
    L["caps_r"] = comp([M.end_cap(k, 1, P4) for k in ks])
    L["blocks_l"] = M.block(3, -1, P4)
    L["blocks_r"] = M.block(3, 1, P4)
    L["toplink"] = M.link((0, 0, 700.0), "Y", P4)
    L["botlink"] = M.link((0, 0, D4["zs"][-1] - P4["tail"]), "Y", P4)
    L["protectors"] = protectors_local(P4)
    return L


def protectors_local(Pp):
    Dd = M.derived(Pp)
    out = []
    top_z = Dd["ro"] + Pp["bush_len"] + Pp["seize_len"] + 10
    for sx in (-1, 1):
        a = (sx * Pp["rope_pitch"] / 2, 0, top_z)
        b = (sx * 18.0, 0, 700.0 - Pp["link_major"] + 2 - 40)
        from build123d import Vector
        v = Vector(*b) - Vector(*a)
        p0 = Vector(*a) + v.normalized() * 120
        p1 = p0 + v.normalized() * 250
        out.append(cyl_between(tuple(p0), tuple(p1), 12.0) - cyl_between(tuple(p0), tuple(p1), Pp["rope_d"] / 2))
    return comp(out)


def stowed():
    """Rungs folded into the box in three stacks; rope coil and throw weight beside them (world axes)."""
    xf = D["box_front"] + P["box_t"]
    xc = xf + 20 + P["rung_len"] / 2 + 2
    z0 = P["box_z0"] + P["box_t"] + P["foam_od"] / 2
    pieces = []
    stacks = [(-215.0, 5), (-85.0, 4), (45.0, 4)]
    for y, n in stacks:
        for i in range(n):
            z = z0 + i * (P["foam_od"] + 2)
            pieces.append(cyl_x(xc - P["rung_len"] / 2 - 2, xc + P["rung_len"] / 2 + 2, D["ro"], y=y, z=z))
            pieces.append(cyl_x(xc - P["foam_len"] / 2, xc + P["foam_len"] / 2, P["foam_od"] / 2, y=y, z=z))
    rungs = comp(pieces)
    coil = Pos(xc - 60, 200, P["box_z0"] + 40) * Torus(70, 12)
    weight = Pos(xc + 110, 210, P["box_z0"] + 40) * cyl_x(-50, 50, 35)
    return rungs, coil, weight


# ------------------------------------------------------------------ overview
def overview():
    st = M.station()
    L = ladder4()
    sh = (-1500, 0, 1300)              # hang the short ladder beside the post
    T = lambda s: Pos(*sh) * s          # noqa: E731
    rope_only = L["ropes"]
    parts = [
        part("Post", st["post"], "post", (0, 0, 0)),
        part("Concrete footing", st["footing"], "footing", (0, 0, -700)),
        part("Crush tube", st["crush"], "crush", (0, -300, 0)),
        part("Anchor bolt and washers", st["bolt"], "bolt", (380, 0, 0)),
        part("Forged eye nut", st["eyenut"], "eyenut", (-260, 0, -60)),
        part("Box mounting plate", st["plate"], "plate", (-160, 0, 0)),
        part("Square U-bolts", st["ubolts"], "ubolts", (330, 0, 0)),
        part("Storage box with lid", st["box"], "box", (-420, 0, 260)),
        part("Box fixings", st["boxfix"], "boxfix", (-260, -420, 120)),
        part("Post cap", st["cap"], "cap", (0, 0, 260)),
        part("Decals and tamper tag", st["decals"], "decals", (-620, 0, 520)),
        part("Rescue knife", st["knife"], "knife", (-420, 0, 800)),
        part("Rungs (4 of 13 shown)", T(L["rungs"]), "rungs", (0, 0, 0)),
        part("Float sleeves", T(L["foam"]), "foam", (0, -500, 0)),
        part("Wall stand-off blocks", T(L["blocks"]), "blocks", (0, 0, 0)),
        part("Stand-off bolts", T(L["sobolts"]), "sobolts", (0, 0, 120)),
        part("Rope bushes", T(L["bushes"]), "bushes", (0, 0, -90)),
        part("Rung end caps", T(comp([L["caps_l"], L["caps_r"]])), "caps", (0, 0, 0)),
        part("Side ropes with knots", T(rope_only), "ropes", (0, 350, 0)),
        part("Seizings", T(L["seizings"]), "seizings", (0, 350, 60)),
        part("Screw links", T(comp([L["toplink"], L["botlink"]])), "links", (0, 350, 0)),
        part("Soft throw weight", T(L["weight"]), "weight", (0, 350, -200)),
        part("Edge protector sleeves", T(L["protectors"]), "protectors", (0, 600, 0)),
    ]
    # the blocks sit on the rung; pull them out sideways in the picture
    parts[14] = part("Wall stand-off blocks", T(comp([Pos(-160, 0, 0) * L["blocks_l"], Pos(160, 0, 0) * L["blocks_r"]])), "blocks")
    parts[17] = part("Rung end caps", T(comp([Pos(-90, 0, 0) * L["caps_l"], Pos(90, 0, 0) * L["caps_r"]])), "caps")
    return bv.overview(parts, OUT / "overview.png", "CanalRung: every component, in build order",
                       subtitle="Bank station at right, ladder at left (shown with 4 of its 13 rungs); pulled apart and numbered in build order",
                       elev=20, azim=-62, key=True, size=(11, 8))


# ------------------------------------------------------------------ making sketches
def rope_straight(Pp=P):
    """One side rope laid out straight, finished: top loop, knots, bottom loop (Z up)."""
    Dd = M.derived(Pp)
    r = Pp["rope_d"] / 2
    lead = rope_marks()["lead"]
    zt = lead
    zb = Dd["zs"][-1] - 40 - Pp["tail"]
    pieces = [cyl_z(zb, zt, r)]
    pieces += [Pos(0, 0, M.knot_z(k, Pp)) * Sphere_(Pp["knot_r"]) for k in range(1, Pp["n_rungs"] + 1)]
    for z, s in ((zt, 1), (zb, -1)):
        pieces.append(Pos(0, 0, z - s * 20) * Sphere_(Pp["knot_r"]))
        pieces.append(Pos(0, 0, z + s * 45) * Rot(90, 0, 0) * Torus(40, r))
    return comp(pieces)


def Sphere_(r):
    from build123d import Sphere
    return Sphere(r)


def rope_marks():
    from build123d import Vector
    a = Vector(*M.to_world((P["rope_pitch"] / 2, 0, 40.0)))
    e = Vector(-2.0, -130.0, 5.5)
    k = Vector(D["eye_cx"] - 2 * P["link_major"] - 30, -8.0, P["eye_z"])
    lead = (a - e).length + (e - k).length + 30 + 40
    return {"lead": lead, "cut": M.rope_cut_length()}


def sheets(which=None):
    st = M.station()
    L13 = M.ladder_local(P, hang=False)
    jobs = {}
    nb = [part(n, st[k], k) for n, k in (("Footing", "footing"), ("Crush tube", "crush"), ("Bolt", "bolt"), ("Eye nut", "eyenut"),
                                         ("Plate", "plate"), ("U-bolts", "ubolts"), ("Box", "box"), ("Cap", "cap"))]
    jobs[101] = (part("Post", st["post"], "post"), nb, "Post: making sketch", "Hot-dip galvanised steel 60 x 60 x 3 SHS, S235 or better", [
        "Cut 2,300 long, square; file the burr off both ends.",
        "Mark one face as the canal side. 1,350 up from the bottom end",
        "(250 above ground when set), on the face centre line:",
        "  canal-side wall: drill 17.5 for the M16 bolt;",
        "  back wall, same axis: drill 21.5 for the crush tube.",
        "Use a drill guide or drill press so both holes share one axis.",
        "Deburr; cold galvanising paint on the holes and cut ends.",
        "Mark a ground line 1,100 up from the bottom end.",
        "Fits: 1,100 sits in the footing, 100 above its base;",
        "plate and box on the canal face; cap on top."], None)
    jobs[102] = (part("Crush tube", st["crush"], "crush"), [part("Post", win(st["post"], 900, 1100, -80, 80, 150, 350), "post"),
                                                           part("Bolt", st["bolt"], "bolt")],
                 "Crush tube: making sketch", "Steel tube 21.3 x 2.0 (1/2 in pipe class)", [
        "Cut 57 long; ends square to 0.5; deburr inside and out.",
        "Bore 17.3 passes the M16 bolt; 21.3 outside slides",
        "into the 21.5 hole in the back wall of the post.",
        "Fits: one end bears on the inside of the canal-side wall;",
        "the other is flush with the back face, under the 50 mm",
        "washer. It stops the bolt crushing the post walls.",
        "Check: push it in; it must stop on the far wall with its",
        "end flush (within 0.5) with the back face."], None)
    jobs[103] = (part("Footing", st["footing"], "footing"), [part("Post", st["post"], "post")],
                 "Concrete footing: making sketch", "25 MPa concrete, about 0.23 m3 (about 22 bags of 25 kg)", [
        "Hole 500 dia x 1,200 deep, centre 1,000 back from the",
        "coping; keep it clear of the lining and any drains.",
        "100 of concrete under the post; post bottom 1,100 down.",
        "Crown the top 10 to 20 above ground so water runs off.",
        "This is the standard footing at every site, wet or",
        "dry bank (calculation note, G4 and G5).",
        "Fits: concrete wraps the bottom 1,100 of the post and",
        "fills its bottom end.",
        "Check: post plumb in both directions within 5 over 1 m."], None)
    jobs[104] = (part("Plate", st["plate"], "plate"), [part("Post", win(st["post"], 900, 1100, -80, 80, 400, 850), "post"),
                                                       part("U-bolts", st["ubolts"], "ubolts"), part("Box", st["box"], "box")],
                 "Box mounting plate: making sketch", "Aluminium sheet 5052 or 6061, 4 mm, 400 x 300", [
        "Cut 400 wide x 300 tall; round the corners about 5;",
        "file every edge.",
        "Four 9 mm holes for the U-bolt legs: 34 each side of",
        "the centre line, 80 and 240 up from the bottom edge.",
        "Deburr both faces.",
        "Fits: flat on the canal face of the post, bottom edge",
        "480 above ground; the box back wall sits flat on its",
        "other face; the U-bolt legs pass through both."], None)
    jobs[105] = (part("Box", st["box"], "box"), [part("Plate", st["plate"], "plate"), part("Post", win(st["post"], 900, 1100, -80, 80, 300, 1000), "post"),
                                                 part("U-bolts", st["ubolts"], "ubolts")],
                 "Storage box: drilling sketch", "Bought 70 L UV-stabilised box, about 450 x 650 x 360 outside", [
        "Back wall (against the plate): four 9 mm holes, 34 each",
        "side of the centre line, 110 and 270 up from the base",
        "outside (drill through the plate as a template).",
        "Base: four 8 mm drain holes, 40 in from each corner.",
        "Front rim: notch 30 wide x 25 deep at the centre, for",
        "the ropes to pass under the closed lid.",
        "Fits: base 450 above ground; lid hinge at the back."], None)
    # ladder parts (local axes), shown on rung 3, a stand-off rung
    nr = [part("Bushes", comp([M.bush(3, s) for s in (-1, 1)]), "bushes"), part("Foam", M.foam(3), "foam"),
          part("Blocks", comp([M.block(3, s) for s in (-1, 1)]), "blocks"), part("Caps", comp([M.end_cap(3, s) for s in (-1, 1)]), "caps")]
    z3 = D["zs"][2]
    jobs[106] = (part("Rung", M.rung_tube(3), "rungs"), nr, "Rung: making sketch (make 13)", "Aluminium 6061-T6 tube 28.6 x 1.65 (1-1/8 x 0.065 in)", [
        "Cut 360 long, ends square; deburr inside and out.",
        "Rope holes: 16 dia right across the tube, 20 in from",
        "each end; drill through both walls on one line (use a",
        "V-block and a drill press; pilot 6 first).",
        "Rungs 3, 6, 9 and 12 only: two 5.3 holes across the",
        "tube, 40 in from each end, on the same line as the",
        "rope holes.",
        "Round every hole edge with a deburring tool so no",
        "sharp edge is left for the bush or the rope.",
        "Check: a 16 rod passes straight through both holes."], Pos(0, 0, -z3) * M.rung_tube(3))
    jobs[107] = (part("Foam", M.foam(1), "foam"), [part("Rung", M.rung_tube(1), "rungs"), part("Bushes", comp([M.bush(1, s) for s in (-1, 1)]), "bushes")],
                 "Float sleeve: making sketch (make 13)", "Closed-cell cross-linked PE foam tube, 50 OD x 28 bore, orange", [
        "Cut with a sharp knife against a square end stop:",
        "nine sleeves 294 long (plain rungs) and four 260 long",
        "(stand-off rungs 3, 6, 9 and 12).",
        "Check it is closed-cell: a cut end must not take up water.",
        "Fits: slides over the rung (stretch fit on 28.6) before",
        "the blocks and bushes; centred, 2 clear of the bush",
        "flanges or blocks at each end. A bead of polyurethane",
        "adhesive inside each end stops it turning."], Pos(0, 0, 0) * M.foam(1))
    jobs[108] = (part("Block", M.block(3, 1), "blocks"), [part("Rung", M.rung_tube(3), "rungs"), part("Foam", M.foam(3), "foam"),
                                                           part("Bush", M.bush(3, 1), "bushes")],
                 "Wall stand-off block: making sketch (make 8)", "HDPE sheet 16 mm, UV-stabilised", [
        "Mark the outline from this sketch: 115 long, 40 tall at",
        "the rung end, tapering to a 24 tall nose over the last 60.",
        "Saw and file; round the nose corners 4 so it slides",
        "on concrete.",
        "28.8 hole for the rung, centre 20 from the back end",
        "and on the height centre line (step drill or hole saw).",
        "5.3 hole straight down through the middle of the 16",
        "thickness, crossing the rung hole.",
        "Fits: on the rung just inside the bush, nose toward the",
        "wall, held by one M5 x 50 bolt through block and rung."], M.block_profile_solid())
    rm = rope_marks()
    jobs[109] = (part("Rope", rope_straight(), "ropes"), [], "Side rope: making sketch (make 2)",
                 "9 mm EN 1891 type B low-stretch kernmantle, polyester preferred", [
        f"Cut {rm['cut'] / 1000:.1f} m; tape, cut and heat seal both ends.",
        "Top loop: figure-eight on a bight with a 60 tail, loop",
        "about 80 long (fits the 10 mm screw link).",
        f"From the loop's knot measure {rm['lead']:,.0f} down: mark rung 1.",
        f"Then mark every {P['pitch']:.0f} for rungs 2 to 13 (12 more marks).",
        "Mark both ropes side by side so the marks match.",
        "At each mark: overhand stopper knot, its top at the mark,",
        "tied when the rung is threaded (build step 11).",
        f"Below rung 13: {P['tail']:.0f} to a figure-eight loop for the bottom link.",
        "Dress and set every knot by hand before loading."], None)
    for n, (pt, nbr, title, mat, notes, vs) in jobs.items():
        if which and n not in which:
            continue
        print(bv.component_sheet(pt, nbr, "CanalRung", f"CNR-DWG-{n}", title, mat, notes, DATE, view_shape=vs))


# ------------------------------------------------------------------ joints
def joints(which=None):
    st = M.station()
    out = {}
    z = P["eye_z"]

    def j1():
        return bv.joint([part("Post", win(st["post"], 900, 1100, -100, 100, -1200, 300), "post"),
                         part("Concrete footing", win(st["footing"], 700, 1300, -300, 300, -1200, 0), "footing")],
                        OUT / "joint-01.png", "Joint 1: post in the concrete footing", "Cut open; 1,100 of post in 1,200 of concrete", cut="+Y")

    def j2():
        _, _, tl = M.top_lead()
        return bv.joint([part("Post (canal-side wall left)", win(st["post"], 940, 1060, -60, 60, z - 70, z + 70), "post"),
                         part("Crush tube", st["crush"], "crush"), part("M16 bolt, 50 mm washer at the back", st["bolt"], "bolt"),
                         part("Forged eye nut on 30 mm washer", st["eyenut"], "eyenut"), part("Top screw link", tl, "links")],
                        OUT / "joint-02.png", "Joint 2: anchor bolt, crush tube and eye nut",
                        "Cut open on the bolt axis; the crush tube carries the clamp load across the post", cut="+Y", azim=-70)

    def j3():
        zc = 640
        return bv.joint([part("Post", win(st["post"], 950, 1060, -60, 60, 500, 780), "post"),
                         part("Mounting plate", win(st["plate"], 960, 980, -120, 120, 500, 780), "plate"),
                         part("Box back wall", win(M.storage_box(lid=False), 955, 970, -120, 120, 500, 780), "box"),
                         part("U-bolts", st["ubolts"], "ubolts"), part("Fender washers and nyloc nuts", st["boxfix"], "boxfix")],
                        OUT / "joint-03.png", "Joint 3: box, plate and post clamped by two U-bolts",
                        "Seen from inside the box; the U-bolts go round the back of the post", elev=20, azim=-150)

    def j4():
        k, s = 1, 1
        zc = D["zs"][0]
        return bv.joint([part("Rung tube", win(M.rung_tube(k), 120, 190, -20, 20, zc - 20, zc + 20), "rungs"),
                         part("Float sleeve", win(M.foam(k), 110, 150, -30, 30, zc - 30, zc + 30), "foam"),
                         part("Nylon bush, flange down", M.bush(k, s), "bushes"), part("End cap", M.end_cap(k, s), "caps"),
                         part("Rope", win(M.rope_local(s, 120.0), 140, 180, -10, 10, zc - 70, zc + 90), "ropes"),
                         part("Seizing above the rung", M.seizing(k, s), "seizings")],
                        OUT / "joint-04.png", "Joint 4: rope through the rung end",
                        "Cut on the rope; the overhand knot under the bush flange carries the rung, the seizing stops it lifting",
                        cut="+Y", elev=12, azim=-80)

    def j5():
        k = 3
        zc = D["zs"][k - 1]
        return bv.joint([part("Rung tube", win(M.rung_tube(k), 90, 185, -20, 20, zc - 20, zc + 20), "rungs"),
                         part("Float sleeve", win(M.foam(k), 80, 140, -30, 30, zc - 30, zc + 30), "foam"),
                         part("Stand-off block", M.block(k, 1), "blocks"), part("M5 x 50 bolt and nyloc nut", M.so_bolt(k, 1), "sobolts"),
                         part("Bush", M.bush(k, 1), "bushes"), part("End cap", M.end_cap(k, 1), "caps")],
                        OUT / "joint-05.png", "Joint 5: wall stand-off block on rungs 3, 6, 9 and 12",
                        "Nose toward the wall (+Y); the bolt locks the block to the rung", elev=22, azim=-35)

    def j6():
        lead, prot, tl = M.top_lead()
        return bv.joint([part("Eye nut", st["eyenut"], "eyenut"),
                         part("Post", win(st["post"], 960, 1040, -40, 40, z - 60, z + 60), "post"),
                         part("Top screw link, gate closed", tl, "links"),
                         part("Rope figure-eight loops", win(lead, 700, 900, -60, 60, z - 60, z + 60), "ropes")],
                        OUT / "joint-06.png", "Joint 6: rope loops on the top screw link",
                        "Both loops in the link; the link through the eye; gate screwed shut", elev=30, azim=-120)

    def j7():
        Dd = D
        zl = Dd["zs"][-1]
        L = M.ladder_local(P, hang=False)
        return bv.joint([part("Bottom rung", win(L["rungs"], -200, 200, -30, 30, zl - 20, zl + 20), "rungs"),
                         part("Float sleeve", win(L["foam"], -200, 200, -40, 40, zl - 30, zl + 30), "foam"),
                         part("Ropes and knots", win(L["ropes"], -200, 200, -30, 30, zl - 400, zl + 60), "ropes"),
                         part("Bottom screw link", M.link((0, 0, zl - P["tail"]), "Y"), "links"),
                         part("Soft throw weight on its webbing loop", L["weight"], "weight")],
                        OUT / "joint-07.png", "Joint 7: bottom end and throw weight",
                        f"The two rope tails meet in one link {P['tail']:.0f} below the bottom rung", elev=15, azim=-70)

    def j8():
        lead, prot, _ = M.top_lead()
        s = M.site(yw=450)
        return bv.joint([part("Coping and lining (site)", win(s["lining"], -400, 150, -250, 250, -300, 10), "site"),
                         part("Bank (site)", win(s["bank"], 0, 300, -250, 250, -100, 0), "site"),
                         part("Edge protector sleeves", prot, "protectors"),
                         part("Ropes", win(lead, -300, 300, -250, 250, -100, 120), "ropes")],
                        OUT / "joint-08.png", "Joint 8: ropes over the coping in their edge protectors",
                        "The sleeves slide on the rope and sit on the edge when the ladder is thrown", elev=25, azim=-140)

    fns = {1: j1, 2: j2, 3: j3, 4: j4, 5: j5, 6: j6, 7: j7, 8: j8}
    for n, f in fns.items():
        if which and n not in which:
            continue
        print(f())


# ------------------------------------------------------------------ steps
def steps(which=None):
    st = M.station()
    L = ladder4()
    lead, prot, tl = M.top_lead()
    S = lambda n, k, e=(0, 0, 0): part(n, st[k], k, e)   # noqa: E731
    G = lambda n, k, e=(0, 0, 0): part(n, L[k], k if k in C else "ropes", e)   # noqa: E731
    rung_set = [G("Rungs", "rungs")]
    foam_p = G("Float sleeves", "foam", (330, 0, 0))
    blocks_p = [part("Stand-off block, left", L["blocks_l"], "blocks", (-140, 0, 0)),
                part("Stand-off block, right", L["blocks_r"], "blocks", (140, 0, 0)),
                part("M5 bolts", L["sobolts"], "sobolts", (0, 0, 90))]
    bush_caps = [part("Rope bushes (from below)", L["bushes"], "bushes", (0, 0, -70)),
                 part("End caps, left", L["caps_l"], "caps", (-70, 0, 0)), part("End caps, right", L["caps_r"], "caps", (70, 0, 0))]
    rung_done = rung_set + [part("Float sleeves", L["foam"], "foam"), part("Blocks", L["blocks"], "blocks"),
                            part("Bolts", L["sobolts"], "sobolts"), part("Bushes", L["bushes"], "bushes"),
                            part("Caps", comp([L["caps_l"], L["caps_r"]]), "caps")]
    ropes_p = part("Side ropes, top loops on the link", comp([L["ropes"], L["toplink"]]), "ropes", (0, 0, 0))
    stn = [S("Post", "post"), S("Footing", "footing")]
    rungs_box, coil, wt = stowed()
    T = {
        1: ([], [S("Post", "post", (0, 0, 700))], "Step 1: stand the post in the hole",
            "Hole 500 dia x 1,200 deep; post on 100 of concrete, plumb and braced", [part("Footing hole", st["footing"], "footing")]),
        2: ([S("Post", "post")], [S("Concrete footing", "footing", (0, 0, -350))], "Step 2: pour the footing",
            "Fill in layers, rod each one; crown the top; leave 7 days before loading", []),
        3: (stn, [S("Crush tube", "crush", (300, 0, 0))], "Step 3: crush tube into the post",
            "In through the 21.5 hole in the back wall until it stops on the far wall", []),
        4: (stn + [S("Crush tube", "crush")], [S("Bolt with 50 mm washer", "bolt", (300, 0, 0)), S("Eye nut on 30 mm washer", "eyenut", (-220, 0, 0))],
            "Step 4: anchor bolt and eye nut", "Bolt from the back; eye nut with threadlocker, ring upright, facing the canal", []),
        5: (stn + [S("Eye nut", "eyenut"), S("Bolt", "bolt")], [S("Mounting plate", "plate", (-200, 0, 0)), S("U-bolts", "ubolts", (300, 0, 0))],
            "Step 5: mounting plate and U-bolts", "Plate on the canal face, bottom edge 480 up; U-bolts round the back of the post", []),
        6: (stn + [S("Plate", "plate"), S("U-bolts", "ubolts"), S("Eye nut", "eyenut")], [S("Storage box", "box", (-450, 0, 0))],
            "Step 6: box onto the U-bolt legs", "Back wall flat on the plate; lid hinge at the back", []),
        7: (stn + [S("Plate", "plate"), S("U-bolts", "ubolts"), S("Box", "box")],
            [S("Washers and nyloc nuts", "boxfix", (0, 0, 420)), S("Post cap", "cap", (0, 0, 250)),
             S("Decals and tag", "decals", (-250, 0, 0)), S("Knife", "knife", (0, 0, 500))],
            "Step 7: box fixings, post cap, decals and knife", "Nuts inside the box, snug, not crushing it; knife tethered under the lid", []),
        8: (rung_set, [foam_p], "Step 8: float sleeves onto the rungs",
            "Short ladder shown (4 of 13 rungs); 260 sleeves on the stand-off rungs", []),
        9: (rung_set + [part("Float sleeves", L["foam"], "foam")], blocks_p, "Step 9: stand-off blocks on rungs 3, 6, 9 and 12",
            "Slide on from each end, nose toward the wall; M5 bolt down through block and rung", []),
        10: (rung_set + [part("Float sleeves", L["foam"], "foam"), part("Blocks", L["blocks"], "blocks"), part("Bolts", L["sobolts"], "sobolts")],
             bush_caps, "Step 10: rope bushes and end caps", "Bushes up from below, flange under the rung; caps tapped into both ends", []),
        11: (rung_done, [ropes_p], "Step 11: thread the ropes and tie the knots",
             "Hang the top link; thread each rung from the bottom end and knot under it at its mark", []),
        12: (rung_done + [part("Ropes", comp([L["ropes"], L["toplink"]]), "ropes")], [part("Seizings", L["seizings"], "seizings", (0, -120, 60))],
             "Step 12: seizings above every rung end", "20 long, tight, with the ends tucked; they stop the rung floating up the rope", []),
        13: (rung_done + [part("Ropes", comp([L["ropes"], L["toplink"]]), "ropes")],
             [part("Bottom link", L["botlink"], "links", (0, 0, -150)), part("Throw weight", L["weight"], "weight", (0, 0, -300))],
             "Step 13: bottom link and throw weight", "Both bottom loops and the weight's webbing loop in one link; gate shut", []),
        14: (rung_done + [part("Ropes", comp([L["ropes"], L["toplink"]]), "ropes")], [part("Edge protectors", L["protectors"], "protectors", (0, -200, 0))],
             "Step 14: edge protectors on the top lead", "Wrap round each rope above rung 1 and close the hook-and-loop", []),
        15: ([S("Post", "post"), S("Footing", "footing"), S("Eye nut", "eyenut"), S("Box", "box"), S("Plate", "plate")],
             [part("Top link with the rope loops", comp([tl, lead]), "ropes", (-250, 0, 150))],
             "Step 15: top link onto the eye nut", "Open the gate, through the eye, screw the gate fully shut", []),
        16: ([S("Post", "post"), S("Footing", "footing"), S("Eye nut", "eyenut"), S("Plate", "plate"),
              part("Box (lid open)", M.storage_box(lid=False), "box")],
             [part("Ladder folded into the box", rungs_box, "foam", (0, 0, 600)), part("Rope coil", coil, "ropes", (0, 0, 600)),
              part("Throw weight on top", wt, "weight", (0, 0, 700))],
             "Step 16: fold the ladder into the box", "Rungs in three stacks, top rung at the bottom; throw weight last, on top", []),
    }
    for n, (done, new, title, sub, ctx) in T.items():
        if which and n not in which:
            continue
        el, az = (22, -60) if n <= 7 or n >= 15 else (18, -55)
        if n in (3, 4, 5, 6, 7, 15, 16):
            az = -140
        print(bv.step(done, new, OUT / f"step-{n:02d}.png", title, sub, context=ctx, elev=el, azim=az))


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    nums = [int(a) for a in sys.argv[2:]] or None
    if what in ("overview", "all"):
        print(overview())
    if what in ("sheets", "all"):
        sheets(nums)
    if what in ("joints", "all"):
        joints(nums)
    if what in ("steps", "all"):
        steps(nums)
