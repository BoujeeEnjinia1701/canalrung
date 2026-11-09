---
doc_id: CNR-DDR-004
title: CanalRung concept options and selection
project: CanalRung
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-11-05'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-11-05'
  author: Amish Chadha
  change: "Concept options A, B and C compared and scored; option A recommended; choice proposed, awaiting Amish; two option B fixes recorded under the 2026-10-23 standing instruction"
---

# 0004: Concept options and selection

- **Date:** 2026-11-05
- **Status:** Proposed, awaiting Amish. The concept choice is Amish's decision. Two detail fixes inside option B (items 2 and 3 below) were made under his standing instruction of 2026-10-23 and are decided as such.

## Context

The kit 1.9.1 pipeline asks for at least two concept options with different working principles. The current design (the thrown rope ladder on a bank post, built up over CNR-DDR-001 to CNR-DDR-003) is option A and does not change. Options B and C were added and modelled at the same D3 detail (`cad/src/cnr_opts.py`). CNR-OPT-001 holds the full comparison and scores; CNR-STM-001 the science checks.

## Options considered

*Table 1. Options.*

| Option | Working principle | Score (of 145) | STEM check |
| --- | --- | --- | --- |
| A | A bystander throws a floating 13-rung rope ladder that is already linked to an anchor eye on a bank post; the person climbs out | 107 | 4 within, 9 plausible |
| B | A rigid folding aluminium ladder is lowered over the coping and hangs on rubber pads with a lanyard to the post; the person climbs out | 88 | 3 within, 2 plausible, 2 fixed |
| C | A bystander cranks a hand winch on a bank post that hauls a floating sling, put on by the person, up the wall; nobody climbs | 92 | 3 within, 2 plausible |

## Decision

1. **Concept choice (Proposed, awaiting Amish):** option A, 14 percent ahead of option C, outside the 10 percent band, so both are not sent forward as a tie. `project.yaml` records `concept_chosen` as proposed and open. If Amish prefers a different option, the model, drawings, BOM, build plan and calculations are for A and would need to be redone.
2. **Option B rung (decided under the 2026-10-23 standing instruction):** the rung is 25.4 x 3.2 mm tube instead of 25.4 x 1.6 mm, because 206 MPa (0.86 of yield) failed the two-thirds rule (STM S13); now 125 MPa (0.52). Same outside diameter, so the stile holes are unchanged; the ladder weighs about 0.1 kg more per rung, 10.6 kg in all.
3. **Option B splice (decided under the same instruction):** the stile splice moved from mid-span between the wall pads onto the middle pad (z 2,250 mm), with a 200 mm sleeve, because bolt bearing of 188 MPa failed (STM S16); now 70.5 MPa. Neither fix changes the working principle, pitch or scope.

## Consequences

- A stays the current design; nothing in the BOM, drawing, calculations or build plan changes.
- The graft ideas (B's EPDM pads for grip, C's collar as a second grab point) are listed in CNR-OPT-001 and are not designed.
- The open STEM rows (S4, S5, S8, S9, S10, S11, S12, S15, S17, S18, S22, S23) are test, datasheet or decision items; three independent-review findings on option A (footing on a slope crest, rope margin at end of life, eye nut off axis) go to Amish as open decisions 3 to 5 in CNR-DEC-001. Tests are TRL 4 and not started here.
- Nothing in this record authorizes building or testing. TRL 4 is outside the current portfolio phase.

> **Safety:** The weaker scores of A (climb on a slick wall, rope margin 4.08 against 4) are safety points. The choice among options does not make any of them safe to use; only proof loads and supervised trials can show that.
