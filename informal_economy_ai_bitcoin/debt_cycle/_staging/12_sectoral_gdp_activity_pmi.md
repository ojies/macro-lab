# Nigeria — Sectoral GDP, Real-Activity Proxies & PMI (2015–2026)

**Dataset:** Big-Debt-Cycle / Nigeria
**Compiled:** 2026-06-30
**Coverage:** Annual 2015–2026, plus quarterly/monthly where the underlying series is naturally higher-frequency.
**Source priority:** NBS (National Bureau of Statistics, GDP), Stanbic IBTC / S&P Global (PMI), NERC & TCN (electricity), NPA (ports), Dangote/BUA & MAN (cement / capacity utilisation), CBN, World Bank (cross-checks).

**Flag legend:** `[SOURCED]` = taken directly from a cited primary/secondary source for the stated period · `[PROVISIONAL]` = sourced but vintage/period/precision uncertain, or a single-source value · `[ESTIMATED]` = derived/computed (method noted) · blank / "—" = not reliably sourceable this pass, left blank rather than guessed.

---

## CRITICAL METHODOLOGY NOTES (read first)

**1. THE 2025 GDP REBASING IS A STRUCTURAL BREAK — there are now TWO incompatible GDP vintages.**
In mid-2025 (released ~July–August 2025) NBS re-based the National Accounts from a **2010 base year to a 2019 base year** (first base-year change in ~11 years; the old base covered only 14 sector groups). Effects:
- **Nominal GDP for 2024 jumped ~34–35%**, from ₦277.5tn (old) to **₦372.8tn** (rebased) ≈ US$243bn.
- **Sector weights shifted:** Services and informal activity weighted **up**; Industry weighted **down**. Real estate, ICT/telecoms, trade and the informal economy gained share through better survey coverage (2019 National Business Sample Census + 2022 National Agricultural Sample Survey).
- **The informal sector** was measured at **₦86.85tn = 42.5% of 2019 GDP** (vs ₦39.00tn estimated in the 2015 rebasing) — a near-doubling of measured informality.
- **Real GROWTH rates were also restated.** The rebased series shows a much deeper 2020 COVID contraction and weaker 2021 than the old series (see §1c). So **do not splice old-base 2015–2018 growth onto rebased 2019–2025 growth** without flagging the break.

**2. Two PMI series.** (a) **Stanbic IBTC Bank Nigeria PMI**, compiled by **S&P Global** (whole-economy/composite, ~400 firms across agriculture, manufacturing, services, construction, retail; endorsed/adopted by NBS) — the continuous, citable monthly series. (b) The **CBN's own Manufacturing/Composite PMI** ran 2014→**suspended early 2023** (last regular prints ~Feb/Mar 2023, during the cash-crunch/naira-redesign period); CBN later published some PMI factsheets again in 2024, but the Stanbic IBTC/S&P Global series is the de-facto market reference. Treat the CBN series as **discontinued ~2023** for continuity purposes.

**3. Electricity is Nigeria's binding real-activity constraint.** Installed capacity ~12–13.6 GW but **average ON-GRID sent-out generation has been stuck at ~3.5–4.8 GW for a decade** due to gas supply, transmission (TCN) and DisCo offtake/liquidity limits, plus frequent total grid collapses. Generation "MW" and "MWh/h" (average power) are used interchangeably by NERC for the hourly average.

---

## 1a. REAL GDP GROWTH — HEADLINE, ANNUAL (%)

Two vintages shown side-by-side because the 2025 rebasing restated history. **Use the rebased column from 2019 onward; the old-base column is the series that was in force 2015–mid-2025.**

| Year | Real GDP growth — OLD (2010-base) NBS | Real GDP growth — REBASED (2019-base) NBS | Flag / note |
|---|---|---|---|
| 2015 | +2.65 | — | OLD [PROVISIONAL — widely-reported NBS 2010-base figure] |
| 2016 | −1.62 (recession) | — | OLD [PROVISIONAL] |
| 2017 | +0.81 | — | OLD [PROVISIONAL] |
| 2018 | +1.92 | — | OLD [PROVISIONAL] |
| 2019 | +2.27 | ~ (base year) | OLD [PROVISIONAL] |
| 2020 | −1.79 (COVID) | **≈ −6.96** | OLD [PROVISIONAL]; rebased [PROVISIONAL — single NBS-cited source] |
| 2021 | +3.40 | **≈ +0.95** | OLD [PROVISIONAL]; rebased [PROVISIONAL — single NBS-cited source] |
| 2022 | **+3.10** | — | OLD [SOURCED — NBS, confirmed] |
| 2023 | **+2.74** | — | OLD [SOURCED — NBS, confirmed] |
| 2024 | +3.40 (pre-rebasing print) | **+3.38** | rebased [SOURCED — NBS Q4 2025 report] |
| 2025 | n/a | **+3.87** | rebased [SOURCED — NBS Q4 2025 report] |
| 2026 | n/a | Q1 2026 +3.89 (YoY) | [SOURCED — TradingEconomics/NBS print] |

**World Bank cross-check (Macro Poverty Outlook, rebased-aligned est., real GDP growth %):** 2016 −1.8 · 2017 +0.4 · 2018 +1.2 · 2019 +1.0 · 2020 **−6.4** · 2021 +1.1 · 2022 +4.3 · 2023 +3.3 · 2024 +4.1 · 2025E +4.0. [SOURCED — World Bank country data sheet]. *These are WB estimates, not exact NBS prints (e.g. WB 2024 4.1 vs NBS rebased 3.38), but corroborate the rebased shape: deep 2020 trough, weak 2021, ~3–4% from 2022.*

**Nominal (rebased, 2019-base) GDP, ₦ trillion:** 2019 **205.09** · 2020 **213.63** · 2021 **243.30** · 2022 **274.23** · 2023 **314.02** · 2024 **372.82** · 2025 **441.5**. [SOURCED — NBS rebased release / World Bank current-LCU]. Q4 2025 nominal ₦122.81tn; real ₦63.97tn.

## 1b. OIL vs NON-OIL GDP GROWTH (%) — REBASED where noted

| Period | Oil GDP growth (YoY) | Non-oil GDP growth (YoY) | Oil share of GDP | Non-oil share | Flag |
|---|---|---|---|---|---|
| FY 2024 (rebased) | +5.54 | ~3.x | ~3.5 | ~96.5 | [SOURCED — NBS] |
| FY 2025 (rebased) | **+8.50** | ~3.7 | **3.53** | **96.47** | [SOURCED — NBS Q4 2025 report] |
| Q4 2024 | +2.08 | +3.80 | — | 95.40 | [SOURCED — NBS] |
| Q3 2025 | — | +3.91 | — | — | [SOURCED — NBS] |
| Q4 2025 | **+6.79** | **+3.99** | **2.87** | **97.13** | [SOURCED — NBS Q4 2025 report] |

*Oil average production: Q4 2025 ≈ 1.58 mbpd (Q3 2025 1.64; Q4 2024 1.54). Oil is now a tiny GDP share (~3%) but still dominates FX/fiscal revenue — the classic Nigeria debt-cycle asymmetry.*

## 1c. BROAD SECTOR — GROWTH RATE (YoY, %) and SHARE OF GDP

**Latest detailed quarter — Q4 2025 (rebased, 2019-base):**

| Sector | Growth YoY (Q4 2025) | Growth YoY (Q4 2024, comp.) | Share of GDP (Q4 2025) | Flag |
|---|---|---|---|---|
| **Agriculture** | +4.00 | +2.54 | 28.66 | [SOURCED — NBS] |
| **Industry** (total) | +3.88 | +2.49 | 15.42 | [SOURCED — NBS] |
| **Services** | +4.15 | +4.75 | 55.92 | [SOURCED — NBS] |
| of which **Manufacturing** | +1.13 | ~1.3 | (within Industry) | [SOURCED — NBS] |
| of which **Real estate** | +3.43 | +5.28 | 14.57 | [SOURCED — NBS] |
| of which **Trade** | + (key driver) | — | 16.84 | [SOURCED — NBS] |
| of which **ICT / Telecoms & info** | + | — | **8.12** (telecom & info svcs) | [SOURCED — NBS] |
| **Oil** | +6.79 | +2.08 | 2.87 | [SOURCED — NBS] |
| **Non-oil** | +3.99 | +3.80 | 97.13 | [SOURCED — NBS] |

**Full-year 2025 sector SHARES of GDP (rebased):** Crop/Agriculture **27.55%**, Trade **17.37%**, Real estate **13.57%**, ICT **10.07%**, Manufacturing (among top contributors), Services aggregate the largest block. [SOURCED — NBS FY2025]. Q4-2025 individual-activity ranking: Crop production 20.44% > Trade 16.84% > Real estate 14.57% > Telecom & info 8.12%.

**Pre-rebasing reference (old 2010-base), FY2024 / Q4 2024:** Services share **57.38%** (grew +5.37% in Q4), Agriculture +1.76%, Industry +2.00%; **ICT annual contribution 17.68%** of 2024 GDP (Q4 17.00%), of which telecom **14.40%** in Q4 2024 — telecom was the 3rd-largest single activity behind crop production and trade. [SOURCED — NBS Q4 2024 report]. *Note the rebasing roughly HALVED the headline ICT share (≈17.7% old-base → ≈10% rebased) because the much larger informal/real-estate base dilutes ICT's weight — a key interpretive caveat.*

**Rebased 2019 base-year sector shares (for reference):** Services **53.1%** (was 50.2% under old method), Agriculture **25.8%**, Industry **22.1%** (down from 27.7%). Top 5 activities at 2019: Crop production 17.6%, Trade 17.4%, Real estate 10.8%, Telecommunications 6.8%, Crude petroleum & natural gas 5.9% (oil dropped from 3rd to 5th). [SOURCED — NBS rebasing factsheet].

---

## 2. PURCHASING MANAGERS' INDEX (PMI) — Stanbic IBTC / S&P Global (50 = no change)

**Long-run sense (whole series, 2014–2026):** average ≈ **52.8**; all-time high **59.1 (May 2018)**; record low **37.1 (Apr 2020, COVID)**. The series ran mostly in expansion 2017–2019 and 2021, swung into a contraction patch in 2022–2024 (FX shock, fuel-subsidy removal June 2023, naira float, cash crunch early 2023, four straight contraction months **Jul–Oct 2024**), then recovered through 2025–2026. [SOURCED — TradingEconomics / S&P Global].

**Monthly values (most reliable points):**

| Month | PMI | Flag / note |
|---|---|---|
| 2018-05 | 59.1 | all-time high [SOURCED] |
| 2020-04 | 37.1 | record low (COVID) [SOURCED] |
| 2023-03 | ~ low-40s | CBN-cash-crunch trough; Stanbic series weak [PROVISIONAL] |
| 2024-Q3 (avg) | 49.6 | quarter in contraction [SOURCED] |
| 2024-09 | 49.8 | [SOURCED] |
| 2024-10 | 46.9 | 4th straight contraction; sharpest since Mar 2023 [SOURCED] |
| 2025-04 | 54.2 | [SOURCED] |
| 2025-05 | 52.7 | [SOURCED] |
| 2025-08 | 54.2 | [SOURCED] |
| 2025-09 | 53.4 | [SOURCED] |
| 2025-10 | 54.0 | 6-month output high [SOURCED] |
| 2025-11 | 53.6 | [SOURCED] |
| 2025-12 | 53.5 | [SOURCED] |
| 2026-01 | 49.7 | dipped below 50 [SOURCED] |
| 2026-02 | 53.2 | recovery [SOURCED] |
| 2026-03 | 51.9 | selling-price inflation lowest in 6+ yrs [SOURCED] |
| 2026-04 | 52.4 | [SOURCED] |
| 2026-05 | 54.1 | 9-month high; strongest since Aug 2025 [SOURCED] |

⚠️ **Data-quality flag:** search sources returned identical Jan/Feb/Mar values (49.7 / 53.2 / 51.9) attributed to *both* 2025 and 2026 — almost certainly a 2025↔2026 conflation. The Jan–May 2026 row is treated as the reliable **current** print; **2025 H1 monthly values (Jan–Mar) are NOT asserted here** to avoid propagating the conflation. The 2025 H2 values (Aug–Dec) are internally consistent with their dated press releases.

**CBN PMI (legacy):** manufacturing & composite PMI published by CBN from 2014; **suspended ~Q1 2023**; superseded as the reference series by Stanbic IBTC/S&P Global. Not continued here.

---

## 3. ELECTRICITY — ON-GRID GENERATION (Nigeria's binding constraint)

| Year | Avg on-grid generation (MWh/h ≈ MW) | Installed capacity (MW) | Peak / notable | Grid collapses | Flag |
|---|---|---|---|---|---|
| 2015 | **3,557** | 12,132 | — | — | [SOURCED — NERC via Nairametrics] |
| 2016 | — | — | recession + pipeline vandalism cut output | — | gen [—] |
| 2017 | — | — | — | — | [—] |
| 2018 | — | — | peak ~5,222 MW (Dec 2018) | — | [PROVISIONAL] |
| 2019 | — | — | — | — | [—] |
| 2020 | — | — | — | — | [—] |
| 2021 | — | — | peak ~5,615 MW (Mar 2021) | several | [PROVISIONAL] |
| 2022 | **3,892** | 13,097 (avail. 4,059) | multiple total collapses | several | [SOURCED — NERC] |
| 2023 | ~4,1xx | ~13,000 | — | several | gen [—]; capacity [PROVISIONAL] |
| 2024 | **4,207** (Q4 avg; 9,289.95 GWh in Q4) | 5,296.89 (avail. cap. Q4) | — | **12** | gen/collapses [SOURCED — NERC Q4-2024] |
| 2025 | **4,770.59** (Q1 avg; 10,304.47 GWh Q1); 5,506 generated Oct 2025 | 5,366.88 (Q1) / installed 13,625 (NERC Feb-2026) | **record 5,801.84 MW peak, 4 Mar 2025**; record 128,370.75 MWh daily delivery same day | **4** (Feb 12, Mar 7, Sep 10, Dec 29) | [SOURCED — NERC / TCN / Premium Times] |
| 2026 | — (Q1 NERC report pending) | 13,625 (Feb-2026 factsheet) | TCN wheeling cap. cited 8,700 MW | — | capacity [SOURCED] |

**Key facts:** installed ≈ **13,625 MW** but average **sent-out generation only ~3.5–4.8 GW**; TCN claims **8,700 MW** transmission/wheeling capacity (i.e. transmission now exceeds what is generated). Distribution (DisCo) delivered only ~4,290 MW of the 5,506 MW generated in Oct 2025 — offtake/liquidity is now a co-binding constraint. April 2025 "Band A" cost-reflective tariff hike reshaped DisCo economics. Between 2010–2022 the grid suffered **222+ partial/total collapses**; 12 in 2024 and 4 in 2025. [SOURCED — NERC quarterly reports, TCN, Guardian/Intelpoint/Daily Post].

*Gaps: clean ANNUAL average-generation figures for 2016–2021 and 2023 are not openly published in a single citable table — they require the NERC quarterly-report archive or the System Operator's daily logs. Only 2015 and 2022 annual averages, and 2024-Q4 / 2025-Q1 quarter averages, are cleanly citable. Left blank rather than guessed.*

---

## 4a. PORT ACTIVITY / CARGO THROUGHPUT — Nigerian Ports Authority (NPA)

| Year | Total cargo throughput (metric tonnes) | Container throughput (TEU) | Flag |
|---|---|---|---|
| 2023 | 71,213,197 (≈71.21 Mt) | 1,591,194 | [SOURCED — NPA] |
| 2024 | **103,336,863 (≈103.34 Mt)** (+45.1% YoY) | **1,744,972** (+9.7%) | [SOURCED — NPA] |
| 2025 | +24.8% YoY (NPA full-year statement); Q3 2025 cargo traffic +16.2% YoY | — | [SOURCED — NPA via Economic Confidential / Ecofin] |

**2024 cargo mix:** Liquid bulk 55.6%, containerised 20.9%. Transhipment containers +136.5% (Lekki Port ramp-up, +2,160.8% throughput growth off a tiny base; Onne +9.4%, Tin Can +7.3%). [SOURCED — NPA]. *Gap: a clean 2015–2022 annual throughput series requires NPA annual reports / NBS port-statistics tables (NPA "Ports Statistics" portal) — not retrieved this pass.*

## 4b. CEMENT PRODUCTION / SALES (industrial-activity proxy)

| Year | Dangote Cement — Nigeria volumes (Mt) | Dangote Group total (Mt) | Notes | Flag |
|---|---|---|---|---|
| 2023 | 16.4 | ~27.3 | — | [SOURCED — Dangote Cement FY2023] |
| 2024 | **17.7** (+7.9%) | **27.7** (+1.6%) | Nigeria revenue ₦3,580.6bn (+62.2%, mostly price) | [SOURCED — Dangote Cement FY2024 audited] |
| 2025 (9M) | — | **20.24** (9M, vs 20.67 9M-2024, −2%) | volumes soft, revenue up on price; BUA revenue ₦858.7bn 9M (+47%) | [SOURCED — Nairametrics / company 9M-2025] |

*Volume growth has been weak/flat while naira revenue ballooned — i.e. cement "boom" is largely **price**, not volume; real demand constrained by purchasing power. BUA Cement publishes revenue/profit but volume tonnage not cleanly retrieved. 2015–2022 annual volume series available in Dangote annual reports — not compiled this pass.*

## 5. MANUFACTURING CAPACITY UTILISATION

| Year | Capacity utilisation (%) | Source basis | Flag |
|---|---|---|---|
| 2023 | 55.1 | MAN Economic Review | [SOURCED — MAN] |
| 2024 | **57.0** (H2 +1.2pp vs H1; CEIC reports 61.9% Dec-2024) | MAN Economic Review H2-2024 | [SOURCED — MAN] |

**Context (2024):** bank lending rates to manufacturers rose to **35.5%** (from 28.06% in 2023) as MPR hit 27.50%; manufacturers' spend on **alternative/self-generated energy reached ₦1.11tn** (+42.3% YoY) — a direct, quantified read-through from the electricity constraint in §3 to manufacturing competitiveness. [SOURCED — MAN]. *Gap: 2015–2022 MAN/CBN capacity-utilisation series (CBN Statistical Bulletin / earlier MAN reviews) not compiled this pass; historically ~45–55%.*

---

## SOURCES

**GDP / sectors (NBS & cross-checks)**
1. NBS Q4 2025 GDP report coverage — Premium Times, "Nigeria's economy grows 4.07% in Q4 2025…": https://www.premiumtimesng.com/business/business-news/860155-nigerias-economy-grows-4-07-in-q4-2025-as-non-oil-sector-drives-expansion-nbs.html
2. Vanguard, "Nigeria's GDP grows 4.07% in Q4 2025 as services, oil lift economy — NBS": https://www.vanguardngr.com/2026/02/nigerias-gdp-grows-4-07-in-q4-2025-as-services-oil-lift-economy-nbs/
3. Punch, "Services drive GDP growth to 4.07% in Q4 2025 - NBS": https://punchng.com/services-drive-gdp-growth-to-4-07-in-q4-2025-nbs/
4. Federal Ministry of Finance, "Nigeria Records Over 4% GDP Growth in Q4 2025": https://finance.gov.ng/nigeria-records-over-4-gdp-growth-in-q4-2025-signaling-broad-based-economic-growth-and-momentum/
5. NBS Q4 2024 GDP report coverage — Premium Times: https://www.premiumtimesng.com/business/business-news/776742-nigerias-gdp-grew-by-3-84-in-q4-2024-nbs.html ; Punch: https://punchng.com/nigerias-gdp-expanded-by-3-84-in-q4-2024-nbs/
6. ICT contribution FY2024/Q4 2024 — Nairametrics: http://nairametrics.com/2025/02/26/ict-contributes-17-to-nigerias-gdp-in-q4-2024-despite-slower-growth-nbs/ ; Vanguard: https://www.vanguardngr.com/2025/02/why-nigerias-ict-sector-recorded-17-gdp-contribution-in-q4-2024-experts/
7. GDP rebasing (2019 base) — Nairametrics factsheet (NBS): https://nairametrics.com/2025/08/07/nbs-factsheet-nigerias-economy-expands-by-35-4-following-gdp-rebasing/ ; Africa Check: https://africacheck.org/fact-checks/factsheets/factsheet-nigeria-rebases-its-economy-again-heres-what-sets-it-apart ; Nairametrics overview: https://nairametrics.com/2025/01/10/what-nigerias-2025-gdp-rebasing-means/
8. NBS Nigeria (X) rebased nominal GDP series 2019–2024: https://x.com/NBS_Nigeria/status/1947343745692680243
9. NBS GDP Q4 2023 report (FY2022 3.10%, FY2023 2.74%): https://www.nigerianstat.gov.ng/elibrary/read/1241460
10. World Bank Nigeria country data sheet (Macro Poverty Outlook indicators, real GDP growth & nominal LCU): https://thedocs.worldbank.org/en/doc/b3502c65235d8c72aef5f34d87ed6298-0500062021/related/data-nga.pdf
11. World Bank — GDP growth (annual %) Nigeria: https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=NG
12. TradingEconomics — Nigeria GDP annual/full-year growth: https://tradingeconomics.com/nigeria/full-year-gdp-growth ; https://tradingeconomics.com/nigeria/gdp-growth-annual

**PMI (Stanbic IBTC / S&P Global)**
13. TradingEconomics — Stanbic IBTC Nigeria Composite PMI (history, high/low/avg): https://tradingeconomics.com/nigeria/composite-pmi
14. S&P Global PMI press releases (Stanbic IBTC Nigeria PMI): https://www.pmi.spglobal.com/Public/Home/PressRelease/8c90bc93f6d44033889ff15cb9330d75
15. Stanbic IBTC PMI report PDFs (e.g. April 2025, May 2025, Dec 2025): https://www.stanbicibtcbank.com/static_file/Nigeria/nigeriabank/Corporate%20and%20Investment/Downloads/Stanbic%20IBTC%20PMI-%20April%202025.pdf ; https://www.stanbicibtcbank.com/static_file/Nigeria/nigeriabank/Corporate%20and%20Investment/Insights/Stanbic%20IBTC%20Bank%20PMI%20December%202025.pdf
16. May 2026 PMI (54.1, 9-month high) — Brand Spur: https://brandspurng.com/2026/06/01/stanbic-ibtc-bank-nigeria-pmi-new-order-growth-hits-nine-month-high-in-may/
17. Oct 2025 PMI (six-month output high) — Brand Spur: https://brandspurng.com/2025/11/03/stanbic-ibtc-bank-nigeria-pmi-output-growth-hits-six-month-high-in-october/
18. CBN Purchasing Managers' Index page (legacy series): https://www.cbn.gov.ng/documents/PurchManIndex.html

**Electricity (NERC / TCN)**
19. NERC capacity/generation 2015 vs 2022 (3,557→3,892 MWh/h; installed 12,132→13,097 MW) — Nairametrics citing NERC: https://nairametrics.com/2023/10/09/electricity-capacity-in-nigeria-grew-7-95-between-2015-and-2022-nerc/
20. NERC 2025 Q1 report (Q1 2025 avg 4,770.59 MWh/h; Q4 2024 avg 4,207.41): https://nerc.gov.ng/wp-content/uploads/2025/07/2025_Q1_Report.pdf
21. Record peak 5,801.84 MW (4 Mar 2025) & 2025 milestones — Premium Times: https://www.premiumtimesng.com/news/top-news/844691-nigerias-transmitted-electricity-reached-highest-ever-5801mw-in-2025-official.html ; P.M. News: https://pmnewsnigeria.com/2025/08/12/nigerias-electricity-grid-hits-record-breaking-milestones-in-2025/
22. Oct 2025 generation 5,506 MW / distributed 4,290 MW (NERC) — Technext: https://technext24.com/2025/11/18/nerc-nigeria-generated-5506mw-of-power/
23. TCN 8,700 MW wheeling capacity / 13,625 MW installed (NERC Feb 2026 factsheet) — Guardian: https://guardian.ng/news/tcn-says-transmission-exceeds-peak-generation-cites-8700mw-wheeling-capacity/ ; Businessday: https://businessday.ng/energy/power/article/national-grid-can-transmit-more-power-than-nigeria-generates-tcn-boss/
24. Grid collapses 2024 (12) — Intelpoint: https://intelpoint.co/insights/nigerias-national-grid-has-collapsed-12-times-in-2024/ ; Guardian timeline: https://guardian.ng/news/timeline-the-12-times-national-grid-collapsed-in-2024/
25. Grid collapses 2025 (4) — Daily Post: https://dailypost.ng/2025/12/30/2025-fourth-national-grid-collapse-wreaks-havoc-on-nigerians-businesses/

**Ports (NPA)**
26. NPA 2024 cargo (103.34 Mt, +45.1%) & container (1.745m TEU) — NPA performance synopsis: https://nigerianports.gov.ng/2025/06/18/10830/
27. NPA 2025 cargo +24.8% — Economic Confidential: https://economicconfidential.com/ports-cargo-growth-npa/ ; Q3 2025 +16.2% — Ecofin Agency: https://www.ecofinagency.com/news-industry/1812-51525-nigeria-ports-record-16-2-rise-in-cargo-traffic-in-q3-2025
28. NPA Ports Statistics portal: https://nigerianports.gov.ng/ports-statistics/

**Cement (Dangote / BUA)**
29. Dangote Cement FY2024 audited results (Nigeria 17.7 Mt, group 27.7 Mt, rev ₦3,580.6bn): https://www.dangotecement.com/wp-content/uploads/2025/03/Dangote-Cement-Full-Year-2024-Results-Statement.pdf
30. Dangote Cement FY2023 presentation: https://cement.dangote.com/wp-content/uploads/2024/03/Dangote-Cement-Presentation-FY-2023-Final.pdf
31. Dangote 9M-2025 volumes/revenue — Nairametrics: https://nairametrics.com/2025/09/04/how-dangote-cement-made-revenue-of-n2-07-trillion-in-6-months-of-2025/ ; cement-giants profit/BUA — MSME Africa: https://msmeafricaonline.com/nigerias-cement-giants-post-n984-4-billion-profit-as-price-hikes-boost-growth/

**Capacity utilisation (MAN)**
32. MAN Economic Review H2-2024 — capacity utilisation 57.0% (2024) vs 55.1% (2023), energy spend ₦1.11tn, lending 35.5% — The Nation: https://thenationonlineng.net/manufacturing-capacity-utilisation-improves-to-57/
33. CEIC — Nigeria Capacity Utilization Rate: Manufacturing (61.9% Dec-2024): https://www.ceicdata.com/en/nigeria/capacity-utilization-rate/capacity-utilization-rate-manufacturing
34. CBN Annual Statistical Bulletin (historical capacity-utilisation / real-sector series): https://www.cbn.gov.ng/documents/Statbulletin.html

---

### Confidence & gaps (analyst note)
- **High confidence:** Q4-2025 & FY-2025 sector growth/shares and oil/non-oil split (NBS primary); the rebasing facts and magnitude; 2024 NPA cargo & container; Dangote FY2024 volumes; MAN 2023–24 capacity utilisation; 2024-Q4/2025-Q1 electricity averages, the 5,801.84 MW peak, and grid-collapse counts; current (2026) PMI prints.
- **Medium / provisional:** old-base annual GDP growth 2015–2021 (widely-reported NBS 2010-base figures, not re-opened from primary this pass); rebased real-growth restatement for 2020 (≈−6.96%) & 2021 (≈+0.95%) rest on a single NBS-cited source.
- **Open gaps (blank, not guessed):** clean ANNUAL average grid generation for 2016–2021 & 2023; NPA 2015–2022 throughput series; cement volumes 2015–2022 & BUA tonnage; capacity-utilisation 2015–2022; 2025 H1 monthly PMI (flagged 2025↔2026 conflation risk). These require NERC quarterly archive, NPA/Dangote/MAN annual reports, and the CBN Statistical Bulletin Excel files.
