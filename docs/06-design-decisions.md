---
doc_id: CNR-DEC-001
title: CanalRung design decisions register
project: CanalRung
doc_type: Design decisions register
version: "0.1"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Register opened at TRL 3; every decision made under Amish's 2026-10-03 pre-approval"
---

# CanalRung design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list open decisions.

> **Safety:** CanalRung is safety-critical rescue and rope equipment. Every decision below that touches safety took the conservative option, and the decision records say what evidence would relax it. Nothing here makes the ladder safe to use without proof loads and supervised trials (TRL 4). Never enter the water to rescue someone.

## Open decisions

None. All decisions were made under Amish's 2026-10-03 pre-approval.

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The storage box takes a 370 mm rung across its inside depth (about 440 mm), and its back wall is flat where the plate sits | The folded ladder and the U-bolt clamp depend on it; choose a different box if not | CNR-DDR-002, P6 |
| 2 | The eye nut is forged and marked with a working load limit of at least 700 kg in line with its thread | The anchor factor of 1.53 rests on it | CNR-CAL-001, G1 |
| 3 | The screw links are marked with a working load limit of at least 1,000 kg and are long enough (about 60 mm inside) to pass round the eye nut's ring with both rope loops in | The top joint needs room for the ring and two loops | CNR-DDR-002, P7 |
| 4 | The rope is EN 1891 type A, 10.5 mm, with a declared breaking strength of at least 22 kN; polyester if available | The rope strength of 22.4 kN wet with knots rests on it | CNR-CAL-001, E1 |
| 5 | The foam tube is closed-cell (a cut end takes up no water) and grips 28.6 mm tube | Buoyancy and the sleeve's fit | CNR-CAL-001, C1 |
| 6 | The nylon bushes are 12 mm bore, 16 mm outside, with a 22 mm flange, and the 10.5 mm rope passes freely | The rope and knot seat | CNR-DDR-002, P1 |
| 7 | The bank soil at the first site: drained and medium dense, or wet or soft | Sets the standard footing or the 500 x 1,200 mm footing | CNR-CAL-001, G4 and G5 |
| 8 | The Rapid Rung patent number, read before public release | Confirms the no-elastic-stowing design-around | CNR-PRC-001 |

## Value engineering

Value-engineering target: USD 500 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 543.60 (USD 43.60 over the target). Main cost drivers and savings worth trying:

- The station costs USD 286.20 and the ladder USD 257.40. The largest lines are the concrete footing (USD 78), the 13 aluminium rungs (USD 72.80), the post (USD 48), the storage box (USD 45), the ropes (USD 40) and the edge protectors (USD 30).
- Savings worth trying: buying rope by the 50 m reel for several stations; a post and footing shared with an existing district marker post or fence line; sewn canvas edge protectors instead of bought ones; rungs cut from 6 m tube lengths.
- Mass (R2, 4.48 kg against 4.0 kg) is the other value-engineering gap. Worth trying at TRL 4: ropes of 10 mm instead of 10.5 mm (about 0.08 kg), stand-off blocks with a lightening hole (about 0.10 kg), a 0.4 kg throw weight if the throw trials allow (0.10 kg). Lighter rungs were rejected on strength (CNR-DDR-001, D3).

## Decisions made

All decided by Amish under his pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost."

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-10-03 | Design envelope: water to 2.0 m below the coping on 1.5:1 slopes and to 3.0 m on vertical walls; currents to 2.0 m/s; a longer variant later | Amish, pre-approval quoted above | CNR-DDR-001, D1 |
| 2026-10-03 | The station post is the anchor: forged M16 eye nut on an M16 bolt through the post, 250 mm above ground, ladder linked in advance | Amish, pre-approval quoted above | CNR-DDR-001, D2 |
| 2026-10-03 | Rungs of 28.6 x 1.65 mm 6061-T6 tube (strength before mass) | Amish, pre-approval quoted above | CNR-DDR-001, D3 |
| 2026-10-03 | Ropes of 10.5 mm EN 1891 type A kernmantle, polyester preferred, through nylon bushes; overhand knot under and seizing over each rung end | Amish, pre-approval quoted above | CNR-DDR-001, D4 |
| 2026-10-03 | Stand-off blocks on rungs 3, 6, 9 and 12, 95 mm off the wall | Amish, pre-approval quoted above | CNR-DDR-001, D5 |
| 2026-10-03 | Soft 0.5 kg throw weight 280 mm below the bottom rung, rungs floating | Amish, pre-approval quoted above | CNR-DDR-001, D6 |
| 2026-10-03 | No throw line on the first prototype | Amish, pre-approval quoted above | CNR-DDR-001, D7 |
| 2026-10-03 | Bought 70 L UV-stabilised box clamped to the post, no lock, drain holes, rope notch, rescue knife | Amish, pre-approval quoted above | CNR-DDR-001, D8 and D11 |
| 2026-10-03 | Load standard: EN 1891 rope; rung and anchor targets of CNR-REQ-001, proof-loaded with CalRig at TRL 4; no certification claimed | Amish, pre-approval quoted above | CNR-DDR-001, D9 and D12 |
| 2026-10-03 | Keep the stronger rung and report R2 (mass) as not met | Amish, pre-approval quoted above | CNR-DDR-001, D10 |
| 2026-10-03 | First candidates to approach: Kittitas Reclamation District (co-design) and Water Safety Council of Fresno County (water safety); not contacted, not agreed | Amish, pre-approval quoted above | CNR-DDR-001, D13 |
| 2026-10-03 | Pitch, problem and the USD 500 value-engineering target unchanged; the USD 43.60 overrun accepted | Amish, pre-approval quoted above | CNR-DDR-001, D14 |
| 2026-10-03 | Design for construction: rope-through-rung joint with bushes, knots and seizings; bolted stand-off blocks; foam sleeve lengths; end caps; eye nut with crush tube; box on a plate with U-bolts; rope notch and drain holes; screw links; edge protectors; footing sizes | Amish, pre-approval quoted above | CNR-DDR-002 |
| 2026-10-03 | Saturated or soft banks get a 500 x 1,200 mm footing and a 2,300 mm post (conservative; a site pull test could relax it) | Amish, pre-approval quoted above | CNR-DDR-002, P11 |
| 2026-10-03 | Appearance model and render scenes as modelled, with no appearance deviations from the model | Amish, pre-approval quoted above | `docs/REVIEW.md` |
