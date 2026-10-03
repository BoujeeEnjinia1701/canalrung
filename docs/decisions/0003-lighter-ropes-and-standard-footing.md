---
doc_id: CNR-DDR-003
title: CanalRung lighter ropes and one standard footing
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
  change: Decisions 4A and 9A recorded and carried into the model, calculations, bill of materials, requirements, drawings and build plan
---

# 0003: Lighter ropes and one standard footing

- **Date:** 2026-10-03
- **Status:** decided. Decided by Amish on 2026-10-03, choosing option A on every requirement decision put to him: "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A". This record carries decisions 4A (R2) and 9A (R6).

> **Safety:** CanalRung is safety-critical rescue and rope equipment. A smaller rope has less reserve; the 9 mm rope chosen still meets the four-times rope factor of R4, but only just, so the bought rope must declare at least 18 kN and the TRL 4 proof load must use wet, knotted rope. Never enter the water to rescue someone.

## Context

At TRL 3 (CNR-CAL-001 v0.2) the ladder as thrown weighed 4.48 kg against the 4.0 kg target of R2, and R2 was reported as not met. The 10.5 mm EN 1891 type A ropes (1.08 kg) were the second largest mass after the rungs, which were kept strong on purpose (CNR-DDR-001, D3 and D10). Separately, the standard 400 x 1,000 mm footing met R6 only in drained soil (factor 1.92) and fell to 0.85 in a saturated bank, so the larger 500 x 1,200 mm footing was kept for wet or soft banks and the soil had to be judged at each site.

## Options considered

- **4A (chosen).** Downsize the two ropes to a rope that still holds at least three times the 4.5 kN target wet with knots; keep the stronger rungs. If the thrown ladder still exceeds 4.0 kg, restate R2 to 4.5 kg.
- **4B.** Keep the 10.5 mm ropes and keep reporting R2 as not met.
- **9A (chosen).** Make the 500 x 1,200 mm footing the standard footing at every site.
- **9B.** Keep two footings and decide the size from the soil at each site.

## Decision

**Ropes (4A).** The side ropes become 9 mm low-stretch kernmantle to EN 1891 type B, polyester preferred, with a declared breaking strength of at least 18 kN and about 55 g/m. Nine millimetres is the smallest common life-safety rope with a standard minimum strength; 8 mm accessory cord (EN 564) would save another 0.2 kg but its standard minimum of about 12.8 kN gives only 2.9 times the target wet with knots, below Amish's floor of three. The cut length (8.0 m each), knots, seizings, bushes (12 mm bore), screw links and edge protectors (for 9 to 13 mm rope) are unchanged. The model's overhand knot is drawn at 23 mm across instead of 26 mm, and 26 new model checks confirm that the 9 mm rope runs at least 1 mm clear of every bush bore.

The thrown ladder still weighs more than 4.0 kg (4.27 kg), so under Amish's fallback in 4A R2 is restated to 4.5 kg (9.9 lb).

**Footing (9A).** The 500 mm diameter x 1,200 mm deep footing, with a 2,300 mm post set 1,100 mm into it, is the standard at every site. The anchor stays 250 mm above the ground, so the bolt holes move to 1,350 mm from the bottom of the post. R6 is restated for drained or saturated granular bank soil.

## Results (CNR-CAL-001 v0.3)

| Requirement | Target | Before | After |
| --- | --- | --- | --- |
| R2 | Ladder as thrown at most 4.5 kg (was 4.0 kg) | 4.48 kg, not met | 4.27 kg, met on paper [B3] |
| R3 | At least 0.15 kg spare per rung; weight factor at least 1.5 | 0.274 and 0.218 kg; 1.73 | 0.277 and 0.221 kg; 1.75 [C1], [C2] |
| R4 | Ropes wet with knots at least 4 times 4.5 kN (18 kN) | 22.4 kN, 5.0 times | 18.4 kN, 4.08 times [E1] |
| R6 | Each anchor element at least 1.5, drained or saturated soil | Footing 1.92 drained, 0.85 saturated | Footing 3.58 drained, 1.59 saturated [G4], [G5] |
| R9 | Reported against USD 500 | USD 543.60 | USD 605.20 [I1] |

The model passes 271 of 271 constructability checks (245 before, plus 26 rope-in-bush checks).

## Consequences

- Value-engineering target: USD 500. Estimated cost of the constructable design: USD 605.20 (USD 105.20 over the target). The footing grows from about 12 to about 22 bags of concrete (USD 78.00 to USD 143.00 at USD 6.50 a bag), the post from 2.1 to 2.3 m (USD 48.00 to USD 52.60, pro rata), and the ropes fall from USD 40.00 to USD 32.00 (16 m at about USD 2.00 a metre). `budget_usd` is unchanged at 500.
- The footing needs about 0.23 m3 of concrete instead of 0.12 m3: about 550 kg of bagged premix to carry to the bank, or a small ready-mix delivery. The build plan says so.
- One footing size removes the soil judgement from each install, but soft clay or peat banks are still outside the screening values and need a site pull test.
- The rope margin over R4 is thin (4.08 against 4). If the bought rope declares less than 18 kN, R4 is not met and the rope must be changed.
- Throw trials at TRL 4 will show whether 4.3 kg is easy to throw for untrained adults.
