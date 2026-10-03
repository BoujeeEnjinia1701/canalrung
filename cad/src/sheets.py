"""CanalRung general arrangement sheet CNR-DWG-001, Rev P2 (TRL 3; constructable design CNR-DDR-002).

Run from the repo root:  python cad/src/sheets.py
Writes cad/drawings/CNR-DWG-001.svg, .pdf and .png from cad/src/model.py with .kit/drawing.py.
The station and the thrown ladder are drawn on the design wall (1.5:1 lined slope, water 2.0 m
below the coping). Small parts (bushes, end caps, knots, seizings, fixings) are left out at this
scale; they are on the making sketches CNR-DWG-101 to 108. The concept sheet is CNR-DWG-010.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Compound  # noqa: E402
from drawing import Sheet, project_views, _viewbox, _t, M as MARGIN, TB_Y, INK, MUTED  # noqa: E402
import model as M  # noqa: E402

P, D = M.PARAMS, M.derived()
DATE_P1, DATE = "2026-10-03", "2026-10-03"


def cells(sheet, views, k):
    """Where add_ortho put each view (x, y, w, h), repeating its layout arithmetic (kit 1.7)."""
    ax, ay, aw, ah = MARGIN + 10, MARGIN + 16, 245, TB_Y - MARGIN - 20
    gap, lab, dl = 14, 12, 11
    v = {n: _viewbox(Path(views[n]).read_text())[2:] for n in ("front", "top", "right")}
    fw, fh = v["front"]
    tw, th = v["top"]
    rw, rh = v["right"]
    ax += (aw - (k * (max(fw, tw) + rw) + gap + dl)) / 2 + dl
    ay += (ah - (k * (th + max(fh, rh)) + gap + 2 * lab + dl)) / 2 + dl
    colw = k * max(fw, tw)
    fy = ay + k * th + lab + gap
    return {"top": (ax, ay, colw, k * th), "front": (ax, fy, colw, k * max(fh, rh)),
            "right": (ax + colw + gap, fy, k * rw, k * max(fh, rh))}


def main():
    work = ROOT / "cad" / "drawings" / "_views"
    light = M.simple_parts()
    site = M.site(yw=450.0)
    asm = Compound(list(light.values()) + [site["lining"], site["bank"]])
    views = project_views(asm, work)
    bb = asm.bounding_box()
    s = Sheet(project="CanalRung", title="Throwable canal ladder and bank station: general arrangement",
              dwg_no="CNR-DWG-001", rev="P2", author="Amish Chadha", date=DATE, scale=1 / 50, theme="technical", concept="PRELIMINARY, NOT FOR FABRICATION",
              material="Steel post, aluminium rungs, kernmantle rope; see bom/bom.csv. PRELIMINARY, NOT FOR FABRICATION",
              revisions=[("P1", "Preliminary GA for TRL 3 (from cad/src/model.py)", DATE_P1, "AC"),
                         ("P2", "CNR-DDR-002: design for construction", DATE, "AC")])
    s.add_ortho(views)
    k = s.scale
    c = cells(s, views, k)
    L = []

    # front view (looking along +Y): X to the right, Z up
    x, y, w, h = c["front"]
    X = lambda mx: x + (mx - bb.min.X) * k   # noqa: E731
    Z = lambda mz: y + h - (mz - bb.min.Z) * k   # noqa: E731
    ztop = P["post_len"] - P["post_embed"]
    s._dim(X(0), Z(0), X(P["post_x"]), Z(0), f"{P['post_x']:,.0f} coping to post", "above", off=Z(0) - Z(ztop) + 6)
    s._dim(X(P["post_x"] + 30), Z(0), X(P["post_x"] + 30), Z(ztop), f"{ztop:,.0f}", "right", off=6)
    s._dim(X(P["post_x"] + 200), Z(0), X(P["post_x"] + 200), Z(-P["footing_depth"]), f"{P['footing_depth']:,.0f}", "right", off=4)
    s._dim(X(-P["water_drop"] * P["slope_h"]), Z(-P["water_drop"]), X(-P["water_drop"] * P["slope_h"]), Z(0),
           f"{P['water_drop']:,.0f}", "left", off=8)
    L.append(_t(X(-P["water_drop"] * P["slope_h"]) - 13, Z(-P["water_drop"]) - 1.0, "DESIGN WATER LINE", 1.9, 400, MUTED, "end"))
    L.append(_t(X(-1200), Z(-1500), "1.5:1 LINED WALL (SITE)", 1.9, 400, MUTED, "middle"))
    L.append(_t(X(420), Z(-700), f"EYE NUT (5), {P['eye_z']:.0f} ABOVE GROUND", 1.9, 400, INK, "middle"))
    L.append(_t(X(-2000), Z(200), "13 RUNGS AT 335 PITCH (13)", 1.9, 400, INK, "middle"))
    L.append(_t(X(P["post_x"]), Z(-P["footing_depth"]) + 4, "FOOTING 400 DIA (2)", 1.9, 400, INK, "middle"))

    s._layers += L
    s.add_svg(views["iso"], 276, 36, 140, 84, label="Isometric view",
              sublabel="Not to scale; seen from the bank side, front right and above; grey wall is the site")
    m = M.masses()
    s.add_notes("Main dimensions and interfaces (mm)", [
        f"Post 60 x 60 x 3 SHS x {P['post_len']:,.0f}; {P['post_embed']:.0f} in a {P['footing_d']:.0f} x {P['footing_depth']:,.0f} footing",
        f"Post centre {P['post_x']:,.0f} back from the coping; top {ztop:,.0f} above ground",
        f"Anchor: M16 forged eye nut on an M16 x 90 bolt, {P['eye_z']:.0f} above ground",
        f"Box about {P['box'][0]:.0f} x {P['box'][1]:.0f} x {P['box'][2]:.0f}, base {P['box_z0']:.0f} up; 2 square U-bolts M8",
        f"Ladder: {P['n_rungs']} rungs, {P['pitch']:.0f} pitch, ropes {P['rope_pitch']:.0f} apart; section {D['span']:,.0f}",
        f"Rung 28.6 x 1.65 Al tube x {P['rung_len']:.0f}; foam float sleeve 50 OD",
        f"Stand-offs on rungs 3, 6, 9, 12: rung axis {P['so_depth']:.0f} off the wall",
        f"Ropes 10.5 kernmantle, about 8.0 m each; knot under every rung end",
        f"Ladder as thrown about {m['total']:.1f} kg; soft 0.5 kg throw weight",
        "Small parts (bushes, caps, knots, seizings): DWG-106, 109",
        "Third-angle; front view from -Y; canal along Y; (n) = BOM line",
    ], x=276, y=136, width=146)
    out = s.save(ROOT / "cad" / "drawings" / "CNR-DWG-001")
    shutil.rmtree(work, ignore_errors=True)
    print(f"wrote {out} and .pdf, .png at scale 1:{1 / k:g}")


if __name__ == "__main__":
    main()
