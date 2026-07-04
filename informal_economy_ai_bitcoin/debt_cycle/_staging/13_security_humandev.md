# Nigeria — Security & Human-Development Indicators (2015–2026)

**Dataset:** Big-Debt-Cycle / Nigeria
**Compiled:** 2026-06-30
**Role in model:** Security/conflict feeds the **Political Stability** governance gauge; human-development indicators contextualise social stress and state capacity.
**Coverage:** Annual (calendar year or report vintage), 2015–2026 where sourceable.
**Source priority:** ACLED, UNDP HDR, World Bank (WDI), UNHCR / IOM DTM / IDMC, UNICEF / UNESCO UIS, IEP Global Terrorism Index.

**Flag legend:** `[SOURCED]` = taken directly from a cited primary source for the stated period · `[PROVISIONAL]` = sourced but period/precision/vintage uncertain, or partial-year / projection · `[ESTIMATED]` = derived/computed (method noted) · blank = not reliably sourceable, left blank rather than guessed.

---

## CRITICAL METHODOLOGY NOTES (read first)

**1. "Fatalities" are not one number.** Three different conflict-death series circulate for Nigeria and must NOT be conflated:
- **ACLED political-violence fatalities** (battles + violence against civilians + explosions/remote violence + mob violence; excludes protests) — the broadest, thousands/yr.
- **GTI "terrorism" deaths** (IEP; non-state terrorism only) — far lower (hundreds/yr).
- **IOM/IDMC displacement counts** — people moved, not killed.
This file keeps them in separate tables. ACLED revises history continuously; figures below are the **25 Jun 2026 vintage, accessed 30 Jun 2026**.

**2. GTI report edition ≠ data year.** Each Global Terrorism Index edition reports the **prior** calendar year. **No GTI edition exists for data-year 2020** (IEP published GTI 2020 covering 2019, then skipped to GTI 2022 covering 2021). Table B is indexed by both edition and data year.

**3. HDI vintages & base revisions.** UNDP HDRs publish with a ~2-year lag and **re-base the whole back-series each edition**, so the same year carries different values across reports. Example: 2022 HDI = **0.548** in HDR 2023/24 (2022 reference year) but **0.557** in the HDR 2025 back-series. Use one vintage internally; do not mix. Rank denominators: 193 countries (HDR 2023/24 and HDR 2025).

**4. IDP scope mismatch.** IOM **DTM** historically tracked the **North-East (BAY: Borno, Adamawa, Yobe)** only, later adding North-Central/North-West rounds — so DTM ≠ national. **IDMC GRID** reports a national stock (conflict + disaster). UNHCR cites a ~3.5m national IDP figure. These cover different geographies; the table flags scope.

**5. Under-5 mortality vintage.** The World Bank WDI `SH.DYN.MORT` values below (≈116–118) are the vintage live on the WB API at access date; the **UN IGME 2024/2025 estimation round** revises Nigeria's U5MR notably lower (~107–110 for recent years). Treat the level as vintage-sensitive; the *direction* (slow decline, still among the world's highest) is robust.

---

## A. CONFLICT / POLITICAL VIOLENCE — ACLED (calendar year)

Source: **ACLED**, "Nigeria – Conflict Events" file on HDX (`…political_violence_events_and_fatalities_by_month-year_as-of-25jun2026.xlsx`), coverage 1 Jan 1997–19 Jun 2026, accessed 30 Jun 2026. Political-violence only (excludes peaceful protests).

| Year | Events | Reported fatalities | Period | Flag |
|---|---:|---:|---|---|
| 2015 | 952 | 11,075 | Jan–Dec | [SOURCED] |
| 2016 | 786 | 4,826 | Jan–Dec | [SOURCED] |
| 2017 | 951 | 4,912 | Jan–Dec | [SOURCED] |
| 2018 | 1,400 | 6,087 | Jan–Dec | [SOURCED] |
| 2019 | 1,634 | 5,925 | Jan–Dec | [SOURCED] |
| 2020 | 2,854 | 8,420 | Jan–Dec | [SOURCED] |
| 2021 | 3,526 | 10,943 | Jan–Dec | [SOURCED] |
| 2022 | 3,730 | 10,929 | Jan–Dec | [SOURCED] |
| 2023 | 3,546 | 8,688 | Jan–Dec | [SOURCED] |
| 2024 | 4,400 | 9,896 | Jan–Dec | [SOURCED] |
| 2025 | 5,515 | 12,883 | Jan–Dec (complete) | [SOURCED] |
| 2026 | 3,404 | 8,175 | **1 Jan–19 Jun 2026 (partial)** | [PROVISIONAL] |

### A.2 Reported fatalities by main driver / region (same ACLED file)

| Year | NE Boko Haram/ISWAP | NW banditry/kidnap | Middle-Belt farmer-herder | SE IPOB/separatist | S-South/Delta |
|---|---:|---:|---:|---:|---:|
| 2015 | 8,803 | 697 | 981 | 41 | 155 |
| 2016 | 2,850 | 309 | 819 | 208 | 362 |
| 2017 | 3,183 | 207 | 478 | 319 | 538 |
| 2018 | 2,589 | 1,034 | 1,622 | 160 | 287 |
| 2019 | 2,510 | 2,108 | 534 | 138 | 405 |
| 2020 | 3,651 | 3,141 | 615 | 143 | 455 |
| 2021 | 3,336 | 4,507 | 1,216 | 763 | 529 |
| 2022 | 3,015 | 5,010 | 1,162 | 797 | 429 |
| 2023 | 3,036 | 2,888 | 1,323 | 490 | 395 |
| 2024 | 2,390 | 4,505 | 1,354 | 595 | 441 |
| 2025 | 4,163 | 5,213 | 2,021 | 510 | 366 |
| 2026* | 3,472 | 3,143 | 1,034 | 73 | 135 |

\*2026 partial to 19 Jun. **Narrative:** 2015 = Boko Haram peak (NE ≈ 79% of all deaths). 2016–17 NE decline after offensive. 2018–19 diversification (Middle-Belt farmer-herder + rising NW banditry). **2020–22 NW banditry (Zamfara epicentre) overtakes the NE** as deadliest driver; mass school abductions; SE IPOB/ESN unrest peaks. 2023 election-year dip. 2024 NW resurgence (ACLED rates Nigeria "extreme"). 2025 deadliest since 2015 (NE + NW + record Middle-Belt). 2026 NE Boko Haram/ISWAP re-escalation flagged. Oil/Niger-Delta militancy is a minor fatality contributor (~150–540/yr); its impact is economic/infrastructural. [SOURCED]

---

## B. GLOBAL TERRORISM INDEX — IEP (rank + score; terrorism deaths only)

Publisher: **Institute for Economics & Peace**. Each edition reports the prior calendar year; rank/score read directly from the official report-PDF results tables (accessed 30 Jun 2026). 163 countries assessed from the 2016 edition onward (162 in 2015).

| Edition | Data year | Rank | Of N | Score | Flag |
|---|---|---:|---:|---:|---|
| GTI 2015 | 2014 | 3 | 162 | 9.213 | [SOURCED] |
| GTI 2016 | 2015 | 3 | 163 | 9.314 | [SOURCED] |
| GTI 2017 | 2016 | 3 | 163 | 9.009 | [SOURCED] |
| GTI 2018 | 2017 | 3 | 163 | 8.660 | [SOURCED] |
| GTI 2019 | 2018 | 3 | 163 | 8.597 | [SOURCED] |
| GTI 2020 | 2019 | 3 | 163 | 8.314 | [SOURCED] |
| *(none)* | 2020 | — | — | — | no edition published |
| GTI 2022 | 2021 | 6 | 163 | 8.233 | [SOURCED] |
| GTI 2023 | 2022 | 8 | 163 | 8.065 | [SOURCED] |
| GTI 2024 | 2023 | 8 | 163 | 7.575 | [SOURCED] |
| GTI 2025 | 2024 | 6 | 163 | 7.658 | [SOURCED] |
| GTI 2026 | 2025 | 4 | 163 | 7.792 | [SOURCED] |

**Terrorism-death context (IEP):** 2014 ≈ 7,512 → 2022 ≈ 392 (lowest since 2011) → 2023 ≈ 533 (+34%) → 2024 ≈ 565 (+6%) → 2025 ≈ 750 (+46%, largest absolute global rise). Nigeria was **3rd most impacted for six straight editions (2014–2019 data)**, improving to 6th–8th as the Sahel (Burkina Faso, Mali, Niger) and Pakistan worsened, then climbing back to 4th (2025 data). [SOURCED]

---

## C. FORCED DISPLACEMENT — IDPs & REFUGEES

### C.1 New conflict displacements per year (IDMC, via World Bank `VC.IDP.NWCV`)
Internal displacements *newly triggered by conflict/violence* in the year (flows, not stock). Accessed 30 Jun 2026.

| Year | New conflict displacements | Flag |
|---|---:|---|
| 2015 | 737,000 | [SOURCED] |
| 2016 | 501,000 | [SOURCED] |
| 2017 | 279,000 | [SOURCED] |
| 2018 | 541,000 | [SOURCED] |
| 2019 | 248,000 | [SOURCED] |
| 2020 | 169,000 | [SOURCED] |
| 2021 | 376,000 | [SOURCED] |
| 2022 | 148,000 | [SOURCED] |
| 2023 | 291,000 | [SOURCED] |
| 2024 | — | (WB vintage shows no value yet) |

IDMC also reports large **disaster** displacement flows (e.g. ~2.4m in 2022 from floods; ~166,000 in 2023). [SOURCED — IDMC GRID 2023/2024]

### C.2 IDP stock (year-end) — note scope differences

| As of | IDP stock | Scope / source | Flag |
|---|---:|---|---|
| End-2020 | ~2.7 million | National (IDMC GRID) | [PROVISIONAL] |
| Jul 2022 (DTM R42) | 2,455,190 | NE BAY states (IOM DTM) | [SOURCED] |
| Feb 2023 (DTM R43) | 2,375,661 | NE BAY states (IOM DTM) | [SOURCED] |
| Dec 2023 (DTM R46) | 2,305,335 | NE BAY states (IOM DTM) | [SOURCED] |
| End-2023 | ~3.4 million | National, conflict+disaster (IDMC GRID 2024) | [PROVISIONAL] |
| 2024 (DTM R47) | 2,271,987 | NE BAY states (IOM DTM) | [SOURCED] |
| 2024 (DTM R48) | 2,255,595 | NE BAY states (IOM DTM) | [SOURCED] |
| Nov 2024 (DTM NC/NW) | 1,322,766 | 10 NC/NW states (Benue, Kaduna, Kano, Katsina, Kogi, Nasarawa, Niger, Plateau, Sokoto, Zamfara) | [SOURCED] |
| End-2024 | ~3.5 million | National (UNHCR Global Trends / ARR 2024) | [SOURCED] |

*DTM (NE-only or NC/NW-only) and the national IDMC/UNHCR totals are NOT additive across rows and use different methodologies.*

### C.3 Refugees

| As of | Figure | Description | Flag |
|---|---:|---|---|
| End-2024 | ~127,000 | Refugees & asylum-seekers **hosted in** Nigeria (from 41 countries; mostly Cameroonians, ~71,000 registered in S-South, 64% in Cross River); 81% in host communities | [SOURCED — UNHCR] |
| End-2023 | (share in host communities 77%) | — | [SOURCED — UNHCR] |
| 2024 | ~400,000 | Nigerian refugees **in neighbouring countries** (Niger, Cameroon, Chad) | [SOURCED — UNHCR] |

Per-year UNHCR origin/asylum time-series (2015–2022) not cleanly retrievable from the public API at access date — left blank rather than guessed.

---

## D. HUMAN DEVELOPMENT INDEX — UNDP (note vintages)

| Vintage | Reference year | HDI value | Rank | Of N | Flag |
|---|---|---:|---:|---:|---|
| HDR 2023/24 ("Breaking the Gridlock") | 2022 | 0.548 | 161 | 193 | [SOURCED] |
| HDR 2025 | 2023 | 0.560 | 164 | 193 | [SOURCED] |

**HDR 2025 back-series (revised base; values only, no contemporaneous rank):** 2000 = 0.379 · 2005 = 0.435 · 2010 = 0.502 · 2015 = 0.530 · 2020 = 0.547 · 2021 = 0.554 · 2022 = **0.557** · 2023 = 0.560. [SOURCED] — note the 2022 value (0.557) differs from the HDR 2023/24 print (0.548) due to base revision (see Methodology Note 3).

**HDI components (2023, HDR 2025):** life expectancy 54.5 yrs · expected years schooling 10.5 · mean years schooling 7.6 · GNI per capita ~$5,569 (2021 PPP). Classification: **Low human development**. Inequality-adjusted HDI loss ≈ **32.7%**. [SOURCED]

---

## E. HEALTH — LIFE EXPECTANCY & UNDER-5 MORTALITY (World Bank WDI)

Accessed 30 Jun 2026. Life expectancy `SP.DYN.LE00.IN`; under-5 mortality `SH.DYN.MORT` (UN IGME-sourced — see vintage Note 5).

| Year | Life expectancy at birth (yrs) | Under-5 mortality (per 1,000) | Flag |
|---|---:|---:|---|
| 2015 | 51.94 | 117.8 | [SOURCED] |
| 2016 | 52.19 | 117.4 | [SOURCED] |
| 2017 | 52.40 | 117.2 | [SOURCED] |
| 2018 | 52.67 | 117.2 | [SOURCED] |
| 2019 | 53.01 | 117.4 | [SOURCED] |
| 2020 | 53.07 | 117.4 | [SOURCED] |
| 2021 | 53.46 | 117.6 | [SOURCED] |
| 2022 | 54.08 | 117.5 | [SOURCED] |
| 2023 | 54.46 | 116.8 | [SOURCED] |
| 2024 | 54.64 | 115.6 | [SOURCED] |

Life expectancy shows muted COVID-era stall (2019→2020 essentially flat) then resumed rise. U5MR is among the highest globally and declines only slowly in this WB vintage; the latest UN IGME round revises levels lower (~107–110) — direction unchanged.

---

## F. EDUCATION — OUT-OF-SCHOOL, COMPLETION, LITERACY

### F.1 Out-of-school children (definitions genuinely differ — not errors)

| Figure | Definition / age band | Source & vintage | Flag |
|---|---|---|---|
| ~10.5 million | Children 5–14 not in school (long-standing UNICEF Nigeria headline) | UNICEF Nigeria (standing, ~2017–present) | [SOURCED] |
| 10.2 million | **Primary**-age out of school | UNICEF, 2024 | [SOURCED] |
| 8.1 million | **Junior-secondary**-age out of school | UNICEF, 2024 | [SOURCED] |
| **18.3 million** | Primary + junior-secondary combined | UNICEF, May 2024 | [SOURCED] |
| ~20.2 million | Children **and youth** out of school (new UIS/GEM cross-referenced method) | UNESCO UIS/GEM, 2021 data, pub. 2022 | [SOURCED] |

Girls ≈ 60% of out-of-school children (UNICEF). World Bank carries **no** annual out-of-school series for Nigeria (`SE.PRM.UNER` NULL 2015–2022).

### F.2 Primary completion & adult literacy (World Bank WDI)

| Indicator | Value | Year | Flag |
|---|---:|---|---|
| Primary completion rate (`SE.PRM.CMPT.ZS`) | 70.16% | **2010** (only WB value; NULL 2011–2025) | [SOURCED] |
| Adult literacy (15+, `SE.ADT.LITR.ZS`) | 58.22% | 2016 | [SOURCED] |
| Adult literacy | 63.16% | 2021 | [SOURCED] |
| Adult literacy | 70.41% | 2024 | [SOURCED] |

Literacy is published only in survey years (2016/2021/2024 from MICS/NLSS via UIS) — rising trend, no annual interpolation. Primary completion is effectively unavailable from WB after 2010.

### F.3 Electricity access (% of population) — World Bank `EG.ELC.ACCS.ZS` (= Tracking SDG7 custodian dataset)

| Year | Access (%) | Flag |
|---|---:|---|
| 2015 | 52.5 | [SOURCED] |
| 2016 | 59.3 | [SOURCED — non-monotonic, see note] |
| 2017 | 54.4 | [SOURCED] |
| 2018 | 56.5 | [SOURCED] |
| 2019 | 55.4 | [SOURCED] |
| 2020 | 55.4 | [SOURCED] |
| 2021 | 59.5 | [SOURCED] |
| 2022 | 60.5 | [SOURCED] |
| 2023 | 61.2 | [SOURCED] |
| 2024 | — | not yet released in this vintage |

The 2016 spike (59.3%, above 2017–18) is a known Tracking-SDG7 artifact from periodic re-anchoring to new household surveys + population-denominator revisions; reported as-published. Trajectory: ~52.5% (2015) → 61.2% (2023).

---

## SOURCES

**Conflict / ACLED**
- ACLED, "Nigeria – Conflict Events" (HDX): https://data.humdata.org/dataset/nigeria-acled-conflict-data — file as-of 25 Jun 2026, coverage 1997–19 Jun 2026, accessed 30 Jun 2026
- ACLED Nigeria country page: https://acleddata.com/country/nigeria
- ACLED Conflict Index: https://acleddata.com/series/acled-conflict-index

**Global Terrorism Index (IEP) — report PDFs (accessed 30 Jun 2026)**
- GTI 2015: https://www.economicsandpeace.org/wp-content/uploads/2015/11/Global-Terrorism-Index-2015.pdf
- GTI 2016: https://www.economicsandpeace.org/wp-content/uploads/2016/11/Global-Terrorism-Index-2016.2.pdf
- GTI 2017: https://www.visionofhumanity.org/wp-content/uploads/2020/10/Global-Terrorism-Index-2017.pdf
- GTI 2018: https://www.visionofhumanity.org/wp-content/uploads/2020/10/Global-Terrorism-Index-2018.pdf
- GTI 2019: https://www.visionofhumanity.org/wp-content/uploads/2020/11/GTI-2019-web.pdf
- GTI 2020: https://www.visionofhumanity.org/wp-content/uploads/2020/11/GTI-2020-web-1.pdf
- GTI 2022: https://www.visionofhumanity.org/wp-content/uploads/2022/03/GTI-2022-web_110522-1.pdf
- GTI 2023: https://www.economicsandpeace.org/wp-content/uploads/2023/12/GTI-2023-web.pdf
- GTI 2024: https://www.economicsandpeace.org/wp-content/uploads/2024/02/GTI-2024-web-290224.pdf
- GTI 2025: https://www.economicsandpeace.org/wp-content/uploads/2025/03/Global-Terrorism-Index-2025.pdf
- GTI 2026: https://www.visionofhumanity.org/wp-content/uploads/2026/03/Global-Terrorism-Index-2026-Report.pdf

**Displacement**
- IDMC Nigeria: https://www.internal-displacement.org/countries/nigeria/
- IDMC GRID 2024: https://api.internal-displacement.org/sites/default/files/publications/documents/IDMC-GRID-2024-Global-Report-on-Internal-Displacement.pdf
- World Bank `VC.IDP.NWCV` (new conflict displacements): https://api.worldbank.org/v2/country/NGA/indicator/VC.IDP.NWCV?format=json
- IOM DTM Nigeria: https://dtm.iom.int/nigeria
- UNHCR Nigeria: https://www.unhcr.org/where-we-work/countries/nigeria · Data portal: https://data.unhcr.org/en/country/nga
- UNHCR Global Trends 2024: https://www.unhcr.org/sites/default/files/2025-06/global-trends-report-2024.pdf · Nigeria ARR 2024: https://www.unhcr.org/sites/default/files/2025-06/Nigeria%20ARR%202024.pdf

**Human development / health**
- UNDP HDR Data Centre (HDI): https://hdr.undp.org/data-center/human-development-index
- HDR 2025 Statistical Annex (HDI Table): https://hdr.undp.org/sites/default/files/2025_HDR/HDR25_Statistical_Annex_HDI_Table.pdf
- UNDP Nigeria — HDR 2023/24 launch: https://www.undp.org/nigeria/press-releases/undp-nigeria-launches-2023/24-human-development-report-hdr-titled-breaking-gridlock-reimagining-cooperation-polarized-world
- World Bank life expectancy `SP.DYN.LE00.IN`: https://data.worldbank.org/indicator/SP.DYN.LE00.IN?locations=NG
- World Bank under-5 mortality `SH.DYN.MORT` (UN IGME): https://data.worldbank.org/indicator/SH.DYN.MORT?locations=NG · UN IGME: https://childmortality.org

**Education / electricity**
- UNICEF Nigeria – Education: https://www.unicef.org/nigeria/education
- UNICEF "18.3m" (May 2024): https://www.vanguardngr.com/2024/05/nigerias-out-of-school-children-now-18-3m-unicef/
- UNICEF Nigeria 2024 SitAn: https://www.unicef.org/nigeria/media/10591/file/State-of-Nigerias-Children_Summary-of-the-2024-Updated-SitAn.pdf
- UNESCO GEM Report (~20m, new method): https://www.unesco.org/gem-report/en/publication/out-school-numbers-are-growing-sub-saharan-africa
- World Bank primary completion `SE.PRM.CMPT.ZS`: https://data.worldbank.org/indicator/SE.PRM.CMPT.ZS?locations=NG
- World Bank adult literacy `SE.ADT.LITR.ZS`: https://data.worldbank.org/indicator/SE.ADT.LITR.ZS?locations=NG
- World Bank electricity access `EG.ELC.ACCS.ZS` (Tracking SDG7): https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS?locations=NG
