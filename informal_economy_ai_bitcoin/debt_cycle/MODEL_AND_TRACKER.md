# Nigeria Debt-Cycle — Living Model & Quarterly Tracker (Phase 2)

**Compiled:** 2026-06-30 · **Engine:** `scenario_model.py` → `scenario_projections.csv`

This turns the static `ANALYSIS.md` diagnosis into a **living model**: a transparent scenario engine that projects the base/bull/bear paths off the strengthened gauges, and a **quarterly scorecard** that flags which scenario is currently winning. Re-run the engine and update the scorecard each quarter as new prints land.

---

## 1. The scenario engine

`scenario_model.py` projects 2026–2030 for the variables that decide the "average Nigerian" outcome. Method is deliberately simple and auditable (see the docstring): nominal GDP compounds real growth × deflator; USD GDP = nominal ÷ FX; debt accumulates the deficit plus FX-revaluation on the external share; the real-wage index deflates the (occasionally re-based) minimum wage by cumulative CPI; poverty moves with real per-capita growth. **All assumptions live in the `SCENARIOS` dict — edit and re-run.**

**Key assumption dials (2026→2030):**

| Dial | Base (~55%) | Bull (~25%) | Bear (~20%) |
|---|---|---|---|
| Real GDP growth | 3.9→4.2% | 4.5→5.0% | 2.2→2.4% |
| CPI inflation | 16→11.5% | 14→7% | 20→22% (re-accel) |
| NGN/USD (avg) | 1550→1880 | 1450→1310 | 1700→3000 |
| Fiscal deficit (% GDP) | 4.2→3.5% | 3.5→2.5% | 5.5→5.2% |
| Min-wage re-basing | ₦100k (2027) | ₦120k (2027) | none |

FX paths are kept **PPP-consistent** (FX depreciates roughly with the inflation differential) so high-inflation scenarios don't spuriously inflate USD income.

---

## 2. Projection results — 2030 endpoints

*Source: `scenario_projections.csv` (full annual paths inside). 2025 base shown for reference.*

| Path | GDP/capita USD | Debt/GDP | Real-wage idx (2015=100) | Extreme poverty | Debt-service/rev |
|---|---|---|---|---|---|
| **2025 actual** | $1,239 | 36.1% | 71.8 | 50.9% | ~44% |
| **Base 2030** | **$1,957** | 32.8% | 54.8 | 45.0% | 46.7% |
| **Bull 2030** | $2,453 | 28.5% | 78.3 | 38.2% | 36.9% |
| **Bear 2030** | $1,732 | 36.3% | 24.3 | 52.6% | 61.6% |
| **Prob-weighted 2030** | **$2,036** | — | 54.6 | 44.8% | — |

**Reading:** On the central (base) path the average Nigerian is **better than the 2024 trough but their dollar income does not regain its 2023 level ($2,139) by 2030**, real wages stay **below** their 2025 level, and extreme poverty eases only slowly (~51%→45%). The bull path restores real wages and cuts poverty meaningfully; the bear path is a real-income collapse (real wage index 24, poverty rising). This confirms the `ANALYSIS.md` split-screen — quantified.

> ⚠️ The USD-income figures embed the 2025 GDP rebasing (≈+34% level). They are not comparable to pre-2025 USD-GDP-per-capita prints on the old base — see `DATA_NOTES.md`.

---

## 3. Quarterly gauge tracker — which scenario is winning?

Update the "Latest reading" column each quarter from `nigeria_debt_cycle_quarterly.csv` (+ the security/social CSVs). Each gauge votes bull / base / bear; the tally gives the live read.

| Gauge | 🟢 Bull signal | 🟡 Base signal | 🔴 Bear signal | Latest reading (Q2-2026) | Vote |
|---|---|---|---|---|---|
| Headline inflation | <10% & falling | 11–18%, easing | >22% & rising | **15.9%** (May-26), falling | 🟡→🟢 |
| Naira (NGN/USD) | appreciating | range ₦1,400–1,700 | >₦2,000 & sliding | **₦1,379** (Jun-26), firm | 🟢 |
| Parallel premium | <3% | 3–10% | >15% | **~1.5%** | 🟢 |
| Net FX reserves | rising >$40bn | stable $25–40bn | drawdown | **$34.8bn** (2025), rising; gross $51bn (Jun-26) | 🟢 |
| MPR / policy | cutting on disinflation | on hold high | hiking on re-accel | **26.5%**, cutting since Nov-25 | 🟢 |
| PMI | >53 sustained | 50–53 | <50 | **54.1** (May-26) | 🟢 |
| Oil production | >1.6 mbpd | ~1.4–1.5 | <1.3 | **~1.5 mbpd** | 🟡 |
| Debt-service/revenue | falling <40% | 40–60% | >70% / >100% retained | gross easing ~44% | 🟡 |
| **Political Stability** (ACLED) | fatalities falling | stable | **rising / record** | **12,883 in 2025 — highest since 2015** | 🔴 |
| Govt Effectiveness / Reg. Quality (WGI) | improving | flat | falling | flat-to-weak (≈ −1.0) | 🟡 |
| Real wages / poverty | recovering | flat below 2022 | falling, poverty >55% | poverty 50.9%, real wage idx ~62 | 🟡→🔴 |

### Live verdict (Q2-2026): **BASE, drifting toward BULL on the macro — but the bear tail is the security gauge.**

- **The macro stabilization gauges are firmly base→bull:** inflation disinflating (15.9%), naira firm (₦1,379) with the parallel premium near-closed (~1.5%), reserves rebuilt, MPR easing, PMI in expansion. This is the "beautiful deleveraging" working on the sovereign side.
- **The household & security gauges flash the bear risk:** ACLED political-violence fatalities hit **12,883 in 2025 — the deadliest year since 2015**, extreme poverty is still rising (50.9%), and governance scores are flat-to-weak. Per the framework, **Political Stability is the single biggest swing variable** — a further deterioration there is the most likely trigger to flip the path from base toward bear, regardless of how good the FX/inflation numbers look.
- **Net:** the central case is intact and the *direction* of the sovereign balance sheet is up; the *household recovery is slow and conditional*, and the live risk is political/security, not the currency.

---

## 4. How to update each quarter

1. Add the latest quarter's row to `nigeria_debt_cycle_quarterly.csv` (FX, reserves, inflation, MPR, debt) and refresh the security CSV (ACLED YTD).
2. If the outturn diverges materially from a scenario's assumptions, edit the relevant dial in `SCENARIOS` (`scenario_model.py`) and re-run: `python3 scenario_model.py`.
3. Update the "Latest reading" column and re-tally the verdict in §3.
4. If a trigger is breached for **two consecutive quarters**, shift the scenario probabilities (currently 55/25/20) accordingly — that is the signal the path is changing, well before the annual GDP data confirms it.

*The model is intentionally simple so it stays legible and updatable. It is a scenario-projection tool for tracking the cycle, not a precise forecast — the assumptions, not the arithmetic, carry the uncertainty.*
