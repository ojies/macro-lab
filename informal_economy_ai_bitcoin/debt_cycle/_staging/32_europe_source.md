# Europe — UK & Eurozone Macro / Debt-Cycle Panel — Source Notes & Structural Diagnosis

**Deliverable:** `../europe/europe_macro.csv`
**Coverage:** annual 2000–2025, 5 entities × 26 years = 130 rows.
**Entities:** UK, Euro area (aggregate), Germany, France, Italy.
**Retrieved:** 2026-07-05.
**Theme:** the "stagnation pole" — aging, low-growth, high-debt advanced Europe; and the euro area's structural fragility as a monetary union *without* a fiscal union.

Primary sources (all official / official-mirror): **Eurostat** (HICP, Maastricht government debt & deficit, EMU-convergence 10y bond yields), **ECB** (Deposit Facility Rate, main refi rate), **ONS** (UK CPI), **Bank of England** (Bank Rate, 10y gilt yield), **IMF WEO** (Apr-2025 vintage — general government gross debt & net lending for UK/DE/FR/IT), **World Bank / ILO** (real GDP growth, unemployment). Machine-readable pulls via the World Bank API, the ECB/Eurostat/IMF/ONS mirrors on **DBnomics** (`api.db.nomics.world`), and the Bank of England IADB CSV endpoint.

---

## Column-by-column

| Column | Definition | Source (by entity) | Native → transform | Flag |
|---|---|---|---|---|
| `gdp_growth` | Real GDP, % change | World Bank `NY.GDP.MKTP.KD.ZG` (all 5, incl. Euro area = "EMU") | annual, used directly | [SOURCED] |
| `cpi_inflation` | Consumer-price inflation, annual % | UK → **ONS** CPI annual rate (series `D7G7`, MM23). EA/DE/FR/IT → **Eurostat** HICP annual-average rate of change (`prc_hicp_aind`, `RCH_A_AVG`, `CP00`) | annual, used directly | [SOURCED] |
| `unemployment` | Unemployment rate, % of labour force | World Bank / ILO-modelled `SL.UEM.TOTL.ZS` (harmonised-consistent; cross-checks Eurostat/ONS to ±0.1–0.2pp) | annual, 1 dp | [SOURCED] |
| `debt_gdp_pct` | General government **gross** debt, % GDP (Maastricht basis) | UK/DE/FR/IT → **IMF WEO** `GGXWDG_NGDP`. Euro area → **Eurostat** `gov_10dd_edpt1` (S13, `GD`, `PC_GDP`, `EA20`) | annual | [SOURCED]; EA 2025 [ESTIMATED] |
| `deficit_gdp_pct` | General government net lending(+)/**borrowing(−)**, % GDP. **Negative = deficit** | UK/DE/FR/IT → **IMF WEO** `GGXCNL_NGDP`. Euro area → **Eurostat** `B9` | annual | [SOURCED]; EA 2025 [ESTIMATED] |
| `policy_rate` | Central-bank policy rate, **year-end** (%) | UK → **BoE Bank Rate** (`IUDBEDR`, last obs of year). EA/DE/FR/IT → **ECB Deposit Facility Rate** (`ECB/FM D.U2.EUR.4F.KR.DFR.LEV`, last obs of year) | daily → year-end level | [SOURCED] |
| `gov_10y_yield` | 10-year benchmark government bond yield, annual average (%) | **Eurostat** EMU-convergence long-term rate `irt_lt_mcby_a` (`A.MCBY.{geo}`) for EA/DE/FR/IT/UK. UK 2025 → **BoE** 10y gilt `IUDMNPY` (annual avg 4.58) | annual average | [SOURCED] |

The three euro-area members (Germany, France, Italy) **share the same `policy_rate`** (the single ECB rate) — this is the entire point of the monetary union, and its central fragility (see below). Their `gov_10y_yield` **diverges** (Bund vs OAT vs BTP spreads) — the market's pricing of that fragility.

---

## Method notes (read before using)

- **CPI method mixes two official headline conventions.** ONS's UK "CPI annual rate" is the **average of the 12 monthly year-on-year rates** (→ UK 2022 = 9.1%, 2023 = 7.3%). Eurostat's HICP `RCH_A_AVG` is the **annual-average-index ratio** (→ Euro area 2022 = 8.4%, Germany 8.7%, Italy 8.7%, France 5.9%). In a sharply *accelerating* year these differ: on the strictly comparable index-ratio basis the UK's 2022 figure is ≈ **7.9%** (World Bank `FP.CPI.TOTL.ZG`), i.e. marginally *below* the euro area rather than above it. Both figures in the CSV are each agency's published headline. The sibling USA panel (`27_usa_monetary_macro_source.md`) used the index-ratio method throughout (US 2022 = 7.99%); for strict UK–US comparability use ≈7.9% for the UK, not 9.1%.
- **These are annual figures; the anchors are monthly peaks.** UK CPI **peaked at 11.1% in Oct-2022** (41-year high); euro-area HICP **peaked at 10.6% in Oct-2022**. Neither appears as an annual value — the annual averages are 9.1% (UK) and 8.4% (EA).
- **`deficit_gdp_pct` sign: negative = deficit, positive = surplus.** This is the raw official net-lending/borrowing convention (IMF, Eurostat, OECD all use it). E.g. UK 2000 = +1.4 (Blair-era surplus); UK 2020 = −13.2, Italy 2020 = −9.4 (COVID). Do **not** read −13.2 as a surplus.
- **`policy_rate` is year-end, not annual average** (unlike the USA panel's fed-funds annual mean). Year-end makes the step-changes and anchors legible. The euro group uses the **Deposit Facility Rate (DFR)**, which since ~2008 (excess-liquidity floor system) is the *effective* policy rate anchoring €STR — and which the task's anchors reference (−0.5% → 4.0%). Pre-2008 the **main refinancing rate (MRO)** was the operational anchor; MRO year-end for reference: 2000 = 4.25, 2007 = 4.00, 2008 = 2.50, 2023 = 4.50, 2024 = 3.15, 2025 = 2.15 (vs DFR 2023 = 4.00, 2024 = 3.00, 2025 = 2.00).
- **Debt basis.** IMF WEO general-government gross debt for EU members is sourced from Eurostat, so the country figures (IMF WEO) and the euro-area aggregate (Eurostat) are on a consistent Maastricht basis (cross-check: Italy 2024 IMF 135.3 ≈ Eurostat 135.3; France 113.1 ≈ 113.0). IMF WEO is used for the four countries because it also carries the 2025 estimate; Eurostat gov-finance stats currently end 2024.
- **[ESTIMATED] cells.** Euro-area `debt_gdp_pct` (89.0) and `deficit_gdp_pct` (−3.0) for **2025** — Eurostat annual GFS not yet released; central values from IMF WEO Apr-2025 / European Commission Spring-2025 forecast. Euro-area HICP 2000 (2.1) is the ECB/Eurostat euro-area figure (the `EA20` HICP series begins 2001).

---

## Validation anchors confirmed

| Anchor (task) | In CSV | ✓ |
|---|---|---|
| UK inflation peaked ~11.1% (Oct-2022) | annual 2022 = 9.1% (monthly peak 11.1% noted) | ✓ |
| UK 2022 gilt/LDI crisis, 10y ~4.5% Sep-2022 (Truss mini-budget) | 2022 **annual avg** gilt = 2.38%; intra-year spiked ≈4.5% (Sep) — see note | ✓ |
| Euro-area inflation peaked ~10.6% (Oct-2022) | annual 2022 HICP = 8.4% (monthly peak 10.6% noted) | ✓ |
| Italy debt/GDP ~135–140% | 2022 = 138.3, 2023 = 134.6, 2024 = 135.3 | ✓ |
| Germany debt/GDP ~63% | 2024 = 63.9, 2023 = 62.9 | ✓ |
| ECB deposit rate −0.5% (2019–22) → 4.0% (2023) → cutting from mid-2024 | DFR 2019/20/21 = −0.50; 2022 = 2.00; 2023 = 4.00; 2024 = 3.00; 2025 = 2.00 | ✓ |
| Eurozone growth ~0–1% 2023–24; Germany near-recession | EA GDP 2023 = 0.46, 2024 = 0.94; **Germany 2023 = −0.87, 2024 = −0.50** | ✓ |
| German Bund negative-yield era | Bund 10y 2019 = −0.25, 2020 = −0.51, 2021 = −0.37 | ✓ |
| Italy sovereign-crisis yields | BTP 10y 2011 = 5.42, 2012 = 5.49 (annual avg; intra-year peaked ~7%) | ✓ |

Additional cross-checks: UK budget **surplus** 2000–2001 (+1.4/+0.3); COVID deficits (UK −13.2, IT −9.4, FR −8.9, EA −7.0 in 2020); euro-area debt peaked **96.5% in 2020**; UK 10y gilt 2024 BoE 4.14 ≈ Eurostat 4.12.

---

# STRUCTURAL DIAGNOSIS — the "stagnation pole"

## 1. AGING (the demographic anchor of low growth)

Europe is the old end of the advanced world, and Italy/Germany are its oldest large economies.

- **Median age (Eurostat, 2025):** EU = 44.9; **Italy = 49.1 (oldest large EU economy, near Japan's ~49.5)**; Germany ≈ 45.5 (dipped slightly from 45.9 in 2015 as immigration offset ageing, but still well above EU average); France younger (~42) thanks to higher fertility.
- **Share aged 65+:** Italy = 24.7% (highest in the EU) — roughly one in four Italians.
- **Old-age dependency ratio (65+ per 100 working-age, 2025):** Italy = **39.0% (highest in EU)** — fewer than 3 working-age people per pensioner — with Portugal/Bulgaria close behind; Germany ~34%. Rising across every EU region.
- **Shrinking working-age population:** Germany's and Italy's 15–64 cohorts are contracting; without immigration the labour force falls, which mechanically caps trend GDP (GDP ≈ workers × productivity). This is the demographic transmission belt into "Japanification."

## 2. LOW GROWTH / PRODUCTIVITY — the EU–US gap and "Japanification"

- **The Draghi report** — *"The Future of European Competitiveness,"* Mario Draghi, **9 September 2024** — is the canonical diagnosis. Key findings: **~70% of the EU–US gap in GDP per capita (PPP) is explained by lower EU productivity**, itself concentrated in the **tech sector** (Europe has no hyperscaler / frontier-AI champions); the US–EU gap *widened ~12% in 2023 alone*. To arrest the divergence Draghi calls for **€750–800 billion of additional investment per year (~4.4–5% of EU GDP)** — a scale comparable to the post-war Marshall Plan and roughly double the RRF, but *annually*.
- **Japanification risk:** the pre-2022 euro area displayed the classic Japanese template — near-zero trend growth, sub-target inflation (HICP 2014–2020 mostly 0.2–1.5%), **negative policy rates (DFR −0.5%) and negative bond yields (Bund below zero 2019–2021)**, aging, high debt, and a central bank pinned at the effective lower bound with large-scale asset purchases. The 2022–23 inflation shock was cyclical/energy-driven, not a break from the structural low-growth trend: growth fell back to ~0–1% in 2023–24, with **Germany in outright contraction (−0.9% in 2023, −0.5% in 2024)** amid a deindustrialisation debate (high energy costs + China competition in autos/chemicals).

## 3. THE EUROZONE'S UNIQUE FRAGILITY — monetary union WITHOUT fiscal union

This is the pole's defining structural risk and the reason a euro-member's debt is *not* like the UK's or the US's.

- **The core design flaw:** 20 sovereigns share one currency and one central bank but keep **separate national budgets, separate debt, and no common treasury / joint fiscal backstop**. A euro member therefore **issues debt in a currency it cannot print** — it is closer to an emerging-market or a sub-sovereign (a US *state*) than to a monetary sovereign. There is no national lender of last resort standing behind its bond market.
- **The 2010–2012 sovereign-debt crisis** made the flaw concrete: **Greece** (first bailout May 2010), then **Ireland, Portugal**, and market attacks on **Spain and Italy**. Peripheral 10y yields blew out — **Italian and Spanish 10y reached ~7% in 2011–12** (BTP annual avg 5.4–5.5%, intra-year ~7%) — a self-fulfilling run: higher yields → worse debt sustainability → higher yields.
- **The bank–sovereign "doom loop":** domestic banks hold large stocks of their own government's bonds. When the sovereign wobbles, banks' capital is hit → banks retrench / need state support → the state's contingent liabilities rise → the sovereign wobbles more. Sovereign risk and bank risk reinforce each other — a channel largely absent for a monetary sovereign.
- **ECB backstops evolved precisely to break this loop:**
  - **"Whatever it takes"** — Draghi, London, **26 July 2012** — followed by **OMT (Outright Monetary Transactions, Sep-2012):** a *conditional* promise of unlimited secondary-market purchases of a stressed member's bonds. Never used, but its mere existence collapsed spreads.
  - **PEPP (Pandemic Emergency Purchase Programme, Mar-2020, €1.85 trn):** flexible cross-country purchases that compressed spreads through COVID.
  - **TPI (Transmission Protection Instrument, Jul-2022):** the modern anti-fragmentation tool — unlimited, un-pre-announced purchases to counter "unwarranted, disorderly" spread-widening not justified by fundamentals, deployable as the ECB *hiked* rates. It exists so that raising rates for the union does not blow up the periphery.
  - **What is still missing:** a genuine **fiscal union** — no permanent joint borrowing at scale, no euro-area treasury, no common deposit insurance (banking union incomplete). NGEU/RRF (2021, ~€800bn joint issuance) was a partial, one-off step, not a standing fiscal capacity.

## 4. THE ENERGY SHOCK — a terms-of-trade blow the US escaped

- The **2022 Russia/Ukraine gas shock** hit Europe hardest because the EU was structurally dependent on Russian pipeline gas (Germany ~55% of gas imports pre-war). TTF wholesale gas spiked above **€300/MWh (Aug-2022)**, ~10× the historical norm.
- This was a **terms-of-trade / real-income transfer out of the bloc** — Europe had to pay far more for imported energy — concentrated on energy-intensive industry (German chemicals, autos, steel). It is a principal driver of the 2022 HICP surge (8.4% EA, 8.7% Germany/Italy) and of German deindustrialisation fears.
- **The US escaped it:** the US is a **net energy exporter** (shale oil & LNG), so the same shock was, on net, a *terms-of-trade gain* for it. This asymmetry — plus the dollar's reserve status — is a large part of why US growth ran ~2.5–3% in 2023–24 while the euro area ran ~0–1%.

---

## KEY CONTRAST — where the UK sits, and why the periphery is different

- **UK ≈ a smaller US, not a euro member.** The UK has **its own currency (sterling), its own central bank (BoE), and issues gilts in a currency it controls** — it can, in extremis, print. Its risk is *inflation / currency* risk, not *default* risk; a UK fiscal scare shows up as a weaker pound and higher yields, not a redenomination/default premium. The **2022 LDI/gilt crisis** (10y gilt spiking ~4.5% in Sep-2022 after the un-funded Truss mini-budget) proved the point *and* its resolution: the **BoE could and did intervene directly** as gilt buyer of last resort, and the crisis ended in days once the budget was reversed. No euro member has an equivalent unilateral backstop.
- **The euro periphery (Italy especially) is closer to EM fragility.** Italy carries ~135–140% debt/GDP in a currency it cannot issue, dependent on the ECB's *conditional* willingness to backstop (OMT/TPI) — i.e. its bond market is ultimately a *political* question about euro-area solidarity, not a monetary-sovereignty question. Hence the persistent **BTP–Bund spread** (Italy 10y consistently 150–250bp over Germany in the CSV) as the market's standing price of break-up / non-backstop risk.
- **Net:** the UK and the euro core (Germany) share the *stagnation-pole* pathologies — aging, low productivity, high debt, energy exposure — but the **euro periphery adds a distinct, EM-like sovereign-fragility layer** that neither the UK nor the US (own-currency reserve issuer) carries. Same demographic/growth disease; categorically different debt-sustainability regime.

---

## Reproducibility (endpoints used)

- World Bank: `https://api.worldbank.org/v2/country/{GBR,DEU,FRA,ITA,EMU}/indicator/{NY.GDP.MKTP.KD.ZG,FP.CPI.TOTL.ZG,SL.UEM.TOTL.ZS}?format=json&date=2000:2025`
- IMF WEO (Apr-2025) via DBnomics: `IMF/WEO:2025-04/{GBR,DEU,FRA,ITA}.{GGXWDG_NGDP,GGXCNL_NGDP}.pcent_gdp`
- Eurostat via DBnomics: debt/deficit `Eurostat/gov_10dd_edpt1/A.PC_GDP.S13.{GD,B9}.EA20`; HICP `Eurostat/prc_hicp_aind/A.RCH_A_AVG.CP00.{EA20,DE,FR,IT}`; 10y yields `Eurostat/irt_lt_mcby_a/A.MCBY.{EA,DE,FR,IT,UK}`
- ECB via DBnomics: `ECB/FM/D.U2.EUR.4F.KR.{DFR,MRR_FR}.LEV` (year-end level)
- ONS via DBnomics: `ONS/MM23/D7G7` (UK CPI annual)
- Bank of England IADB CSV: `IUDBEDR` (Bank Rate), `IUDMNPY` (10y gilt) — `www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp`
