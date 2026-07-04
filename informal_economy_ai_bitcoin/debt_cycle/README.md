# Nigeria — 5-Year Economic Outlook (2026–2030) through Ray Dalio's Big Debt Cycle Framework

**Prepared by:** ojies · **Compiled:** 2026-06-28
**Goal:** a structured, evidence-based way to judge where the **finances of the average
Nigerian** are likely to be by ~2030 — not a single point forecast, but a framework +
scenarios so you can update the conclusion as facts change.

> ⚠️ **On "predict with certainty":** no honest method delivers certainty about a 5-year
> macro path — Dalio's own point is that debt cycles are *probabilistically* readable
> through a repeating template, not deterministically. What this folder gives you is:
> (1) a diagnosis of *where in the debt cycle* Nigeria sits, (2) the handful of gauges
> that actually drive the outcome, and (3) base / bull / bear scenarios with explicit
> triggers — so you can assign your own probabilities and watch the gauges move.

---

## Files in this folder

**Analysis & methodology**
| File | Contents |
|---|---|
| `README.md` | This overview + the Dalio framework applied to Nigeria |
| `ANALYSIS.md` | **Full diagnosis, base/bull/bear scenarios, and the "average Nigerian" household projection** |
| `DATA_NOTES.md` | **Read-me-first for the data** — file inventory, the four statistical breaks (CPI/GDP/unemployment rebasings + naira float), a do/don't comparison table, flag conventions, and corrections applied |

**Core debt-cycle gauges**
| File | Contents |
|---|---|
| `nigeria_debt_cycle_gauges.csv` | **Core annual gauges 2015–2026, 31 columns** (debt, debt-service gross+retained, W&M, reserves gross/net, FX official+parallel, REER, MPR, inflation, oil price, terms of trade, real min wage, poverty) |
| `nigeria_debt_cycle_quarterly.csv` | High-frequency gauges 2020Q1–2026Q2 (debt, FX, reserves, MPR, inflation, Bonny Light) — the early-warning series |
| `nigeria_external_debt_profile.csv` | External-debt creditor composition (multilateral/bilateral/commercial), 2025 quarterly |
| `nigeria_eurobond_maturity_wall.csv` | FGN Eurobond maturity schedule 2025–2051 |
| `imf_weo_nigeria_projections.csv` | IMF WEO actuals + forecasts to 2031 (GDP, growth, deficit, debt/GDP-WEO, per-capita USD & PPP, population) |

**Thematic / expansion data (clusters A–E + PE + NGX)**
| File | Contents |
|---|---|
| `nigeria_monetary_credit_banking.csv` | Broad money (M2/M3), private-sector credit, rates, T-bill/bond yields, NPL/CAR |
| `nigeria_markets_capital.csv` | NGX ASI level/return, market cap ₦+$, Eurobond yield, CDS, foreign participation |
| `nigeria_sectoral_gdp_activity.csv` | Sectoral GDP growth (old+rebased), oil/non-oil, sector shares, electricity, capacity, ports |
| `nigeria_labour_demographics.csv` | Unemployment (old+new methodology), youth, LFPR, informal-employment share |
| `nigeria_cost_of_living.csv` | Petrol/diesel/LPG, Band-A electricity, rice, food inflation, food-security (Cadre Harmonisé) |
| `nigeria_consumer_spending_indicators.csv` | Household consumption, food budget share, CPI weights, downtrading/BNPL, informal-retail share |
| `nigeria_financial_inclusion_remittances.csv` | EFInA/Findex inclusion, SANEF agents, NIP value, remittances (WB + IMTO) |
| `nigeria_fiscal_detail.csv` | FIRS tax by type, tax-to-GDP, state IGR, FAAC, pension assets, capex share |
| `nigeria_social_security_humandev.csv` | ACLED conflict events/fatalities, GTI, displacement, HDI, life expectancy, U5MR, electricity access |
| `nigeria_migration_japa.csv` | "Japa" emigration — Canada IRCC, UK nurses, US students/visas, remittances, UN net migration, Afrobarometer intent |
| `nigeria_private_capital_vc.csv` | VC/startup funding, deal count, Africa rank, fintech share, FDI sizing |

**Models (Phase 2 + 3) — `uv run python <script>.py`**

The modelling stack has four complementary layers (`pyproject.toml` + `uv` manage the venv):

| Layer | File(s) | Question answered |
|---|---|---|
| **Structure / early-warning** | `graph_model.py` → `graph_mst_edges.csv`, `graph_correlation_matrix.csv` · **`GRAPH_MODEL.md`** | Which gauges are hubs? what's the transmission spine? (Mantegna MST + directed lead-lag) |
| **Transmission / shocks** | `var_model.py` → `var_irf_oil_shock.csv` | If oil falls, what happens to FX→inflation→growth, with lags? (VAR + Granger + impulse-response) |
| **Full feedback "what-if"** | `sfc_model.py` → `sfc_simulation.csv` | How does an oil shock *become* a household shock through reserves→FX→debt feedback? (stock-flow / system-dynamics) |
| **Full feedback (closed)** | `sfc_national.py` → `sfc_national_simulation.csv` · **`ADVANCED_MODELS.md`** | 4-sector stock-flow-consistent model with the **dollarization loop** (accounts close, Walras≈0) |
| **Projection / scenarios** | `scenario_model.py` → `scenario_projections.csv` · **`MODEL_AND_TRACKER.md`** | Where do base/bull/bear lead by 2030? + the **quarterly gauge-tracker scorecard** |
| **Spatial / sub-national** | `state_gcn.py` · **`ADVANCED_MODELS.md`** | State-level poverty/fragility via a **spatial GCN** (graph beats no-graph) over 36 states + FCT |
| **Probability calibration** | **`ANALOGUE_CALIBRATION.md`** | Backtest vs Argentina/Turkey/Egypt/Ghana/Nigeria-2005 → scenario weights (55/20/25) |
| **Positioning (Phase 4)** | `positioning_model.py` → `positioning_returns.csv` · **`POSITIONING.md`** | Scenario → assets: USD-return barbell; bridges back to the AI+Bitcoin layer |
| **Monte Carlo (Phase 5)** | `montecarlo_model.py` → `montecarlo_summary.csv` | Regime-mixture MC (40k draws): the discrete scenarios → a **distribution** — fan charts, 2030 event probabilities, portfolio VaR/expected-shortfall |

Key findings: the graph identifies the **current account (oil-driven external balance) as the system hub**; the VAR confirms **oil → FX (1-yr lag) → inflation** (Granger-significant); the SFC's **dollarization loop** is the macro engine behind the stablecoin thesis; the analogue calibration set the weights at **base 55% / bull 20% / bear 25%**; positioning resolves to a **carry + USD-stablecoin/gold barbell**.

**Provenance & working files**
| File / Folder | Contents |
|---|---|
| `SOURCES.md` | Consolidated source index — provenance model + CSV→staging→source map + institutions |
| `_staging/` | 17 fully-sourced research files (per-cell source URLs + `[SOURCED]/[ESTIMATED]/[PROVISIONAL]` flags) behind every CSV |

> **Start with `DATA_NOTES.md`** before using any CSV — it documents the four 2023–2025 statistical breaks (CPI rebasing, GDP rebasing, unemployment-methodology change, naira float) that make naive cross-year comparison wrong, plus the corrections applied to the original gauges file.

**Long-run history**
| File | Contents |
|---|---|
| `nigeria_historical_precycle.csv` | **Pre-2015 backbone, 1980–2014** (external debt, real GDP growth, USD GDP, inflation incl. the 1995 72.8% hyperinflation peak, FX, reserves, oil price/production, current account) |
| `_staging/17_historical_precycle.md` | The five prior debt-cycle episodes narrated, incl. the fully-quantified **2005–06 Paris/London Club debt relief** (~$18bn cancelled, sovereign external → ~$3.5bn, debt/GDP ~52%→~7%) |

Sister dataset: `../../nigeria_fdi_fpi/` (FDI/FPI, governance, macro, capital flows) feeds the
external-sector parts of this analysis. The pre-2015 history above is the deep trough of Nigeria's
*first* big debt cycle — the baseline against which the post-2015 re-leveraging should be read.

---

## 1. Dalio's Big Debt Cycle — the template we're applying

From *Principles for Navigating Big Debt Crises* (Ray Dalio). A big debt cycle moves
through phases:

1. **Early / healthy** — debt grows roughly in line with incomes; borrowing funds
   productive activity.
2. **Bubble** — debt grows faster than income; asset prices and borrowing self-reinforce.
3. **Top** — incomes/cash-flows can no longer service debt; tightening triggers the turn.
4. **Depression / deleveraging** — debt burdens must fall relative to income via some mix of:
   - **austerity** (spend less),
   - **defaults/restructurings** (write debt down),
   - **money printing / monetization** (central bank funds the gap), and
   - **wealth transfers** (e.g. devaluation, taxes).
5. **Reflation / "beautiful deleveraging"** — when printing + restructuring + growth are
   balanced so nominal growth > nominal rates and debt/GDP falls without a deflationary
   collapse.
6. **Normalization.**

**The decisive split for Nigeria — deflationary vs inflationary deleveraging.** Dalio
shows the outcome hinges on the *currency of the debt* and whether the country has reserve-
currency status:
- Debt in **your own currency** + reserve status → deflationary deleveraging, manageable.
- Debt in **foreign currency** / no reserve status → **inflationary deleveraging**: capital
  flees, the currency falls, inflation spikes, and the debt burden is resolved by
  devaluing the real value of local-currency claims (i.e. **the population's savings and
  wages absorb the adjustment**).

This second case is the lens for Nigeria. The transmission to *the average Nigerian* runs
through **currency depreciation → imported inflation → falling real wages and savings**,
even when headline GDP keeps growing.

## 2. The gauges that decide the outcome (what to watch)

Dalio reduces the diagnosis to a small set of readings. For Nigeria:

| Gauge | Why it matters | Where it's tracked here |
|---|---|---|
| Debt **service**-to-revenue | Cash-flow stress (the trigger), more than debt/GDP | gauges CSV |
| Share of debt in **foreign currency** | Determines deflationary vs inflationary path | gauges CSV |
| **Reserves** & months of import cover | Capacity to defend the currency / pay external debt | gauges CSV + FDI dataset |
| **Monetization** (CBN Ways & Means) | Money-printing channel → inflation | gauges CSV |
| **Current account** & oil exports | Hard-currency earnings | IMF CSV + FDI dataset |
| **Real exchange rate / parallel-rate gap** | How much adjustment is still pending | FDI dataset (REER) |
| **Inflation vs nominal wage growth** | Direct read on household real income | gauges CSV |
| **Nominal growth vs nominal interest rate** | Whether a "beautiful deleveraging" is possible | IMF CSV |

## 3. IMF baseline (from `imf_weo_nigeria_projections.csv`)

The IMF's own 2026–2030 baseline (a useful "official optimism" anchor to stress-test):
- Real GDP growth steady ~4.0–4.3%/yr.
- Inflation falling from ~33% (2024) toward ~10% by 2029–30.
- Govt gross debt easing from ~39% to ~31% of GDP.
- Current account in surplus (~3–6% of GDP).
- **But** USD GDP-per-capita collapsed from ~$2,139 (2023) to ~$1,083 (2024) on the naira
  float, recovering only slowly to ~$1,760 by 2030 — i.e. **the IMF's own numbers show the
  average Nigerian's dollar income does not regain its 2023 level within the window.**
  PPP per-capita keeps rising (~$8.7k→$11.7k), the gap between the two being precisely the
  devaluation/inflation wealth-transfer Dalio describes.

*(Full diagnosis, scenario table, and the household projection are completed in
`ANALYSIS.md` once the debt-gauge research lands.)*
