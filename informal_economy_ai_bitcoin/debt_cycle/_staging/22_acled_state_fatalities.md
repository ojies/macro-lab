# ACLED Political-Violence Fatalities by Nigerian State — 2024 & 2025

**Analyst pull date (access date): 2026-07-03**
**Source vintage:** ACLED file "as-of 01 July 2026" (data current through June 2026).

## Method & source (READ THIS FIRST)

- **Primary source:** ACLED curated dataset on HDX — *"Nigeria - Conflict Events"*, resource
  `nigeria_HRP_political_violence_events_and_fatalities_by_month-year_as-of-01jul2026.xlsx`.
  This is an official ACLED file (ACLED is the HDX publisher), disaggregated to
  **Admin1 (state) × Admin2 (LGA) × Month × Year**, columns: Country, Admin1, Admin2, ISO3,
  Admin2 Pcode, Admin1 Pcode, Month, Year, Events, Fatalities. 273,289 data rows, 1997–Jun 2026.
- **What I did:** downloaded the XLSX via the HDX CKAN API and summed `Fatalities` by `Admin1`
  for `Year == 2024` and `Year == 2025`. This is a direct aggregation of official ACLED
  event data — NOT an estimate.
- **Event scope:** ACLED "political violence" = battles + violence against civilians +
  explosions/remote violence + the mob-violence sub-type of riots. (Protests/peaceful
  demonstrations are excluded — this is the same universe ACLED uses for its Conflict Index.)
- **Date window:** **calendar year, Jan–Dec.** Both 2024 (12/12 months) and 2025 (12/12 months)
  are COMPLETE in this vintage. (2026 only runs Jan–Jun, so no 2026 column.)
- **Coverage: all 37 admin1 units present and matched (36 states + FCT). 37/37 [SOURCED].**

### Direct download URL (HDX / ACLED)
```
https://data.humdata.org/dataset/a58fc2b9-3079-47f9-9755-47e7a1f77d19/resource/425bbb8f-5ca8-426b-bbb5-083eb59474ea/download/nigeria_hrp_political_violence_events_and_fatalities_by_month-year_as-of-01jul2026.xlsx
```
Dataset landing page: https://data.humdata.org/dataset/nigeria-acled-conflict-data
CKAN API: `https://data.humdata.org/api/3/action/package_show?id=nigeria-acled-conflict-data`

---

## CSV-ready table

```csv
state,acled_fatalities_2024,acled_fatalities_2025,source,flag
Abia,83,88,ACLED via HDX (as-of 01jul2026),[SOURCED]
Adamawa,43,151,ACLED via HDX (as-of 01jul2026),[SOURCED]
Akwa Ibom,52,16,ACLED via HDX (as-of 01jul2026),[SOURCED]
Anambra,184,158,ACLED via HDX (as-of 01jul2026),[SOURCED]
Bauchi,35,60,ACLED via HDX (as-of 01jul2026),[SOURCED]
Bayelsa,19,27,ACLED via HDX (as-of 01jul2026),[SOURCED]
Benue,661,895,ACLED via HDX (as-of 01jul2026),[SOURCED]
Borno,2203,3863,ACLED via HDX (as-of 01jul2026),[SOURCED]
Cross River,32,34,ACLED via HDX (as-of 01jul2026),[SOURCED]
Delta,149,115,ACLED via HDX (as-of 01jul2026),[SOURCED]
Ebonyi,78,60,ACLED via HDX (as-of 01jul2026),[SOURCED]
Edo,125,114,ACLED via HDX (as-of 01jul2026),[SOURCED]
Ekiti,16,2,ACLED via HDX (as-of 01jul2026),[SOURCED]
Enugu,88,62,ACLED via HDX (as-of 01jul2026),[SOURCED]
FCT,129,62,ACLED via HDX (as-of 01jul2026),[SOURCED]
Gombe,6,16,ACLED via HDX (as-of 01jul2026),[SOURCED]
Imo,162,142,ACLED via HDX (as-of 01jul2026),[SOURCED]
Jigawa,14,34,ACLED via HDX (as-of 01jul2026),[SOURCED]
Kaduna,819,325,ACLED via HDX (as-of 01jul2026),[SOURCED]
Kano,4,90,ACLED via HDX (as-of 01jul2026),[SOURCED]
Katsina,1319,1435,ACLED via HDX (as-of 01jul2026),[SOURCED]
Kebbi,48,256,ACLED via HDX (as-of 01jul2026),[SOURCED]
Kogi,64,154,ACLED via HDX (as-of 01jul2026),[SOURCED]
Kwara,22,251,ACLED via HDX (as-of 01jul2026),[SOURCED]
Lagos,107,103,ACLED via HDX (as-of 01jul2026),[SOURCED]
Nasarawa,118,89,ACLED via HDX (as-of 01jul2026),[SOURCED]
Niger,554,628,ACLED via HDX (as-of 01jul2026),[SOURCED]
Ogun,95,37,ACLED via HDX (as-of 01jul2026),[SOURCED]
Ondo,17,64,ACLED via HDX (as-of 01jul2026),[SOURCED]
Osun,24,33,ACLED via HDX (as-of 01jul2026),[SOURCED]
Oyo,46,20,ACLED via HDX (as-of 01jul2026),[SOURCED]
Plateau,477,574,ACLED via HDX (as-of 01jul2026),[SOURCED]
Rivers,64,60,ACLED via HDX (as-of 01jul2026),[SOURCED]
Sokoto,336,585,ACLED via HDX (as-of 01jul2026),[SOURCED]
Taraba,130,145,ACLED via HDX (as-of 01jul2026),[SOURCED]
Yobe,144,149,ACLED via HDX (as-of 01jul2026),[SOURCED]
Zamfara,1429,1984,ACLED via HDX (as-of 01jul2026),[SOURCED]
```

**National totals (sum of 37 units):** 2024 = **9,896**; 2025 = **12,881** fatalities.
Name mapping applied: ACLED "Federal Capital Territory" -> `FCT`; ACLED "Nassarawa" -> `Nasarawa`.
All other 35 names matched the panel exactly.

---

## Anchor reconciliation (IMPORTANT — vintage/window caveat)

The task's anchors come from ACLED's **2024 Conflict Index infographic (published 06 Dec 2024)**,
whose window is **1 Dec 2023 – 29 Nov 2024** (a rolling 12-month index, NOT calendar 2024).
My primary column above is **calendar Jan–Dec 2024** from the **01 Jul 2026 vintage**.

Two things move the numbers relative to the anchors: (1) different date window, and
(2) ~19 months of ACLED's continuous back-revisions since the Dec-2024 snapshot.

| State   | Anchor (Conflict Index, Dec'23–Nov'24, as published Dec-2024) | My reconstruction of SAME window (Dec'23–Nov'24) from 01Jul2026 vintage | My primary: calendar 2024 (Jan–Dec, 01Jul2026 vintage) |
|---------|------:|------:|------:|
| Borno   | 2,143 | 2,157 | 2,203 |
| Zamfara | 1,347 | 1,332 | 1,429 |
| Katsina | 1,306 | 1,262 | 1,319 |
| Kaduna  |   813 |   957 |   819 |

**Verdict on anchors:** APPROXIMATE MATCH, series confirmed identical (ACLED political violence),
but NOT bit-exact. Reconstructing ACLED's exact Dec'23–Nov'24 window from the current vintage
lands within ~1–3% for Borno/Zamfara/Katsina; Kaduna diverges more (957 vs 813, +18%), which is
attributable to ACLED revising Kaduna upward after the Dec-2024 publication. The residual gaps are
**data-vintage revisions**, not a source mismatch. If you need the panel to reproduce the published
Dec-2024 anchors exactly, you would need ACLED's December-2024 data snapshot (not retrievable via
web now; ACLED overwrites the HDX file weekly). Recommendation: use the calendar-2024 column above
and cite the 01 Jul 2026 vintage + access date, since it is internally consistent for 2024 AND 2025.

---

## Notes, caveats, flags

- **Flag = [SOURCED] for all 37 rows.** Every value is a direct sum of official ACLED
  event-level fatalities (via the HDX curated file), not an estimate or a secondary citation.
- **Window is explicit:** columns are calendar-year totals (Jan–Dec 2024; Jan–Dec 2025), both
  complete. This differs from ACLED's 12-month "Conflict Index" window — see reconciliation above.
- **ACLED revises continuously.** Any re-pull on a later date will differ slightly, especially for
  recent months of 2025. Always re-state the "as-of" vintage and access date. This pull: vintage
  as-of 01 Jul 2026, accessed 03 Jul 2026.
- **Definition:** political violence only (battles, violence against civilians, explosions/remote
  violence, mob violence). Excludes peaceful protests. This is the correct universe for a
  conflict-intensity / fragility indicator.
- **2025 note:** Borno (3,863) and Zamfara (1,984) rose sharply vs 2024; Benue (895) and
  Plateau (574) also elevated. Kaduna FELL (819 -> 325). These are consistent with 2025 ACLED
  Nigeria reporting (JAS/ISWAP resurgence in the North East; farmer-herder violence in the
  Middle Belt). Numbers are exact from the file, not estimated.
- **Cross-checks not needed for the core table** (we have the primary ACLED source at admin1),
  but for triangulation: Nigeria Security Tracker (CFR) and Nigeria Watch use different
  inclusion rules and typically report LOWER totals than ACLED; do not expect them to match.

## Source URLs
- HDX dataset (Nigeria - Conflict Events, ACLED): https://data.humdata.org/dataset/nigeria-acled-conflict-data
- Direct XLSX (political violence, by month-year, admin1/admin2): see "Direct download URL" above.
- ACLED Nigeria country page: https://acleddata.com/country/nigeria
- ACLED Nigeria 2024 Conflict Index (source of anchors, window Dec'23–Nov'24): https://acleddata.com/2024/12/06/nigeria-2024-conflict-index-infographic/
- ACLED Data Export Tool (event-level, requires free registration): https://acleddata.com/conflict-data/data-export-tool
