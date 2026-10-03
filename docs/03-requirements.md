---
doc_id: CNR-REQ-001
title: CanalRung requirements
project: CanalRung
doc_type: Requirements
version: "0.4"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "TRL 2: measurable targets; R1 restated for a stated design envelope; R4 and R6 given margins; R6 restated for the fixed station anchor; R10 added (nothing thrown can hurt the person in the water); decided under Amish's 2026-10-03 pre-approval (CNR-DDR-001)"
- version: "0.3"
  date: '2026-10-03'
  author: Amish Chadha
  change: "TRL 3: status of every requirement from CNR-CAL-001 on the constructable design (CNR-DDR-002); R2 not met on mass; R9 reported against the value-engineering target"
- version: "0.4"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Amish's requirement decisions of 2026-10-03 (4A and 9A, CNR-DDR-003): R2 mass target restated to 4.5 kg; R6 restated for the 500 x 1,200 mm footing as the standard at every site, in drained or saturated soil; R4 and R9 results updated for the 9 mm ropes and larger footing"
---

# CanalRung requirements

CanalRung meets nine of its ten requirements on paper or by design at TRL 3 and is over its value-engineering target on the tenth (R9). On 2026-10-03 Amish decided "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A": for CanalRung, 4A (smaller ropes, and R2 restated to 4.5 kg if the ladder still exceeds 4.0 kg) and 9A (the 500 x 1,200 mm footing standard at every site). Four requirements also need trials with people before they can be closed (R2 throw accuracy, R5 climb time, R7 deploy time, R8 ageing); those are TRL 4 work. Status comes from the calculation note CNR-CAL-001; the tag in brackets is the line of `docs/04-calcs/sizing.py` that carries the figure.

> **Safety:** CanalRung is safety-critical rescue and rope equipment. These requirements describe a research prototype, published as an open engineering reference and never as certified life-saving equipment. Meeting them on paper does not make the ladder safe to use; only proof loads, tank trials under lifeguard supervision and field trials can show that. Never enter the water to rescue someone: throw, anchor and call the emergency number.

## Design envelope

The first version is sized for lined canals where the water is up to 2.0 m below the coping on a 1.5:1 (horizontal to vertical) side slope, or up to 3.0 m below the coping on a vertical wall, with surface currents up to 2.0 m/s and water from 5 to 30 °C. The design case in the model is the 1.5:1 slope with the water 2.0 m below the coping. Deeper slopes need a longer ladder (a later variant, CNR-DDR-001, D1).

*Table 1. Requirements and status at TRL 3.*

| ID | Requirement | Target | Verification | Status at TRL 3 |
| --- | --- | --- | --- | --- |
| R1 | Reach the water from the bank | Rung section at least 4.0 m; at least two rungs at or below the water line on the design walls (1.5:1 slope to 2.0 m, vertical wall to 3.0 m) | Calculation [A1] to [A5]; deploy on a test wall at TRL 4 | Met on paper: 4,020 mm; two rungs in the water on the design slope and four on a 3.0 m vertical wall; works on 1.5:1 slopes to 2.1 m and vertical walls to 3.8 m |
| R2 | Throwable by one adult | Ladder as thrown (everything that leaves the box) at most 4.5 kg (9.9 lb), restated by Amish on 2026-10-03 from 4.0 kg; 8 of 10 untrained adults land the throw weight within 1 m of a target 3 m upstream | Weigh; throw trials with volunteers | Met on paper on mass: 4.27 kg [B3], 0.23 kg inside; throw accuracy needs trials |
| R3 | Rungs float at the water line | Every rung floats with at least 0.15 kg to spare, with its share of rope; the bottom three rungs carry the throw weight with a factor of at least 1.5 | Calculation [C1] to [C3]; tank test | Met on paper: 0.27 kg (plain) and 0.22 kg (stand-off) per rung; factor 1.73 |
| R4 | Carry a climbing adult | Each rung takes 1.5 kN at mid-span at no more than two thirds of yield; the two side ropes with their knots, wet, hold at least four times 4.5 kN (18 kN) | Calculation [D1], [E1]; proof-load test (TRL 4) | Met on paper: rung at 0.56 of yield; 9 mm ropes 18.4 kN, 4.08 times 4.5 kN |
| R5 | Climbable on a flat wall | Clear width at least 280 mm; rung pitch 300 to 350 mm; at least 60 mm of hand room behind the rung at the stand-offs; an adult volunteer climbs out of a 1.5 m deep test tank with a smooth vertical wall in under 60 s | Geometry [A6]; supervised tank trials with lifeguards | Geometry met by design (298 mm, 335 mm, 70 mm); climb time needs trials |
| R6 | Anchor holds | Station anchor (eye nut, bolt, post and the standard 500 x 1,200 mm footing used at every site) holds 4.5 kN with a factor of at least 1.5 on each element, in drained or saturated granular bank soil (restated by Amish on 2026-10-03) | Calculation [G1] to [G6]; pull test on site | Met on paper: eye nut 1.53; footing 3.58 drained, 1.59 saturated |
| R7 | Deploy quickly | Lid open to ladder in the water in under 30 s, using only the pictogram on the lid | Timed trials with untrained volunteers | Not verifiable at TRL 3; estimate 15 s [H1] |
| R8 | Survive outdoor storage | Ropes and rungs keep at least 80 % of strength after the equivalent of 2 years of outdoor exposure | Accelerated UV ageing and pull test | Met by design (stored in an opaque UV-stabilised box) [H2]; to confirm by test |
| R9 | Value for money | Parts cost reported against the value-engineering target of USD 500, including the post, footing and box | Costed bill of materials [I1] | Value-engineering target: USD 500. Estimated cost of the constructable design: USD 605.20 (USD 105.20 over the target) |
| R10 | Nothing thrown can hurt the person in the water | Soft throw weight; no exposed sharp edges or tube ends; a blunt-tip knife at the station to cut rope if anyone is caught | Inspection | Met by design [H3] |

## Requirements not met or at risk

- **R2 (restated, now met on mass):** with 9 mm ropes the ladder as thrown weighs 4.27 kg, still 0.27 kg over the earlier 4.0 kg, so the target was restated to 4.5 kg under Amish's fallback in decision 4A (CNR-DDR-003). The stronger rungs were kept. Whether 4.3 kg is easy to throw is a question for the TRL 4 throw trials.
- **R4 (thin margin on the ropes):** the 9 mm EN 1891 type B ropes hold 18.4 kN wet with knots, 4.08 times 4.5 kN, just over the four times R4 asks for and above Amish's floor of three times. The bought rope must declare at least 18 kN.
- **R6 (soil outside the screening values):** the standard footing holds with factors of 3.58 in drained and 1.59 in saturated granular soil. Soft clay or peat banks need a site pull test.
- **R9 (over the target):** the larger standard footing adds USD 65.00 of concrete; the estimate is USD 105.20 over the value-engineering target.

## Assumptions

- Many canal falls happen near places where a station can be placed: crossings, pump houses, paths and farms.
- A person in cold water can grip a rung long enough to climb if the rung is within reach.
- Throwing upstream and letting the current carry the ladder is easier for a bystander than throwing to the person.
- Irrigation districts would allow stations on their banks.
- The design climber is 100 kg with a dynamic factor of 1.5 (1.47 kN); the 4.5 kN anchor target is about three times that.
