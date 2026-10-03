"""CanalRung concept media from the TRL 3 parametric model (constructable design, CNR-DDR-002).

Run from the repo root:  python cad/src/concept_media.py [hero|exploded|web|blueprint ...]
With no argument it draws everything; on a small machine run one picture per process.
Geometry comes from cad/src/model.py; key figures from docs/04-calcs/sizing.py (CNR-CAL-001).
Uses the pieces of .kit/concept.py render_all one at a time, because the ladder lies on a wall
that faces the canal, so the hero is seen from the canal side rather than the kit's default.
No cutaway (the joints that matter are shown cut open in the build plan) and no flow diagram
(the station moves no energy or material). CONCEPT, NOT FOR FABRICATION.

Axes as model.py: the canal runs along Y, the bank is X >= 0, the coping edge is X = 0, Z = 0.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import concept as K  # noqa: E402
from concept import Part  # noqa: E402
from build123d import Compound, Color, Pos, Rot, export_gltf  # noqa: E402
import model as M  # noqa: E402

PROJECT, TITLE, DWG, DATE = "CanalRung", "Throwable floating canal ladder and bank station", "CNR-DWG-010", "2026-10-03"
MD = ROOT / "media"

COLORS = {"post": "#9CA3AF", "crush": "#6B7280", "footing": "#D6D3D1", "bolt": "#374151", "eyenut": "#B45309",
          "plate": "#CBD5E1", "ubolts": "#4B5563", "box": "#EAB308", "boxfix": "#111827", "cap": "#1F2937",
          "rungs": "#D1D5DB", "bushes": "#F5F5F4", "caps": "#111827", "foam": "#F97316", "blocks": "#374151",
          "sobolts": "#6B7280", "ropes": "#DC2626", "seizings": "#111827", "links": "#71717A", "weight": "#16A34A",
          "protectors": "#0F766E", "decals": "#1D4ED8", "knife": "#111827"}

D = M.derived()
_n = D["n"]


def out_of_wall(k):
    return tuple(k * c for c in _n)


EXPLODE = {"post": (0, 0, 0), "crush": (0, -260, 0), "footing": (0, 0, -850), "bolt": (320, 0, 0),
           "eyenut": (-260, 0, -120), "plate": (-180, 0, 0), "ubolts": (300, 0, 120), "box": (-520, 0, 420),
           "boxfix": (-330, 0, 200), "cap": (0, 0, 300), "decals": (-600, 0, 560), "knife": (-520, 0, 900),
           "rungs": (0, 0, 0), "bushes": out_of_wall(900), "caps": out_of_wall(650), "foam": out_of_wall(380),
           "blocks": out_of_wall(-120), "sobolts": out_of_wall(1150), "ropes": out_of_wall(1450),
           "seizings": out_of_wall(1750), "links": out_of_wall(2000), "weight": out_of_wall(2300),
           "protectors": (0, 0, 450)}


def parts():
    return [Part(c.name, c.shape, COLORS[c.key], c.bom, EXPLODE[c.key]) for c in M.components()]


def context():
    s = M.site(yw=900.0)
    from context_parts import mannequin
    person = Pos(620, 560, 0) * Rot(0, 0, -90) * mannequin(1750, "stand")
    return [Part("Canal bank (site)", s["bank"], "#A8B49A"), Part("Concrete canal lining (site)", s["lining"], "#E7E5E4"),
            Part("Canal water (site)", s["water"], "#60A5FA", alpha=0.35),
            Part("Person, 1.75 m (scale)", person, "#9CA3AF")]


def hero():
    return K._render(parts() + context(), MD / "hero.png", elev=24, azim=-135, title=PROJECT,
                     note="Seen from the canal side, upstream and above, 24 deg elevation; ladder thrown and lying "
                          "down a 1.5:1 lined wall with water 2.0 m below the coping. Grey figure: 1.75 m person for scale")


def exploded():
    return K._render(parts(), MD / "exploded.png", elev=24, azim=-135, offsets=True, labels=True,
                     title=f"{PROJECT}: exploded view",
                     note="Seen from the canal side and above, 24 deg elevation; ladder parts pulled out from the wall; "
                          "numbers match bom/bom.csv")


def web():
    """glTF with a coarse mesh (a few MB), and the viewer page from the kit."""
    ps = parts() + context()[:3]
    kids = []
    import matplotlib.colors as mc
    for p in ps:
        sh = p.shape
        sh.color = Color(*mc.to_rgb(p.color))
        sh.label = p.name
        kids.append(sh)
    MD.mkdir(exist_ok=True)
    export_gltf(Compound(kids), str(MD / "model.glb"), binary=True, linear_deflection=1.0, angular_deflection=0.35)
    glb = MD / "model.glb"
    # viewer page as the kit writes it (concept.export_web_model), without re-exporting the mesh
    (MD / "viewer.html").write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{PROJECT}: {TITLE}</title>
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer@3/dist/model-viewer.min.js"></script>
<style>body{{margin:0;font-family:system-ui,sans-serif;background:#F9FAFB}}model-viewer{{width:100vw;height:100vh}}
.tag{{position:fixed;left:12px;top:10px;font-size:12px;color:#B45309;letter-spacing:.06em}}</style></head>
<body><div class="tag">CONCEPT, NOT FOR FABRICATION</div>
<model-viewer src="model.glb" poster="hero.png" alt="{PROJECT}: {TITLE}" camera-controls auto-rotate shadow-intensity="0.6"
  exposure="1.0" camera-orbit="-135deg 70deg auto" interaction-prompt="auto"></model-viewer></body></html>
""")
    return glb


def blueprint():
    sys.path.insert(0, str(ROOT / "docs" / "04-calcs"))
    from drawing import Sheet, project_views
    m = M.masses()
    light = list(M.simple_parts().values())       # small parts do not show at this scale
    views = project_views(Compound(light), MD / "_views")
    views["iso"] = project_views(Compound(light + [M.site()["lining"]]), MD / "_views_fig")["iso"]
    s = Sheet(project=PROJECT, title=TITLE, dwg_no=DWG, rev="P2", author="Amish Chadha", date=DATE, theme="blueprint",
              material="Massing model for concept communication",
              revisions=[("P1", "Concept sheet from the constructable model", DATE, "AC"),
                         ("P2", "CNR-DDR-003: 9 mm ropes; 500 x 1,200 footing", DATE, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 37, 140, 113, label="Isometric view",
              sublabel="Not to scale; seen from the bank side, front right and above; grey is the site")
    s.add_notes("Key figures", [
        "13 floating rungs at 335 mm pitch; 4.02 m rung section",
        "Reaches water 2.1 m down a 1.5:1 wall, 3.8 m down a vertical wall",
        "Each rung floats with 0.22 to 0.28 kg to spare; soft 0.5 kg throw weight",
        "Rung: 0.56 of yield at 1.5 kN; 9 mm ropes 18.4 kN wet with knots",
        "Anchor eye nut on a post in a 500 x 1,200 footing; 4.5 kN target",
        f"Ladder as thrown {m['total']:.1f} kg (4.5 kg target); about 15 s to deploy (est.)",
        "Never enter the water: throw, anchor and call for help"], x=276, y=168, width=140)
    s.save(MD / "concept-blueprint")
    shutil.rmtree(MD / "_views", ignore_errors=True)
    shutil.rmtree(MD / "_views_fig", ignore_errors=True)
    return MD / "concept-blueprint.png"


if __name__ == "__main__":
    fns = {"hero": hero, "exploded": exploded, "web": web, "blueprint": blueprint}
    for w in sys.argv[1:] or list(fns):
        print(w, "->", fns[w]())
