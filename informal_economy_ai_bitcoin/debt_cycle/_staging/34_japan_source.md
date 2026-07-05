# Japan Macro / Debt-Cycle Panel — Source Notes & Structural Diagnosis

**Deliverable:** `../japan/japan_macro.csv`
**Coverage:** annual 1980–2025 (46 rows, one per year)
**Retrieved:** 2026-07-05
**Primary sources:** IMF (WEO April-2026 vintage, via DataMapper API), Bank of Japan (BoJ — policy-rate history, balance-sheet assets via FRED mirror), Japan Ministry of Finance (MOF — historical JGB yields), World Bank WDI (demographics, fertility), OECD/FRED (10-year JGB yield).

Japan is **the PRECEDENT** — the 1990 bubble burst and the "lost decades" balance-sheet recession that every other pole (US, Europe, China) is now measured against. This panel documents the full arc: the late-1980s asset/credit bubble, the burst, the deflationary balance-sheet recession, the world-first policy experiments (ZIRP → QE → QQE → NIRP → YCC → exit), the demographic drag, and the 2022–24 return of inflation with the BoJ's historic normalisation.

---

## Column-by-column

| Column | Source | Series / basis | Coverage | Flag |
|---|---|---|---|---|
| `gdp_growth` | IMF WEO | NGDP_RPCH — real GDP growth, annual % | 1980–2025 | [SOURCED] |
| `cpi_inflation` | IMF WEO | PCPIPCH — avg consumer prices, annual % change | 1980–2025 | [SOURCED] |
| `unemployment` | IMF WEO | LUR — unemployment rate, % of labour force | 1980–2025 | [SOURCED] |
| `govt_debt_gross_pct_gdp` | IMF WEO | GGXWDG_NGDP — general govt GROSS debt, % GDP (**April-2026 vintage — see revision note**) | 1980–2025 | [SOURCED] |
| `govt_debt_net_pct_gdp` | IMF WEO | GGXWDN_G01_GDP_PT — general govt NET debt, % GDP | 1990–2025 | [SOURCED] |
| `policy_rate` | BoJ | End-of-year policy rate: Official Discount Rate 1980–94; uncollateralised overnight call-rate target 1998/99–2025 | 1980–2025 | [SOURCED] |
| `boj_balance_sheet_pct_gdp` | BoJ ÷ Cabinet Office | BoJ total assets (year-end Dec) ÷ nominal GDP (annual avg, yen) × 100 | 1998–2025 | [SOURCED] |
| `jgb_10y_yield` | MOF / OECD-FRED | 10-year JGB yield, annual avg. 1980–85 = 7-yr JGB (pre-1986 benchmark long bond, proxy) | 1980–2025 | [SOURCED] 1986–2025; [ESTIMATED] 1980–85 |
| `working_age_pop_pct` | World Bank WDI | SP.POP.1564.TO.ZS — population aged 15–64, % of total | 1980–2024 | [SOURCED] |
| `fertility_rate` | World Bank WDI | SP.DYN.TFRT.IN — total fertility rate (births/woman) | 1980–2024 | [SOURCED] |

**Blank cells:** net debt 1980–89 (IMF WEO net-debt series begins 1990); BoJ balance sheet 1980–97 (FRED JPNASSETS begins 1998-04; pre-QE the BoJ balance sheet was small, ~10% of GDP); working-age share & fertility 2025 (WDI not yet posted).

## Series identifiers / endpoints
- IMF WEO DataMapper: `https://www.imf.org/external/datamapper/api/v1/<CODE>/JPN` — codes NGDP_RPCH, PCPIPCH, LUR, GGXWDG_NGDP, GGXWDN_G01_GDP_PT.
- BoJ policy-rate history: BoJ "Monetary Policy Measures" / Official Discount Rate archive; cross-checked to BoJ press releases and BIS Paper No. 31.
- BoJ balance sheet: FRED `JPNASSETS` (Central Bank Assets for Japan, 100-mn-yen), year-end December value.
- Nominal GDP (yen, denominator for BoJ ratio): FRED `JPNNGDP` (Cabinet Office SNA, bn yen, SAAR), annual average of 4 quarters.
- JGB 10-year yield: MOF historical CSV `https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/historical/jgbcme_all.csv` (daily from 1974; 10Y column populated from 1986); OECD via FRED `IRLTLT01JPM156N` (monthly from 1989, annual averages computed). MOF 1989 = 5.15 ≈ FRED 5.13 (cross-check ✓).
- Demographics/fertility: World Bank API `https://api.worldbank.org/v2/country/JPN/indicator/<CODE>`.

## Transform / consistency notes
- **policy_rate is end-of-year, and the operative instrument changed.** 1980–94 values are the **Official Discount Rate** (the BoJ's policy tool in that era); from the mid-1990s the **uncollateralised overnight call rate** became the target. 1999 (ZIRP) shown as 0.02 (guided "as low as possible", effectively ~0); 2001–05 (QE) shown as 0.0 (call rate ~0.001); 2016–23 shown as −0.10 (NIRP applied to marginal reserves). This is a spliced "policy stance" series, not one continuous instrument — see the policy timeline below.
- **jgb_10y_yield 1980–85 uses the 7-year JGB** (MOF), because a continuous 10-year benchmark yield only begins in the MOF series in 1986; the 7-year was the benchmark long bond then. Flagged [ESTIMATED]. 1986–88 are MOF 10Y; 1989–2025 are OECD/FRED 10Y annual averages.
- **boj_balance_sheet_pct_gdp** = year-end assets ÷ annual-average nominal GDP. Peak ≈ 127% (2020); falls to ~102% (2025) as normalisation/QT and higher nominal GDP shrink the ratio. Using a lower (year-start) GDP denominator or peak-quarter assets yields the ~130–135% figures sometimes quoted; method here is consistent and conservative.
- **cpi_inflation is IMF annual-average CPI.** Note the deflation signature: negative or ~zero in **1995, 1999–2003, 2005, 2009–12, 2016** — i.e. mild deflation/near-zero across most of 1995–2020 — then a regime break to **2.5 (2022), 3.3 (2023), 2.7 (2024), 3.2 (2025)**, the first sustained inflation in a generation.

## ⚠️ IMPORTANT — the gross-debt figure and the 2025–26 IMF revision
The `govt_debt_gross_pct_gdp` column uses the **current (April-2026) IMF WEO vintage**, which puts Japan's general-government gross debt at **214.5% (2024)**, peaking **228.8% (2020, COVID)**. This is materially LOWER than the "**~250–260%**" figure widely cited (and named in the task anchor). The gap is real and vintage-driven:

| Year | Current IMF WEO (CSV) | Older IMF vintage (FRED GGGDTAJPA188N) |
|---|---|---|
| 2019 | 206.3 | 236.4 |
| 2020 | 228.8 | **258.4** |
| 2021 | 222.7 | 253.7 |
| 2022 | 227.8 | 248.3 |
| 2023 | 220.3 | 240.0 |

The older IMF vintage (and OECD "general government gross financial liabilities") shows the classic **~250%+**, the highest in the developed world. The IMF's recent vintages carry a **persistent ≈ 25–30pp downward level shift across all years** (visible even in 2012: 197 vs 226), consistent with a statistical/consolidation revision plus the mechanical effect of the 2022–24 inflation lifting **nominal** GDP (the denominator). **Both are IMF numbers.** For cross-pole comparison with the "highest-debt-in-the-developed-world / ~250%" narrative, the older-vintage / OECD ≈ 250–260% figure is the canonical headline; the CSV keeps the latest official IMF series and documents the older one here. Net debt (~140–160%) is far lower than gross because the Japanese government holds enormous financial assets (FX reserves, the Government Pension Investment Fund GPIF, social-security fund JGB holdings) — the gross/net gap is itself part of the "why no crisis" story.

## Validation anchors confirmed
- **Nikkei** peaked ~38,900 (29-Dec-1989) then collapsed (halved within ~10 months) — the bubble top coincides with policy tightening. ✓ (contextual; not a CSV column)
- **Growth arc:** ~4–5% (1980s, incl. 6.7% in 1988) → ~1% and two recessions (1990s: −0.5% 1993, −1.8% 1998) → near-zero/volatile (2000s–2020s). ✓
- **Deflation:** CPI negative/near-zero across most of 1995–2020; regime break to 2.5–3.3% in 2022–25. ✓
- **Policy path:** ODR 2.5% (1987–88, the bubble-fuel low) → 6.0% (1990, the burst) → ZIRP 1999 → QE 2001 → QQE 2013 → NIRP −0.1% 2016 → **exit March-2024** (first hike since 2007; ended NIRP & YCC) → 0.25% (2024) → 0.75% (Dec-2025). ✓
- **JGB 10Y:** 6.96% (1990) → sub-2% from 1998 → **negative in 2016 & 2019** (YCC/NIRP) → back to 0.9% (2024), 1.55% (2025) as the BoJ exits. ✓ World's lowest long yields alongside the world's highest debt.
- **BoJ balance sheet** ~127% of GDP (2020) — the **largest among major central banks** (vs Fed ~35%, ECB ~50% at their peaks). ✓
- **Demographics:** working-age (15–64) share peaked ~70.0% (1991–93) → 58.8% (2024); total population **peaked ~2008** (~128mn) and is shrinking; **fertility** 1.57 ("1.57 shock", 1989) → 1.26 (2005) → **1.20 (2023), 1.15 (2024)** — repeated record lows; median age ~49, the world's oldest. ✓

---

# STRUCTURAL DIAGNOSIS

## 1. The bubble & the burst (1985–1991)
After the 1985 **Plaza Accord** drove the yen sharply higher, the BoJ eased aggressively to offset the export drag — cutting the Official Discount Rate from 5.0% to **2.5% by Feb-1987** and holding it there for over two years despite a booming economy. Ultra-cheap credit poured into **equities and urban land**: the Nikkei quadrupled to ~38,900 (Dec-1989) and Tokyo land values reached levels at which the Imperial Palace grounds were, notionally, worth more than California. It was a classic **asset + credit bubble**, banks lending against ever-rising land collateral. The BoJ reversed hard — ODR to **4.25% (end-1989)** then **6.0% (Aug-1990)** — and the MOF imposed lending limits on real estate. The Nikkei peaked on 29-Dec-1989 and **halved within ten months**; land followed with a lag. The bubble burst in **1990–91**.

## 2. The balance-sheet recession (Richard Koo)
The burst left corporations and banks holding assets worth a fraction of the debt raised to buy them — **negative net worth on a mark-to-market basis**. Koo's insight: firms shifted from **profit-maximising to debt-minimising**. Even as the BoJ drove rates to zero, the private sector kept **paying down debt rather than borrowing and investing** — a *liquidity trap* in which monetary policy pushes on a string. Corporate demand for credit went negative for years; the household saving rate stayed high. With private demand structurally deficient, the economy tipped into **mild but persistent deflation** (CPI ≈ 0 or negative across most of 1995–2020), which raised **real** debt burdens and real rates, deepening the trap. **Fiscal deficits filled the demand gap** — every attempt at premature consolidation (notably the 1997 consumption-tax hike) tipped Japan back into recession. The mechanical result: private de-leveraging was offset by **public re-leveraging**, and gross government debt climbed from ~55% of GDP (1990) to ~200%+ (2010s). The debt is a *consequence* of the balance-sheet recession, not (as in China) the growth engine itself.

## 3. The policy timeline — the playbook everyone later copied
Japan ran, first and in sequence, nearly every tool the Fed and ECB deployed after 2008:
- **ZIRP (Feb-1999)** — overnight call rate to ~0; the first zero-rate regime in a major economy.
- **QE (Mar-2001–2006)** — the first "quantitative easing", targeting the level of current-account (reserve) balances.
- **Abenomics / QQE (Apr-2013)** — "Quantitative and Qualitative Easing" under Governor Kuroda: a 2% inflation target, mass JGB and ETF purchases; the BoJ balance sheet went from ~31% to ~100%+ of GDP.
- **NIRP (Jan-2016)** — −0.10% on marginal reserves, and **Yield-Curve Control (Sep-2016)** — pinning the 10-year JGB near 0%, a tool no other major central bank had tried.
- **The exit (Mar-2024)** — the **first rate hike since 2007**, ending NIRP and YCC together; further hikes to 0.25% (Jul-2024), 0.50% (Jan-2025) and **0.75% (Dec-2025, a 30-year high)** as 2% inflation looked durable and Shuntō wage growth ran ~5%.
Japan proved these tools *work mechanically* (yields can be pinned, balance sheets can dwarf GDP) but also revealed their limits: two decades of ZIRP/QE did **not** by themselves defeat deflation — it took a global supply-shock + wage dynamic in 2022–24.

## 4. Demographics — the structural drag ("Japanification")
Japan is the demographic frontier: **fertility** fell below replacement in the mid-1970s and has never recovered (1.57 "shock" in 1989; ~1.2 today), the **working-age share peaked ~1991–93 (~70%)** and total **population peaked ~2008** and is now shrinking ~0.5%/yr. A falling workforce lowers trend growth and the natural rate of interest, while an aging population saves heavily and spends cautiously — reinforcing weak demand and low inflation. "**Japanification**" has become shorthand for the syndrome now stalking Europe and China: **high public debt + deflation/low-inflation + aging + zero/low rates**, all self-reinforcing.

## 5. Why 250% debt/GDP never became a crisis
The decisive lesson for the US, Europe and China is that **the debt ratio matters less than who owns the debt and in what currency**:
- **Domestic ownership.** ~90%+ of JGBs are held domestically — by Japanese banks, insurers, pension funds, the postal system, and the **BoJ itself** (which now holds roughly half of all JGBs outstanding). There is no foreign-creditor "sudden stop" channel.
- **Own currency, own central bank.** Debt is 100% **yen-denominated** and Japan issues its own currency; the BoJ can and does backstop the JGB market (YCC literally *set* the price). Default risk is nominal-zero.
- **High domestic savings.** Decades of household and corporate surpluses provide a captive pool that funds the deficits at home.
- **Net external CREDITOR.** Japan runs one of the world's largest positive **Net International Investment Positions** (net foreign assets ≈ 70–80% of GDP) — the nation as a whole is a *lender* to the world, not a borrower. Add ~US$1.2trn of FX reserves and the large government financial assets that make **net** debt (~140%) far below **gross**.
Together these let **the world's highest gross debt coexist with the world's lowest bond yields** for two decades — the exact opposite of an emerging-market debt crisis. The risk was never solvency; it was the *slow* cost — a generation of lost growth, and a debt stock so large that even the BoJ's 2024–25 exit must be glacial to avoid a JGB-market and fiscal-cost shock. **The lesson for the other poles:** the US (reserve currency, but rising foreign-held debt), Europe (a shared currency without a shared treasury — the vulnerable case), and China (high debt but domestic/closed-capital-account, the most Japan-like) are each measured against Japan's demonstration that a domestically-owned, own-currency, creditor-nation debt is survivable — and that the price of surviving it is the lost decades themselves.
