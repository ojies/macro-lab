# 16 — Consumer Spending & Household Expenditure (Nigeria)

Part of the Nigeria Big-Debt-Cycle / informal-economy dataset. Figures carry source + period + a confidence flag:
**[SOURCED]** = direct from a primary/reputable publication · **[PROVISIONAL]** = preliminary/projection · **[ESTIMATED]** = derived or rounded · blank = not sourceable (left empty, not guessed).

**Vintage warning:** Nigeria's only full consumption-structure survey is the **NLSS 2018/19** (published 2020). Budget-share structure below is therefore ~6-7 years old and predates the 2023-25 inflation shock — treat as the latest *structural* baseline, not a current snapshot. CPI basket weights (rebased Feb 2025) are the more current proxy for spending structure.

---

## 1. Household consumption — scale and share of GDP

| Indicator | Value | Period | Flag | Source |
|---|---|---|---|---|
| Private (household) consumption, % of nominal GDP | **61.2%** | 2023 | [SOURCED] | CEIC / NBS national accounts |
| Private consumption, % of nominal GDP | 65.0% | 2022 | [SOURCED] | CEIC / NBS |
| Household consumption (incl. NPISH), total | **≈ ₦139.8 trillion** | 2023 | [SOURCED] | CEIC / NBS national accounts |
| Final consumption as share of GDP (NBS general note) | "about 60% of total GDP" | NLSS 2018/19 text | [SOURCED] | NBS, Consumption Expenditure Pattern 2019 |
| Household final consumption (% of GDP) — World Bank series | *(blank — WB API returns null for Nigeria 2015-2024)* | — | — | World Bank WDI (data gap) |
| Private consumption per capita | *(blank — not separately sourced; ≈ ₦139.8tn ÷ ~220m ≈ ₦635k/yr is [ESTIMATED] only)* | 2023 | [ESTIMATED] | derived |

> Nigeria is a consumption-driven economy: household consumption is roughly **60-65% of GDP**, the dominant demand component. World Bank's machine-readable WDI series for Nigeria's household-consumption-%-of-GDP is **null** (a real data gap), so NBS/CEIC national-accounts figures are used.

---

## 2. Structure of household spending — budget shares

### 2a. NLSS 2018/19 survey shares (latest full survey)

| Category | Share of total household expenditure | Flag | Source |
|---|---|---|---|
| **Food (total)** | **56.65%** | [SOURCED] | NBS Consumption Expenditure Pattern 2019 |
| Non-food (total) | 43.35% | [SOURCED] | NBS 2019 |
| — Food consumed outside home + transport (combined, top 2 line items) | 24.16% of total | [SOURCED] | NBS 2019 |
| Non-food dominated by (in order): transport, health, education, services (incl. telecoms), rent, fuel & light — combined | 79.40% of *non-food* spend | [SOURCED] | NBS 2019 |
| *Memo: food share 2009/10* | 60.2% | [SOURCED] | NBS 2019 (comparison) |
| Total household expenditure (food + non-food), 2019 | **₦40.21 trillion** (₦21.62tn in 2009/10) | [SOURCED] | NBS 2019 |

*Note: NBS reports non-food sub-categories largely at zonal/state level rather than a clean single national % per category; the national table gives the ordering (transport > health > education > services/telecoms > rent > fuel/light) but not isolated national percentages for each — those cells are left blank rather than guessed.*

### 2b. NBS CPI basket weights — old vs rebased (Feb 2025)

The 2025 CPI rebasing (base year shifted from Nov-2009 to **2024 average**; items 740 → **934**; weights from 2003/04 NLSS → **2023**; a 13th COICOP division "Insurance & Financial Services" added) sharply cut the food weight:

| COICOP division | Old weight (2009 base) | New weight (2024 base, rebased Feb 2025) | Flag | Source |
|---|---|---|---|---|
| **Food & non-alcoholic beverages** | **51.8%** | **40.1%** | [SOURCED] | NBS CPI rebasing; Business Post / NISER |
| Restaurants & accommodation | 1.2% | 12.9% | [SOURCED] | same |
| Other divisions (housing/utilities, transport, health, education, clothing, communications, etc.) | *(blank — not individually sourced in retrieved material)* | — | — | NBS CPI June 2025 report (not extracted) |

> The headline effect: applying the new basket cut measured headline inflation from **34.80% → 24.48%** when first published (Jan 2025 recompute). The lower food weight does **not** mean Nigerians spend less on food — it reflects a newer base year and methodology; survey evidence (Section 3) shows food's real budget burden *rose* under inflation.

---

## 3. Food share / Engel coefficient — THE key spending fact

Nigeria has one of the world's highest Engel coefficients: food dominates the household budget, and the share is *regressive* (poorer/rural households spend more).

| Measure | Value | Period | Flag | Source |
|---|---|---|---|---|
| Average household food share | **56.65%** | NLSS 2018/19 | [SOURCED] | NBS Consumption Expenditure Pattern 2019 |
| Food share, 2009/10 (prior survey) | 60.2% | 2009/10 | [SOURCED] | NBS 2019 |
| Food share, average household (Poverty Assessment framing) | ~56% | 2018/19 | [SOURCED] | World Bank Nigeria Poverty Assessment 2022 |
| Food share, northern zones / rural | >60% | 2018/19 | [SOURCED] | World Bank / NBS |
| Food share, poorest 20% of households | >65% | 2018/19 | [SOURCED] | World Bank / NBS |
| Direction under 2023-25 inflation | Rising real burden; food inflation hit ~23-40% y/y, squeezing budgets further | 2024-25 | [SOURCED] | NBS CPI; SBM Intelligence |

> Engel's Law holds strongly in Nigeria (confirmed in GHS-Panel 2018/19 studies): higher-income households spend a smaller *share* on food. With food inflation peaking near/above 40% y/y in 2024, the effective food share for low-income households pushed toward and beyond 60-65%, leaving little room for discretionary, health, or savings outlays.

---

## 4. Savings

| Indicator | Value | Period | Flag | Source |
|---|---|---|---|---|
| Gross savings, % of GDP | **33.87%** | 2021 | [SOURCED] | World Bank WDI (via Trading Economics) |
| Gross national savings, % of GDP, 2022-2026 | *(blank — IMF DataMapper/Article IV table not retrievable; not guessed)* | — | — | IMF WEO / Art. IV 25/157 (access blocked) |
| Household savings rate | *(blank — not separately published for Nigeria)* | — | — | — |
| Bank deposits per capita | *(blank — not sourced)* | — | — | — |

> Gross savings ~34% of GDP (2021) is high by appearance but heavily skewed by corporate/oil and a small high-income segment; with ~60%+ of household budgets on food and large informality, **household-level** discretionary savings are thin. Reliable post-2021 and household-specific savings figures were not sourceable here — flagged gaps.

---

## 5. Consumer behaviour under the 2023-25 cost-of-living crisis

| Behaviour | Evidence / figure | Period | Flag | Source |
|---|---|---|---|---|
| **Brand-switching** | ~6 in 10 (≈60%) Nigerian shoppers switched brands due to price; cleaning/laundry 53%, skincare 51%, milk & toothpaste 44% | 2024-25 | [SOURCED] | NielsenIQ (via BusinessDay) |
| **Trading to value / private label** | 57% seek extra reasons to buy private-label brands | 2024-25 | [SOURCED] | NielsenIQ |
| **Bulk-buying to cut unit cost** | 65% opting for bulk/larger sizes or wholesalers | 2024-25 | [SOURCED] | NielsenIQ |
| **Sachetisation / smaller packs** | Surge in demand for small packs (cited ~72%); Reckitt and others expanded sachets; "sachet economy" entrenched | 2022-25 | [SOURCED] | WARC/Reckitt; Al Jazeera; NielsenIQ |
| **Reduced meal frequency / skipping meals** | ~1 in 3 households cannot afford enough food; nearly two-thirds face hunger from financial constraints (GHS) | 2024-25 | [SOURCED] | NBS GHS via SBM Intelligence; HRW 2025 |
| **Cutting protein / nutrition downgrade** | Turkey +500% since 2016; jollof-pot cost +19% (Sept '24→Mar '25); fruit consumption down to 38% of households | 2024-25 | [SOURCED] | SBM Intelligence "Staple Under Stress"; NBS |
| **Financial stress sentiment** | Cost-of-living top concern (85%); 36% feel financially constrained (improving from prior year) | 2024-25 | [SOURCED] | NielsenIQ |
| **Rising consumer credit / BNPL** | BNPL market ≈ US$1.55bn (2025), growing ~20%+/yr (CAGR 25.9% in 2022-25); CredPal, EasyBuy, Motito; Jumia integrated installments May 2024 | 2024-26 | [SOURCED] | ResearchAndMarkets / GlobeNewswire |

---

## 6. Spending channels — informal retail & digital payments

| Indicator | Value | Period | Flag | Source |
|---|---|---|---|---|
| Informal / open-market retail share of total retail value | **~90%** | 2024-25 | [SOURCED] | BusinessDay; FieldAssist |
| Modern / formal trade share | <10% | 2024-25 | [SOURCED] | BusinessDay |
| Modern-trade outlet count | ~15,000-18,000 nationwide | 2025-26 | [SOURCED] | Brand Spur; BusinessDay |
| Digital/instant payment transactions (volume) | **7.9 billion** (≈2.97% of global real-time transactions) | 2024 | [SOURCED] | ACI/industry via Leadership/Brand Communicator |
| Formal financial inclusion (adults) | 64% (up from 57% in 2020) | 2023 | [SOURCED] | EFInA Access to Financial Services |
| Overall financial inclusion | ~74% | 2023 | [SOURCED] | EFInA |
| Mobile-money / non-bank financial service use (adults) | 57% (up from 32% in 2020) | 2023 | [SOURCED] | EFInA |

> Consumer spending still flows overwhelmingly through **informal channels** (kiosks, open-air markets, hawkers ≈90% of value), but the *payment layer* is rapidly digitising — instant/mobile payments surged after the 2023 cash crunch, and mobile-money adoption nearly doubled 2020→2023.

---

## Narrative — inflation-era spending shifts

Nigeria entered the 2023-25 cost-of-living shock with an already extreme expenditure structure: food alone took **~57% of the average household budget** (NLSS 2018/19), rising above **60-65% for the poor and rural North**. With consumption running at **60-65% of GDP**, household demand is the economy's backbone — and that backbone bends almost entirely around food.

The 2023 fuel-subsidy removal and naira float drove food inflation toward **40% y/y** in 2024, compressing already-thin discretionary room. Documented responses cluster into a clear *downtrading* pattern: roughly **6 in 10 shoppers switched brands** to cheaper or local alternatives, **65% bulk-bought** to cut unit costs, and demand shifted to **private-label and sachet** formats — entrenching the "sachet economy." More severe coping is widespread: about **one in three households skip meals** and protein/fruit intake fell (turkey +500% since 2016; jollof-pot cost +19% in six months). Credit filled part of the gap, with **BNPL scaling past US$1.5bn** and ~20%+ annual growth.

Structurally, spending still runs through **~90% informal retail**, but the **payment rail digitised fast** — 7.9bn instant transactions in 2024 and mobile-money use jumping to 57% of adults. The Feb-2025 CPI rebasing cut the official food weight from **51.8% → 40.1%**, but this is a methodology/base-year effect, not relief: survey evidence shows the *real* food burden rose. Net picture: a low-savings, food-dominated, increasingly value-seeking and credit-reliant consumer, transacting informally but paying digitally.

---

## Sources

1. NBS — *Consumption Expenditure Pattern in Nigeria 2019* (NLSS 2018/19): https://www.nigerianstat.gov.ng/pdfuploads/Consumption%20Expenditure%20Pattern%20in%20Nigeria%202019.pdf
2. World Bank — *Nigeria Living Standards Survey 2018-2019* microdata: https://microdata.worldbank.org/index.php/catalog/3827
3. World Bank — *Nigeria Poverty Assessment 2022*: https://documents1.worldbank.org/curated/en/099730003152232753/pdf/P17630107476630fa09c990da780535511c.pdf
4. NBS — CPI June 2025 report / rebasing highlights: https://microdata.nigerianstat.gov.ng/index.php/catalog/154
5. Business Post — "Nigeria's CPI Rebase Broke the Data" (old vs new weights): https://businesspost.ng/featureoped/nigerias-cpi-rebase-broke-the-data-heres-what-the-unbroken-picture-actually-shows/
6. NISER — *CPI Rebasing and Cost of Living Reality in Nigeria* (2025): https://niser.gov.ng/v2/wp-content/uploads/2025/04/NISER-Brief-_-CONSUMER-PRICE-INDEX-REBASING-AND-COST-OF-LIVING-REALITY-IN-NIGERIA.pdf
7. CEIC — Nigeria Private Consumption % of nominal GDP: https://www.ceicdata.com/en/indicator/nigeria/private-consumption--of-nominal-gdp
8. World Bank WDI / Trading Economics — Nigeria Gross Savings % of GDP: https://tradingeconomics.com/nigeria/gross-savings-percent-of-gdp-wb-data.html
9. IMF — Nigeria Article IV / Country Report 25/157 (2025, savings table not extractable): https://www.imf.org/-/media/files/publications/cr/2025/english/1ngaea2025001-print-pdf.pdf
10. NielsenIQ — "Brand loyalty wanes as six in ten Nigerians switch products" (via BusinessDay): https://businessday.ng/companies/article/brand-loyalty-wanes-as-six-in-ten-nigerians-switch-products-nielseniq/
11. NielsenIQ — *State of the Nation 2023, FMCG Kenya & Nigeria* / *Adapting to High Living Costs in East & West Africa*: https://nielseniq.com/global/en/insights/analysis/2024/nigeria-state-of-the-nation-2023-overview/
12. SBM Intelligence — Jollof Index / "Staple Under Stress" & "Starving and Stunted": https://medium.com/@sbmintel/starving-and-stunted-3ce6b0bfb3df
13. Human Rights Watch — "Rising Food Prices Deepen Nigeria's Poverty Crisis" (May 2025): https://www.hrw.org/news/2025/05/15/rising-food-prices-deepen-nigerias-poverty-crisis
14. WARC — "Reckitt embraces sachetisation in Nigeria": https://www.warc.com/content/feed/reckitt-embraces-sachetisation-in-nigeria/10198
15. Al Jazeera — "The satchetisation of Africa's largest economy": https://www.aljazeera.com/economy/2022/5/30/analysis-the-satchetisation-of-africas-largest-economy
16. ResearchAndMarkets / GlobeNewswire — *Nigeria Buy Now Pay Later Report 2025/2026*: https://www.globenewswire.com/news-release/2026/02/04/3231830/28124/en/Nigeria-Buy-Now-Pay-Later-Business-and-Investment-Report-2026-A-3-96-Billion-Market-by-2031-from-1-55-Billion-in-2025-Featuring-CredPal-EasyBuy-and-Carbon-Zero.html
17. BusinessDay — "Reeling in Nigeria's outsized informal retail market": https://businessday.ng/features/article/reeling-in-nigerias-outsized-informal-retail-market-into-the-modern-market/
18. FieldAssist — "Decoding Nigeria's FMCG Open Market Sector": https://www.fieldassist.com/blog/decoding-nigerias-fmcg-open-market-sector
19. Brand Spur — "Nigeria's Modern Retail Sector Expands to 18,000 Outlets" (May 2026): https://brandspurng.com/2026/05/15/nigerias-modern-retail-sector-expands-to-18000-outlets-as-indigenous-supermarket-chains-gain-market-dominance/
20. Leadership / Brand Communicator — "Nigeria Hits 7.9bn Transactions on Digital Payment Platforms in 2024": https://leadership.ng/nigeria-hits-7-9bn-transactions-on-digital-payment-platforms/
21. EFInA — Access to Financial Services in Nigeria 2023 survey (financial inclusion 64%, mobile money 57%): https://efina.org.ng/ (and FinDev Gateway summary: https://www.findevgateway.org/blog/2026/01/pocket-banks-nigerias-mobile-money-journey-to-financial-inclusion)
