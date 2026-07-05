# macro-lab

[![models](https://github.com/ojies/macro-lab/actions/workflows/models.yml/badge.svg)](https://github.com/ojies/macro-lab/actions/workflows/models.yml)

**Nigeria macro-economics research + a multi-country quantitative stack** — tracing one arc from raw
capital-flows data → a Ray-Dalio Big-Debt-Cycle diagnosis → a set of runnable models → an
AI + Bitcoin/stablecoin opportunity thesis for the informal economy — now extended to the **US,
Europe, China, and Japan** as comparative poles of the debt cycle. **See [MODELS.md](MODELS.md) for the
full model index**, and **[WORLD_ORDER.md](WORLD_ORDER.md)** for the capstone synthesis — where the
world is going and what it's aligning with, drawn from the models.

Every figure is sourced; every model is re-runnable (`uv run python <script>.py`); every
statistical break is flagged. Start with **[`NIGERIA_RESEARCH_OVERVIEW.md`](NIGERIA_RESEARCH_OVERVIEW.md)**.

---

## What's inside — three linked layers

```
macro-lab/
├── NIGERIA_RESEARCH_OVERVIEW.md          ← read this first (the index)
├── nigeria_fdi_fpi/                       DATA LAYER — FDI/FPI + determinants (2000–2025)
└── informal_economy_ai_bitcoin/           APPLICATION LAYER — the opportunity
    ├── MASTER_REPORT.md                    the AI + Bitcoin thesis (start here for layer 3)
    ├── README.md + 6 thematic deep-dives
    └── debt_cycle/                         ANALYSIS LAYER — macro engine + models
        ├── data: 17 CSVs (1980–2026) + 30+ sourced staging files
        ├── Nigeria models: graph · VAR · SFC · scenario · GCN · positioning · Monte-Carlo · Development-Age
        ├── usa/     — monetary VAR · presidential scorecard · debt-cycle · fiscal+QE  (reserve-currency pole)
        ├── europe/  — stagnation diagnosis + euro fragility gauge                      (stagnation pole)
        ├── china/   — state-directed-model exhaustion                                  (state-directed pole)
        └── docs: MODELS.md (index) · DATA_NOTES · SOURCES · ADVANCED_MODELS · …
    └── app/                                 DASHBOARD — FastAPI backend + Next.js frontend
```

## Run the dashboard (`app/`)

An interactive web app (six animated views) over the models — every chart pulled **live** from the
model outputs. One command; full details in **[`app/README.md`](app/README.md)**.

```bash
cd app && docker compose up --build     # containerized → localhost:3000  (API :8000/docs)
#  — or, locally with uv + Node:
cd app && make install && make dev       # runs backend + frontend together (Ctrl-C stops both)
```

The frontend proxies `/api/*` to the backend, so the browser fetches same-origin — no CORS setup.

1. **Data layer** (`nigeria_fdi_fpi/`) — capital flows (FDI & FPI) and the variables that explain
   them: the six governance indicators, macro fundamentals, markets/monetary, global push factors.
2. **Analysis layer** (`.../debt_cycle/`) — a Big-Debt-Cycle diagnosis of Nigeria plus an
   **nine-model quantitative stack** and a strengthened **1980–2026** dataset.
3. **Application layer** (`informal_economy_ai_bitcoin/`) — what to *build* given that macro
   reality: a financial-services opportunity for the informal economy using AI to underwrite and
   stablecoins to settle.

---

## The nine-model stack

Managed with [uv](https://docs.astral.sh/uv/) (`pyproject.toml` in `.../debt_cycle/`). From that folder:

```bash
uv sync                      # create the venv from pyproject/uv.lock
uv run python scenario_model.py    # (or any model below)
```

| Model | Question | Headline finding |
|---|---|---|
| `graph_model.py` (Mantegna MST) | which gauges are hubs? | **current account** = system hub; spine oil→CA→reserves→FX→inflation |
| `var_model.py` (VAR + IRF) | transmission with lags? | **oil → FX (1-yr lag) → inflation** (Granger-significant) |
| `sfc_model.py` / `sfc_national.py` | full feedback? | closed 4-sector stock-flow model (Walras≈0) with the **dollarization loop** |
| `scenario_model.py` | base/bull/bear to 2030? | central path: dollar income doesn't regain 2023 by 2030 (+ quarterly tracker) |
| `state_gcn.py` (spatial GCN) | sub-national poverty/conflict? | real NBS+ACLED data; border graph beats no-graph, + conflict-shock early-warning |
| `positioning_model.py` | what to own? | carry + USD-stablecoin/gold **barbell** |
| `montecarlo_model.py` | the odds, not 3 points? | 40k-draw regime-mixture MC → fan charts + event probabilities (**P(dollar income regains 2023) ≈ 26%**) + portfolio VaR |
| `development_age.py` | how does Nigeria compare? | by development *level*, Nigeria ≈ **Korea-1970 income** — but conditions (security/oil/institutions) tilt it to **stall, not escape** |

Scenario weights (**base 55 / bull 20 / bear 25**) are calibrated against historical
inflationary deleveragings (Argentina, Turkey, Egypt, Ghana) in `ANALOGUE_CALIBRATION.md`.

---

## Beyond Nigeria — comparative macro

macro-lab is becoming a **multi-country** engine:
- **`development_age.py`** — compares countries by development *level*: Nigeria ≈ Korea-1970 income, but conditions tilt it to stall not escape (rendered live in the [`app/`](app/) dashboard).
- **`debt_cycle/usa/`** — the **US reserve-currency pole**: a monetary-transmission VAR (a +100bp Fed hike → GDP −0.57pp, unemployment +0.37pp) and a Fed-cycle event study (soft landings are ~⅓ of tightening cycles). Nigeria = inflationary EM cycle with no policy space; the US = reserve-currency cycle where the Fed is the lever — the two poles of the debt-cycle spectrum, same toolkit.

## The thesis in four lines

1. Nigeria is mid-way through an **inflationary deleveraging**: the state's finances are being
   fixed by a collapsing naira and high inflation rather than by default.
2. The **sovereign** gauges are healing; the **household** is paying for it (dollar income per
   capita ~halved 2023→2024, not back to 2023 levels by 2030 on the central path).
3. That wealth-transfer is why ~95% of surveyed Nigerians reach for **stablecoins** — which *is*
   the demand an AI + stablecoin venture serves.
4. The models confirm it bottom-up: the graph finds the **current account** hub, the VAR times the
   **oil→FX→inflation** chain, and the stock-flow model **generates the dollarization loop** that
   is the stablecoin demand — so the macro engine and the business opportunity are one mechanism.

---

## Data, sources & caveats

- **Sourcing:** every value traces to a citation in the `_staging/` research files and
  `debt_cycle/SOURCES.md`; each cell is flagged `[SOURCED]/[ESTIMATED]/[PROVISIONAL]`; blanks are
  deliberate (never guessed). Primary sources include **NBS, CBN, DMO, IMF, World Bank, OPEC, ACLED,
  UNDP**, and others — all rights to that underlying data remain with the original publishers.
- **⚠ Read `debt_cycle/DATA_NOTES.md` before using any CSV** — it documents four 2023–25
  statistical breaks (CPI/GDP/unemployment rebasings + the naira float) that make naive cross-year
  comparison wrong.
- **Not investment advice.** The models are scenario/analysis tools, not forecasts; assumptions
  (not arithmetic) carry the uncertainty.
- **Third-party data terms:** some sources (e.g. **ACLED**) have their own attribution /
  redistribution terms — review them before redistributing that data.

## License

Original code, models, and analysis: **MIT** (see [`LICENSE`](LICENSE)). Third-party data included
for reproducibility remains under its originators' terms (see `debt_cycle/SOURCES.md`).

*Prepared by ojies. Contributions and corrections welcome.*
