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
| `usa_presidents.csv` | Economic outcomes by administration (Truman→2026): GDP, jobs, unemployment, inflation, S&P, deficit, debt |
| `usa_presidential.py` | **Presidential scorecard** — rankings + by-party pattern, framed on-watch-not-causation |
| `usa_debt_cycle_gauges.csv` | US Big-Debt-Cycle gauges 1960–2025: debt/GDP, deficit, interest/revenue, foreign-held share, USD reserve share, NIIP, real yield |
| `usa_debt_cycle.py` | **US big-debt-cycle diagnosis** (Dalio lens) + the programmatic **US-vs-Nigeria "two poles" comparison** |
| *(staging 27–30)* | Sourced data notes (FRED/IMF/BEA/Treasury ids, transforms, framing caveats) |

## What the model finds

**1. Monetary transmission (VAR, recursive ID, fed funds ordered last — Christiano-Eichenbaum-Evans):**
- **Granger:** the fed funds rate causes **GDP growth (p=0.009)** and **inflation (p=0.031)**; unemployment borderline (p=0.06).
- **Impulse response to a +100bp hike:** GDP growth **−0.57pp** (trough after ~1yr), unemployment **+0.37pp** (peak after ~3yr), inflation eases with a lag — after a brief **"price puzzle"** uptick (the known VAR artifact from omitting commodity prices). Textbook transmission: rates hit output fast, unemployment slowly, prices last.
- **FEVD:** monetary shocks explain ~15% of GDP-growth and ~17% of unemployment variance.

**2. Fed-cycle event study — is a soft landing rare?** Of the policy-linked tightening cycles since 1970: **6 hard landings** (Burns, Volcker ×2, 1988-89, 1999-2000, 2004-06) vs **3 soft** (1983-84, the canonical **1994-95**, and **2022-23 provisionally**) → a **~33% soft-landing rate**. A clean soft landing is historically rare; the 2022-23 cycle (+525bp, fastest in four decades) has avoided recession ~3 years on, but the historical prior sits against it.

**3. Presidential scorecard (`usa_presidential.py`)** — outcomes *on their watch*, 1945–2026, with rankings and the by-party pattern:
- **Democrats 3.71% avg GDP vs Republicans 2.39%** on-watch (+1.3pp) — matching **Blinder-Watson (2016)**: the gap is real but attributed mostly to **luck** (oil shocks, defense, productivity, world timing landing under D terms), **not** party policy.
- Top jobs/yr: Biden (COVID rebound) & Clinton; widest deficits: Biden, Trump-1, Obama (all crisis-era, both parties); highest inflation: Carter, Nixon/Ford, Biden.
- **Shocks set the sign:** the only net job loss (Trump-1, COVID) and near-zero gain (G.W. Bush, GFC) were exogenous-recession terms — the shock, not the president.
- Framed throughout as **accountability-with-context, not causation** (presidents inherit the economy; Fed independence; Congress controls spending; ~1–2yr lags).

**4. US big-debt-cycle diagnosis (`usa_debt_cycle.py`)** — the Dalio lens applied to the US, the *leading reserve power late in its cycle*: debt held by public ~98% of GDP (gross ~120%), a **structural ~6% peacetime deficit**, **interest/revenue ~21%** (interest now exceeds defense), real yields swung −0.6%→+2.0%, and the reserve privilege eroding (USD **72%→57%** of reserves; foreign Treasury share 34%→24%; NIIP **−71%**). The resolution is *not* external default — it's inflation/financial-repression/slow privilege-loss. Late-stage, chronic, not acute.

## The two poles of macro-lab
`usa_debt_cycle.py` prints this programmatically (loading both modules' gauges):

| Dimension | **United States** | **Nigeria** |
|---|---|---|
| Position in the cycle | LATE (reserve power) | MID inflationary deleveraging |
| Debt currency | own reserve currency | ~47% external + local |
| Reserve status | yes — 57% of reserves (eroding) | none |
| Deleveraging type | printing / debasement (latent) | inflation + devaluation (underway) |
| Debt / GDP | ~98% public (~120% gross) | ~39% (rebased) |
| Debt-service / revenue | ~21% (interest only) | ~44% gross / >100% retained |
| Central-bank lever | the Fed — vast | almost none |
| Household shock via | inflation, rates, unemployment | naira collapse / dollarization |
| External-default risk | ≈ nil (own currency) | real (FX / rollover) |
| The trap | exorbitant privilege eroding | no privilege to begin with |

> **The US is running down its exorbitant privilege slowly; Nigeria never had it.** Same Dalio template, opposite ends.

Remaining in the US module (per the plan): fiscal multipliers / stimulus-effect view, and the QE-balance-sheet channel folded into the monetary model.
