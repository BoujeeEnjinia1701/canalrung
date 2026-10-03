---
doc_id: CNR-DEC-001
title: CanalRung design decisions register
project: CanalRung
doc_type: Design decisions register
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Register opened at TRL 3; every decision made under Amish's 2026-10-03 pre-approval"
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's requirement decisions 4A and 9A of 2026-10-03 recorded (CNR-DDR-003): 9 mm ropes with R2 restated to 4.5 kg; the 500 x 1,200 mm footing standard at every site"
---

# CanalRung design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list open decisions.

> **Safety:** CanalRung is safety-critical rescue and rope equipment. Every decision below that touches safety took the conservative option, and the decision records say what evidence would relax it. Nothing here makes the ladder safe to use without proof loads and supervised trials (TRL 4). Never enter the water to rescue someone.

## Open decisions

None. All decisions were made under Amish's 2026-10-03 pre-approval, and requirement decisions 4A and 9A were decided by Amish on 2026-10-03 (below).

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | The storage box takes a 370 mm rung across its inside depth (about 440 mm), and its back wall is flat where the plate sits | The folded ladder and the U-bolt clamp depend on it; choose a different box if not | CNR-DDR-002, P6 |
| 2 | The eye nut is forged and marked with a working load limit of at least 700 kg in line with its thread | The anchor factor of 1.53 rests on it | CNR-CAL-001, G1 |
| 3 | The screw links are marked with a working load limit of at least 1,000 kg and are long enough (about 60 mm inside) to pass round the eye nut's ring with both rope loops in | The top joint needs room for the ring and two loops | CNR-DDR-002, P7 |
| 4 | The rope is EN 1891 type B, 9 mm, with a declared breaking strength of at least 18 kN and about 55 g/m; polyester if available | The rope strength of 18.4 kN wet with knots (4.08 times 4.5 kN, R4) and the 4.27 kg ladder mass rest on it | CNR-CAL-001, E1 and B1; CNR-DDR-003 |
| 5 | The foam tube is closed-cell (a cut end takes up no water) and grips 28.6 mm tube | Buoyancy and the sleeve's fit | CNR-CAL-001, C1 |
| 6 | The nylon bushes are 12 mm bore, 16 mm outside, with a 22 mm flange, and the 9 mm rope passes freely while its overhand knot cannot pull through | The rope and knot seat | CNR-DDR-002, P1 |
| 7 | The bank soil at the first site is granular (sand or gravel), drained or saturated, and not soft clay or peat | The standard 500 x 1,200 mm footing is checked for granular soil only; clay or peat needs a site pull test | CNR-CAL-001, G4 and G5; CNR-DDR-003 |
| 8 | The Rapid Rung patent number, read before public release | Confirms the no-elastic-stowing design-around | CNR-PRC-001 |

## Value engineering

Value-engineering target: USD 500 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 605.20 (USD 105.20 over the target). Main cost drivers and savings worth trying:

- The station costs USD 358.80 and the ladder USD 246.40. The largest lines are the concrete footing (USD 143, the 500 x 1,200 mm footing now standard at every site), the 13 aluminium rungs (USD 72.80), the post (USD 52.60), the storage box (USD 45), the ropes (USD 32) and the edge protectors (USD 30).
- Savings worth trying: ready-mix delivered for several stations at once instead of bagged premix; buying rope by the 50 m reel; a post and footing shared with an existing district marker post or fence line; sewn canvas edge protectors instead of bought ones; rungs cut from 6 m tube lengths.
- Mass: the ladder as thrown is 4.27 kg, inside the 4.5 kg of R2 as restated on 2026-10-03. Worth trying at TRL 4 if the throw trials ask for less: stand-off blocks with a lightening hole (about 0.10 kg), a 0.4 kg throw weight (0.10 kg). Lighter rungs were rejected on strength (CNR-DDR-001, D3), and ropes below 9 mm would fall under Amish's three-times floor (CNR-DDR-003).

## Decisions made

Decided by Amish under his pre-approval of 2026-10-03, except the last two rows, which he decided directly on 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost."

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
| 2026-10-03 | R2 (4A): side ropes downsized to 9 mm EN 1891 type B (18.4 kN wet with knots, 4.08 times 4.5 kN, above the three-times floor); stronger rungs kept; the ladder still exceeds 4.0 kg (4.27 kg), so R2 restated to 4.5 kg. Supersedes the 10.5 mm rope of D4 and the "R2 not met" of D10 | Amish, 2026-10-03: "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A" | CNR-DDR-003 |
| 2026-10-03 | R6 (9A): the 500 x 1,200 mm footing with a 2,300 mm post is the standard footing at every site (factor 3.58 drained, 1.59 saturated); R6 restated for drained or saturated soil. Supersedes the two footing sizes of P11 | Amish, 2026-10-03: "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A" | CNR-DDR-003 |
