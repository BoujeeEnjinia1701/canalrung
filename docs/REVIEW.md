# Review note: CanalRung

## Session 2026-09-30: scaffolded

### What was done

- Repository created from kit 1.6.0 at TRL 1, target TRL 2.
- `docs/01-problem.md` (CNR-PRB-001 v0.1): problem with cited evidence, users, environment, constraints, prior work, open questions.
- `docs/02-concept.md` (CNR-PRC-001 v0.1): how it works, components, patent design-arounds, shared blocks, safety.
- `docs/03-requirements.md` (CNR-REQ-001 v0.1): 9 proposed requirements.
- `README.md` with concept rationale, burning platform, where it could be used, and what sparked the idea.

### Next

- Run `/populate` to bring the repo to a strong TRL 2 with concept media.

## Session 2026-10-03: TRL 2 (populate), kit 1.7.0

Run as the first half of `/to-trl3` under Amish's pre-approval of 2026-10-03: "start with the first 14 repos from the list of 29 projects. I pre-approve the batch runs along with any recommendations you come up with. I also accept any cost overruns or variations from the assumed scope cost."

### What was done

- Kit 1.7.0 installed (`.kit/`, `.claude/commands/`); root `CLAUDE.md` replaced by `.kit/CLAUDE.md`; `.kit/PHASE.yaml` as installed.
- CNR-PRB-001 v0.2: design envelope, open questions answered, first co-design candidates, safety section.
- CNR-REQ-001 v0.2: measurable targets; R1 restated for the design envelope, R6 for the fixed station anchor, R10 added.
- CNR-PRC-001 v0.2: how it works, components, first-order numbers, key design choices, safety.
- CNR-DDR-001 (`docs/decisions/0001-trl2-review-decisions.md`): items D1 to D14.
- Concept media from the model: `media/hero.png`, `media/exploded.png`, `media/concept-blueprint.png` and `.pdf` (CNR-DWG-010), `media/model.glb` (coarse mesh, about 4 MB) and `media/viewer.html`. No cutaway (the joints are shown cut open in the build plan) and no flow diagram (the station moves no energy or material).
- `bom/bom.csv`: every line priced.

### Results

- The concept reaches the water on the design walls, floats, and carries a heavy climber on paper; it is over its 4.0 kg mass target and its USD 500 value-engineering target (figures in the TRL 3 section below).

### Requirements not met

- R2 (mass). See the TRL 3 section.

### Decisions made under the pre-approval

D1 to D14 of CNR-DDR-001, all dated 2026-10-03 and decided by Amish under the quote above: design envelope; the station post as the anchor; 28.6 mm rungs; EN 1891 rope with knots and seizings; stand-offs on every third rung; soft weight with floating rungs; no throw line; bought box with no lock, tamper tag and knife; load standard; R2 reported as not met; candidates Kittitas Reclamation District and the Water Safety Council of Fresno County (not contacted); pitch, problem and target unchanged.

### Safety concerns

- Rescue and rope equipment: every document carries a safety section; the conservative option was taken at D2, D3, D6, D7 and D11.
- Entanglement in moving water: no throw line; a knife in the lid.

## Session 2026-10-03: TRL 3 (advance and build plan)

### What was done

- CNR-CAL-001 (`docs/04-calcs/01-sizing.md`, script `docs/04-calcs/sizing.py`, output `results.csv`): reach, mass, buoyancy, rung and rope strength, loads in use, anchor and footing, deployment, cost.
- Parametric model `cad/src/model.py` (build123d) with 245 constructability checks, all passing (`python cad/src/model.py --check`); STEP: `cad/step/canalrung-assembly.step`, `canalrung-ladder.step`, `post.step`, `mounting-plate.step`, `rung.step`, `standoff-block.step`, `crush-tube.step`; STL of the same five parts in `cad/stl/`.
- General arrangement CNR-DWG-001 Rev P2 (`cad/src/sheets.py`), at 1:50 on the design wall.
- Design made constructable (CNR-DDR-002, `docs/decisions/0002-design-for-construction.md`); `design_state: constructable`.
- Build plan pictures (`cad/src/build_plan_media.py`): overview, 9 making sketches (CNR-DWG-101 to 109), 8 joint close-ups, 16 step pictures in `docs/05-build-plan/`.
- CNR-BLD-001 (`docs/05-build-plan.md`) and CNR-DEC-001 (`docs/06-design-decisions.md`).
- Appearance model `cad/src/product_model.py` (`product_parts()`, `TITLE`, `RENDER_VIEWS` hero, exploded and detail) and render scenes exported to `/home/claude/renders/canalrung` for the photoreal renders on Amish's Mac. `media/render-hero.png`, cards and the social preview do not exist yet; the README already leads with `media/render-hero.png`.
- CNR-PRC-001 v0.3, CNR-REQ-001 v0.3, README (TRL 3, build plan section and links), `project.yaml` (trl 3, trl_target 3, evidence).

### Results

| Quantity | Value |
| --- | --- |
| Reach | 4,020 mm rung section; water to 2.1 m on a 1.5:1 wall, 3.8 m on a vertical wall |
| Ladder as thrown | 4.48 kg (target 4.0 kg) |
| Buoyancy | 0.27 kg (plain) and 0.22 kg (stand-off) spare per rung; bottom three rungs carry the weight 1.73 times |
| Rung at 1.5 kN | 0.56 of yield |
| Ropes, wet, with knots | 22.4 kN (5.0 times 4.5 kN) |
| Anchor | Eye nut 1.53, post 0.39 of yield, footing 1.92 (drained soil); saturated soil needs the 500 x 1,200 mm footing |
| Deploy time | About 15 s (estimate) |
| Cost | Value-engineering target: USD 500. Estimated cost of the constructable design: USD 543.60 (USD 43.60 over the target) |

### Requirements not met

- **R2, mass:** 4.48 kg against 4.0 kg. Kept deliberately (stronger rungs, D3 and D10); savings to try are in CNR-DEC-001.
- **R9:** over the value-engineering target by USD 43.60 (accepted under the pre-approval; `budget_usd` unchanged at 500).
- Not verifiable at TRL 3: R2 throw accuracy, R5 climb time, R7 deploy time, R8 ageing (TRL 4 trials).

### Decisions made under the pre-approval

- CNR-DDR-002, P1 to P12: rope-through-rung joint (bush, knot under, seizing over); bolted stand-off blocks; foam sleeve lengths; end caps; eye nut with a crush tube through a 21.5 mm back-wall hole; box on a plate with two U-bolts; rope notch and drain holes; screw links (sized to pass round the eye's ring); edge protectors; footing 400 x 1,000 mm, 500 x 1,200 mm on wet banks; rope cut length 8.0 m.
- Appearance model: no deviations from `model.py`; context only (bank, lining, water, mannequin, hand). Decided under the pre-approval and listed in CNR-DEC-001.
- Open decisions: none. Eight facts to confirm when parts are bought are in CNR-DEC-001.

### Build plan findings: design changes made for construction (2026-10-03)

1. Rung to rope: 16 mm holes, flanged nylon bushes, overhand knot under, seizing over (the concept had no joint).
2. Stand-off blocks: HDPE, locked by an M5 bolt through block and rung.
3. Float sleeves: two lengths (294 and 260 mm) to fit between bushes or blocks; this sets the build order (foam, blocks, bushes).
4. End caps with a short insert that clears the rope hole.
5. Anchor: forged eye nut on an M16 bolt; crush tube so the post walls do not crush; the first model's crush tube could not be fitted through the 17.5 mm bolt hole, so the back-wall hole is 21.5 mm.
6. Box: plate and U-bolts, legs through the box back wall; no holes in the post.
7. Rope notch and drain holes so the lid closes over the anchored ropes.
8. Screw links: the first model link clashed with the eye nut ring; enlarged to pass round it (6 mm clear).
9. Edge protectors on the top lead.
10. Footing sized; larger footing for saturated banks.
11. BOM renumbered in build order; parts added for each change.

### Safety concerns

- Life-critical load path (rungs, knots, ropes, links, eye nut, post, footing): proof loads with CalRig and supervised tank trials are needed before anyone climbs; the build plan's safety stops say so.
- Footing on wet canal banks: the standard footing has a factor of only 0.85 in saturated soil; the site soil must be checked.
- Entanglement: rope in moving water can trap a person; no throw line, knife in the lid.
- Working at the canal edge during installation: second person, life jacket, services located.
- Throw weight: soft pouch, thrown upstream, never at the person.

### Checks

- `python .kit/render.py` and `python .kit/render.py --check`: see the final run; the only expected warning is the missing storefront (`media/render-hero.png`, cards).
- `python .kit/drawing.py --check-text` on all sheets and the concept blueprint: no overlaps.

### Recommended next step

- Photoreal renders, cards and the social preview on Amish's Mac from `/home/claude/renders/canalrung`.
- TRL 4 (outside the current phase cap): build the prototype to CNR-BLD-001 and proof-load the rungs, ropes and anchor with CalRig before any tank trial.

## 2026-10-03: photoreal renders

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.

## 2026-10-03: Amish's requirement decisions carried out

Amish chose option A on every requirement decision put to him on 2026-10-03: "1A 2A 3A 4A 5A 6A 7A 8A 9A 10A 11A". For CanalRung that is 4A (R2) and 9A (R6). Recorded in CNR-DDR-003 (`docs/decisions/0003-lighter-ropes-and-standard-footing.md`) and in the register CNR-DEC-001 v0.2.

### Changes made

- **4A, ropes (R2):** side ropes downsized from 10.5 mm EN 1891 type A to 9 mm EN 1891 type B (at least 18 kN declared, about 55 g/m); stronger rungs kept. Model `rope_d` 9.0 and knot 23 mm across; 26 new checks that the rope runs at least 1 mm clear of every bush bore. The ladder still exceeds 4.0 kg, so R2 is restated to 4.5 kg (Amish's fallback in 4A).
- **9A, footing (R6):** the 500 x 1,200 mm footing with a 2,300 mm post (1,100 mm in the concrete, bolt holes 1,350 mm from the bottom end) is the standard at every site; R6 restated for drained or saturated granular soil.
- Files: `cad/src/model.py` (271 of 271 checks pass; STEP and STL regenerated), `bom/bom.csv` (lines 1, 2 and 19 repriced; line 4's unquoted note fixed), CNR-CAL-001 v0.3 and `results.csv`, CNR-REQ-001 v0.4, CNR-PRC-001 v0.4, CNR-BLD-001 v0.2, CNR-DEC-001 v0.2, README, `project.yaml` (evidence).
- Pictures: general arrangement CNR-DWG-001 Rev P3; concept blueprint Rev P2, `media/hero.png`, `media/exploded.png`, `media/model.glb`; making sketches CNR-DWG-101 (post), 103 (footing) and 109 (rope); build plan overview, joints and steps regenerated (joint 1 and steps 1 and 2 show the new footing; rope pictures show the 9 mm rope).
- Appearance model `cad/src/product_model.py`: takes the new rope and footing from the model; exploded footing offset moved to suit the deeper footing. Render scenes re-exported to `/home/claude/renders/canalrung` (hero, exploded, detail). The photoreal renders on Amish's Mac need re-running to show the change.

### New results

| Requirement | Target | Before | After |
| --- | --- | --- | --- |
| R2, mass | At most 4.5 kg (restated from 4.0 kg) | 4.48 kg, not met | 4.27 kg, met on paper |
| R3, buoyancy | At least 0.15 kg per rung; weight factor at least 1.5 | 0.27 and 0.22 kg; 1.73 | 0.28 and 0.22 kg; 1.75 |
| R4, ropes | Wet with knots at least 4 times 4.5 kN (18 kN); Amish's floor 3 times | 22.4 kN, 5.0 times | 18.4 kN, 4.08 times |
| R6, footing | At least 1.5, drained or saturated soil | 1.92 drained, 0.85 saturated | 3.58 drained, 1.59 saturated |
| R9, cost | Reported against USD 500 | USD 543.60 | USD 605.20 |

Value-engineering target: USD 500. Estimated cost of the constructable design: USD 605.20 (USD 105.20 over the target). Footing +USD 65.00 (22 bags instead of 12 at USD 6.50), post +USD 4.60 (2.3 m pro rata), ropes save USD 8.00 (USD 2.00 a metre). Ladder as thrown 4.27 kg. `budget_usd` unchanged at 500.

### Decisions awaiting Amish

None. Nothing new needs Amish.

### Safety concerns

- The 9 mm rope meets the four-times rope factor of R4 only just (4.08). The bought rope must declare at least 18 kN, and the TRL 4 proof load must use wet, knotted rope.
- The standard footing is checked for granular soil only; soft clay or peat banks need a site pull test. About 550 kg of bagged concrete per footing is a manual handling load at the canal edge: use a second person or ready-mix.

## 2026-10-03: photoreal renders redone after Amish's requirement decisions

Rendered with Blender Cycles on Amish's Mac from `cad/src/product_model.py`; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` made with `.kit/cards.py`. Views: hero, exploded, detail. image_qc passes and `render.py --check` has no FAIL.
