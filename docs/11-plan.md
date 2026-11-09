---
doc_id: CNR-PLN-001
title: CanalRung project plan
project: CanalRung
doc_type: Project plan
version: "0.1"
status: Draft
date: '2026-11-05'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-11-05'
  author: Amish Chadha
  change: "First project plan (kit 1.9.1 upgrade): stage P3 reached; P4 to P6 on hold under the TRL 3 cap"
---

# CanalRung project plan

CanalRung is at stage P3 (design outputs, TRL 3) for option A, with options B and C modelled at the same detail; the next gate is Amish's choice among the options (CNR-DDR-004, proposed, awaiting Amish), after which the stage cap decides whether verification (P4) may start. Method: STANDARDS sections 19 and 23.

## Workstreams

Table 1. Workstreams.

| Workstream | Owner (role) | Deliverable | Status |
| --- | --- | --- | --- |
| Problem, concept and requirements | Design lead | CNR-PRB-001, CNR-PRC-001, CNR-URS-001, CNR-PRS-001 | Done (P3) |
| STEM check and concept options | Design lead | CNR-STM-001, CNR-OPT-001, CNR-DDR-004 | Done; choice proposed, awaiting Amish; independent review recorded |
| Calculations | Design lead | CNR-CAL-001 (option A only); options B and C screened in the STEM check | Done for A |
| Detailed CAD | Design lead | `cad/src/model.py` for A, B and C at D3; STEP, drawings, media | Done |
| Pipeline documents | Design lead | CNR-REG-001, CNR-FEA-001, CNR-RSK-001, CNR-MKT-001, CNR-PLN-001, CNR-RTM-001 | Done (first issue) |
| Build plan and BOM | Design lead | CNR-BLD-001, `bom/bom.csv` | Done (option A) |
| Partner contact | Amish | Kittitas Reclamation District; Water Safety Council of Fresno County | Not started; not contacted |
| Verification (P4) | To be named | Proof loads, throw and climb trials, UV ageing | On hold |

## Resources needed

Table 2. Resources.

| Resource | Deliverable | Effort | Estimated cost (USD) |
| --- | --- | --- | --- |
| Design lead (Claude with Amish's review) | P0 to P3 documents | Done | 0 |
| Prototype parts | One option A station (P4, on hold) | | 605.20 (BOM, indicative; Amish decides) |
| Proof-load rig (CalRig, a candidate shared block) | Rope, rung and anchor proof loads (P4, on hold) | To assess | To assess |
| Supervised test tank and lifeguards | Climb and throw trials (P4, on hold) | To assess | To assess |
| Partner site survey | Heights, slopes, soils, flows | To assess | To assess |
| Regulatory reviewer | Classification and approval route (CNR-REG-001 G3) | To assess | To assess |

## Stage gates

Table 3. Stages (P4 to P6 on hold while the stage cap is P3).

| Stage | Gate criteria | Status |
| --- | --- | --- |
| P0 Proposal | PRB, STM, OPT, REG, FEA, PLN | Done 2026-11-05 (kit 1.9.1 documents) |
| P1 Definition | URS, PRS draft, RSK, MKT, REG | Done 2026-11-05 |
| P2 Design inputs | PRS targets, CAL, RTM, DDR, STEM check closed | Done 2026-11-05; twelve STEM rows stay open for tests, datasheets or Amish's decisions (S4, S5, S8, S9, S10, S11, S12, S15, S17, S18, S22, S23) |
| P3 Design outputs | Model, STEP, DWG, BOM, BLD, DEC, FMEA | Done 2026-11-05 |
| P4 Verification | Proof loads, throw and climb trials, UV ageing | On hold |
| P5 to P6 | Field trials with a partner, launch | On hold |

## Next steps and decision requested

Decision requested from Amish: choose among options A, B and C (recommended: A, CNR-DDR-004), and decide the three fixes proposed after the independent review (CNR-DEC-001, open decisions 3 to 5: a deeper footing, the rope margin rule, the eye nut off axis). Also open: whether to keep the USD 605.20 cost against the USD 500 target as a reported overrun (the target is not changed here), and whether to approve contacting the two candidate partners. After the cap is lifted: proof loads of the rope and a roped rung, a supervised tank trial of climbing and throwing, and an ageing test (all TRL 4 and not started).

## References

- CNR-PRB-001 prior work table, for the competitor sources.
- See the source lists in CNR-STM-001, CNR-REG-001 and CNR-MKT-001.
