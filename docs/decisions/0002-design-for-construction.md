---
doc_id: CNR-DDR-002
title: CanalRung design for construction
project: CanalRung
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Changes that make the concept physically buildable, with the reason for each; decided under Amish's 2026-10-03 pre-approval"
---

# 0002: Design for construction

- **Date:** 2026-10-03
- **Status:** accepted. Decided by Amish under his pre-approval of 2026-10-03: "I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost."

## Context

STANDARDS section 18 asks for a design in which every part can be made by its stated process and fits and fastens to the parts next to it (Amish, 2026-09-30: "fix the design assumptions to match and be physically feasible"). The concept of CNR-PRC-001 v0.2 and CNR-DDR-001 said what CanalRung does: rungs fixed at even spacing between two ropes, spacers on some rungs, a weighted bottom end, a bank anchor and a storage post and box. It did not say how a rung is held on a rope, how a spacer or the box is fixed, what the anchor is screwed into, or how the ropes reach the anchor. Working through each part with the model found the problems below. `cad/src/model.py` now runs 245 constructability checks (`python cad/src/model.py --check`): parts that must touch do touch and parts that must not touch are apart by at least the stated clearance. All pass.

The changes keep what the ladder does: the same reach, rung count and pitch, floating rungs, stand-offs, weighted end, fixed anchor and box. Nothing here changes the pitch or the safety case; P5, P8 and P11 make the safety case stronger.

## Decision

*Table 1. Changes made to the model, the BOM and the calculations.*

| # | Problem in the concept | Change made | Why this way |
| --- | --- | --- | --- |
| P1 | Rungs "fixed at even spacing" with no joint between rung and rope | Each rope runs through a 16 mm hole across each rung end, lined by a flanged nylon bush (12 mm bore, flange on the underside). An overhand stopper knot under the flange carries the rung; a 20 mm twine seizing above the bush stops it floating up the rope. In the model the knot bears on the rim of the bush bore | The classic rope ladder joint: no special tools, inspectable by eye, and the load path is rung, flange, knot, rope. The bush keeps the rope off the aluminium hole edges |
| P2 | Wall spacers on "some rungs" with no fixing; a loose spacer could slide along the rung or turn round it | HDPE blocks 16 mm thick, 115 mm long, slid on the rung just inside each bush on rungs 3, 6, 9 and 12, nose 95 mm from the rung axis, each locked by one M5 x 50 bolt down through block and rung (5.3 mm holes in the rung, 40 mm from the ends) | The bolt stops sliding and turning; wall friction puts 610 N across a bolt good for about 6 kN (CNR-CAL-001, D4) |
| P3 | "Buoyant rungs" with no stated float | A closed-cell foam sleeve, 50 mm outside, on every rung: 294 mm long on plain rungs and 260 mm on stand-off rungs, so it sits 2 mm clear of the bushes or blocks; a bead of adhesive inside each end | Sleeve lengths set by the parts beside it; the foam slides on before the blocks and bushes, which fixes the build order |
| P4 | Open tube ends | Plastic end caps with a 10 mm insert, which stops 2 mm short of the rope hole | Closes the ends without blocking the rope (R10) |
| P5 | Anchor "stake, post loop or cross bar"; the M16 eye bolt would crush the 3 mm post walls when tightened | Forged M16 eye nut on an M16 x 90 grade 8.8 bolt through the post 250 mm above ground; a 57 mm crush tube slides in through a 21.5 mm hole in the back wall and bears on the inside of the canal-side wall (17.5 mm hole); a 50 mm washer covers the crush tube end | The crush tube takes the clamp load so the walls stay round; the eye nut is loaded in line with its thread, its strongest direction |
| P6 | Storage box on the post with no fixing; drilling the post for box bolts would need more crush tubes | A 4 mm aluminium plate on the canal face of the post and two square M8 U-bolts round the back of the post; the U-bolt legs pass through the plate and the box back wall, with fender washers and nyloc nuts inside the box | No holes in the post for the box; the plate spreads the clamp load over the plastic wall |
| P7 | Ropes to the anchor and to the throw weight with no termination | A figure-eight loop at each rope end; the two top loops in one 10 mm screw link through the eye nut's ring; the two bottom loops and the weight's webbing loop in a second link 280 mm below the bottom rung. The first model link was too small to pass round the eye's ring and clashed with it; the link is now modelled with a 20 mm radius (about 60 mm inside) and is 6 mm clear | Rated, replaceable connectors; a link that fits round the ring with both loops in |
| P8 | Ropes dragged over the concrete coping edge | Two hook-and-loop edge protector sleeves, 500 mm long, on the top lead | Rope over a 10 mm edge can lose half its strength (CNR-CAL-001, E2) |
| P9 | The box lid could not close over ropes that must stay linked to the eye nut below the box | A 30 x 25 mm notch in the centre of the front rim; the ropes run from the eye nut under the box and up into it through the notch, and lift out when the lid is open; four 8 mm drain holes in the base | The ladder stays linked to the anchor while stored, and rain drains out |
| P10 | No footing size | 400 mm x 1,000 mm concrete footing, post 900 mm deep on 100 mm of concrete; 1,000 mm from the coping to the post centre | Holds 4.5 kN with a factor of 1.92 in drained soil (CNR-CAL-001, G4) |
| P11 | The standard footing is not enough in a saturated bank (factor 0.85) | On wet or soft banks: 500 mm x 1,200 mm footing and a 2,300 mm post | Conservative; a site pull test could relax it (CNR-CAL-001, G5) |
| P12 | Rope length not known | Each side rope cut to 8.0 m: top lead to the eye nut about 1.1 m, rung section with 13 knots about 5.4 m, tail 0.3 m, two loops about 1.2 m | From the model geometry (CNR-CAL-001, B1) |

*Table 2. Knock-on changes.*

| Item | Change | Reason |
| --- | --- | --- |
| Mass | Ladder as thrown 4.48 kg (bushes, caps, blocks, bolts, links and protectors added) | R2 not met by 0.48 kg; reported in CNR-CAL-001 and the register |
| Cost | Lines for the crush tube, U-bolts, plate, fixings, bushes, end caps, stand-off bolts, seizing twine, screw links, edge protectors, decals and knife; the BOM renumbered in build order. Value-engineering target: USD 500. Estimated cost of the constructable design: USD 543.60 (USD 43.60 over the target) | Parts added for construction |
| Drawings | CNR-DWG-001 Rev P2; making sketches CNR-DWG-101 to 109 | Follows the model |
| Documents | CNR-PRC-001 v0.3, CNR-REQ-001 v0.3, CNR-CAL-001 v0.2 | Follows the model; no requirement changed status because of these changes |

## Consequences

- `design_state: constructable` in `project.yaml`. The build plan CNR-BLD-001 shows every component and step in pictures generated from the model (`cad/src/build_plan_media.py`).
- The facts that only real parts can settle (the box's inside depth, the link's inside length, the eye nut and rope markings, the foam and bushes, the site soil) are listed under "To confirm when parts are bought" in CNR-DEC-001.

> **Safety:** P5, P7, P8 and P11 are on the load path a person's life depends on. They follow the conservative option; none removes the need to proof-load the rope, knots, rungs, links and anchor before anyone climbs the ladder (CNR-BLD-001, section 6).
