---
doc_id: CNR-MKT-001
title: CanalRung market and viability
project: CanalRung
doc_type: Market and viability
version: "0.1"
status: Draft
date: '2026-11-05'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-11-05'
  author: Amish Chadha
  change: "First market and viability note (kit 1.9.1 upgrade). No price could be re-checked on 2026-11-05 (vendor pages were not reachable from the working environment); prices are those cited in CNR-PRB-001 and the BOM, with their original dates"
---

# CanalRung market and viability

Irrigation districts, farms and canal-side villages would buy or build a throwable canal ladder station if it costs well under what a district spends on a fixed escape ladder, which is not known; the open design matters because a village workshop can build and mend it. No price in this note was re-checked on 2026-11-05: the competitor prices come from CNR-PRB-001 (checked in the TRL 2 session of 2026-10-03) and the CanalRung cost from the BOM; anything not cited is marked "to assess". Method: STANDARDS section 23.

> **Safety:** CanalRung is a research and educational design, never certified life-saving equipment. Nothing here is a sales claim.

Table 1. Market segments.

| Segment | Target users and region | Competitive benchmark (cited price) | Estimated cost per unit (USD) | Value proposition |
| --- | --- | --- | --- | --- |
| Irrigation districts and water authorities | Western United States and similar lined-canal systems | Fixed canal escape ladders set into the lining at intervals (US Bureau of Reclamation, cited in CNR-PRB-001); price to assess | 605.20 for option A parts (BOM, indicative prices, unverified), no labour | A station that is placed in a day at a crossing or pump house, not cast into the lining; throwable to a person who has drifted past a fixed ladder |
| Farms, pump houses and orchard canals | Private banks with a steep concrete lining | Rescue throw bag, about USD 24 (Airhead, CNR-PRB-001, checked 2026-10-03): a rope only, no way to climb | 605.20 as above | A way to climb out, not only a line to be pulled in |
| Village committees, schools and NGOs | Canal-side villages in South Asia and elsewhere | Rapid Rung swim ladder from USD 150 (CNR-PRB-001, checked 2026-10-03): made for boats; Shore Safety rescue ladder: price to assess | To assess for a local build with local labour and stock | An open design and a build plan a workshop can follow, with parts bought locally |

## Open route

A fencing or metal workshop, or a water-district shop, cuts the post, rungs and box plate from the drawings and the build plan, buys the rope, eye nut and foam as marked catalogue parts, and sets the post. Water-safety councils, irrigation districts and NGOs carry the design between canals, and CERN-OHL-S-2.0 keeps changes open. The station is not an attractive theft target in itself (about 20 kg of steel post and box, 4 kg of ladder), but aluminium and rope have scrap value: no lock is fitted so the box opens in an emergency, and a tamper tag shows interference (CNR-DDR-001 D11). Viability depends on the cost coming down toward USD 500, a co-design partner confirming the need, and trials showing that people can use it; none is yet shown.

## Sources

- CNR-PRB-001 prior work table: Airhead rescue throw bag, [airhead.com](https://www.airhead.com/products/rescue-throw-bag), about USD 24 (checked in the 2026-10-03 session, not re-checked 2026-11-05); Rapid Rung, [rapidrung.com](https://www.rapidrung.com/), from USD 150 (same); Shore Safety rescue ladder, [shoresafety.se](https://shoresafety.se/en/products/components/rescue-ladder-type-approved/), price not stated.
- US Bureau of Reclamation canal safety, found by search 2026-11-05: [usbr.gov](https://www.usbr.gov/research/challenges/canalsafety.html); fixed ladder cost not found.
- `bom/bom.csv`: every price is an indicative estimate with its basis in the notes column; none was checked against a supplier on 2026-11-05.
