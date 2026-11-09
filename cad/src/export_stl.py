"""Export STL of the chosen design (option A) from cad/src/model.py: one file per made, bought and fastener part in
cad/stl/A/, and the whole assembly as cad/stl/A-assembly.stl. Tolerance 0.15 mm (kit rule: about 0.1 to 0.2 mm, never the
0.001 default). Run from the repo root:  python cad/src/export_stl.py
Context parts (embankment, lining, water) are not exported. CONCEPT, NOT FOR FABRICATION."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
from build123d import Compound, export_stl  # noqa: E402
import model as M  # noqa: E402

TOL, ANG = 0.15, 0.3


def main():
    out = ROOT / "cad" / "stl"
    (out / "A").mkdir(parents=True, exist_ok=True)
    parts = [p for p in M.components(M.CHOSEN) if p["kind"] != "context"]
    for i, p in enumerate(parts, 1):
        slug = re.sub(r"[^a-z0-9]+", "-", p["name"].lower()).strip("-")[:60]
        export_stl(p["shape"], str(out / "A" / f"{i:03d}-{slug}.stl"), tolerance=TOL, angular_tolerance=ANG)
    export_stl(Compound([p["shape"] for p in parts]), str(out / "A-assembly.stl"), tolerance=TOL, angular_tolerance=ANG)
    print(f"{len(parts)} part STL files and the assembly in {out} at tolerance {TOL} mm")


if __name__ == "__main__":
    main()
