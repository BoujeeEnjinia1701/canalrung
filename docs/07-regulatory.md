---
doc_id: CNR-REG-001
title: CanalRung regulatory and standards register
project: CanalRung
doc_type: Regulatory and standards register
version: "0.1"
status: Draft
date: '2026-11-05'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-11-05'
  author: Amish Chadha
  change: "First register (kit 1.9.1 upgrade); only sources named in CNR-PRB-001, CNR-CAL-001 and the BOM, plus two search listings; every classification and approval route is marked to assess"
---

# CanalRung regulatory and standards register

CanalRung is rescue and rope equipment, so product rules probably apply to a finished, sold station, but this register names no certification route as settled: nothing here is a classification, approval or legal opinion, and every row marked "to assess" needs a qualified reviewer before any product claim. The design is published as a research and educational prototype, never as certified life-saving equipment (CNR-PRS-001, PR-013). Method: STANDARDS section 23. Not legal advice.

Table 1. Regulatory and standards register.

| # | Standard or regulation | Jurisdiction | What it covers | Applicability to this design | Owner (role) | Status |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | EN 1891:1998, low stretch kernmantel ropes (type A and type B) | Europe, used worldwide | Construction, strength and testing of low-stretch ropes for rescue and work at height | The side ropes of option A are bought as 9 mm type B and sized on the catalogue 18 kN minimum; the rope must declare it. The standard was not read; the strengths are class values (CNR-CAL-001 E1) | Design lead | Applies to the bought rope; to confirm with the supplier datasheet |
| G2 | Rescue ladder type approval: AFS 2004:3 and EN 131 as cited for the Shore Safety ladder in CNR-PRB-001 | Sweden and Europe | Type approval of a marine rescue ladder; step and platform ladders | A competitor's route, for a rigid quay ladder. Whether any ladder or rescue standard applies to a thrown ladder on a canal bank is to assess | Regulatory reviewer | To assess |
| G3 | Classification of the station: personal protective equipment, life-saving appliance, machinery, or none | EU, US and other | Which regime a bystander rescue ladder or hand winch falls under | Not established. Option C's hand winch would raise machinery and lifting-equipment questions | Regulatory reviewer | To assess |
| G4 | Irrigation canal safety guidance (US Bureau of Reclamation and districts) | US | Canal safety practice, escape ladders and cables, signage, public information | Guidance, not a product rule; cited as prior art in CNR-PRB-001. A district permits a station on its bank | Co-design partner | Applies as guidance; permission to assess |
| G5 | Site and land rules: permission to place a post and footing on a canal bank; local building or excavation rules; call-before-you-dig rules | Per district and country | Right to place and dig; buried services | A 500 x 1,200 mm footing is dug at every site | Co-design partner | To assess |
| G6 | Liability and good Samaritan rules for a publicly placed rescue device | Per jurisdiction | Who is liable if the device fails or is misused | Not assessed; a published design does not remove the maker's duties | Legal reviewer | To assess |
| G7 | Marking and instructions: pictogram, warning, emergency number | Per jurisdiction | Safety signs and language | The lid and front decals (BOM line 11); the sign standard to follow is to assess | Design lead | To assess |
| G8 | CERN-OHL-S-2.0 hardware licence and MIT software licence | International | Terms for the open design files | The repository licence (`REUSE.toml`); no product claim | Maintainer | Applies |
| G9 | Galvanising, concrete and steel section standards (post, footing) | Per country | Material grades for the post and footing | The BOM asks for S235 or better and 25 MPa concrete; no standard number is cited here | Design lead | To assess |

Status: to assess, applies, does not apply, met by design, certification needed later.

## Sources

- EN 1891:1998 listing, checked 2026-11-05 (the standard was not read): [Genorma](https://genorma.com/en/standards/en-1891-1998).
- US Bureau of Reclamation, Canal Safety Challenge, found by search on 2026-11-05 and not read in full: [usbr.gov](https://www.usbr.gov/research/challenges/canalsafety.html).
- Shore Safety rescue ladder, type approved to AFS 2004:3 and EN 131, as cited in CNR-PRB-001: [shoresafety.se](https://shoresafety.se/en/products/components/rescue-ladder-type-approved/).
- US Bureau of Reclamation, canal escape ladders, as cited in CNR-PRB-001 (see its prior work table).
