# China Macro / Debt Cycle Panel — Source Notes & Structural Diagnosis

**Deliverable:** `../china/china_macro.csv`
**Coverage:** annual 2000–2025 (26 rows, one per year)
**Retrieved:** 2026-07-05
**Primary sources:** IMF (WEO, Article IV), BIS (total credit to the non-financial sector, via FRED mirror), World Bank (WDI), China NBS (real-estate development investment). Rhodium/academic and IMF Article IV used for LGFV/augmented-debt commentary.

China is the state-directed "great-catch-up" model now confronting a **debt + property + demographic** overhang. This panel is built to document that turn: the debt-fuelled-investment engine hitting diminishing returns, the property bust from 2021, and the demographic reversal after the 2021–22 population peak.

---

## Column-by-column

| Column | Source | Series / basis | Coverage | Flag |
|---|---|---|---|---|
| `gdp_growth` | World Bank WDI | NY.GDP.MKTP.KD.ZG — official real GDP growth % (rounded 1dp) | 2000–2025 | [SOURCED] |
| `cpi_inflation` | World Bank WDI | FP.CPI.TOTL.ZG — annual-average CPI % change | 2000–2025 | [SOURCED] |
| `total_nonfinancial_debt_pct_gdp` | BIS (FRED QCNCAM770A) | Total credit to non-financial sector, market value, % GDP, adj. for breaks | 2000–2025 | [SOURCED] |
| `govt_debt_pct_gdp` | IMF WEO | GGXWDG_NGDP — general government gross debt, % GDP (explicit). **LGFV-augmented figures documented separately below.** | 2000–2025 | [SOURCED] |
| `household_debt_pct_gdp` | BIS (FRED QCNHAM770A) | Credit to households, % GDP | 2006–2025 | [SOURCED] |
| `corporate_debt_pct_gdp` | BIS (FRED QCNNAM770A) | Credit to non-financial corporations, market value, % GDP | 2006–2025 | [SOURCED] |
| `investment_pct_gdp` | World Bank WDI | NE.GDI.TOTL.ZS — gross capital formation, % GDP | 2000–2024 | [SOURCED] |
| `savings_pct_gdp` | World Bank WDI | NY.GNS.ICTR.ZS — gross national savings, % GDP | 2000–2024 | [SOURCED] |
| `property_investment_pct_gdp` | NBS ÷ World Bank | NBS real-estate development investment ÷ nominal GDP (yuan) × 100 | 2000–2025 | [SOURCED] 2023–25; [ESTIMATED] 2000–22 |
| `working_age_pop_pct` | World Bank WDI | SP.POP.1564.TO.ZS — population aged 15–64, % of total | 2000–2025 | [SOURCED] |
| `fertility_rate` | World Bank WDI | SP.DYN.TFRT.IN — total fertility rate (births/woman) | 2000–2024 | [SOURCED] |

Blank cells: household/corporate debt 2000–2005 (BIS series begin 2006 — left blank, unsourceable at this granularity; household debt was ~5–8% of GDP, corporate the balance). Investment/savings/fertility 2025 blank (WDI not yet posted).

## Series identifiers
- BIS via FRED CSV endpoint `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<ID>`: QCNCAM770A (total), QCNPAM770A (private), QCNHAM770A (households), QCNNAM770A (non-fin corporates), QCNGAN770A (general govt, cross-check). Original: BIS Data Portal, topic TOTAL_CREDIT (WS_TC), https://data.bis.org/topics/TOTAL_CREDIT.
- World Bank API `https://api.worldbank.org/v2/country/CHN/indicator/<CODE>`.
- IMF WEO DataMapper `https://www.imf.org/external/datamapper/api/v1/GGXWDG_NGDP/CHN`.
- NBS real-estate development investment: NBS English press releases (2023: 11,091.3bn yuan; 2025: 8,278.8bn yuan, −17.2% y/y → 2024 ≈ 9,999bn), https://www.stats.gov.cn/english/PressRelease/.

## Transform / consistency notes
- **BIS additivity checks out:** total (C) = households (H) + non-fin corporates (N) + general government (G). 2024: 60.0 + 137.9 + 90.4 ≈ 288.4. ✓ The BIS general-government series (90.5, 2024) matches IMF WEO explicit general govt debt (90.4). ✓
- **2025 debt values are the latest 2025 quarter (Q1), not year-end** — total 300.1, household 58.0, corporate 142.8, govt 99.2. Flagged current-year partial.
- **CPI is annual-average** (WDI). 2023 = 0.24%, 2024 = 0.22%, 2025 ≈ 0.06% — i.e. **CPI near zero for three straight years; borderline deflation** (GDP deflator went outright negative 2023–24).
- **gdp_growth is the OFFICIAL real series.** Widely regarded as smoothed/overstated for the 2020s: independent estimates (e.g. Fed FEDS Note "Is China Really Growing at 5 Percent?", Rhodium) put true 2023–24 growth 1–3pp below the ~5% official prints. The CSV keeps the official figure and flags the caveat here.
- **property_investment_pct_gdp** = NBS real-estate *development investment* ÷ nominal GDP. This is the narrow, hard-data measure; it peaks at ~14.5% (2013–14) and falls to ~5.9% (2025). It is NOT the broad "real estate ~25% of GDP" figure — see below.

## LGFV / augmented ("hidden") government debt — [ESTIMATED]
The `govt_debt_pct_gdp` column is the **explicit** general-government measure. Off-balance-sheet **local-government financing vehicle (LGFV)** borrowing and other quasi-fiscal funds are excluded. The IMF's **augmented general government debt** concept adds these:

| Year | Explicit (CSV) | IMF augmented (incl. LGFV) |
|---|---|---|
| 2019 | 59.8 | ~86 [SOURCED, IMF] |
| 2020 | 70.1 | ~98 [ESTIMATED] |
| 2021 | 72.1 | ~105 [ESTIMATED] |
| 2022 | 77.3 | ~110 [ESTIMATED] |
| 2023 | 84.1 | ~116 [SOURCED, IMF 2024 AIV] |
| 2024 | 90.4 | ~124 [SOURCED, IMF 2024 AIV] |
| 2025 | 99.2 | ~130+ [ESTIMATED] |

IMF 2024 Article IV: augmented debt rose from 86.3% (2019) to ~124% (2024) and, on baseline, **stabilises only around 150–155% of GDP**. LGFV liabilities alone are estimated at ~48–70% of GDP (Rhodium/IMF ranges). Source: IMF People's Republic of China 2024 Article IV (Country Report 24/258); East Asia Forum "China's debt reckoning" (2025).

## Validation anchors confirmed
- Total non-financial debt ~288% GDP (2024), ~300% (2025 Q1) — matches BIS ~280–300% anchor. ✓
- Growth arc: 10%+ (2000s, peak 14.2% in 2007) → 6–7% (2010s) → ~5% official (2020s). ✓
- Fertility 1.03 (2022), 1.00 (2023) — among the world's lowest. ✓
- Working-age share peaked 72.9% (2010) → 69.1% (2023). ✓ Total population peaked ~1,412mn in 2021–22 (NBS: first decline in 2022 since 1961), now shrinking. ✓
- Property investment 14.5% GDP peak (2014) → 5.9% (2025); real-estate development investment −9.6% (2023), −17.2% (2025). ✓
- GNI/capita (Atlas): $13,750 (2023), $13,660 (2024) — at the upper-middle/high-income boundary, just **below** the ~$14,005 high-income threshold; **not yet reclassified**. ✓

---

# STRUCTURAL DIAGNOSIS

## 1. The state-directed, investment/savings-led model
China's catch-up ran on a **high-savings, high-investment** engine unlike any of the other poles: gross national savings ~45–51% of GDP (2004–2010) funding gross capital formation ~42–46%. The surplus of savings over investment financed a vast current-account surplus and reserve accumulation. The mechanics that made this possible:
- **Financial repression** — deposit rates capped below nominal growth, channeling household savings cheaply to state banks and thence to SOEs and infrastructure.
- **Capital controls** — a closed capital account keeps that captive savings pool at home; the renminbi is managed, not floated.
- **SOE / industrial policy** — state banks lend to state firms and strategic sectors; investment is directed, not purely price-allocated.
- **Local-government land-finance** — local governments, barred from broad taxation and running unfunded mandates, monetised land: sell land-use rights to developers, book the proceeds, and borrow against future land values through **LGFVs** to build infrastructure. Property and local-government finance became two ends of the same machine.

This model delivered the fastest sustained catch-up in history (GDP/capita doubling ~2005→2013) but is **capital-deepening with falling marginal product**: each yuan of new credit buys less growth. The economy's total non-financial debt climbed from ~127% of GDP (2000) to ~288% (2024) — the leverage *is* the growth model, not (as in Japan post-1990) a consequence of stagnation.

## 2. The overhang / the reckoning
- **Property bust (from 2021).** Real estate — ~25% of GDP once upstream/downstream linkages, construction, local-government land revenue and housing wealth effects are counted (Rhodium, Rogoff-Yang) — turned from tailwind to drag. Evergrande defaulted Dec-2021; developer credit seized; NBS real-estate development investment fell −10% (2022), −9.6% (2023), and −17.2% (2025). New-home prices are down high-single-digits officially, but secondary/existing prices in major cities are off ~15–30% from 2021 peaks. The narrow property-investment ratio has halved from ~14.5% to ~6% of GDP.
- **LGFV hidden debt.** The land-finance model runs in reverse: falling land sales gut the collateral and the revenue that serviced LGFV borrowing. Explicit government debt (~90% of GDP, 2024) understates the true fiscal position; **IMF-augmented debt is ~124% and rising toward ~150–155%**.
- **Corporate/SOE leverage.** Non-financial corporate debt ~138% of GDP (2024) is among the highest in the world; much of it sits on SOEs and property developers.
- **Diminishing returns + deflation risk.** With credit intensity rising and returns falling, the marginal stimulus fades. **CPI has been near zero 2023–25 and the GDP deflator turned negative** — a demand shortfall / balance-sheet-repair signature, not a supply boom.

## 3. Demographics — "grow old before rich?"
The demographic dividend that powered the catch-up has reversed:
- **Population peaked ~2021–22** (~1,412mn) and is now shrinking — the first sustained decline since the early-1960s famine.
- **Working-age share (15–64)** peaked at 72.9% (2010) and has fallen to ~69% and declining; the *absolute* working-age population is contracting.
- **Fertility ~1.0** (2023) — collapsed from ~1.6–1.8 through the 2010s (the one-child legacy, then economic/housing costs); among the lowest on earth, well below the ~2.1 replacement rate and below even Japan.
- **Rapid aging** with a still-thin pension/health safety net. The classic worry: China may **grow old before it grows rich** — GNI/capita (~$13.7k) is right at the high-income line, so it is aging at a *lower* income level than the advanced economies did.

## 4. The Japan parallel — "Japanification" at lower income
China in the 2020s rhymes with Japan post-1990: **high debt + property/asset bust + aging + deflation** → the risk of a **balance-sheet recession** (households and firms deleveraging, paying down debt rather than spending/investing, blunting monetary policy). Key differences:
- **Lower per-capita income.** Japan hit its bubble at frontier high-income (~$40k+ in today's terms); China faces the same syndrome at ~$13–14k — the unresolved **middle-income-to-high-income transition** question. Stagnation now would strand China *below* the frontier.
- **Earlier in the cycle / more state control.** China's banks, developers and local governments are largely state-controlled, giving Beijing tools Japan's fragmented private sector lacked — but also concentrating the losses on the state balance sheet.
- **Same core dynamic:** debt built for growth, now a drag; demand deficient; prices flat-to-falling; a slow, drawn-out workout rather than a sharp crisis.

## 5. Policy space — how China differs from the other poles
China faces **structural growth-model exhaustion** the other poles do not — but has more room to manage a *slow* workout:
- **Own currency + capital controls + state-owned banking system** → it can roll over, forbear, and socialise bad debt (LGFV swaps into local-government bonds, directed lending) without a market-forced reckoning. A closed capital account means no sudden-stop / capital-flight channel.
- **~$3.2trn FX reserves + net external creditor** → no external-debt or FX crisis of the kind that constrains **Nigeria** (Nigeria's bind is *external*/FX and hard-currency debt-service, at low income and low debt/GDP — the opposite problem: too little productive credit, not too much).
- **Unlike the US**, China's debt is overwhelmingly domestic and renminbi-denominated, but it lacks the dollar's exorbitant privilege and deep, open capital markets; its problem is a *domestic* demand/property/demographic overhang, not fiscal-external financing.
- **Unlike the euro area**, China has full monetary-fiscal sovereignty and a unitary state — no single-currency straitjacket, no redenomination risk — but its banks and localities carry the property/LGFV losses that Europe's fragmented sovereigns would have to socialise explicitly.

**Bottom line:** China has the policy space (sovereign currency, capital controls, state banks, huge reserves) to avoid an acute crisis and stretch the adjustment over years — but no obvious escape from the *structural* trilemma of debt saturation, a deflating property sector, and a shrinking, aging workforce. The open question is whether it completes the middle-to-high-income transition before demographics and diminishing returns freeze it in place — the reason "grow old before rich" and "Japanification at lower income" are the two framing risks.
