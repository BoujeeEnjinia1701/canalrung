---
doc_id: CNR-RSK-001
title: CanalRung risk register and hazard analysis
project: CanalRung
doc_type: Risk register and hazard analysis
version: "0.1"
status: Draft
date: '2026-11-05'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-11-05'
  author: Amish Chadha
  change: "First risk register, preliminary hazard analysis and design FMEA (kit 1.9.1 upgrade), for option A; hazards of options B and C noted where they differ"
---

# CanalRung risk register and hazard analysis

The top risks are a rescue that fails when it is needed (a rope, rung or anchor that is weaker than the paper numbers, with the thinnest margins in the rope and the saturated-soil footing), a bystander who enters the water, and a cost that stays over the USD 500 target; none has been tested. Method: STANDARDS section 23. Likelihood, impact, severity and occurrence are scored 1 (low) to 5 (high); detection 1 (certain to be caught) to 5 (not caught).

> **Safety:** All scores are the author's first-pass judgement from paper design, not test or incident data. CanalRung is a research and educational design, never certified life-saving equipment, and nothing here shows it is safe. Never enter the water to rescue someone.

## Project risk register

Table 1. Project risks.

| # | Risk | Cause | Effect | Likelihood | Impact | Owner (role) | Response |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | Concept choice not made | Amish has not decided among options A, B and C (CNR-DDR-004) | Work stays on A; B and C modelled but unused | 3 | 2 | Amish | Decision requested in CNR-PLN-001 |
| P2 | Cost stays over the target | USD 605.20 against USD 500; footing is USD 143 | Fewer stations per district | 4 | 3 | Design lead | Savings listed in CNR-DEC-001; cost is reported, `budget_usd` is not raised |
| P3 | Unverified prices | No supplier prices could be checked on 2026-11-05 | Cost off by an unknown amount | 4 | 3 | Design lead | Mark "to assess"; get quotes at TRL 4 |
| P4 | Rope rating not proven | 9 mm type B strength taken from catalogue class values; margin 4.08 against 4 | Rope or knot fails in a proof load | 3 | 5 | Design lead | Proof load with CalRig at TRL 4; require a declared minimum of 18 kN |
| P5 | No co-design partner yet | Kittitas Reclamation District and the Water Safety Council of Fresno County named, not contacted | Needs, heights and soils stay assumed | 4 | 4 | Amish | Contact when allowed; plan in CNR-PLN-001 |
| P6 | Regulatory route unknown | Classification of the station is to assess (CNR-REG-001 G3) | A product claim could be unlawful | 3 | 5 | Regulatory reviewer | Keep the "research and educational prototype" wording |
| P7 | Test facility and lifeguards unavailable | Tank trials need supervised water | TRL 4 delayed | 3 | 3 | Project lead | Plan only; no testing at TRL 3 |
| P8 | Price or part drift | Prices and part availability change | The BOM goes stale | 3 | 2 | Design lead | Re-check cited prices before any release |

## Preliminary hazard analysis

Table 2. Hazards (option A; B and C noted).

| # | Hazard | Cause | Harm | Severity | Likelihood | Control | Residual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | A bystander enters the water to help | Urge to rescue; the ladder is slow to deploy | Drowning of the rescuer | 5 | 3 | Front decal "do not enter the water"; pictogram on the lid; throw and call | High until trials show the throw works |
| H2 | The person is entangled in the ropes in a current | Ropes and knots in moving water | Drowning | 5 | 2 | Blunt-tip knife in the lid; no loose throw line (CNR-DDR-001 D7); ropes end at a weight, not a loop | Medium |
| H3 | A rung, rope or anchor fails under the climber | Weaker than calculated; ageing; a bad knot | Person falls back, injury | 5 | 2 | Rung at 0.56 of yield, rope 4.08, anchor factors 1.53 to 3.58 (CNR-CAL-001); proof loads at TRL 4 | Medium until proof loaded |
| H4 | The thrown weight hits the person | Poor throw | Blunt injury | 3 | 2 | Soft shot pouch of 0.5 kg; no hard parts thrown (PR-010) | Low |
| H5 | The ladder lies on the wall but the person cannot climb it | Cold, tired, a child; slick wall | Person stays in the water | 5 | 3 | 335 mm pitch, 70 mm hand room at stand-offs, floating rungs; trials | High until trials; B or C might serve such a person better |
| H6 | Rope burn or cut to the thrower or to the person pulling | Rope runs over the hand | Hand injury | 2 | 3 | Edge protectors; gloves not required; user guidance | Low |
| H7 | A child hangs on or plays with the ladder | Always-ready equipment | Fall or entanglement | 3 | 2 | Ladder folded in a latched box with a tamper tag; no lock so it opens in an emergency | Medium |
| H8 | A sharp or hard edge hurts someone | Cut tube ends, box rim | Cuts | 2 | 2 | Rung ends capped, edges broken in the model, bushed holes | Low |
| H9 | A bystander slips on the wet bank while throwing | Wet, steep bank edge | Fall into the canal | 4 | 3 | Post set 1,000 mm back from the coping; throw from behind the post; guidance | Medium |
| H10 | Option B: a rigid ladder falls onto a person in the water | Lowering over the edge | Blunt injury | 4 | 3 | None designed; handling and lanyard only | High (option B) |
| H11 | Option C: crank handle spins back on the cranker | Pawl fails or is released under load | Hand or face injury | 3 | 3 | Ratchet and pawl in the model; no brake designed | High (option C) |

## Design FMEA (first pass, P3)

Table 3. Failure modes for option A. RPN = severity x occurrence x detection.

| # | Item | Function | Failure mode | Effect | Cause | S | O | D | RPN | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | Rung | Carry the climber's weight | Rung bends or buckles | The ladder gives way under one foot | Over-load; cold-worked tube | 4 | 2 | 3 | 24 | Proof-load a rung (TRL 4) |
| F2 | Side rope at a knot | Carry the load into the anchor | Rope breaks at the knot | The ladder falls | Knot weakens the rope; wet; abrasion | 5 | 2 | 4 | 40 | Proof-load a roped rung; inspect each season |
| F3 | Knot and seizing | Hold the rung in place | Knot slips or seizing loosens | A rung drops down the rope | Wet, UV, wrong knot | 4 | 3 | 3 | 36 | Show the knot in the build plan; inspect |
| F4 | Footing | Hold the anchor | Footing pulls out | Whole station fails | Soft or saturated soil (factor 1.59); crest of a slope cuts the passive wedge (STEM S4, S5) | 5 | 3 | 4 | 60 | Site pull test; deeper footing proposed (CNR-DEC-001, open decision 3) |
| F5 | Eye nut and bolt | Link ladder to post | Nut or bolt fails | The ladder is lost | Wrong grade; side loading | 5 | 1 | 3 | 15 | Buy marked parts; load in line |
| F6 | Float sleeve | Float the rung | Foam soaks or degrades | Rung sinks | UV; cut; open-cell foam | 3 | 3 | 3 | 27 | Closed-cell grade only; inspect |
| F7 | Folded ladder in the box | Pay out cleanly | Tangle | Throw fails | Fold order; wind | 4 | 3 | 4 | 48 | Fold test and pictogram at TRL 4 |
| F8 | Aluminium mounting plate | Clamp the box on the post | Galvanic corrosion at the plate | Box loosens | Zinc and aluminium couple, wet (STEM S11) | 2 | 3 | 2 | 12 | Watch at TRL 4 |
| F9 | Lid latch | Open without tools | Latch jams or tag is broken | Delay in an emergency | Ice, dirt, vandalism | 5 | 2 | 3 | 30 | No lock; tamper tag; inspection |
| F10 | Stand-off block | Hold the rung off the wall | Block cracks or bolt loosens | Hand room lost | UV, load | 3 | 3 | 3 | 27 | HDPE; inspect |
| F11 | Edge protector | Keep the rope off the coping | Slips off | Rope abraded to 50 percent strength (CNR-CAL-001 E2) | Movement | 4 | 3 | 3 | 36 | Check fit and retention at TRL 4 |
| F12 | Rope bush | Protect the rope in the rung hole | Bush cracks or crushes | Rope chafes; knot pulls through | UV, load; wet nylon yields near 35 MPa against 32.8 MPa from a foot at the rung end (STEM S9) | 4 | 3 | 3 | 36 | Proof load at TRL 4; inspect |
| F13 | Throw weight | Carry the ladder end down | Snags or splits | Ladder hangs short | Rough edge; shot spills | 3 | 2 | 2 | 12 | Check the pouch seams at TRL 4 |
| F14 | Eye nut | Link ladder to post | Eye nut loaded off its axis fails or bends | The ladder is lost | Rope pulls 14 to 34 degrees off the thread; the rating is in line only (STEM S23) | 5 | 3 | 4 | 60 | Get the off-axis rating or use a swivel hoist ring (CNR-DEC-001, open decision 5) |

RPN above 40 or severity 5 with detection 4 or more are the items to act on first: F4 (60), F14 (60), F7 (48) and F2 (40). Each action is paper work for TRL 4 and is not started here.

## Sources

- CNR-CAL-001 for the strength, anchor and edge figures; CNR-STM-001 for S3, S5, S10, S11 and S12; CNR-DDR-001 for D7 (no throw line).
- Severity and likelihood scales are the author's judgement; no incident database was used.
