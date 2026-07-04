# Nigeria Debt-Cycle — Advanced Models (SFC National + Spatial GCN)

**Compiled:** 2026-06-30 · Run any with `uv run python <script>.py`

The two "next level up" models beyond the practical stack — a **calibrated stock-flow-consistent national model** (the rigorous "model the whole economy" build) and a **state-level spatial GCN** (the regime where a graph neural net is genuinely the right tool).

---

## 1. SFC National Model — `sfc_national.py`

A closed, four-sector **stock-flow-consistent** model (Godley–Lavoie tradition): **Households · Government · Banks+Central Bank · External/RoW**. Every financial asset is another sector's liability; flows accumulate into stocks; and the **transactions-flow matrix closes** — the four sectors' net financial balances sum to zero each period (the "Walras residual", verified ≈ 0 in the output). That closure is what makes it *consistent* rather than a loose set of equations.

### What it adds over the stylized `sfc_model.py`
`sfc_model.py` traces one chain (oil → reserves → FX). This model carries **full sector balance sheets** and, crucially, models the **dollarization feedback loop** that is the heart of Nigeria's predicament:

```
   households expect depreciation
            │  (raise dollar-preference λ)
            ▼
   buy dollars / stablecoins  ──►  drains CB reserves  ──►  naira depreciates
            ▲                                                      │
            └────────  inflation & expected-depreciation rise  ◄───┘   (self-reinforcing)
```

### Results
- **Base:** naira drifts ₦1,529→1,637, inflation ~9.6%, reserves build (CA surplus cushions), debt/GDP 35.7→44.2%, **dollarization 19%→27%** of household financial wealth.
- **Confidence shock** (dollar-preference +25pp from 2027): naira to ₦1,722, **dollarization jumps to 39%**, λ to ~60% — the doom-loop visible but contained by Nigeria's current current-account surplus (an honest result: the surplus is what stops it becoming Argentina).
- **Walras residual = 0.0 every period** → the accounts are consistent.

### Why it matters for the program
This is the **macro engine behind the stablecoin thesis** (`MASTER_REPORT.md`), modelled explicitly: the dollarization variable the SFC generates *is* the demand the AI+Bitcoin businesses serve. The model says that demand is structural (rises even in base) and explosive under a confidence shock — exactly when a licensed dollar/stablecoin rail is most valuable.

> Honest limits: parameters are calibrated-but-illustrative, not estimated; it's a 4-sector model (firms folded into households/banks); it demonstrates mechanisms and closure, it is not a forecasting tool. A fully-estimated SFC would need a national flow-of-funds matrix.

---

## 2. State-Level Spatial GCN — `state_gcn.py`

A 2-layer **Graph Convolutional Network** (Kipf–Welling propagation, pure-numpy with manual backprop — no torch) over **Nigeria's 36 states + FCT** on the geographic/geopolitical-zone graph. This is the case flagged earlier as *where a GNN earns its keep*: many nodes (37), strongly **spatially-autocorrelated** targets (poverty, fragility, revenue cluster North vs South), and a graph that carries real signal.

### Task & test
Semi-supervised **node regression** on the **real geographic land-border graph** (37 nodes, 87 edges) with real data (`state_panel.csv` — NBS MPI 2022, NBS 2024 IGR, NBS population, and **exact per-state ACLED-2024 political-violence fatalities** pulled from the ACLED/HDX curated file, `_staging/22_acled_state_fatalities.md`): predict each state's **Multidimensional-Poverty headcount** from its features (population, IGR-per-capita, log ACLED fatalities) **plus its neighbours**, 30% held out, averaged over 20 random splits. GCN (border adjacency) vs identical-capacity MLP (no graph). Features deliberately exclude the WB monetary-poverty column (near-circular).

### Result (REAL data — NBS panel + real ACLED conflict)
| Setup | GCN (border graph) | MLP (no graph) | Graph adds |
|---|---|---|---|
| **[A]** features incl. zone one-hot | **18.11** | 18.73 | **3%** |
| **[B]** non-spatial features only | **16.69** | 21.54 | **23%** |
*(held-out RMSE in MPI percentage-points; target range 27–90%, mean 60.6%)*

- **The GCN beats no-graph in both setups** — and adds **most (23%)** when the features carry no spatial information, because then the **border graph is the only source of the North–South signal**.
- Wiring in **real ACLED fatalities** (replacing a coarse fragility proxy) *improved the no-graph baseline* in [A] (conflict is itself a strong, spatially-clustered poverty predictor, so it partly substitutes for the graph) but *widened* the graph's advantage in [B] to 23% — i.e., conflict intensity and poverty share the same North–South geography the graph encodes.
- Verdict: **the GCN earns its keep.** Nigerian MPI poverty is steeply spatially clustered (**North-West/North-East ~73–90% vs South-West/South-East ~28–49%**), and so is conflict (Borno 3,863 / Zamfara 1,984 fatalities in 2025 vs Ekiti 2), so a state's neighbours genuinely predict its poverty beyond its own attributes.

### Conflict-shock diffusion (a graph-native early-warning)
`state_gcn.py` also runs a **graph-diffusion** analysis (output: `state_conflict_exposure.csv`): it takes each state's **2024→2025 fatality escalation** (log-change), **spreads it to neighbours** through the border graph (row-normalized adjacency = mean of neighbours), and crosses the resulting *exposure* with existing MPI poverty to flag **compounding risk** — states that are already poor *and* seeing conflict rise (own or spilled-over).

- **Top escalation hotspots** (acceleration, not just level): **Kano** (4→90), **Kwara** (22→251), **Kebbi** (48→256), Adamawa, Jigawa, Sokoto — states where violence is *emerging or accelerating* (the log-change deliberately highlights new escalation over chronic-but-flat hotspots like Borno).
- **Compounding-risk set** (high poverty × rising conflict): **Kano, Kebbi, Sokoto, Jigawa, Gombe, Kwara, Bayelsa, Borno** — the North-West/North-East belt where the debt-cycle household squeeze and the security shock **stack**.
- **Why it matters:** these are the states most likely to tip the *national* Political-Stability gauge — the tracker's top bear trigger. The graph sees a spatial early-warning the national models (VAR/SFC/scenario) structurally cannot: a shock in one state pressures its neighbours *before* their own prints move. (Caveat: "exposure" is a log-*change* signal — it flags acceleration; absolute-level hotspots like Borno/Zamfara are separately visible in the fatality columns.)

### Where this scales — the real prize
37 nodes × a few static features is a demonstrator. The architecture scales to **36 states + FCT × MONTHLY indicators** (food prices, ACLED conflict, IGR, fuel prices, displacement) → a **spatial early-warning system**: a shock in one state (a conflict spike, a food-price jump) propagates predictions to its neighbours *before* their own data prints. That is the genuinely powerful version — and the one a GNN, not a VAR or an MST, is built for.

---

## 3. The complete modelling stack (6 models)

| # | Model | Tool | Question | Status |
|---|---|---|---|---|
| 1 | `graph_model.py` | Mantegna MST + lead-lag | Which gauges are hubs? the spine? | ✅ current account = hub |
| 2 | `var_model.py` | VAR + Granger + IRF | Oil shock → FX→inflation, with lags | ✅ oil→FX (1-yr lag) |
| 3 | `sfc_model.py` | stylized stock-flow | Oil shock → household shock | ✅ |
| 4 | `sfc_national.py` | **closed 4-sector SFC** | Full feedback incl. **dollarization loop** | ✅ accounts close |
| 5 | `scenario_model.py` | scenario projection | Base/bull/bear to 2030 + tracker | ✅ 55/20/25 |
| 6 | `state_gcn.py` | **spatial GCN** | State-level poverty/fragility, spatial | ✅ graph beats no-graph |
| + | `positioning_model.py` | scenario→assets | What to own (USD-return barbell) | ✅ Phase 4 |

**The honest hierarchy:** the **graph** maps the nervous system (what's connected, what leads); the **VAR** measures transmission (signs, lags, magnitudes); the **SFC** closes the circuit (full feedback with accounting consistency); the **scenario engine** is the practical projection; the **GCN** is the spatial layer for sub-national early-warning; and **positioning** turns it all into a portfolio. Each answers a question the others can't — together they are about as complete a picture as this data supports, and every one is re-runnable and documented.
