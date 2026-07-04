# USA Economic Scorecard by Presidential Administration — Source Notes

**Deliverable:** `../usa/usa_presidents.csv`
**Coverage:** 13 administrations, Truman (1945) through Trump-2 (in progress, data through mid-2026)
**Retrieved:** 2026-07-04
**Primary sources:** FRED (Federal Reserve Economic Data), Federal Reserve Bank of St. Louis — machine-readable CSV endpoint `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>`. S&P 500 monthly price index from the Robert Shiller dataset (via the `datasets/s-and-p-500` tidy CSV mirror). NBER for business-cycle (recession) dating.

## CRITICAL FRAMING — "on their watch," NOT "what they caused"

This scorecard measures **what the economy did during each president's term of office**, not what each president caused. Read every number as accountability-with-context, not causation:

- **Presidents inherit an economy.** The starting conditions (unemployment, debt, market level, momentum) are set by predecessors and prior shocks, not the incoming president.
- **Policy acts with long, variable lags (~1–2 years).** A term's first year — often its whole first two years — reflects the prior administration's fiscal stance and the Fed's earlier decisions. Fiscal-year budget timing (below) makes the very first year largely a predecessor's budget.
- **The Federal Reserve is independent.** Interest rates, and hence much of the growth/inflation/market path, are set by the Fed, not the White House.
- **Congress controls spending and taxes.** Deficits and debt reflect legislation, which the president signs but does not write alone.
- **Exogenous shocks dominate.** Oil embargoes (1973, 1979), the 2008 Global Financial Crisis, and the 2020 COVID shock swamped whatever policy was in place. Obama's 0 recessions-begun and Trump-1's COVID recession are the clearest examples: the GFC recession *began* in Dec-2007 under G.W. Bush and *ended* under Obama; the COVID recession was a global pandemic, not a policy.

Cross-administration patterns stated later are **on-watch correlations**, not proof of presidential effect.

## Term definitions

Inauguration is Jan-20; each term runs from the president taking office to the successor taking office. A president's consecutive terms are combined; terms are split where the president changed mid-term (Kennedy→Johnson combined as one Democratic run 1961–69; Nixon→Ford combined as one Republican run 1969–77).

| president | party | term_start | term_end | note |
|---|---|---|---|---|
| Truman | D | 1945-04 | 1953-01 | Succeeded FDR **12-Apr-1945** (no Jan inauguration in 1945); watch starts April |
| Eisenhower | R | 1953-01 | 1961-01 | |
| Kennedy/Johnson | D | 1961-01 | 1969-01 | JFK assassinated Nov-1963; LBJ completed |
| Nixon/Ford | R | 1969-01 | 1977-01 | Nixon resigned Aug-1974; Ford completed |
| Carter | D | 1977-01 | 1981-01 | |
| Reagan | R | 1981-01 | 1989-01 | |
| G.H.W. Bush | R | 1989-01 | 1993-01 | |
| Clinton | D | 1993-01 | 2001-01 | |
| G.W. Bush | R | 2001-01 | 2009-01 | |
| Obama | D | 2009-01 | 2017-01 | |
| Trump-1 | R | 2017-01 | 2021-01 | |
| Biden | D | 2021-01 | 2025-01 | |
| Trump-2 | R | 2025-01 | 2026-06 | **In progress** — data through latest available month (see caveats) |

## Column-by-column methodology

| Column | Series / source | Method | Flag |
|---|---|---|---|
| `avg_gdp_growth` | GDPC1 (real GDP, chained, quarterly) | Annualized growth from term-start quarter to term-end quarter: `(GDP_end/GDP_start)^(1/years)−1` ×100 | [SOURCED] |
| `jobs_added_m` | PAYEMS (nonfarm payrolls, thousands, monthly) | `(PAYEMS_end − PAYEMS_start)/1000`, inauguration month vs term-end month | [SOURCED] |
| `unemp_start` / `unemp_end` | UNRATE (%, monthly) | Value at inauguration month vs term-end month | [SOURCED] |
| `avg_inflation` | CPIAUCSL (CPI-U index, monthly) | Annualized: `(CPI_end/CPI_start)^(1/years)−1` ×100 | [SOURCED] |
| `sp500_annual_return` | S&P 500 price index (Shiller monthly avg) | Annualized **price** return: `(P_end/P_start)^(1/years)−1` ×100 | [SOURCED] — see caveat |
| `avg_deficit_pct_gdp` | FYFSGDA188S (federal surplus/deficit % GDP, annual) | Simple mean of annual values for calendar years `start_year … end_year−1`. Negative = deficit | [SOURCED] — see fiscal-year caveat |
| `debt_gdp_change_pts` | GFDEGDQ188S (total public debt % GDP, quarterly) | End-quarter minus start-quarter (points) | [SOURCED]; blank pre-1966 |
| `recessions` | NBER business-cycle peaks | Count of NBER recessions whose **peak (start month) falls within the term** | [SOURCED] |

### Series URLs
- GDPC1 (Real GDP): https://fred.stlouisfed.org/series/GDPC1
- PAYEMS (Nonfarm payrolls): https://fred.stlouisfed.org/series/PAYEMS
- UNRATE (Unemployment rate): https://fred.stlouisfed.org/series/UNRATE
- CPIAUCSL (CPI-U): https://fred.stlouisfed.org/series/CPIAUCSL
- FYFSGDA188S (Federal surplus/deficit % GDP): https://fred.stlouisfed.org/series/FYFSGDA188S
- GFDEGDQ188S (Total public debt % GDP): https://fred.stlouisfed.org/series/GFDEGDQ188S
- S&P 500 (Shiller monthly): https://shillerdata.com/ · tidy mirror https://github.com/datasets/s-and-p-500
- NBER cycle dates: https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions

## Caveats & flags on specific cells

- **S&P 500 is PRICE return, not total return.** Dividends (historically 2–4%/yr) are excluded, so every `sp500_annual_return` understates investor total return by roughly that much. Values are month-average index levels (Shiller convention), so they smooth intramonth swings. G.W. Bush's **−5.28%/yr** spans the dot-com peak (Jan-2001) to the GFC trough (Jan-2009) and is the only negative — a start/end-point artifact as much as anything.
- **Fiscal-year timing (deficit).** `avg_deficit_pct_gdp` averages calendar-labeled fiscal-year values over `start_year…end_year−1`. The U.S. fiscal year runs Oct–Sep (Jul–Jun before FY1977), so a president's *first* labeled year is largely the **predecessor's budget**, and their last budget's deficit lands under the successor. Treat the term average as "deficits recorded on their watch," not "deficits they enacted." Example: Biden's 2021 value (−11.7%) is FY2021, which includes Trump-era CARES spending; Truman's term average (−2.68%) blends the enormous **FY1945 WWII deficit (−20.9%)** with the 1947–49 surpluses.
- **Truman GDP & inflation are PARTIAL [ESTIMATED].** GDPC1 and CPIAUCSL both begin **1947**, so Truman's `avg_gdp_growth` (4.83%) and `avg_inflation` (3.65%) are computed 1947-01→1953-01 and **miss the 1945–46 postwar demobilization contraction and the 1946–47 inflation spike** (headline CPI ran ~14–18% in 1947). His true term inflation was higher; treat these two Truman cells as understated estimates.
- **Truman `unemp_start` blank.** UNRATE begins 1948-01; no FRED value for Apr-1945. Left blank rather than guessed (wartime unemployment was ~1.9% from other historical series, but not in UNRATE).
- **`debt_gdp_change_pts` blank for Truman, Eisenhower, Kennedy/Johnson.** GFDEGDQ188S begins 1966-01, so no start value exists before Nixon. (Publicly, debt/GDP fell sharply across 1945–1966 as GDP outgrew the WWII debt.)
- **Trump-2 is an in-progress, PARTIAL term.** GDP growth is one year only (2025-Q1→2026-Q1); jobs, inflation, S&P are through the latest available month (PAYEMS/UNRATE 2026-06, CPI 2026-05, S&P 2026-06); deficit is the single FY2025 value; debt change is 2025-Q1→2026-Q1. Not comparable to full four-year terms.
- **`unemp_start`/`unemp_end` use the inauguration month, not the term peak.** Obama's start shows **7.8%** (Jan-2009), not the ~10.0% peak reached Oct-2009; his end 4.7% (Jan-2017). Carter genuinely began and ended at 7.5% (coincidence, both months verified).

## Recession assignment (NBER peak month → term)

Recessions are counted by **peak (onset) month** falling in the term:

| Recession (peak→trough) | Onset term |
|---|---|
| Feb-1945 → Oct-1945 | FDR (before Truman's Apr-1945 succession) — **not counted to Truman** |
| Nov-1948 → Oct-1949 | Truman (1) |
| Jul-1953 → May-1954; Aug-1957 → Apr-1958; Apr-1960 → Feb-1961 | Eisenhower (3) |
| — | Kennedy/Johnson (0) |
| Dec-1969 → Nov-1970; Nov-1973 → Mar-1975 | Nixon/Ford (2) |
| Jan-1980 → Jul-1980 | Carter (1) |
| Jul-1981 → Nov-1982 | Reagan (1) |
| Jul-1990 → Mar-1991 | G.H.W. Bush (1) |
| — | Clinton (0) |
| Mar-2001 → Nov-2001; Dec-2007 → Jun-2009 | G.W. Bush (2) |
| — | Obama (0) — GFC recession *began* under Bush, *ended* under Obama |
| Feb-2020 → Apr-2020 | Trump-1 (1) — COVID |
| — | Biden (0); Trump-2 (0) |

## Validation anchors — confirmed

- **Clinton:** budget **surplus** confirmed for FY1998–2001 (+0.76, +1.30, +2.30, +1.21% of GDP); **+22.9m jobs**. ✓ (term-average deficit −0.73% reflects early-1990s deficits before the surplus years.)
- **Obama:** inherited the GFC — unemp **7.8%** at inauguration (peaked 10.0% Oct-2009) → **4.7%** at end; **+11.6m jobs**; 0 recessions began on his watch. ✓
- **Reagan:** deep 1981–82 recession (1 onset) then boom; **avg deficit widened to −4.05%** (from Carter's −2.31%); **debt/GDP +18.9 pts**. ✓
- **Carter:** high inflation — term annualized **10.4%**, running ~13% by 1980. ✓
- **Trump-1:** ended in the COVID recession; **jobs net −2.77m**. ✓
- **Biden:** **+15.4m jobs** (~16m); 2022 inflation spike lifts term average to **4.97%**. ✓

## Striking on-watch patterns (correlation, not causation)

- **Jobs:** the four strongest job-creation terms are Clinton (+22.9m), Reagan (+16.1m), K/Johnson (+15.8m) and Biden (+15.4m) — a Democratic-leaning tilt, but Reagan sits second. The only net job **losses** (Trump-1, −2.8m) and near-zero (G.W. Bush, +1.4m) are Republican terms that each ended in a recession (COVID; GFC) — i.e., the shock, not the party, drove the sign.
- **Deficits:** on this measure deficits are large under *both* parties in crisis terms — Obama (−5.7%, GFC), Trump-1 (−6.6%, COVID) and Biden (−7.3%, COVID aftermath) are the three widest, spanning both parties, because all three overlap 2008–09 or 2020–21 emergency spending. The narrowest averages are Eisenhower (−0.5%) and Clinton (−0.7%). The correlation is with *crisis timing*, not party.
