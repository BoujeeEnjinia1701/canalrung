---
doc_id: CNR-CAL-001
title: CanalRung sizing calculations
project: CanalRung
doc_type: Calculation
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-10-03'
  author: Amish Chadha
  change: "First issue for TRL 3: reach, mass, buoyancy, rung and rope strength, loads in use, anchor and footing, deployment, cost"
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: "Design for construction (CNR-DDR-002) applied: rope-through-rung joint, stand-off blocks, crush tube, rope cut length and mass, cost by build-order BOM"
---

# CanalRung sizing calculations

On paper the constructable CanalRung meets eight of its ten requirements, misses one and is over its value-engineering target on another. The 4,020 mm rung section puts two rungs in the water on the design slope (1.5:1, water 2.0 m below the coping) and four on a 3.0 m vertical wall. Every rung floats with 0.22 to 0.27 kg to spare and the bottom three carry the soft throw weight 1.73 times over. A rung under a 1.5 kN point load reaches 0.56 of yield, and the two ropes with their stopper knots hold 22.4 kN wet, five times the 4.5 kN target. The anchor holds 4.5 kN with factors of 1.53 (eye nut) and 1.92 (footing in drained soil); a saturated bank needs a larger footing. The ladder as thrown weighs 4.48 kg against a 4.0 kg target (R2 not met), and the parts cost USD 543.60 against the USD 500 value-engineering target. Every number below is printed by `docs/04-calcs/sizing.py`; the tag in brackets, for example [C2], is the line of that script's output that carries it.

> **Safety:** These are first-principles estimates for a paper proof of concept. They do not show that the ladder, its knots or the anchor are safe to use. Rope, knot, rung and anchor strengths must be proof-loaded (CalRig, TRL 4) and the climb, throw and deployment tried in a supervised test tank before any station is placed at a canal. Never enter the water to rescue someone. See CNR-PRC-001, Safety.

## Scope and method

The note checks every requirement in CNR-REQ-001 against the constructable design in `cad/src/model.py` (CNR-DDR-002). The script imports the model's parameters and builds the ladder once for part volumes, so the rungs, float sleeves, bushes and stand-off blocks used here are the ones in the STEP files and drawings. It reads `bom/bom.csv` and `budget_usd` in `project.yaml`. Run it from the repo root with `python docs/04-calcs/sizing.py`; it also writes `docs/04-calcs/results.csv`.

The design case is the station 1,000 mm back from the coping of a concrete-lined canal with a 1.5:1 (horizontal to vertical) side slope, the water 2.0 m below the coping and flowing at up to 2.0 m/s, and a 100 kg adult climbing out.

## Assumptions

*Table 1. Main assumptions.*

| Area | Assumption | Basis |
| --- | --- | --- |
| Climber | 100 kg, clothed and wet; dynamic factor 1.5 for grabbing and climbing (1.47 kN) | Screening value for a heavy adult |
| Rung | 6061-T6 drawn tube, 240 MPa minimum yield; load as a point at mid-span between the ropes (320 mm), simply supported | Conservative: hands and feet usually load nearer the ends |
| Rope | EN 1891 type A, minimum breaking strength 22 kN; overhand stopper knot keeps 60 % (literature 55 to 65 %); wet 85 %; over a 10 mm unprotected edge 50 % | Typical published values; to be proof-loaded |
| Buoyancy | Fresh water 1,000 kg/m3; foam 33 kg/m3 closed cell; aluminium 2,700, nylon 1,140, HDPE 950, polyester 1,380 kg/m3; tube bore floods through the rope holes; rope share per rung includes 100 mm in each knot | Handbook densities |
| Current | 2.0 m/s surface current; person holding a rung, drag area 0.35 m2; rung drag coefficient 1.2 | Screening values |
| Anchor | Eye nut working load limit 700 kg in line with the thread (DIN 582 class, M16); 10 mm screw link 1,000 kg; M16 grade 8.8 proof 600 MPa on 157 mm2 | Catalogue classes; the bought parts must be marked |
| Post | S235 square hollow section 60 x 60 x 3; anchor 250 mm above ground | |
| Soil | Drained, medium dense granular bank: unit weight 18 kN/m3, friction angle 30°; saturated case 8 kN/m3 submerged | Screening values; to be confirmed on site |
| Footing | Short rigid pile in cohesionless soil (Broms), free head: ultimate lateral load 0.5 γ D L³ Kp / (e + L) | Broms (1964) |

## A. Reach and climbing geometry (R1, R5)

The rung section is 4,020 mm: 13 rungs at 335 mm pitch [A1]. On the 1.5:1 design slope (33.7°), rung 1 lies 150 mm down the wall from the coping [A2] and the bottom rung ends 2,313 mm below the coping, 313 mm below the water line, so rungs 12 and 13 are in the water and rung 11 is 59 mm above it [A3]. Because the rungs float, the ones that reach the water rise to the surface. The ladder still puts two rungs at or below the water line when the water is 2,127 mm below the coping [A4]. On a vertical wall with the water 3,000 mm down, the bottom rung is 1,170 mm under water with four rungs in it, and two rungs reach the water down to 3,835 mm [A5]. R1 is met for the stated design envelope; deeper sloped canals need the longer variant.

The clear width between the rope bushes is 298 mm, the pitch 335 mm, and at each stand-off rung the float sleeve stands 70 mm off the wall, room for a hand [A6]. R5's geometry is met by design; the climb time needs a tank trial.

## B. Mass (R2)

*Table 2. Mass of the ladder as thrown [B2].*

| Part | Mass (kg) |
| --- | --- |
| Rungs (13) | 1.715 |
| Float sleeves (13) | 0.161 |
| Rope bushes (26) | 0.091 |
| End caps (26) | 0.104 |
| Stand-off blocks (8) | 0.420 |
| Stand-off bolts (8) | 0.080 |
| Side ropes, 2 x 7.95 m at 68 g/m [B1] | 1.081 |
| Seizings | 0.020 |
| Screw links (2) | 0.120 |
| Throw weight with pouch | 0.530 |
| Edge protectors (2) | 0.160 |
| **Total** | **4.48** |

The ladder as thrown weighs 4.48 kg, 0.48 kg over the 4.0 kg target of R2 [B3]. **R2 is not met.** Rungs of 25.4 x 1.65 mm tube would save 0.20 kg [B4] but would take the rung past the stress limit (D2), so they were rejected. Savings worth trying at TRL 4 are listed in the design decisions register.

## C. Buoyancy (R3)

A plain rung with its share of rope floats with 0.274 kg to spare and a stand-off rung with 0.218 kg, both above the 0.15 kg target [C1]. In water the throw weight weighs 0.442 kg; rungs 11, 12 and 13 together lift 0.765 kg, a factor of 1.73 against the 1.5 target [C2], so the weight hangs below the floating rungs instead of pulling them under. The whole ladder in water has 2.89 kg of spare lift [C3]. **R3 is met on paper.** The tube bore is not counted: it floods through the rope holes.

## D. Rung strength (R4)

The 28.6 x 1.65 mm 6061-T6 tube has a section modulus of 890 mm3. A 1.5 kN point load at mid-span over the 320 mm between the ropes gives 120 N m and 135 MPa, 0.56 of the 240 MPa minimum yield, inside the two-thirds limit [D1]. The lighter 25.4 x 1.65 mm tube would reach 175 MPa, 0.73 of yield [D2].

Each rung end passes 750 N through the bush flange onto the knot; the nylon flange bears at about 17 MPa on a 2 mm contact band, against about 50 MPa for nylon to yield [D3]. With the whole climber on one stand-off rung on the 1.5:1 slope, each block pushes on the wall with 612 N; wall friction tries to turn the block round the rung with 17.4 N m, which puts 610 N across the M5 bolt, against about 6 kN for its two shear planes [D4].

## E. Ropes, knots and links (R4)

One side rope with a stopper knot, wet, holds 22 x 0.6 x 0.85 = 11.2 kN; both ropes 22.4 kN, 5.0 times the 4.5 kN target and over the 18 kN that R4 asks for [E1]. If a rope were pulled over an unprotected 10 mm coping edge as well, both ropes would still hold 11.2 kN [E2]; the edge protectors are there to keep the rope off that edge. The 10 mm screw links have a working load limit of 9.8 kN, 2.18 times the target [E3]. **R4 is met on paper.**

## F. Loads in use

The design climber with the dynamic factor loads the ladder with 1.47 kN [F1]. On the 1.5:1 slope the ropes carry only the part of that along the wall, 0.82 kN (wall friction ignored); on a vertical wall they carry all 1.47 kN [F2]. A person holding a rung in a 2.0 m/s current adds 700 N of drag, and three rungs in the water 106 N [F3]. Adding the vertical-wall climb and the full current drag together, which cannot both happen at full value, gives an upper bound of 2.32 kN on the anchor, inside the 4.5 kN target by a factor of 1.94 [F4].

## G. Anchor: eye nut, bolt, post and footing (R6)

*Table 3. Anchor elements against the 4.5 kN target.*

| Element | Capacity | Factor | Tag |
| --- | --- | --- | --- |
| Forged M16 eye nut, in line | 6.87 kN working load limit | 1.53 | [G1] |
| M16 grade 8.8 bolt | 94 kN proof load | 21 | [G2] |
| Post wall under the 50 mm washer | 66 kN punching | 15 | [G2] |
| Post, 60 x 60 x 3 at 250 mm | 91 MPa, 0.39 of yield | 2.6 | [G3] |
| Footing 400 x 1,000, drained soil | 8.6 kN ultimate | 1.92 | [G4] |
| Same footing, saturated soil | 3.8 kN ultimate | 0.85 | [G5] |
| Footing 500 x 1,200, saturated soil | 7.2 kN ultimate | 1.59 | [G5] |

The standard footing takes about 0.12 m3 of concrete, about 12 bags of 25 kg [G6]. **R6 is met on paper in drained soil.** On a saturated or soft bank the standard footing is not enough and the 500 x 1,200 mm footing (with a 2,300 mm post) is used; the soil is a fact to confirm at each site.

## H. Deployment, storage and safety (R7, R8, R10)

Lifting the lid (2 s), taking the throw weight and the top of the folded ladder (4 s), throwing upstream (4 s) and letting the ladder pay out (5 s) add up to about 15 s, inside the 30 s of R7; this is an estimate, and R7 can only be closed by timed trials [H1]. The ropes, rungs and foam live in an opaque UV-stabilised box and see daylight only when used or inspected, which is how R8 is met by design; an ageing test closes it [H2]. Nothing thrown is hard: the throw weight is a soft shot pouch, rung ends are capped and holes bushed, and a blunt-tip knife is kept in the lid (R10, met by design) [H3].

## I. Cost (R9)

Value-engineering target: USD 500. Estimated cost of the constructable design: USD 543.60 (USD 43.60 over the target) [I1]. The station (post, footing, anchor, box, decals, knife and consumables) is USD 286.20 and the ladder USD 257.40 [I2].

## Results against the requirements

*Table 4. Requirement status at TRL 3.*

| ID | Status | Figures |
| --- | --- | --- |
| R1 | Met on paper | 4,020 mm rung section; 1.5:1 slopes to 2.1 m, vertical walls to 3.8 m |
| R2 | **Not met (mass)**; throw accuracy needs trials | 4.48 kg against 4.0 kg |
| R3 | Met on paper | 0.27 and 0.22 kg per rung; bottom three rungs 1.7 times the weight |
| R4 | Met on paper | Rung 0.56 of yield; ropes 22.4 kN wet with knots |
| R5 | Met by design; climb time needs trials | 298 mm clear, 335 mm pitch, 70 mm hand room |
| R6 | Met on paper in drained soil | Footing 1.92; eye nut 1.53; saturated soil needs the larger footing |
| R7 | Not verifiable at TRL 3 | Estimate 15 s |
| R8 | Met by design; to confirm by test | Stored in an opaque box |
| R9 | Over the value-engineering target | USD 543.60 against USD 500 |
| R10 | Met by design | Soft weight, capped ends, knife |
