# USA Monetary Policy & Macro Panel — Source Notes

**Deliverable:** `../usa/usa_monetary_macro.csv`
**Coverage:** annual 1960–2025 (66 rows, one per year)
**Retrieved:** 2026-07-04
**Primary source:** FRED (Federal Reserve Economic Data), Federal Reserve Bank of St. Louis, machine-readable CSV endpoint `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>`. NBER for recession dating.

Note: 2025 reflects the latest available data as of retrieval. FEDFUNDS/UNRATE/GS10 are 2025 averages over available months; real GDP growth 2025 is the FRED annual advance/current estimate.

## Column-by-column

| Column | FRED series | Native freq | Transform | Coverage | Flag |
|---|---|---|---|---|---|
| `fed_funds_rate` | FEDFUNDS | monthly | annual mean (%) | 1960–2025 | [SOURCED] |
| `cpi_inflation` | CPIAUCSL | monthly | annual-average CPI index, then % change vs prior year's annual average | 1960–2025 | [SOURCED] |
| `real_gdp_growth` | A191RL1A225NBEA | annual | used directly (real GDP, % change, annual, BEA via FRED) | 1960–2025 | [SOURCED] |
| `unemployment_rate` | UNRATE | monthly | annual mean (%) | 1960–2025 | [SOURCED] |
| `treasury_10y` | GS10 | monthly | annual mean (%) | 1960–2025 | [SOURCED] |
| `yield_curve_10y_2y` | T10Y2Y | daily | year-end (last valid daily obs of year), % | 1976–2025; blank 1960–1975 | [SOURCED] |
| `fed_balance_sheet_pct_gdp` | WALCL / GDP | weekly / quarterly | year-end WALCL (millions→billions) ÷ annual-average nominal GDP (billions) × 100 | 2008–2025; blank before | [SOURCED] |
| `recession_flag` | NBER business-cycle dates | — | 1 if any NBER-dated recession month falls in the year, else 0 | 1960–2025 | [SOURCED] |

## Series URLs
- FEDFUNDS: https://fred.stlouisfed.org/series/FEDFUNDS
- CPIAUCSL: https://fred.stlouisfed.org/series/CPIAUCSL
- A191RL1A225NBEA (Real GDP, % chg, annual): https://fred.stlouisfed.org/series/A191RL1A225NBEA
- UNRATE: https://fred.stlouisfed.org/series/UNRATE
- GS10: https://fred.stlouisfed.org/series/GS10
- GS2 (fetched for cross-check of spread): https://fred.stlouisfed.org/series/GS2
- T10Y2Y (10y–2y spread, daily): https://fred.stlouisfed.org/series/T10Y2Y
- WALCL (Fed total assets): https://fred.stlouisfed.org/series/WALCL
- GDP (nominal, billions): https://fred.stlouisfed.org/series/GDP
- NBER cycle dates: https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions

## Transform details / notes
- **CPI inflation** is annual-average-over-annual-average (not Dec/Dec). This is why 1980 = 13.50% (annual avg) and 2022 = 7.99% — the widely-cited 9.1% (Jun 2022) and 13.5% headline are month-specific peaks; annual-average change is lower.
- **fed_funds_rate 1981 = 16.38%** is the 1981 annual *average*. The Volcker ~19–20% figure is the monthly peak (mid-1981), consistent with an annual mean near 16.4%.
- **yield_curve_10y_2y** uses the year-end daily observation of T10Y2Y (constant-maturity 10y minus 2y). Blank pre-1976 because GS2 / T10Y2Y begin 1976 (2-year constant maturity not published earlier). Inversions visible: year-end 2022 = −0.53, 2023 = −0.35; re-steepened positive by year-end 2024.
- **fed_balance_sheet_pct_gdp** left blank before 2008 per spec (Fed balance sheet was small and passive pre-GFC; WALCL data begins Dec 2002 but is not economically meaningful for this signal until QE). Values: ~15% (2009), ~34% (2020 QE peak), declining to ~22% (2025 QT).
- **recession_flag** NBER peak→trough spans used (year flagged if it contains any recession month):
  1960 (Apr'60–Feb'61), 1961, 1969 (Dec'69–Nov'70), 1970, 1973 (Nov'73–Mar'75), 1974, 1975,
  1980 (Jan–Jul'80), 1981 (Jul'81–Nov'82), 1982, 1990 (Jul'90–Mar'91), 1991,
  2001 (Mar–Nov'01), 2007 (Dec'07–Jun'09), 2008, 2009, 2020 (Feb–Apr'20).

## Validation anchors confirmed
- fed funds 1981 annual avg = 16.38% (Volcker era; monthly peak ~19%). ✓
- fed funds 2009 = 0.16%, 2021 = 0.08% (ZIRP). ✓  2023 = 5.02%, 2024 = 5.14% (5.25–5.5% target). ✓
- CPI 1980 = 13.50%, 2022 = 7.99% (annual-avg basis). ✓
- unemployment 1982 = 9.71%, 2009 = 9.28% (annual avg of ~10.8%/10.0% peaks); 2019 = 3.68%, 2023 = 3.62%. ✓
- balance sheet 2020 = 34.45% of GDP (QE surge). ✓
