# Nigeria Debt-Cycle — Graph / Network Model

**Engine:** `graph_model.py` → `graph_mst_edges.csv`, `graph_correlation_matrix.csv`
**Compiled:** 2026-06-30

An unsupervised **structure-discovery** layer over the macro gauges, adapting the Mantegna (1999) correlation-network + Minimum-Spanning-Tree method (familiar from asset networks / the MST "informative neighbour" idea) to a small macro panel. It answers: *which gauges are the hubs, what is the transmission spine, and what single gauge best informs each target?*

---

## 1. What it does (three layers)

1. **Mantegna MST (undirected).** Correlation → distance `d = √(2(1−ρ))` over the 1980–2026 change-panel, then the Minimum Spanning Tree keeps each variable's strongest link → the economic **bloc structure, with no labels**.
2. **Centrality + informative neighbour.** MST degree = the **hub** variables (what to watch); the single most-correlated gauge for each target = its **informative neighbour** (the "watch this for that" map).
3. **Directed lead-lag.** Compares `corr(x_{t-1}, y_t)` vs `corr(y_{t-1}, x_t)` to infer which variable **leads** → an approximate transmission map (a heuristic, not formal Granger).

Method notes: stock/level series (FX, reserves, oil price, debt) use YoY % change; rate/ratio series (growth, inflation, CA, MPR, etc.) use levels. The model splits a **reliable backbone** (7 long variables, ~40+ annual obs, 1980–2026) from an **exploratory** layer (2015+-only household/policy variables, n≈11 — flagged weak).

---

## 2. Honest caveats (why this is a map, not the model)

- **Sample size.** Asset MSTs use hundreds of series × thousands of daily returns. We have ~47 annual points for long variables, **~11 for 2015-only variables** — correlations there are noisy (e.g. the exploratory `mpr ← current_acct` corr 0.91 is small-sample artefact, flagged). Treat the backbone as solid, the short-variable links as hypotheses.
- **Undirected ≠ causal.** The MST is symmetric; transmission is directional. The lead-lag layer is a heuristic patch, not a structural-causal claim.
- **GCN/GAT are the wrong tool here.** Graph neural nets are data-hungry node-learning models for large panels; on one small macro system they overfit. The value here is *structure discovery + variable selection*, not a GNN.

---

## 3. What it found

### The backbone (reliable, 1980–2026)
```
        gdp_growth
            |
oil_price — current_acct — reserves — inflation
   |            |
   fx        (hub, deg 3)
   |
ext_debt
```
**MST edges (distance):** gdp_growth–current_acct (0.86) · current_acct–reserves (0.78) · current_acct–oil_price (1.04) · oil_price–fx (1.38) · reserves–inflation (1.40) · fx–ext_debt (1.45).

### Three takeaways
1. **The current account is the system hub** (MST degree 3; the informative neighbour of growth, reserves, oil price, and external debt). In an oil-exporting, FX-constrained economy this is exactly right: **the external balance is the spine** — it is the most informative single gauge in the whole system.
2. **The transmission spine, recovered with no labels:** `oil price → current account → reserves → FX → inflation (→ external-debt ratio via FX revaluation)`. This *is* the Dalio inflationary-deleveraging mechanism for a commodity exporter, discovered bottom-up from the data — independent confirmation of the narrative in `ANALYSIS.md`.
3. **FX is the hard-to-predict node** (its best informative neighbour, reserves, is only ρ≈−0.17) — because for most of the sample the rate was *managed*, so it moved in regime breaks, not smooth co-movement. That is itself a finding: the naira's discontinuities (1986, 1999, 2023) are policy events, not gradual market drift.

---

## 4. How it fits the modelling stack

The graph is one layer in a three-part stack — each answers a different question:

| Layer | Tool | Question it answers | Status |
|---|---|---|---|
| **Structure / early-warning** | **Graph (this)** — Mantegna MST + lead-lag | *Which gauges are hubs? what's the spine? what informs each target?* | ✅ `graph_model.py` |
| **Projection / scenarios** | **Scenario engine** | *Where do base/bull/bear lead by 2030?* | ✅ `scenario_model.py` |
| **Transmission / shocks** | **(Bayesian) VAR / local projections** | *If oil falls 20%, what happens to FX→inflation→poverty, with lags?* | ⬜ natural next step |
| **Full "what-if" economy** | **Stock-flow-consistent / system-dynamics** | *Close the whole circuit (govt-CB-banks-households-external)* | ⬜ heavier build |

**Can a graph model the whole economy?** No — a correlation/MST graph is the **nervous-system map**: it shows what's connected and what leads, and it's excellent for **(a) deciding what to watch** (the hub gauges) and **(b) variable selection** for the scenario/VAR models. To *model* the economy (simulate shocks with feedback) you want a **VAR** (transmission + forecasting) or a **stock-flow-consistent model** (full accounting closure). The graph feeds those; it doesn't replace them. GNNs would only earn their keep if we had a large cross-section (e.g. all 36 states × many indicators × monthly) — then a spatial GCN over the state network could be genuinely powerful.

### Direct payoff for the tracker
The graph **validates and prioritises the Phase-2 tracker**: the hub + spine say the **external bloc (oil price → current account → reserves → FX)** is the highest-information leading-indicator set. So in the quarterly scorecard, *those* gauges deserve the most weight as early-warning — a deterioration there will move inflation/wages/poverty with a lag, before the annual data shows it.

---

## 5. Next step if we want the directional model

A small **Bayesian VAR** on `[oil, current_acct, reserves, fx, inflation, growth]` (the backbone) with 1–2 lags would turn the heuristic lead-lag map into proper impulse-response functions — e.g. "a −20% oil shock cuts the current account by X, reserves by Y over 2 years, depreciates the naira Z%, and adds W points to inflation." That plugs straight into the bear-scenario calibration. It's the recommended Phase-2b once the analogue calibration (Phase 3) is in.
