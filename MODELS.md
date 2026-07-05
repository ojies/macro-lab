# macro-lab — model index

Every model is a plain Python script run through one shared `uv` environment. From
`informal_economy_ai_bitcoin/debt_cycle/`:

```bash
uv sync                                   # once
uv run python <script>.py                 # any model below
```

CI (`.github/workflows/models.yml`) runs **all** of them on every push — the badge on the README
is proof the whole stack reproduces from `pyproject.toml` + `uv.lock` alone.

---

## Nigeria — the anchor economy (inflationary EM deleveraging)

| Model | Script | Question → finding |
|---|---|---|
| Correlation network | `graph_model.py` | which gauges are hubs? → **current account = system hub** (oil→CA→reserves→FX→inflation) |
| VAR + IRF | `var_model.py` | transmission with lags? → **oil → FX (1-yr lag) → inflation** |
| Stock-flow (national) | `sfc_model.py` · `sfc_national.py` | full feedback? → closed 4-sector SFC (Walras≈0) with the **dollarization loop** |
| Scenario projection | `scenario_model.py` | base/bull/bear to 2030? → dollar income doesn't regain 2023 by 2030 |
| Spatial GCN | `state_gcn.py` | sub-national poverty/conflict? → border graph beats no-graph on real NBS+ACLED data |
| Positioning | `positioning_model.py` | what to own? → carry + USD-stablecoin/gold **barbell** |
| Monte Carlo | `montecarlo_model.py` | the distribution? → 40k-draw fan; **P(regain 2023 income) ≈ 26%** |
| Development-age | `development_age.py` | how does Nigeria compare? → ≈ **Korea-1970 income**, but conditions tilt to stall not escape |

## United States — the reserve-currency pole (`usa/`)

| Model | Script | Question → finding |
|---|---|---|
| Monetary VAR + Fed-cycle event study | `usa/usa_monetary_var.py` | rate shock → economy? → +100bp: GDP −0.57pp, unemp +0.37pp; soft landings ~⅓ of cycles |
| Presidential scorecard | `usa/usa_presidential.py` | outcomes by administration? → D 3.7% vs R 2.4% GDP on-watch (**luck, not policy** — Blinder-Watson) |
| Big-debt-cycle diagnosis | `usa/usa_debt_cycle.py` | where in the cycle? → **late reserve power** + the US-vs-Nigeria two-poles table |
| Fiscal multipliers + QE | `usa/usa_fiscal_qe.py` | the policy space? → multipliers 0.4–1.5 (composition/state); QE ~−265bp, diminishing |

## Europe — the stagnation pole (`europe/`)

| Model | Script | Question → finding |
|---|---|---|
| Stagnation diagnosis | `europe/europe_stagnation.py` | UK & euro area? → aging/low-growth; the **BTP–Bund spread** = the price of union-without-fiscal-union |

## China — the state-directed pole (`china/`)

| Model | Script | Question → finding |
|---|---|---|
| Growth-model exhaustion | `china/china_model.py` | the catch-up's reckoning? → debt 127%→300%, **credit-intensity ×3.1**, property halved, "old before rich" |

---

## The comparative layer

macro-lab lines the economies up as **poles of one debt cycle**, same Dalio template:

| Pole | Type | Policy space | The trap |
|---|---|---|---|
| **Nigeria** | early inflationary EM | almost none | no privilege to begin with |
| **China** | state-directed workout | managed (closed capital acct, state banks) | debt/property/demographic trilemma |
| **Europe** | aging stagnation | UK: own currency · periphery: none | union without fiscal union |
| **United States** | late reserve power | vast (Fed + fiscal + QE) | exorbitant privilege eroding |
| *Japan* | *the precedent* | *moderate* | *the balance-sheet recession others are measured against* |

- `usa/usa_debt_cycle.py` prints the **US ↔ Nigeria** comparison programmatically.
- `development_age.py` places Nigeria on the **11-country** catch-up map.
- Visual briefs: `development_age_viz.html`, `usa/two_poles_viz.html` (and the multi-country dashboard).
