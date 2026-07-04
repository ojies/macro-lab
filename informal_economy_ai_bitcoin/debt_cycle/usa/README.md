# macro-lab · USA module (the reserve-currency pole)

Where the Nigeria stack models an **inflationary EM debt cycle with no policy space**, this models
the **US reserve-currency cycle** whose central lever is the Fed. First build: the monetary channel.

Run (from `debt_cycle/`, reusing the shared venv):
```bash
uv run python usa/usa_monetary_var.py
```

## Files
| File | Contents |
|---|---|
| `usa_monetary_macro.csv` | Annual 1960–2025 (FRED): fed funds, CPI inflation, real GDP growth, unemployment, 10y yield, 10y–2y curve, Fed balance sheet %GDP, NBER recession flag |
| `usa_fed_cycles.csv` | Every Fed tightening cycle since 1970 — start/peak rate, +bp, hard-vs-soft landing, recession lag |
| `usa_monetary_var.py` | Monetary-transmission VAR + Fed-cycle event study |
| `usa_var_irf_ratehike.csv` | Model output — impulse response to a +100bp hike |
| *(staging 27–28)* | Sourced data notes (FRED ids, transforms, NBER dating) |

## What the model finds

**1. Monetary transmission (VAR, recursive ID, fed funds ordered last — Christiano-Eichenbaum-Evans):**
- **Granger:** the fed funds rate causes **GDP growth (p=0.009)** and **inflation (p=0.031)**; unemployment borderline (p=0.06).
- **Impulse response to a +100bp hike:** GDP growth **−0.57pp** (trough after ~1yr), unemployment **+0.37pp** (peak after ~3yr), inflation eases with a lag — after a brief **"price puzzle"** uptick (the known VAR artifact from omitting commodity prices). Textbook transmission: rates hit output fast, unemployment slowly, prices last.
- **FEVD:** monetary shocks explain ~15% of GDP-growth and ~17% of unemployment variance.

**2. Fed-cycle event study — is a soft landing rare?** Of the policy-linked tightening cycles since 1970: **6 hard landings** (Burns, Volcker ×2, 1988-89, 1999-2000, 2004-06) vs **3 soft** (1983-84, the canonical **1994-95**, and **2022-23 provisionally**) → a **~33% soft-landing rate**. A clean soft landing is historically rare; the 2022-23 cycle (+525bp, fastest in four decades) has avoided recession ~3 years on, but the historical prior sits against it.

## The two poles of macro-lab
| | **USA** (this module) | **Nigeria** (`debt_cycle/`) |
|---|---|---|
| Cycle type | reserve-currency, late-stage | inflationary EM deleveraging |
| Central lever | the Fed (rates + balance sheet) | almost none — FX float + import of inflation |
| Debt currency | own currency, reserve status | mostly local, but no reserve privilege |
| Household shock via | unemployment (rate hikes) | the naira / dollarization |
| Same toolkit | VAR, scenario, graph, SFC — different parameters | — |

Next in the US module (per the plan): presidential economic scorecard, US big-debt-cycle diagnosis, fiscal multipliers.
