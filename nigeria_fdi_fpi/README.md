# Nigeria FDI & FPI Dataset, 2000–2025

Foreign Direct Investment (FDI) and Foreign Portfolio Investment (FPI) for Nigeria,
with governance and macro control variables. Compiled 2026-06-28.

---

## 0. Quick start — which file do I want?

| You want… | File |
|---|---|
| FDI, one row per year, every source side-by-side | `nigeria_FDI_yearly.csv` |
| FPI, one row per year, every source side-by-side | `nigeria_FPI_yearly.csv` |
| Governance controls (corruption, rule of law, …) | `nigeria_governance_WGI_yearly.csv` |
| Macro controls (GDP, inflation, exchange rate, …) | `nigeria_macro_controls_yearly.csv` |
| NBS capital-importation split (FDI/Portfolio/Other) per year | `nbs_capital_importation_by_type_annual.csv` |
| NBS detailed sub-components (equity, bonds, loans, …) | `nbs_capital_importation_subcomponents.csv` |
| NBS by sector / by source country | `nbs_capital_importation_by_sector.csv`, `..._by_country.csv` |
| NBS quarterly totals | `nigeria_capital_importation_nbs_quarterly.csv` |
| Reserves, debt, current account, market cap, oil rents… | `nigeria_external_markets_yearly.csv` |
| Global push factors (Fed funds, VIX, oil, global FDI) | `nigeria_global_push_factors.csv` |
| **Derived variables** (%GDP, per-capita, logs, ratios) | `nigeria_fdi_fpi_derived.csv` |
| **Event-indicator variables** (crisis/regime markers, 0/1) | `nigeria_event_indicators.csv` |
| NBS by sector, full history 2013–2025 | `nbs_capital_importation_by_sector_annual.csv` |
| NBS by source country, full history 2013–2025 | `nbs_capital_importation_by_country_annual.csv` |
| Greenfield FDI & cross-border M&A (UNCTAD) | `nigeria_greenfield_manda.csv` |
| Institutional indices (CPI, Doing Business, Heritage, Fraser, ICRG) | `nigeria_institutions_indices.csv` |
| Markets & monetary (NGX, MPR, T-bill, Eurobond, ratings) | `nigeria_markets_monetary.csv` |
| **Everything in one tidy/long file for econometrics** | `nigeria_fdi_fpi_tidy_long.csv` |

See `DATA_CATALOG_AND_PLAN.md` for the full A (fetched) + B (derived) plan and status.

**Tidy/long file** (`nigeria_fdi_fpi_tidy_long.csv`): one row per (year, variable)
observation, columns `year, variable, value, category, source, unit, basis`. 841 rows,
38 variables, blanks dropped. Filter by `category` (FDI / FPI / Governance / Macro
control / Capital importation) or `source`; pivot wide on `variable` for regressions.

---

## 1. ⚠️ The most important thing: NET vs GROSS (two frameworks — both included)

FDI/FPI for Nigeria are reported on **two incompatible bases**. We provide **both**;
do not splice them into one column without flagging the structural break.

1. **Balance-of-Payments NET flows** — World Bank/WDI, IMF, UNCTAD, CBN.
   *Net* = inflows minus disinvestment/repatriation. Can be **negative**. This is
   the standard series in cross-country academic literature.
2. **NBS Capital Importation — GROSS inflows** — capital actually brought in through
   Nigerian banks, classified FDI / Portfolio / Other. Always positive, larger and
   more volatile. By-type series starts **2010**. This is what Nigerian policy
   commentary usually quotes.

They tell different stories (2024: WDI net FDI = US$1.08bn; NBS gross FDI = US$0.67bn;
WDI net portfolio equity = US$1.92bn; NBS gross portfolio = US$8.38bn). Pick the basis
that matches your research question.

---

## 2. FDI file — `nigeria_FDI_yearly.csv` (2000–2025)

| Column | Source | Basis | Unit | Notes |
|---|---|---|---|---|
| `wb_imf_fdi_net_inflows_usd` | World Bank WDI (`BX.KLT.DINV.CD.WD`); upstream = IMF BoP | Net | current US$ | 2025 blank (not yet published) |
| `wb_fdi_net_inflows_pct_gdp` | World Bank WDI (`BX.KLT.DINV.WD.GD.ZS`) | Net | % of GDP | |
| `unctad_fdi_inflows_usd_million` | UNCTADstat / WIR 2025 | Net inflow | US$ million | |
| `unctad_fdi_outflows_usd_million` | UNCTADstat / WIR 2025 | Net outflow | US$ million | negative = net disinvestment abroad |
| `unctad_fdi_inward_stock_usd_million` | UNCTADstat / WIR 2025 | Stock | US$ million | |
| `nbs_fdi_gross_usd_million` | NBS Capital Importation | **Gross** | US$ million | from 2010 only |
| `cbn_fdi_usd_million` | CBN Statistical Bulletin / BoP Highlights | Net/inflow | US$ million | 2005–2024 |
| `cbn_fdi_naira_million` | CBN Statistical Bulletin (BPM5 analytical) | Net | ₦ million | 2000–2004 only |

## 3. FPI file — `nigeria_FPI_yearly.csv` (2000–2025)

| Column | Source | Basis | Unit | Notes |
|---|---|---|---|---|
| `wb_portfolio_equity_net_inflows_usd` | World Bank WDI (`BX.PEF.TOTL.CD.WD`) | Net | current US$ | **equity only**; blank 2000–2004 |
| `wb_portfolio_investment_net_usd` | World Bank WDI (`BN.KLT.PTXL.CD`) | Net | current US$ | equity + debt; large debt outflows dominate some years |
| `nbs_portfolio_investment_gross_usd_million` | NBS Capital Importation | **Gross** | US$ million | from 2010 only |
| `cbn_fpi_usd_million` | CBN Statistical Bulletin / BoP Highlights | Net liabilities | US$ million | 2005–2024; equity + debt |
| `cbn_fpi_naira_million` | CBN Statistical Bulletin | Net | ₦ million | 2000–2004 only |

**Choosing an "FPI" column:** on the BoP/net basis, `wb_portfolio_equity_net` is the
narrow equity measure; `cbn_fpi_usd_million` is the broad measure (equity + debt) and
is usually what "portfolio investment liabilities" means. They differ a lot
(e.g. 2017: CBN $10.5bn vs WB equity $1.36bn).

---

## 4. Governance — `nigeria_governance_WGI_yearly.csv` (2000–2024)

World Bank **Worldwide Governance Indicators** (WGI), all six dimensions, two scalings:
- `*_est` — governance estimate, approx. **−2.5 (worst) to +2.5 (best)**
- `*_score_0_100` — percentile-style score, **0–100**

| Code | Dimension |
|---|---|
| `VA` | Voice and Accountability |
| `PV` | Political Stability and Absence of Violence/Terrorism |
| `GE` | Government Effectiveness |
| `RQ` | Regulatory Quality |
| `RL` | Rule of Law |
| `CC` | Control of Corruption |

Source: World Bank WGI (API source 3, indicators `GOV_WGI_*`). Early-year gaps (e.g.
2001) = no estimate published by the source; blank cells.

## 5. Macro controls — `nigeria_macro_controls_yearly.csv` (2000–2024)

14 common FDI/FPI determinants, all World Bank WDI:
`gdp_current_usd`, `gdp_growth_pct`, `gdp_per_capita_usd`, `inflation_cpi_pct`,
`trade_openness_pct_gdp`, `exchange_rate_lcu_per_usd`, `natural_resource_rents_pct_gdp`,
`real_interest_rate_pct`, `population_total`, `gross_capital_formation_pct_gdp`,
`internet_users_pct`, `domestic_credit_private_pct_gdp`, `central_govt_debt_pct_gdp`,
`unemployment_pct`. Blank = not reported by WDI for that year.

---

## 6. NBS Capital Importation breakdown (gross inflows, US$ million)

- **`nbs_capital_importation_by_type_annual.csv`** — 2010–2025, total + FDI/Portfolio/Other.
  ⚠️ By-type series **begins 2010** (NBS "since 2007" refers only to the headline total).
  2015 split is a derived estimate (quarterly type tables for 2015 are scanned images);
  total is exact. 2012–2014 were later revised by CBN — original NBS vintage shown.
- **`nbs_capital_importation_subcomponents.csv`** — FY2023/2024/2025 detailed classes
  (FDI: equity, other capital; Portfolio: equity, bonds, money-market; Other: trade
  credits, loans, currency deposits, other claims).
- **`nbs_capital_importation_by_sector_annual.csv`** — full annual series **2013–2025**,
  10 main sectors × year (banking dominates — mostly short-term money-market "hot money",
  not FDI). Listed sectors don't sum to the all-sector total (minor sectors omitted).
- **`nbs_capital_importation_by_country_annual.csv`** — full annual series **2013–2025**,
  14 top source countries × year (UK consistently largest, then US & South Africa).
- **`nigeria_capital_importation_nbs_quarterly.csv`** — quarterly totals by main type.

Sector/country tables are NBS-quarterly only (no annual table); selected representative
periods are included. All annual NBS figures = sum of four quarters.

---

## 6b. External, markets & push factors

**`nigeria_external_markets_yearly.csv`** (2000–2025, World Bank) — `total_reserves_usd`,
`external_debt_stock_usd`, `debt_service_pct_exports`, `current_account_balance_usd`,
`current_account_pct_gdp`, `net_errors_omissions_usd` (capital-flight proxy),
`fdi_net_outflows_usd`, `electricity_access_pct`, `oil_rents_pct_gdp`,
`stock_market_cap_usd`, `stock_market_cap_pct_gdp`, `gdp_deflator_inflation_pct`,
`real_effective_exch_rate_idx`, `interest_rate_risk_premium_pct`, `tax_revenue_pct_gdp`,
`exports_pct_gdp`, `imports_pct_gdp`.

**`nigeria_global_push_factors.csv`** (2000–2025) — `us_fed_funds_rate_pct`,
`us_10y_treasury_yield_pct`, `vix_index`, `brent_crude_usd_bbl` (all FRED annual means),
`us_cpi_index_1982_84_100` (FRED, used for real deflation), `global_fdi_inflows_usd_billion`
(World Bank, WLD). These are the classic "push" controls — capital leaves EMs when US
rates / VIX rise.

## 6c. Derived variables — `nigeria_fdi_fpi_derived.csv` (2000–2025)

Computed from data already in the dataset (no new source). Five base series are each
expressed in US$ million and transformed: `fdi_bop` (World Bank net FDI), `fpi_bop`
(World Bank net portfolio, equity+debt), `fpi_cbn` (CBN portfolio inflow),
`nbs_fdi` (NBS gross FDI), `nbs_fpi` (NBS gross portfolio).

For each base series `X`: `X_usd_million`, `X_pct_gdp`, `X_per_capita_usd`,
`X_real_usd_m_2024` (US-CPI-deflated, 2024 base), `X_ihs` (inverse hyperbolic sine —
sign-preserving, use instead of log for series that go negative), `X_log` (blank when
≤0), `X_yoy_pct` (growth), `X_first_diff`, `X_vol3` (3-yr rolling SD = flow-risk proxy).

Plus single-column derivations:
- `fpi_fdi_ratio_nbs` — "hot money" ratio (NBS gross portfolio ÷ gross FDI)
- `fdi_share_total_nbs_pct`, `portfolio_share_total_nbs_pct` — shares of total capital importation
- `fdi_net_vs_gross_gap_usd_m` — NBS gross FDI − World Bank net FDI (round-tripping/measurement proxy)
- `fdi_source_spread_usd_m` — max−min across WB/UNCTAD/CBN FDI (data-reliability flag)
- `gov_composite_index` — mean of the six WGI estimates
- `exch_rate_depreciation_pct` — YoY % change in ₦/US$

## 6d. Event-indicator variables — `nigeria_event_indicators.csv`

> **What these are (read this — they are NOT placeholder, filler, or "irrelevant" data).**
> An **event-indicator variable** is a column that equals **1** in the years a specific
> historical event was in effect and **0** in all other years. In econometrics this is
> the standard "**dummy variable**" — here "dummy" is a technical term for a binary
> (0/1) indicator, **not** a synonym for fake, dummy-placeholder, or test data. These
> are deliberate, meaningful regressors used to control for one-off shocks so the
> effect of your real explanatory variables isn't distorted by crisis years.
>
> **Status: author-constructed, not fetched.** Unlike every other file (which is
> measured data from the World Bank, UNCTAD, CBN, NBS, FRED), these five columns were
> coded by hand from documented historical events. The *events are factual*; the 0/1
> *coding is an analyst's modelling choice*. In the tidy file they carry
> `source = "author-constructed from documented historical event"` so they can never be
> mistaken for observed data. Cite them in write-ups as "author-constructed event
> indicators," not as data from a source.

| Variable | =1 in years | Event it marks | Why it matters for FDI/FPI |
|---|---|---|---|
| `d_gfc_2008_09` | 2008, 2009 | Global Financial Crisis | Global deleveraging → portfolio outflows from emerging markets; FDI dip |
| `d_oil_crash_2014_16` | 2014, 2015, 2016 | 2014–16 oil-price collapse | Oil-revenue shock → FX scarcity & capital reversal in oil-dependent Nigeria |
| `d_recession_2016` | 2016 | Nigeria's 2016 recession | First recession in 25 yrs; sharp fall in capital importation |
| `d_covid_2020` | 2020 | COVID-19 shock | Global risk-off + oil crash; portfolio outflows, FDI slump |
| `d_fx_liberalization_2023ff` | 2023, 2024, 2025 | June-2023 naira float / FX reform | Large devaluation (₦/US$ +51% in 2023, +129% in 2024); reshaped reported flows |

(The `d_` prefix is the conventional econometric marker for an indicator/dummy variable.)

Modelling notes: `d_recession_2016` overlaps `d_oil_crash_2014_16` (2016 is in both) —
don't enter both in one regression without checking collinearity.
`d_fx_liberalization_2023ff` is a **step** indicator (1 from 2023 onward), not a
single-year pulse. All five are 0 for every year not listed above (2000–2007,
2010–2013, 2017–2019, 2021–2022).

## 6e. Greenfield FDI & cross-border M&A — `nigeria_greenfield_manda.csv` (2003–2024)

UNCTAD WIR 2025 annex tables (source: fDi Markets / UNCTAD). Captures investment
*intent / activity* that BoP FDI flows miss.
- `greenfield_value_usd_million` — announced greenfield capex pledges (US$ m)
- `greenfield_num_projects` — number of announced projects
- `manda_net_sales_usd_million` — net cross-border M&A, Nigeria as target (negative = net divestment by foreign buyers)
- `manda_net_purchases_usd_million` — net cross-border M&A, Nigeria as acquirer

Note: greenfield *announcements* are far larger than realized BoP FDI (e.g. 2008 ≈ US$25bn
announced vs ~US$8bn actual inflow). UNCTAD revises these retroactively; values reflect the
WIR 2025 vintage. **FDI income / rate of return is NOT available at Nigeria level** from
UNCTAD (published only as global/regional aggregates) — derive it from IMF BoP "investment
income – direct investment" or CBN if needed.

## 6f. Institutional / business-climate indices — `nigeria_institutions_indices.csv` (2000–2025)

Alternatives to the WGI. **Mind the scale & direction — they differ by column:**

| Column | Scale | Direction | Notes |
|---|---|---|---|
| `ti_cpi_score` | 0–10 (2000–2011), **0–100 (2012+)** | higher = cleaner | ⚠️ **scale break in 2012** — `ti_cpi_scale` column flags which applies; the two halves are NOT comparable |
| `ti_cpi_rank` | rank | lower = better | Transparency International |
| `doingbiz_rank_reportyear` | rank | lower = better | by **report** year (DB2006…DB2020); discontinued after 2020; ranks not comparable across years (methodology changes) |
| `doingbiz_dtf_score_0_100` | 0–100 | higher = better | only published DB2015–DB2020; DB2012–14 unavailable |
| `heritage_econ_freedom_score` | 0–100 | higher = freer | Heritage Foundation |
| `heritage_rank` | rank | lower = better | |
| `fraser_efw_index_0_10` | 0–10 | higher = freer | Fraser EFW, by data year; latest = 2023 |
| `fraser_efw_rank` | rank | lower = better | |
| `icrg_political_risk_0_100` | 0–100 | higher = lower risk | ⚠️ only **2011–2015** in open sources (rest paywalled) |

Revised-vs-as-published caveat: Heritage, Fraser and the Doing Business DTF back-series
retroactively restate history; these are the current revised series. B-READY (Doing
Business successor) has no Nigeria data yet (expected B-READY 2026).

## 6g. Markets & monetary — `nigeria_markets_monetary.csv` (2000–2025)

Year-end values (CBN / NGX / DMO / FRED). The pull factors behind portfolio flows:
`ngx_asi_yearend` (All-Share Index), `ngx_equity_mcap_naira_trillion`,
`ngx_equity_mcap_usd_billion`, `cbn_mpr_pct_yearend` (policy rate),
`tbill_91day_pct`, `fgn_10yr_domestic_yield_pct`, `eurobond_10yr_yield_pct`,
`eurobond_minus_us10y_spread_bps` (EMBI-style spread proxy), `external_reserves_usd_billion`,
and three text columns `sp_rating` / `moodys_rating` / `fitch_rating` (year-end rating + outlook).

Gaps flagged: Eurobond yield 2012–2013 (no DMO report); FGN domestic 10-yr clean only
2012,2014–2016; equity mcap US$ null 2000/01/03; T-bill 2000–2005 are annual averages.
The official JP Morgan EMBI stripped spread isn't free — the spread column is a
single-bond proxy (Nigeria 10yr Eurobond − US 10yr Treasury).

## 7. Known gaps & caveats (read before modelling)

- **2025**: World Bank, IMF, UNCTAD have **not** published full-year 2025 (WDI last
  updated 2026-04-08; cells blank). For 2025 use **NBS**: total US$23.22bn, FDI
  US$0.92bn, portfolio US$19.74bn. CBN full-year 2025 BoP not yet released either.
- **Portfolio equity blank 2000–2004**: WDI does not report `BX.PEF.TOTL.CD.WD` for
  Nigeria before 2005, so `wb_portfolio_equity_net_inflows_usd` is empty for those
  years. Use `cbn_fpi_naira_million` (2000–2004) if you need that window.
- **CBN 2000–2004 are Naira, BPM5** — net analytical-statement entries, not strictly
  the same concept as the 2005+ US$ gross-inflow lines. CBN avg. exchange rates if you
  want a rough USD conversion: ₦101.7/$ (2000), 111.9 (2001), 121.0 (2002), 129.4
  (2003), 133.5 (2004).
- **CBN US$ 2005–2024 ≈ UNCTAD ≈ World Bank** — not a coincidence: CBN/IMF BoP is the
  upstream source all three republish. Treat them as one BoP-net series, not three
  independent observations. The genuinely independent cross-check is **NBS (gross)**.
- **IMF**: a standalone IMF column is **not** included — IMF BoP *is* the
  `wb_imf_fdi_net_inflows_usd` column (WDI sources it from IMF). The IMF SDMX API
  (api.imf.org) was reachable but its FDI series duplicates this column.
- **2022–2023 FDI discontinuity** in CBN comes from different release vintages
  (revisions), not measurement error.

---

## 8. Sources

- **World Bank WDI & WGI** — live API: `https://api.worldbank.org/v2/country/NGA/indicator/<CODE>`
  (WGI use `?source=3`). FDI page: https://data.worldbank.org/indicator/BX.KLT.DINV.CD.WD?locations=NG
- **UNCTADstat** — dataset "FDI flows and stock" (US.FdiFlowsStock):
  https://unctadstat.unctad.org/datacentre/dataviewer/US.FdiFlowsStock
- **UNCTAD World Investment Report 2025** (annex tables):
  https://unctad.org/publication/world-investment-report-2025
- **CBN Statistical Bulletin (External Sector)** — https://www.cbn.gov.ng/documents/Statbulletin.html
  ; CBN 2024 Annual BoP Highlights (2023/2024 figures).
- **NBS Capital Importation** — quarterly reports & Excel back-series:
  https://microdata.nigerianstat.gov.ng/index.php/catalog/143/related-materials
  ; https://nigerianstat.gov.ng (e-library, search "Capital Importation").
