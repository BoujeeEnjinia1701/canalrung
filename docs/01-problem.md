---
doc_id: CNR-PRB-001
title: CanalRung problem statement
project: CanalRung
doc_type: Problem statement
version: "0.2"
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
  change: "TRL 2 and 3: design envelope stated; open questions answered under Amish's 2026-10-03 pre-approval (CNR-DDR-001); first co-design candidate named; safety section added"
---

# CanalRung problem statement

A person in a lined canal often cannot climb out, and the bystander on the bank has nothing to give them except their own body.

## The problem

Canals are built to move water, not to let people out. The Kittitas Reclamation District notes steep, sometimes vertical banks of smooth concrete and water that is deceptively fast ([KRD](https://www.kittitasreclamationdistrict.org/safety)). The Water Safety Council of Fresno County lists steep slopes and slippery walls, swift currents and turbulence, and cold water of about 13 °C (55 °F) that stiffens muscles ([Water Safety Council of Fresno County](https://www.watersafe.org/canals)). Would-be rescuers who go in after someone can drown too ([Washington L&I FACE, 2002](https://stacks.cdc.gov/view/cdc/228712/cdc_228712_DS1.pdf)).

Fixed aids exist but are spaced out. The Bureau of Reclamation installed escape ladders on concrete-lined canals at 750 ft (229 m) intervals, with cables and droplines upstream of hazardous structures ([USBR REC-ERC-71-36](https://www.usbr.gov/tsc/techreferences/hydraulics_lab/pubs/REC/REC-ERC-71-36.pdf)), and districts fit escape cleats and ropes at siphons ([KRD](https://www.kittitasreclamationdistrict.org/safety)). A person swept by the current may never reach one. Throw bags cost about $24 USD ([Airhead](https://www.airhead.com/products/rescue-throw-bag)) but need a strong pull from the bank. Portable rescue ladders such as Shore Safety's type-approved aluminium ladder hang from a quay edge ([Shore Safety](https://shoresafety.se/en/products/components/rescue-ladder-type-approved/)) and boat swim ladders like Rapid Rung mount on a hull ([Rapid Rung](https://www.rapidrung.com/)). None is a low-cost ladder that a bystander throws down a canal wall to wherever the person is.

## Users and context

| User | Need | Context |
| --- | --- | --- |
| Bystander on the bank | Something they can throw and anchor quickly without going into the water | A child, farm worker or passer-by has just fallen in |
| Person in the water | Something to grab and a way to climb a steep, slick wall | Cold, fast water with lined sides |
| Irrigation district and farm managers | A cheap, durable station they can place at many points along a canal | Pump houses, crossings, orchards and paths |
| Village committees and schools | A kit they can build, place and teach children to use | Canal-side villages in South Asia and elsewhere |

## Operating environment

- Lined canals with side slopes from about 1.5:1 (horizontal to vertical) to vertical and heights to about 3 m (10 ft) from bank to water (estimate). The first version covers water up to 2.0 m below the coping on a 1.5:1 slope and up to 3.0 m on a vertical wall (CNR-REQ-001, design envelope).
- Flow of up to about 2 m/s (6.5 ft/s) at the surface (estimate, to be checked with a district).
- Water from about 5 to 30 °C (41 to 86 °F); algae, silt and debris on the walls.
- Stored outdoors in a post box or on a hook for years; sun, dust and rain.

## Constraints

- Value-engineering target of USD 500 in parts, including a bank-side storage post (a hypothetical control target, not a spending limit).
- Throwable by one adult from the bank; total mass at or below 4 kg (target).
- Built from rope, plastic or aluminium rungs and hand tools; hardware under CERN-OHL-S-2.0.
- No elastic self-stowing mechanism (see design-arounds).
- Published as an open engineering reference, not as certified rescue or life-saving equipment.

## Out of scope

- Fixed canal escape ladders, cleats or fencing (district civil works).
- Powered or inflatable devices.
- Swiftwater rescue by trained teams entering the water.
- Certification to any life-saving or ladder standard at this TRL.

## Prior work

| Prior work | What it does | Gap for these users | Source |
| --- | --- | --- | --- |
| Fixed canal escape ladders (US Bureau of Reclamation) | Ladders set into concrete-lined canals at 750 ft intervals, plus cables and droplines upstream of structures | Fixed and spaced out; a person carried by the current may not reach one | [link](https://www.usbr.gov/tsc/techreferences/hydraulics_lab/pubs/REC/REC-ERC-71-36.pdf) |
| Shore Safety rescue ladder | Floating aluminium ladder of 3 or 4 m, 7 to 9 kg, hooked on a quay edge, type approved to AFS 2004:3 and EN 131 | Rigid and heavy; made for quays, not for throwing down a sloped canal wall | [link](https://shoresafety.se/en/products/components/rescue-ladder-type-approved/) |
| Rapid Rung swim ladder | Patented self-stowing strap-on swim ladder for boats, from $150 USD | Mounted on a hull, not thrown from a bank | [link](https://www.rapidrung.com/) |
| US3411166A inflatable boarding ladder and paddle | Buoyant ladder that hooks on a gunwale and doubles as a flotation aid (expired) | Boat boarding aid; needs inflation and a gunwale | [link](https://patents.google.com/patent/US3411166) |
| US4989691A inflatable boarding ladder and rescue device | Inflatable ladder with a ballasted lower end that sinks to form a step (lapsed 1995) | Boat-mounted and inflated; not thrown from land | [link](https://patents.google.com/patent/US4989691A/en) |
| Rescue throw bag | Throw line of about 15 m (50 ft) in a bag, about $24 USD | Needs a strong bystander to pull the person up a steep wall | [link](https://www.airhead.com/products/rescue-throw-bag) |

## Co-design

An irrigation district or canal authority with a safety programme, working with a local water-safety council or life-saving society, to define bank heights, flows and placement, and to run trials on a drained or low-flow canal reach. The first candidate to approach is the Kittitas Reclamation District in Washington State, whose canal safety page is cited above, with the Water Safety Council of Fresno County as the first candidate water-safety partner. Neither has been contacted; both are candidates, not partners (CNR-DDR-001, D13).

## Safety

> **Safety:** Canal rescue kills would-be rescuers. CanalRung exists so that the bystander stays on the bank: throw, anchor and call the emergency number; never enter the water. The ladder is rope equipment that a person's life depends on, and rope in moving water can trap a person or a limb, so a blunt-tip rescue knife is kept at the station. CanalRung is a research prototype published as an open engineering reference, not certified life-saving equipment, and it is not a flotation device.

## Questions answered at TRL 2 and TRL 3

All were decided on 2026-10-03 under Amish's pre-approval; the reasons are in CNR-DDR-001.

- **Bank heights, slopes and flows for the first version:** water up to 2.0 m below the coping on a 1.5:1 slope or 3.0 m on a vertical wall; currents to 2.0 m/s (D1). A partner district's data will confirm or change this.
- **Weighted to sink or floating:** both. A soft 0.5 kg weight hangs 280 mm below the bottom rung and the rungs float; the bottom three rungs carry the weight with a factor of 1.73 (D6).
- **Load standard:** rope to EN 1891 type A; rung and anchor targets as set in CNR-REQ-001 (R4, R6), to be proof-loaded with CalRig at TRL 4; no certification is claimed (D9).
- **Theft:** no lock, because a lock defeats the station; a numbered tamper tag on the latch shows when the box has been opened, and the partner district inspects on a set schedule (D11).
- **Fresno County figure of 35 canal drownings from 2005 to 2020:** not confirmed from a primary source, so it is not used in this repository.
