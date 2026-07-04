# USA "Big Debt Cycle" Gauges — Source Notes (Ray Dalio framework)

**Deliverable:** `../usa/usa_debt_cycle_gauges.csv`
**Coverage:** annual 1960–2025 (66 rows, one per year). Some columns start later (see below).
**Retrieved:** 2026-07-04
**Framework:** Ray Dalio, *Principles for Navigating Big Debt Crises* (2018) and *How Countries Go Broke: The Big Cycle* (2025). This dataset diagnoses the US as the **leading reserve-currency power in the late stage of its long-term (≈75–100yr) debt cycle**.
**Primary sources:** FRED (Federal Reserve Bank of St. Louis machine-readable CSV, `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>`); US Treasury TIC; IMF COFER; BEA International Investment Position; CBO Budget & Economic Outlook.

---

## Column-by-column construction

| Column | Source series / basis | Transform | Coverage | Flag |
|---|---|---|---|---|
| `federal_debt_held_by_public_pct_gdp` | FRED **FYPUGDA188S** (Federal Debt Held by the Public as % of GDP, annual, fiscal year) | used directly | 1960–2025 | [SOURCED] |
| `fiscal_deficit_pct_gdp` | FRED **FYFSGDA188S** (Federal Surplus/Deficit as % of GDP, annual). Negative = deficit | used directly | 1960–2025 | [SOURCED] |
| `net_interest_pct_gdp` | FRED **A091RC1Q027SBEA** (federal net interest, NIPA, $bn SAAR, quarterly) ÷ **GDPA** (nominal annual GDP, $bn) | quarterly → annual mean, then /GDP ×100 | 1960–2025 | [SOURCED] |
| `net_interest_pct_revenue` | A091RC1Q027SBEA ÷ FRED **FGRECPT** (Federal current tax receipts, NIPA, $bn) | both quarterly → annual mean, ratio ×100 | 1960–2025 | [SOURCED] |
| `fed_balance_sheet_pct_gdp` | FRED **WALCL** (Fed total assets, $mn, weekly) ÷ GDPA | year-end WALCL (mn→bn) ÷ annual GDP ×100 | 2008–2025; blank before | [SOURCED] |
| `foreign_held_treasury_pct` | FRED **FDHBFIN** (Federal Debt Held by Foreign & Intl Investors, $bn) ÷ **GFDEBTN** (Total Public Debt, gross, $mn) | year-end, foreign / gross total debt ×100 | 1970–2025 | [SOURCED] |
| `usd_share_global_reserves_pct` | **IMF COFER**, allocated reserves, USD share, year-end (Q4) | tabulated (see below) | 1999–2025 | [SOURCED] |
| `niip_pct_gdp` | BEA via FRED **IIPUSNETIA** (US Net International Investment Position, annual, $mn) ÷ GDPA | (mn→bn)/GDP ×100 | 1976–2025 | [SOURCED] |
| `10y_real_yield_pct` | FRED **DFII10** (10-Year TIPS constant-maturity yield, daily, %) | annual mean | 2003–2025; blank before | [SOURCED] |

### FRED series URLs
- FYPUGDA188S: https://fred.stlouisfed.org/series/FYPUGDA188S  (debt held by public, % GDP)
- FYFSGDA188S: https://fred.stlouisfed.org/series/FYFSGDA188S  (deficit, % GDP)
- A091RC1Q027SBEA: https://fred.stlouisfed.org/series/A091RC1Q027SBEA  (federal net interest, NIPA)
- GDPA / GDP: https://fred.stlouisfed.org/series/GDPA
- FGRECPT: https://fred.stlouisfed.org/series/FGRECPT  (federal current receipts)
- WALCL: https://fred.stlouisfed.org/series/WALCL  (Fed total assets)
- FDHBFIN: https://fred.stlouisfed.org/series/FDHBFIN  (foreign-held federal debt)
- GFDEBTN: https://fred.stlouisfed.org/series/GFDEBTN  (total public debt, gross)
- IIPUSNETIA: https://fred.stlouisfed.org/series/IIPUSNETIA  (net IIP)
- DFII10: https://fred.stlouisfed.org/series/DFII10  (10y TIPS)
- IMF COFER: https://data.imf.org/en/datasets/IMF.STA:COFER
- US Treasury TIC (Major Foreign Holders): https://home.treasury.gov/data/treasury-international-capital-tic-system
- CBO Budget & Economic Outlook 2025–2035: https://www.cbo.gov/publication/61172

---

## Important definitional notes (read before using)

1. **Held-by-public vs gross debt.** The task originally pointed at FRED `GFDEGDQ188S`, but that series is **gross total public debt** (~120–122% of GDP in 2025), NOT held-by-public. The key Dalio debt gauge is debt **held by the public** (net of intragovernmental holdings), so this column uses **FYPUGDA188S** = 96.2% (2024), 98.1% (2025). Gross debt for reference: ~120–123% of GDP (GFDEGDQ188S / GFDEBTN÷GDP). Both are captured in the discrete facts below.

2. **`net_interest_pct_revenue` basis.** Computed on a consistent **NIPA** basis (A091RC1 net interest ÷ FGRECPT current receipts) so it matches the numerator of `net_interest_pct_gdp`. This gives **21.6% (2024)**. The **budget/fiscal-year (CBO/OMB) basis** — net interest ÷ total federal revenues — is somewhat lower because NIPA net interest exceeds budget "net interest": CBO net interest FY2024 = **$882bn**, revenues = **$4.92tn** → **≈18%**. Both are elevated and rising; use the CBO 18% figure if you need the budget-basis cash-flow-squeeze number, the 21.6% if you want NIPA consistency across the two interest columns. [SOURCED both bases]

3. **`foreign_held_treasury_pct` denominator.** Expressed as foreign holdings ÷ **gross total public debt outstanding** (FDHBFIN/GFDEBTN). This reproduces the widely-cited trajectory: **peak ≈34% in 2012–2014, ≈32% in 2015, falling to ≈24% by 2024–25**. Note the same numerator on different denominators: as % of debt **held by the public** ≈30% (2025); as % of **marketable** Treasuries ≈33% (TIC June 2024). The decline reflects both faster growth of total US debt and reduced foreign appetite (esp. official-sector; official share of foreign holdings fell from 59%→47%, 2020→2024, per Treasury TIC).

4. **COFER discontinuity.** IMF COFER allocated-USD-share year-end values (used in the CSV): 1999–2013 sit ~62–71%; the jump to ~65% in 2014 partly reflects expanded reporting (China began reporting). Anchors verified: 2000 ≈71.1%, 2015 ≈65.7%, 2020 =58.9%, 2023 =58.4%, 2024 =57.8%, 2025Q3 ≈56.9%. In 2025Q3 the IMF revised COFER back to 2000Q1 to eliminate the "unallocated" bucket. [SOURCED — IMF COFER via IMF/Fed publications]

5. **NIIP.** IIPUSNETIA is the year-end BEA net IIP. Values were **positive** (US net creditor) through ~1988, crossed negative in ~1989, and have deepened to **−75.5% of GDP (2024)**, improving slightly to −71% (2025) on foreign equity/valuation gains. This is one of the most negative NIIPs of any large economy — the flip side of the reserve-currency privilege (the world funds the US).

---

## Validation anchors confirmed

| Year | debt/GDP (pub) | deficit/GDP | net int/GDP | net int/rev (NIPA) | Fed BS/GDP | foreign share | USD reserve % | NIIP/GDP | 10y real |
|---|---|---|---|---|---|---|---|---|---|
| 1980 | 24.9 | −2.6 | 3.8 | 20.2 | — | 13.9 | — | +10.4 | — |
| 2000 | 33.3 | +2.3 | 3.5 | 17.1 | — | 17.9 | 71.1 | −15.0 | — |
| 2008 | 39.3 | −3.1 | 2.6 | 15.0 | 15.2 | 28.8 | 63.8 | −27.1 | 1.77 |
| 2015 | 71.7 | −2.4 | 2.4 | 12.5 | 24.5 | 32.5 | 65.7 | −41.5 | 0.45 |
| 2020 | 98.3 | −14.5 | 2.4 | 13.8 | 34.5 | 25.5 | 58.9 | −55.7 | −0.60 |
| 2024 | 96.2 | −6.2 | 3.8 | 21.6 | 23.5 | 23.8 | 57.8 | −75.5 | 1.94 |
| 2025 | 98.1 | −5.8 | 3.9 | 20.9 | 21.6 | 24.1 | 56.9 | −71.1 | 1.96 |

Cross-checks: deficit 2020 = −14.5% (COVID) ✓; Fed BS 2020 = 34.5% (QE peak) → 21.6% (2025 QT) ✓; foreign peak ~34% 2012–14 ✓; COFER 2023 = 58.4% matching IMF (58.42%) ✓; NIIP 2024 = −75.5% ✓.

---

## DISCRETE FACTS (with sources)

- **Debt held by the public ≈98% of GDP (2025), ~96% (2024); heading to ~100%.** Gross federal debt ≈**120–123% of GDP** (~$36–39tn). [SOURCED — FRED FYPUGDA188S; GFDEBTN/GDP]
- **Net interest outlays overtook defense spending in FY2024 — the first time.** CBO/Treasury: net interest ≈**$882bn** (gross interest ≈$950bn) vs defense ≈$826–874bn in FY2024; interest also exceeds Medicare. **Interest is now the fastest-growing major outlay** (up ~34% y/y in FY2024) and CBO projects interest costs exceed defense every year 2025–2035. [SOURCED — CBO; House Budget Committee; Forbes/Fox 2024]
  - Source: https://budget.house.gov/press-release/interest-costs-surpass-national-defense-and-medicare-spending
- **CBO Budget & Economic Outlook 2025–2035 (Jan 2025):** debt **held by the public rises to ≈118% of GDP by 2035** — a record, surpassing the previous WWII-era peak of 106% (1946); driven by structural primary deficits (~6% of GDP) plus compounding interest. Long-run (2055) path ≈156%. [SOURCED — CBO pub. 61172] https://www.cbo.gov/publication/61172
- **Dollar's declining reserve share:** IMF COFER USD share ≈**72% (2001 peak) → 58% (2024) → ~57% (2025Q3)** — a ~14pp fall over two decades. Losses spread across the euro, the yen, and especially "nontraditional" reserve currencies (AUD, CAD, CNY, KRW) and gold, per the IMF/Fed "gradual diversification, not sudden de-dollarization" reading. This underpins the **"de-dollarization / changing world order"** debate central to Dalio's *Changing World Order*. [SOURCED — IMF COFER; Fed FEDS Note "International Role of the US Dollar 2025"]
- **Foreign ownership of Treasuries has thinned relatively:** from ~34% of total federal debt (2012–15) to ~24% (2024–25), with the **official sector retreating** (its share of foreign holdings fell 59%→47%, 2020→2024). Marketable-basis foreign share ≈33% (TIC 2024). [SOURCED — FRED FDHBFIN/GFDEBTN; Treasury TIC]
- **Real yields have normalized to restrictive territory:** 10y TIPS ≈**+1.9–2.0% (2024–25)** vs **−0.6% (2020)** — the shift from negative to clearly positive real yields sharply raises the cost of rolling a ~100%-of-GDP debt stock (the interest-rate/growth `r–g` dynamic turning adverse). [SOURCED — FRED DFII10]

---

## FRAMING — where the US sits in the Big Debt Cycle (the key point)

Every gauge in this file is consistent with **Dalio's "late stage of the long-term debt cycle for the leading reserve power":** debt held by the public near ~100% of GDP (gross ~120%+), structural deficits ~6% of GDP with no war/recession, net interest now the fastest-growing outlay and past defense, interest absorbing ~18–22% of revenue (the cash-flow-squeeze gauge), a deeply negative NIIP (~−75%), a slowly eroding reserve share (72%→58%), and thinning foreign (esp. official) demand for Treasuries.

**The critical distinction from an emerging market (e.g., Nigeria):** the US **borrows in its own currency, which is also the world's primary reserve asset.** It therefore faces essentially **no external/hard-currency default risk** — it can always print the dollars it owes. Its late-cycle deleveraging risk is instead **inflation and currency debasement plus a slow erosion of the "exorbitant privilege"** (rising term premia, higher real yields, gradual reserve-share and Treasury-demand loss) — i.e., a *monetary/real* adjustment, not a *nominal default*. This is Dalio's core asymmetry: the reserve-currency issuer "goes broke" gradually through the value of its money, not suddenly through inability to pay. The policy end-game tends to be financial repression, negative real returns on cash/bonds, and currency depreciation — which is why the framework pairs this diagnosis with gold, hard assets, and (in the modern debate) Bitcoin as debasement hedges.
