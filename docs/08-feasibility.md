---
doc_id: CNR-FEA-001
title: CanalRung feasibility assessment
project: CanalRung
doc_type: Feasibility assessment
version: "0.1"
status: Draft
date: '2026-11-05'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-11-05'
  author: Amish Chadha
  change: "First feasibility assessment (kit 1.9.1 upgrade) for option A, with a line on options B and C"
---

# CanalRung feasibility assessment

Option A is feasible on paper, with the rope margin, the cost (USD 605.20 against the USD 500 target) and the climb on a slick wall as the open points; none of it is shown by test. Method: STANDARDS section 23.

Table 1. Feasibility by aspect (option A unless stated).

| Aspect | Assessment | Rating | Risks and notes | Evidence |
| --- | --- | --- | --- | --- |
| Design | The reach, mass, buoyancy, rung, rope and anchor numbers all meet their targets on paper; 13 STEM claims for A: 4 within, 9 plausible | High | Rope factor 4.08 against 4 (3.3 after ageing), the saturated-soil footing factor 1.59 against 1.5 (before a slope-crest reduction the CAL does not include) and the eye nut load off its axis are thin or unchecked | CNR-STM-001, CNR-CAL-001 |
| Materials | Stock aluminium tube, galvanised SHS, EN 1891 rope, nylon, HDPE, closed-cell foam, concrete | Medium | UV ageing of rope and foam is a test item; aluminium on galvanised steel is a weak galvanic couple (S10, S11) | CNR-STM-001 |
| Manufacturing and assembly | Cut, drill and bolt with hand tools; no welding; 178 parts, 135 made or bought and 43 fasteners in the D3 model | High | Whether a village workshop can drill and ream 26 rung ends to size | CNR-BLD-001, `cad/fidelity.json` |
| Power and controls | None | High | No electrical or electronic parts | none |
| Supply of parts | Catalogue items in most regions; the rope, eye nut and foam must declare their ratings | Medium | Prices are indicative and unverified on 2026-11-05 (see CNR-MKT-001) | BOM |
| Cost | USD 605.20 for the parts, USD 105.20 over the value-engineering target | Medium | The footing is USD 143 of it; no labour counted | BOM, CNR-CAL-001 I1 |
| Use and safety | A bystander can throw it, a person can climb it | Low | Neither is shown; both need supervised trials (TRL 4) and a person must never enter the water | CNR-PRS-001 PR-002, PR-005, PR-007 |
| Options B and C | B (10.6 kg rigid ladder) and C (hand winch with a floating sling) are buildable on paper at D3 | Medium | B is hard to handle over an edge; C needs welding and an 8 mm rope rating that is not cited | CNR-OPT-001, CNR-STM-001 |

Ratings: High, Medium, Low.
