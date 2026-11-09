"""CanalRung geometry helpers shared by model.py and the option builders (kit 1.9).

Plain build123d helpers (boxes and cylinders along the world axes), the lift that puts the model on its
ground, and the canal site (embankment, concrete lining, water) built as context parts.

Frames. The design was drawn with the coping edge of the bank at Z = 0 and the lined wall falling toward -X
(CNR-DDR-002). Kit 1.9 pictures want ground level at Z = 0, so every part that leaves model.components() is
lifted by COPING_Z = water_drop + water_depth = 3,000 mm: ground is then the top of the concrete canal bed, the
coping is 3,000 mm above it, and the design water line is 1,000 mm above it. Nothing is re-dimensioned.
"""
from __future__ import annotations

import math

from build123d import Box, Compound, Cylinder, Location, Plane, Polygon, Pos, Rot, Vector, extrude

import cad_parts as cp

COPING_Z = 3000.0       # coping edge above ground (the canal bed top): water_drop 2,000 + water_depth 1,000


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
    return Compound([s for s in shapes if s is not None])


def lift(shape, dz=COPING_Z):
    """Move a shape drawn with the coping at Z = 0 onto the ground (Z = 0 at the canal bed top)."""
    return Pos(0, 0, dz) * shape


def to_yz(shape):
    """A sheet or plate built flat in XY (width X, height Y, thickness Z) turned to stand in the YZ plane:
    width along Y, height along Z, thickness along X."""
    from build123d import Axis
    return shape.rotate(Axis((0, 0, 0), (1, 1, 1)), 120)


# ------------------------------------------------------------------ canal site (context parts)
def site_parts(P, yw=450.0, far=False, crest=1800.0, outer_run=0.0, lifted=True):
    """Embankment, concrete lining and water of the design canal as context parts (named "(site)").

    Drawn with the coping at Z = 0 and then lifted onto the ground. The near bank is X >= 0 and the lined wall falls
    toward -X at slope_h : 1. crest: width of the bank top behind the coping. outer_run: horizontal run of the outer
    slope of the embankment per metre of height 0 = a vertical cut (a section model); far=True adds the far wall and
    bank, mirrored about the canal centre line, so the canal is a full channel."""
    H, drop, dep = P["slope_h"], P["water_drop"], P["water_depth"]
    toe_z = -(drop + dep)
    toe_x = toe_z * H
    bed_w = 1200.0 if far else 600.0
    bed_x = toe_x - bed_w
    out = []

    def add(name, shape, material, color=None):
        out.append(cp.part(name, lift(shape) if lifted else shape, material, kind="context", color=color, group="context"))

    ex = crest + outer_run * (-toe_z)
    earth = Plane.XZ * Polygon((0, 0), (crest, 0), (ex, toe_z - 100), (toe_x - 60, toe_z - 100), (-60, -100), (0, -100), align=None)
    add("Embankment, near bank (site)", extrude(earth, amount=yw, both=True), "soil", "#7C8B5A")
    lin = Plane.XZ * Polygon((0, 0), (toe_x, toe_z), (bed_x, toe_z), (bed_x, toe_z - 100), (toe_x - 60, toe_z - 100),
                             (-60, -100), (0, -100), align=None)
    add("Concrete canal lining (site)", extrude(lin, amount=yw, both=True), "concrete")
    wx = -drop * H
    # the water body reaches 50 mm into the lining bed, so that it goes below the ground plane in outdoor renders
    wat = Plane.XZ * Polygon((wx, -drop), (toe_x, toe_z), (toe_x, toe_z - 50), (bed_x, toe_z - 50), (bed_x, -drop), align=None)
    add("Canal water (site)", extrude(wat, amount=yw, both=True), "water")
    if far:
        cx = (toe_x + bed_x) / 2          # canal centre line: mirror everything about it
        mir = lambda s: s.mirror(Plane(origin=(cx, 0, 0), z_dir=(1, 0, 0)))  # noqa: E731
        lin2 = mir(extrude(lin, amount=yw, both=True))
        earth2 = mir(extrude(earth, amount=yw, both=True))
        add("Concrete canal lining, far wall (site)", lin2, "concrete")
        add("Embankment, far bank (site)", earth2, "soil", "#7C8B5A")
        # the near water body already spans the whole channel width (the bed runs to the far wall), so no second body
    return out


def bead_xz(pts, y0, y1):
    """Weld bead or gusset: a polygon drawn in the XZ plane, extruded along Y from y0 to y1."""
    from build123d import Plane, Polygon, extrude
    return Pos(0, (y0 + y1) / 2, 0) * extrude(Plane.XZ * Polygon(*pts, align=None), amount=(y1 - y0) / 2, both=True)


def prism_z(pts, z0, z1):
    """Polygon (x, y) points extruded from z0 to z1, whatever the winding of the points."""
    from build123d import Polygon, extrude
    sh = extrude(Polygon(*pts, align=None), z1 - z0)
    return Pos(0, 0, z0 - sh.bounding_box().min.Z) * sh


def bead_xy(pts, z0, z1):
    """Weld bead: a polygon drawn in the XY plane, extruded along Z from z0 to z1."""
    return prism_z(pts, z0, z1)
