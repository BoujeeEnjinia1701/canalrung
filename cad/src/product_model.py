"""CanalRung product appearance model (build123d), TRL 3, constructable design (CNR-DDR-002, CNR-DDR-003).

Finished-product look for photoreal renders (kit 1.9). The product is model.components("A"): every part of the
detailed model (178 parts with bolts, washers, bushes, caps, seizings, links and sleeves), lifted so that ground level
is Z = 0 (the top of the concrete canal bed; the coping is 3,000 mm above it, the design water line 1,000 mm above it).
Nothing is re-dimensioned here. Context: the embankment, concrete lining and water of the design canal (parts named
"(site)", which reach below ground), a 1.75 m mannequin standing on the bank top, and for the detail view a short length
of ladder (rungs 2 and 3) with a gripping hand for scale.
APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR FABRICATION.

Axes as model.py: canal along Y, bank X >= 0, coping edge X = 0, Z up. Groups: "station" and
"ladder" (the product), "context" (bank, lining, water, mannequin), "detail" (two rungs of the
ladder in its own axes) and "detail_context" (the hand).

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Pos, Rot  # noqa: E402
import model as M  # noqa: E402

TITLE = "CanalRung: throwable floating ladder and bank station for lined canals"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["station", "ladder", "context"], "explode": False, "el": 24, "az": -135,
     "args": ["--scene=outdoor", "--ground=grass", "--ground-z=0", "--sun=40,-110", "--lens=35"],
     "note": "Product render from the canal side, upstream and above (about 24 deg elevation): the ladder thrown from "
             "its bank station and lying down a 1.5:1 concrete-lined wall on its stand-offs, lowest rungs floating at "
             "the water line 2.0 m below the coping; 1.75 m person standing on the bank for scale"},
    {"name": "exploded", "groups": ["station", "ladder"], "explode": True, "el": 24, "az": -135,
     "note": "Exploded view from the canal side and above (about 24 deg elevation): post, footing, anchor bolt and "
             "eye nut, mounting plate, U-bolts and storage box; ladder parts pulled out from the wall (bushes, end "
             "caps, float sleeves, stand-off blocks, ropes, seizings, links, throw weight)"},
    {"name": "detail", "groups": ["detail", "detail_context"], "explode": False, "el": 20, "az": -60,
     "note": "Detail from the water side and above (about 20 deg elevation): a plain rung and a stand-off rung with "
             "their orange float sleeves, nylon rope bushes, end caps, the HDPE stand-off blocks and the side ropes "
             "with a stopper knot under each rung end; a hand gripping a rung for scale"},
]

COLORS = {"rungs": "#D4D4D8", "bushes": "#F5F5F4", "caps": "#111827", "foam": "#F97316", "blocks": "#1F2937",
          "sobolts": "#A1A1AA", "ropes": "#DC2626", "seizings": "#111827"}          # detail view only
MATERIAL = {"rungs": "metal", "bushes": "plastic", "caps": "plastic", "foam": "rubber", "blocks": "plastic",
            "sobolts": "metal", "ropes": "fabric", "seizings": "fabric"}
# photoreal material class of each cad_parts material
CLASS = {"galvanised": "metal", "aluminium": "metal", "stainless": "metal", "zinc_plated": "metal", "mild_steel": "metal",
         "hdpe_black": "plastic", "hdpe_natural": "plastic", "safety_red": "plastic", "insulated_white": "rubber",
         "rope": "fabric", "canvas": "fabric", "concrete": "paper", "label": "paper", "soil": "rubber", "water": "clear"}
# exploded view offsets by BOM line (mm); ladder lines move out of the wall
EXPLODE = {2: (0, 0, -850), 3: (0, -260, 0), 4: (320, 0, 0), 5: (-260, 0, -120), 6: (-180, 0, 0), 7: (300, 0, 120),
           8: (-520, 0, 420), 9: (-330, 0, 200), 10: (0, 0, 300), 11: (-600, 0, 560), 12: (-520, 0, 900),
           23: (0, 0, 450)}
OUT_OF_WALL = {14: 380, 15: -120, 16: 1150, 17: 900, 18: 650, 19: 1450, 20: 1750, 21: 2000, 22: 2300}


def product_parts(P=M.PARAMS):
    D = M.derived(P)
    out = []

    def add(name, shape, color, material, bom, group, explode=(0, 0, 0)):
        out.append(dict(name=name, shape=shape, color=color, material=material, bom=bom, group=group, explode=explode))

    for c in M.components("A", P):
        if c["kind"] == "context":
            continue
        ex = tuple(OUT_OF_WALL.get(c["bom"], 0) * v for v in D["n"]) if c["bom"] in OUT_OF_WALL else EXPLODE.get(c["bom"], (0, 0, 0))
        add(c["name"], c["shape"], c["color"], CLASS.get(c["material_name"], "plastic"), c["bom"], c["group"],
            (ex[0], ex[1], ex[2]))

    from cnr_geom import COPING_Z, site_parts
    for c in site_parts(P, yw=900.0, far=False, crest=3000.0, outer_run=1.5):
        nm = c["name"].replace("Embankment, near bank", "Embankment, grass")
        add(nm, c["shape"], {"soil": "#7C8B5A", "concrete": "#CFCBC4", "water": "#3B82F6"}[c["material_name"]],
            {"soil": "rubber", "concrete": "paper", "water": "clear"}[c["material_name"]], None, "context")
    from context_parts import mannequin, forearm_hand
    person = Pos(620, 560, COPING_Z) * Rot(0, 0, -90) * mannequin(1750, "stand")
    add("Person, 1.75 m mannequin (scale)", person, "#B9B4AC", "clay", None, "context")

    # detail: rungs 2 and 3 of the ladder in its own axes (rungs along X, up the ladder Z, wall side +Y)
    ks = (2, 3)
    det = {
        "rungs": M.comp([M.rung_tube(k, P) for k in ks]),
        "foam": M.comp([M.foam(k, P) for k in ks]),
        "bushes": M.comp([M.bush(k, sx, P) for k in ks for sx in (-1, 1)]),
        "caps": M.comp([M.end_cap(k, sx, P) for k in ks for sx in (-1, 1)]),
        "blocks": M.comp([M.block(3, sx, P) for sx in (-1, 1)]),
        "sobolts": M.comp([M.so_bolt(3, sx, P) for sx in (-1, 1)]),
        "seizings": M.comp([M.seizing(k, sx, P) for k in ks for sx in (-1, 1)]),
    }
    z2, z3 = D["zs"][1], D["zs"][2]
    rope = []
    for sx in (-1, 1):
        x = sx * P["rope_pitch"] / 2
        rope.append(M.cyl_z(z3 - 120, z2 + 120, P["rope_d"] / 2, x=x))
        rope += [Pos(x, 0, M.knot_z(k, P)) * M.Sphere(P["knot_r"]) for k in ks]
    det["ropes"] = M.comp(rope)
    for key, shp in det.items():
        add(f"Detail: {M.BOM[key][1]}", shp, COLORS[key], MATERIAL[key], M.BOM[key][0], "detail")
    hand = forearm_hand("right", "grip", grip_d=P["foam_od"])
    # grip axis of the kit hand lies along its Y at about x = 88, z = -36; turn it onto the rung axis
    hand = Pos(-40, -88, z2 + 36) * Rot(0, 0, 90) * hand
    add("Hand and forearm (scale)", hand, "#B9B4AC", "clay", None, "detail_context")
    return out


if __name__ == "__main__":
    for p in product_parts():
        s = p["shape"]
        print(f"{p['name']:58s} {p['group']:15s} {p['material']:8s} vol={s.volume / 1000:10.2f} cm3")
