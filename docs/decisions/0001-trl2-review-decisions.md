---
doc_id: CNR-DDR-001
title: CanalRung TRL 2 review decisions
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
  change: "TRL 2 review items D1 to D14, decided as recommended under Amish's 2026-10-03 pre-approval"
---

# 0001: TRL 2 review decisions

- **Date:** 2026-10-03
- **Status:** accepted. Decided by Amish under his pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost."

## Context

The scaffold (CNR-PRB-001, CNR-PRC-001 and CNR-REQ-001, all v0.1) left five open questions and several choices undecided: bank heights and flows, sink or float, the load standard, theft, the anchor type, the rung and rope construction, the throw line and the partners. Populating the concept to TRL 2 needed an answer to each. Because Amish pre-approved every recommendation for this batch, each item below is decided as recommended rather than left "Proposed, awaiting Amish". Choices that touch safety take the conservative option, and the record says what evidence would relax them. Partners and regions are named as the first candidates to approach, not as agreed.

## Options considered

*Table 1. Options for each item.*

| # | Item | Options |
| --- | --- | --- |
| D1 | Design envelope | (a) 1.5:1 slopes to 3.0 m (needs a 5.4 m ladder and about 6 kg); (b) 1.5:1 slopes to 2.0 m and vertical walls to 3.0 m with a 4.0 m ladder; (c) vertical walls only |
| D2 | Anchor | (a) ground stake driven at the time; (b) post loop around any nearby post; (c) cross bar across the bank; (d) the station post itself, set in concrete, with the ladder linked to it in advance |
| D3 | Rung | (a) 25.4 x 1.65 mm aluminium tube (lighter); (b) 28.6 x 1.65 mm aluminium tube (stronger); (c) solid HDPE rod (floats but about 6 kg for the set); (d) GFRP tube |
| D4 | Rope and joint | (a) 10.5 mm EN 1891 type A kernmantle through the rung ends, overhand stopper knot under and seizing over each end; (b) polypropylene rope with clamps; (c) laid rope with rungs seized between the strands (Jacob's ladder) |
| D5 | Wall stand-offs | (a) on every rung (about 1.3 kg); (b) on every third rung (0.42 kg); (c) none |
| D6 | Bottom end | (a) weighted to sink; (b) floating; (c) a soft weight on a short tail with floating rungs above it |
| D7 | Throw line | (a) fitted; (b) left out of the first prototype |
| D8 | Storage | (a) a bought UV-stabilised 70 L box on the post, no lock; (b) a made steel cabinet; (c) a locked box |
| D9 | Load standard | (a) certify to a ladder or life-saving standard now; (b) rope to EN 1891 type A, rung and anchor targets as in CNR-REQ-001, proof-loaded at TRL 4, no certification claimed |
| D10 | R2 mass target | (a) meet 4.0 kg with lighter rungs and fewer stand-offs; (b) keep the safer rung and report R2 as not met |
| D11 | Theft | (a) lock; (b) no lock, tamper tag and inspection; (c) no rope or aluminium (not possible) |
| D12 | Shared blocks | CalRig for proof loads; LaneSkiff boarding step |
| D13 | Co-design partner | Western US irrigation districts; Punjab canal authorities; water-safety councils |
| D14 | Pitch, problem and value-engineering target | Change or keep |

## Decision

*Table 2. Items decided, 2026-10-03.*

| # | Decision | Why | What would relax it |
| --- | --- | --- | --- |
| D1 | (b): water to 2.0 m below the coping on 1.5:1 slopes and to 3.0 m on vertical walls; currents to 2.0 m/s | Keeps the ladder near the 4 kg throwing target; covers the vertical-walled and steep reaches where self-rescue is hardest. A 6 m variant for deeper sloped canals is a later option | Partner district data on its reaches |
| D2 | (d): the post is the anchor; forged M16 eye nut on an M16 bolt through the post, 250 mm above ground, ladder linked in advance | A bystander cannot set a 4.5 kN stake in 30 s; a hand-held top pulls people in. The conservative option | A tested portable anchor for a vehicle kit |
| D3 | (b): 28.6 x 1.65 mm 6061-T6, 360 mm long | 0.56 of yield at 1.5 kN against 0.73 for the lighter tube. Safety before mass | Proof-load results showing the lighter tube keeps a two-thirds margin |
| D4 | (a): EN 1891 type A 10.5 mm, polyester preferred; nylon bushes in the rung holes; overhand knot under, seizing over | Rated rope with known knotted strength; a joint anyone can tie and inspect; polypropylene is weak and degrades in sun | |
| D5 | (b): rungs 3, 6, 9 and 12, 95 mm from rung axis to wall | Hand room on a flat wall at a third of the mass of (a) | Tank trials showing climbers manage with fewer |
| D6 | (c): soft 0.5 kg steel shot pouch, 280 mm below the bottom rung, rungs floating | The end goes down and stays put; the rungs stay at the surface; nothing hard is thrown near the person | Throw trials |
| D7 | (b): no throw line on the first prototype | A second line can tangle and is an entanglement hazard in moving water. Conservative | Throw trials showing a line is needed to steer the ladder |
| D8 | (a): bought bright 70 L UV-stabilised box clamped to the post, drain holes, rope notch, blunt-tip knife under the lid | Cheap, replaceable, visible; keeps the rope dark | |
| D9 | (b) | Certification is beyond TRL 3; the targets give margins over the design climber and will be proof-loaded with CalRig | |
| D10 | (b): keep the D3 rung; R2 reported as not met (4.48 kg against 4.0 kg) | The rung margin protects the climber; 0.5 kg more may not matter to a thrower. Savings to try are in the register | Throw trials with the 4.5 kg ladder |
| D11 | (b): no lock; numbered tamper tag on the latch; the partner district inspects on a set schedule and after each use | A locked rescue box fails when it is needed | Theft data from a pilot |
| D12 | CalRig named as the proof-load rig for TRL 4 (candidate shared block); the LaneSkiff boarding step stays outside this repository | Keeps this repository to one product | |
| D13 | First candidates to approach: the Kittitas Reclamation District (Washington) as co-design partner and the Water Safety Council of Fresno County as water-safety partner; neither contacted | Both publish canal safety guidance cited in CNR-PRB-001 | |
| D14 | No change: pitch and problem as scaffolded; `budget_usd` stays 500 as the value-engineering target | Cost overruns are accepted under the pre-approval and reported, not used to change the target | |

## Consequences

- CNR-PRB-001, CNR-PRC-001 and CNR-REQ-001 are revised. R1 is restated for the D1 envelope, R6 for the fixed station anchor of D2, and R10 is added for D6 and D8.
- The design is modelled in `cad/src/model.py` on these decisions and then made constructable in CNR-DDR-002.
- `project.yaml`: only the TRL fields, `design_state` and the evidence list change; `budget_usd`, the pitch and the problem are unchanged.
- Nothing in this record authorizes building or testing. TRL 4 is outside the current portfolio phase.

> **Safety:** Every choice above that touches safety (D2, D3, D6, D7, D11) took the more conservative option. None of them makes the ladder safe without proof loads and supervised trials.
