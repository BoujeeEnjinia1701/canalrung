---
doc_id: CNR-STM-001
title: CanalRung STEM check
project: CanalRung
doc_type: STEM check
version: "0.1"
status: Draft
date: '2026-11-05'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-11-05'
  author: Amish Chadha
  change: "First STEM check for the kit 1.9.1 upgrade: 23 claims for option A (the current design) and options B and C; two failures in option B fixed under the 2026-10-23 standing instruction (CNR-DEC-001); independent review recorded"
---

# CanalRung STEM check

Of 23 claims, 10 sit within known science and 13 are plausible; none fails after two detail failures in option B were fixed under Amish's standing instruction of 2026-10-23 and after the independent review moved three verdicts from within known science to plausible (S4, S9, S15) and added one claim (S23). One plausible claim (S3) is closed by the calculation note CNR-CAL-001 and twelve stay open until a test, a datasheet or Amish's decision on a proposed fix (S4, S5, S8, S9, S10, S11, S12, S15, S17, S18, S22, S23). Method and rules: STANDARDS section 20. Calculations: `docs/04-calcs/stem_check.py` (output `docs/04-calcs/stem_results.csv`), which computes every number from the model parameters and handbook constants, independently of `docs/04-calcs/sizing.py`.

> **Safety:** CanalRung is research and educational rescue-equipment design, never certified life-saving equipment. A claim that sits within known science on paper says nothing about whether the ladder, its ropes or its anchor are safe to use. Never enter the water to rescue someone: throw, anchor and call the emergency number.

## Claims checked

*Table 1. Claims, governing science and verdicts. Figures are those printed by `stem_check.py`.*

| # | Claim (number and unit) | Field | Branch | Governing law or source | First-order check | Verdict | Closed by |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | A: a 28.6 x 1.65 mm 6061-T6 rung carries the 1.47 kN climber load (100 kg x 1.5) at mid-span | Physics | Strength of materials | Simply supported beam M = F L / 4; hollow section modulus; yield 240 MPa | 132.2 MPa against 160 MPa (two thirds of yield) | Within known science | CNR-CAL-001 D1 |
| S2 | A: each foam-sleeved rung floats with at least 0.15 kg spare lift before the rope share | Physics | Fluid statics | Archimedes; bore floods through the rope holes | 0.29 kg against 0.15 kg | Within known science | CNR-CAL-001 C1 |
| S3 | A: two wet 9 mm EN 1891 type B ropes with stopper knots hold four times 4.5 kN | Engineering and technology | Rope and knots | Catalogue breaking strength 18 kN x knot 0.60 x wet 0.85 | 18.36 kN against 18 kN, equal sharing; 14.7 kN (factor 3.3) after the R8 ageing allowance | Plausible, to confirm at TRL 3 | CNR-CAL-001 E1 (proof load at TRL 4); see review finding 2 |
| S4 | A: the 500 x 1,200 mm footing holds 1.5 x 4.5 kN in drained granular soil | Physics | Geotechnics | Broms (1964), short rigid pile, free head, level ground | 16.1 kN against 6.75 kN on level ground; the slope-crest reduction is not applied | Plausible, to confirm at TRL 3 | Open: site pull test; review finding 1; fix proposed to Amish |
| S5 | A: the same footing holds 1.5 x 4.5 kN in saturated soil | Physics | Geotechnics | Broms (1964), submerged unit weight 8 kN/m3, level ground | 7.2 kN against 6.75 kN, 7 percent over, before any slope-crest reduction | Plausible, to confirm at TRL 3 | Open: site pull test; review finding 1; fix proposed to Amish |
| S6 | A: a person holding on in a 2 m/s current while climbing loads the anchor to under 4.5 kN | Physics | Fluid mechanics | Drag F = 0.5 rho Cd A v^2, Cd A 0.35 m2, plus the climbing load | 2.17 kN against 4.5 kN | Within known science | CNR-CAL-001 F3, F4 |
| S7 | A: the 4,020 mm rung section reaches the water on the 1.5:1 design slope with two rungs in it | Mathematics | Geometry | Slope length to the water line less the top offset along the slope, plus one pitch | 3,791 mm against 4,020 mm | Within known science | CNR-CAL-001 A3 |
| S8 | A: one adult throws the 4.27 kg ladder 3 m to the water | Physics | Mechanics | Projectile range, 45 deg; kinetic energy against 300 W for 0.3 s | 62.8 J against 90 J | Plausible, to confirm at TRL 3 | Open: throw trials (R2, TRL 4) |
| S9 | A: a nylon rope bush takes the full 1.47 kN of a foot at one rung end on a 2 mm contact band (the CAL uses 750 N per end) | Engineering and technology | Strength of materials | Flange bearing stress against water-saturated nylon (PA6) yield taken as 35 MPa (dry about 50 MPa; class values) | 32.8 MPa against 35 MPa | Plausible, to confirm at TRL 3 | CNR-CAL-001 D3 (750 N per end); proof load at TRL 4; review finding 7 |
| S10 | A: ropes, rungs and foam keep 80 percent of strength after 2 years of outdoor storage | Chemistry | Polymer ageing | UV degrades polyester and polyamide; the opaque box limits exposure | Literature only, no calculation | Plausible, to confirm at TRL 3 | Open: accelerated ageing and pull test (R8) |
| S11 | A: an aluminium plate on a galvanised steel post does not corrode through in 2 years | Chemistry | Corrosion | Zinc and aluminium sit close together in the galvanic series in neutral water | No calculation | Plausible, to confirm at TRL 3 | Open: watch at TRL 4 (RSK F8) |
| S12 | A: a person in 5 to 30 C water can grip and climb the 335 mm pitch in under 60 s | Biology | Human physiology | Cold immersion reduces grip strength and coordination within minutes | 6 rungs at about 5 s is 30 s for a fit adult; more for a child | Plausible, to confirm at TRL 3 | Open: supervised tank trial (R5, TRL 4) |
| S13 | B: a 25.4 x 3.2 mm 6061-T6 rung carries 1.5 kN at mid-span between the stiles | Physics | Strength of materials | Simply supported beam; yield 240 MPa | 124.8 MPa against 160 MPa. The first design (1.6 mm wall) gave 206 MPa, 0.86 of yield: a fail | Within known science | Fixed, CNR-DEC-001; not in the CAL |
| S14 | B: each RHS 25 x 45 x 2 stile bridges 1.8 m between wall pads under a climber | Physics | Strength of materials | Point load at mid-span, two stiles, strong axis | 89.5 MPa against 160 MPa | Within known science | Not in the CAL |
| S15 | B: the 10 mm lanyard holds the along-slope part of a climber (0.82 kN) with a factor of 4 | Engineering and technology | Rope and knots | A catalogue breaking strength for the 10 mm rope is not cited | Unknown; the vertical-wall case (1.6 kN) is not checked | Plausible, to confirm at TRL 3 | Open: datasheet (to assess); review finding 5 |
| S16 | B: the splice sleeve bolts pass the stile bending moment by bearing on a 2 mm wall | Physics | Strength of materials | Support moment of a stile continuous over a pad, 3PL/32; couple over two M5 bolts 176 mm apart | 70.5 MPa against 160 MPa. The first design put the splice at mid-span: 188 MPa, a fail | Within known science | Fixed, CNR-DEC-001; not in the CAL |
| S17 | B: one adult carries and lowers the 10.6 kg ladder over the coping | Biology | Human factors | NIOSH lifting equation, 23 kg load constant (ideal case) | Under half the constant, but a lever of about 1 m when lowering | Plausible, to confirm at TRL 3 | Open: handling trial |
| S18 | C: one adult hand-cranks a 100 kg person up the wall at 0.043 m/s (98 s for 4.2 m; handle force about 150 N) | Physics | Mechanics | T = m g (sin a + mu cos a), mu 0.5; power T v / 0.85 against 75 W sustained | 47.9 W against 75 W | Plausible, to confirm at TRL 3 | Open: crank trial; review finding 3 |
| S19 | C: the RHS 100 x 60 x 4 boom carries the sheave reaction 1.43 m from the post | Physics | Strength of materials | Sheave resultant 1.2 T; S235 | 49.5 MPa against 157 MPa | Within known science | Not in the CAL |
| S20 | C: the 600 x 1,200 mm footing resists the boom's overturning moment | Physics | Geotechnics | Broms limit moment against 1.5 x the moment at ground level | 3,166 N m against 27,990 N m | Within known science | Not in the CAL |
| S21 | C: the float collar (torus of 270 mm major and 55 mm minor radius) displaces enough water to support a clothed adult; head-up stability is not checked | Physics | Fluid statics | Torus volume 2 pi^2 R r^2; negative buoyancy of an adult taken as 5 kg (screening value) | 16.1 kg against 10 kg | Within known science | Not in the CAL; review finding 4 |
| S22 | C: the 8 mm rescue rope holds the 1.0 kN haul with a factor of 5 | Engineering and technology | Rope and knots | A catalogue breaking strength for 8 mm rope is not cited | Unknown | Plausible, to confirm at TRL 3 | Open: datasheet (to assess) |
| S23 | A: the forged M16 eye nut holds 4.5 kN with a factor of 1.5 at the real pull angle | Engineering and technology | Strength of materials | DIN 582 class working load limit 700 kg applies in line with the thread; the rope pulls 14 to 34 degrees off the axis | 1.53 in line; off axis not shown | Plausible, to confirm at TRL 3 | Open: rating at the pull angle (to assess); review finding 6; fix proposed to Amish |

Verdicts: **Within known science**, **Plausible, to confirm at TRL 3**, **Fails**. S13 and S16 first failed and now carry the verdict of the fixed design; the failing values are in the claim text of `stem_check.py` and in Table 2.

## Failures and fixes

*Table 2. Failures found and the fixes made under the standing instruction of 2026-10-23 (recorded in CNR-DEC-001).*

| Claim | What failed | Fix | Keeps the working principle |
| --- | --- | --- | --- |
| S13 | Option B rung of 25.4 x 1.6 mm tube: 206 MPa, 0.86 of yield, over the two-thirds limit | Wall raised to 3.2 mm at the same 25.4 mm outside diameter (a stock tube, so the stile holes are unchanged); 125 MPa, 0.52 of yield; rung mass up by about 0.1 kg, ladder 10.6 kg | Yes: a rigid hung ladder |
| S16 | Option B splice at mid-span between pads: 188 MPa bearing on the 2 mm wall | Splice moved onto the middle wall pad (z 2,250 mm) where the continuous-beam moment is 0.375 of the mid-span value; 70.5 MPa | Yes |

No claim of option A failed by its own numbers. S3 (18.36 kN against 18 kN), S5 (7.2 kN against 6.75 kN) and S9 (32.8 MPa against 35 MPa) sit within 10 percent of their limits, so they stay "Plausible"; they are the thin margins of the design. The reviewer's findings on the footing (S4, S5) and the eye nut (S23) go to Amish as proposed fixes because they change a decided standard (CNR-DDR-003, 9A) or a bought part; they are not made here.

## Fields not relevant

- Electrical, electronics and software: the design has no powered or electronic parts.
- Thermal and fire: no heat source; the only temperature claim is the 5 to 30 C water range, which touches S12 only.
- Optics and acoustics: none.

## Concept options

- Option A, thrown rope ladder on a bank post: 4 within known science (S1, S2, S6, S7), 9 plausible (S3 closed by CAL; S4, S5, S8, S9, S10, S11, S12, S23 open). Kept.
- Option B, coping-hook folding ladder: 3 within known science (S13, S14, S16), 2 plausible (S15, S17), after two fixes. Kept.
- Option C, post winch with a floating rescue sling: 3 within known science (S19, S20, S21), 2 plausible (S18, S22). Kept. S22 cannot be closed until an 8 mm rope datasheet is cited.

## Independent review

A second reviewer (a separate headless run of `claude -p --model claude-opus-5-5`, the current model by Amish's instruction of 2026-10-28) was given only this document, `stem_check.py`, CNR-CAL-001, the product requirements CNR-PRS-001 and `sizing.py`, none of the author's reasoning and none of the model files, and was asked to refute the headline results and every "Within known science" verdict. It recomputed the numbers by hand (it could not run the scripts). It held the arithmetic of S1, S2, S6, S13, S14, S16, S19 and S20 and found eleven points. What changed:

*Table 3. Findings and responses.*

| # | Finding | Response |
| --- | --- | --- |
| 1 | S4 and S5: Broms assumes level ground; the post is 1.0 m behind the crest of a 1.5:1 lined slope, so the passive wedge is cut; a crest reduction of about 0.5 to 0.7 (the reviewer's estimate, not cited) could take the saturated factor of 1.59 below 1.1. Closing S5 by the same formula in CAL G5 is circular | S4 and S5 moved to Plausible and stay open; "closed by CAL" removed. Proposed to Amish, not made, because it changes the footing he decided (CNR-DDR-003, 9A): deepen the footing to 1,500 mm (saturated 11.6 kN on level ground, factor 2.6; about USD 36 more concrete). CNR-DEC-001, open decision 3 |
| 2 | S3: 18.36 kN assumes equal sharing between the two ropes and a new rope; with the R8 ageing allowance it is 14.7 kN, factor 3.3 | Stays Plausible. The claim text now gives 14.7 kN and 3.3, which stay above Amish's floor of three. Proposed to Amish: say whether the R8 allowance applies to the R4 factor of four (CNR-DEC-001, open decision 4) |
| 3 | S18: the stated speed of 0.07 m/s does not follow from one turn in 5 s on a 34 mm drum radius (0.043 m/s), and losses were ignored | Fixed in the script: 0.043 m/s, efficiency 0.85, 47.9 W, 98 s for 4.2 m. OPT and the options table updated. Verdict stays Plausible |
| 4 | S21: "270/55" could be read as diameters (2 L, a fail) and volume does not show head-up stability | The model's torus is 270 mm major and 55 mm minor radius; the claim text now says so and says stability is not checked. Verdict unchanged, within for the volume only |
| 5 | S15: 9.18 kN rests on an uncited 10 mm rope rating, the same gap as S22 | Moved to Plausible, open (datasheet to assess) |
| 6 | G1 eye nut: 700 kg is an in-line rating; the rope pulls the eye 14 to 34 degrees off axis, and the factors of R6 mix bases | New claim S23 (Plausible, open). Proposed to Amish: a swivel hoist ring or a rating at the worst angle (CNR-DEC-001, open decision 5); not made, because it changes a bought part |
| 7 | S9: a foot at the rung end loads one bush with 1.47 kN, and water-saturated PA6 yields at about 35 to 40 MPa | Recomputed: 32.8 MPa against 35 MPa; moved to Plausible; proof load at TRL 4 (RSK F12) |
| 8 | S6, S1: hold; S1 text said 1.5 kN while the code used 1.47 kN | Text corrected |
| 9 | S7: the code treated the 150 mm top offset as horizontal, the CAL as along the slope | Code corrected to along the slope: 3,791 mm, still under 4,020 mm |
| 10 | CAL says the floating rungs rise to the surface, which conflicts with counting rungs below the water line as footholds | Noted for the TRL 4 tank trial; CNR-CAL-001 not edited |
| 11 | S19 and S20 use the static haul tension with no dynamic or stall case; the saturated footing case for C is missing (it passes at 12,440 N m) | Noted; option C is not chosen |

Not checked by the reviewer, for lack of the model files: foam size, bush bore, knot size, the option B ladder mass and rung count, and EN 1891 knotted-rope values.

## Sources

- Beer, F. P., E. R. Johnston, J. T. DeWolf, and D. F. Mazurek. *Mechanics of Materials*. Beam bending and section modulus (standard text; edition to cite when the repository adds a bibliography).
- Broms, B. B. 1964. "Lateral Resistance of Piles in Cohesionless Soils." *Journal of the Soil Mechanics and Foundations Division, ASCE* 90 (SM3): 123 to 156. Search result for the method, checked 2026-11-05: [ISSMGE paper index](https://www.issmge.org/uploads/publications/1/141/600.pdf) (the page was not read in full; the method is also used in CNR-CAL-001).
- EN 1891:1998, *Personal protective equipment for the prevention of falls from a height: low stretch kernmantel ropes*. Listing checked 2026-11-05: [Genorma](https://genorma.com/en/standards/en-1891-1998). The standard itself was not read; type A and type B strengths are catalogue class values to confirm.
- Waters, T. R., V. Putz-Anderson, A. Garg, and L. J. Fine. 1993. "Revised NIOSH Equation for the Design and Evaluation of Manual Lifting Tasks." *Ergonomics* 36 (7): 749 to 776. Cited from memory for the 23 kg load constant; link to add.
- Handbook values: 6061-T6 minimum yield 240 MPa and S235 yield 235 MPa (EN 10025-2), nylon PA6 yield about 50 MPa, fresh water 1,000 kg/m3, human sustained crank power 75 W and peak 300 W (`.kit/stem_check.py` limits).
- CNR-CAL-001 (`docs/04-calcs/01-sizing.md`) for the closed rows.
