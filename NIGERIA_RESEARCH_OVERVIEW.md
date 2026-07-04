# Nigeria Economics Research — Project Overview

**Prepared by:** ojies · **Compiled:** 2026-06-28 · **Updated:** 2026-07-01

This workspace now holds **three linked layers** that build on each other — a **data layer**
(Nigeria FDI/FPI and its determinants), an **analysis layer** (a Big-Debt-Cycle diagnosis *plus an
eight-model quantitative stack*), and an **application layer** (an opportunity assessment for
building at the intersection of the informal economy, AI, and Bitcoin/stablecoins). Read this
file first.

```
nigeria_data/
├── NIGERIA_RESEARCH_OVERVIEW.md          ← you are here
├── nigeria_fdi_fpi/                       ← DATA LAYER (the evidence base)
└── informal_economy_ai_bitcoin/           ← APPLICATION LAYER (the opportunity)
    ├── MASTER_REPORT.md                    ← start here for layer 3
    ├── README.md + 6 thematic deep-dives
    └── debt_cycle/                         ← ANALYSIS LAYER (macro engine + models)
        ├── README.md · ANALYSIS.md · DATA_NOTES.md · SOURCES.md
        ├── 17 data CSVs (1980–2026) + 21 sourced staging files
        ├── 8 models (graph · VAR · SFC · scenario · GCN · positioning · MonteCarlo)
        └── MODEL_AND_TRACKER · GRAPH_MODEL · ADVANCED_MODELS · ANALOGUE_CALIBRATION · POSITIONING
```

> **Note on structure (2026-06-29):** the debt-cycle study (formerly the top-level
> `nigeria_debt_cycle_forecast/`) now lives **inside** `informal_economy_ai_bitcoin/` as
> `debt_cycle/`, where it serves as **Part 0 (the macro engine)** of the opportunity
> assessment. Its CSVs still reference the FDI/FPI data layer via `../../nigeria_fdi_fpi/`.

---

## How the three layers relate

`nigeria_fdi_fpi/` is the **measured evidence**: capital flows (FDI & FPI from World Bank,
IMF, UNCTAD, CBN, NBS), plus the variables that explain them — governance (the six WGI),
macro fundamentals, markets/monetary pull factors, global push factors, and institutional
indices. Everything is sourced, with net-vs-gross and observed-vs-derived clearly separated.

`informal_economy_ai_bitcoin/debt_cycle/` is the **interpretation**: it takes that evidence,
places Nigeria within Ray Dalio's *Principles for Navigating Big Debt Crises* template, and
projects where the average Nigerian's finances are likely to be by 2030. It pulls the
external sector, governance, and FX/market series straight from the data layer and adds
forward-looking IMF projections and a dedicated debt-gauges table.

`informal_economy_ai_bitcoin/` (the rest) is the **application**: it asks what to *build*
given that macro reality. The debt cycle's central finding — that an inflationary
deleveraging is transferring wealth away from naira-holding households — *is the demand
engine* for the report's thesis: dollar access (via stablecoins) and AI-underwritten credit
for the informal economy. The opportunity assessment is, in effect, "what the household and
the informal trader do to cope with the debt cycle, and where a business can serve that."

**Two threads run through all three layers:**
1. **The six governance variables** (rule of law, regulatory quality, political stability,
   government effectiveness, control of corruption, voice & accountability) are *FDI/FPI
   determinants* in the data layer, the *swing factor* that decides whether the deleveraging
   is "beautiful" or "ugly" in the analysis layer, and the *top regulatory/execution risk* in
   the application layer.
2. **The naira / FX path** is the dependent variable in the data layer, the headline symptom
   in the analysis layer, and the demand driver (and margin risk) in the application layer.

---

## Layer 1 — `nigeria_fdi_fpi/` (data layer)

Annual 2000–2025 unless noted. Full column dictionary in its `README.md`; build plan and
source status in `DATA_CATALOG_AND_PLAN.md`.

| Theme | Files |
|---|---|
| Capital flows | `nigeria_FDI_yearly.csv`, `nigeria_FPI_yearly.csv` (World Bank/IMF, UNCTAD, CBN, NBS side by side) |
| Governance (6 WGI) | `nigeria_governance_WGI_yearly.csv` |
| Macro controls (14) | `nigeria_macro_controls_yearly.csv` |
| External & markets | `nigeria_external_markets_yearly.csv` |
| Markets & monetary | `nigeria_markets_monetary.csv` (NGX, MPR, T-bill, Eurobond, ratings) |
| Global push factors | `nigeria_global_push_factors.csv` (Fed funds, VIX, oil, global FDI) |
| Greenfield & M&A | `nigeria_greenfield_manda.csv` (UNCTAD) |
| Institutional indices | `nigeria_institutions_indices.csv` (CPI, Doing Business, Heritage, Fraser, ICRG) |
| NBS capital importation | by type / sub-component / sector / country / quarterly (5 files) |
| Derived variables (52) | `nigeria_fdi_fpi_derived.csv` (%GDP, per-capita, logs, ratios, etc.) |
| Event indicators | `nigeria_event_indicators.csv` (author-constructed crisis/regime markers — **not** observed data) |
| **Tidy long panel** | `nigeria_fdi_fpi_tidy_long.csv` — everything in one file (1,916 rows, 85 variables, 11 categories) for econometrics |

**Two framing rules** (detailed in its README): (1) keep **net** BoP flows and **gross**
NBS capital-importation separate — they measure different things; (2) distinguish
**observed** data from **derived** (formula) and **constructed** (event indicators).

## Layer 2 — `informal_economy_ai_bitcoin/debt_cycle/` (analysis layer)

Substantially expanded from the original 4-file forecast into a **strengthened dataset + an
eight-model quantitative stack**. Start with its `README.md`; read `DATA_NOTES.md` before using
any CSV (it documents four 2023–25 statistical breaks — CPI/GDP/unemployment rebasings + the
naira float).

**Diagnosis & data** (17 CSVs, annual **1980–2026** + quarterly; 21 sourced staging files):
| Group | Files |
|---|---|
| Diagnosis | `ANALYSIS.md` (base/bull/bear + household projection), `README.md`, `DATA_NOTES.md`, `SOURCES.md` |
| Core gauges | `nigeria_debt_cycle_gauges.csv` (31 cols, 2015–26), `..._quarterly.csv`, external-debt profile + Eurobond wall, `imf_weo_...csv` |
| Long history | `nigeria_historical_precycle.csv` (1980–2014 incl. the 2005–06 Paris Club relief) |
| Thematic | monetary/credit, markets, sectoral GDP, labour, cost-of-living, consumer, financial-inclusion, fiscal-detail, security/human-dev, **migration/japa**, private-capital/VC |
| Sub-national | `state_panel.csv` (36 states + FCT: MPI poverty, IGR, population, fragility) |

**The eight-model stack** (`uv run python <script>.py`; managed by `pyproject.toml`):
| Model | Question | Key finding |
|---|---|---|
| `graph_model.py` (Mantegna MST) | which gauges are hubs? | **current account = system hub**; spine oil→CA→reserves→FX→inflation |
| `var_model.py` (VAR + IRF) | transmission with lags? | **oil → FX (1-yr lag) → inflation** (Granger-significant) |
| `sfc_model.py` / `sfc_national.py` (stock-flow) | full feedback? | closed 4-sector SFC (Walras≈0) with the **dollarization doom-loop** |
| `scenario_model.py` | base/bull/bear to 2030? | central path: dollar income doesn't regain 2023 by 2030 + quarterly tracker |
| `state_gcn.py` (spatial GCN) | sub-national poverty? | border graph beats no-graph **8–18%** on real NBS data |
| `positioning_model.py` | what to own? | **carry + USD-stablecoin/gold barbell** |
| `montecarlo_model.py` | the full distribution? | 40k-draw regime-mixture MC → fan charts + event odds (P(regain 2023 income)≈26%) + portfolio VaR |
| calibration | scenario weights | analogues (Argentina/Turkey/Egypt/Ghana) → **base 55 / bull 20 / bear 25** |
| docs | | `MODEL_AND_TRACKER.md`, `GRAPH_MODEL.md`, `ADVANCED_MODELS.md`, `ANALOGUE_CALIBRATION.md`, `POSITIONING.md` |

## Layer 3 — `informal_economy_ai_bitcoin/` (application layer)

An opportunity/product assessment: can a business be built at the intersection of the
informal economy + AI + Bitcoin/stablecoins in Africa & Nigeria? Start with `MASTER_REPORT.md`.

| File | Contents |
|---|---|
| **`MASTER_REPORT.md`** | **Integrated synthesis** — exec summary, Part 0 (macro engine) → Part IX (niche verdict), key-figures table |
| `README.md` | Foundation overview (informal economy size, enablers, AI, Bitcoin, niche) |
| `competitor_landscape.md` | Three-layer teardown (payments / B2B retail / crypto) + white-space map |
| `ai_credit_underwriting.md` | Alternative-data credit scoring, real cases, the data moat |
| `offramp_liquidity_layer.md` | The stablecoin off-ramp / liquidity "picks-and-shovels" niche |
| `bitcoin_treasury_companies_africa.md` | Can the MicroStrategy/Strategy model be replicated in Africa? |
| `regulatory_risk_memo.md` | Nigeria crypto/FX law, licensing path, ranked risk register |
| `product_spec_trader_account.md` | Spec for "TradeDollar" — a dollar operating account for informal traders |
| `debt_cycle/` | Layer 2 (above), embedded as Part 0 |

**Headline conclusion:** the durable opportunity is a *financial-services company for the
informal economy that uses AI to underwrite and stablecoins to settle*, built on a licensed
liquidity layer, with crypto invisible to the user. Ranked wedges: (1) the off-ramp/liquidity
layer, (2) a dollar operating account for cross-border informal traders/freelancers,
(3) stablecoin treasury-as-a-service for SMEs. Top risk: regulatory whipsaw.

---

## The whole story in three lines

1. **(Data → Analysis)** Nigeria is mid-way through an **inflationary deleveraging** (Dalio's
   archetype for non-reserve, local-currency-debt economies): the state's finances are being
   fixed by a collapsing naira and high inflation rather than by default. The **sovereign**
   gauges are healing; the **household** is paying for it (dollar income per capita halved
   2023→2024, not back to 2023 levels by 2030).
2. **(Analysis → Application)** That household wealth-transfer is exactly why ~95% of surveyed
   Nigerians prefer to be paid in stablecoins. The informal economy (~80–90% of jobs) copes
   with the debt cycle by reaching for **dollars (via stablecoins)** and surviving without
   formal credit — the two pains an AI + stablecoin venture can serve.
3. **(The build)** Don't bet on the naira keeping collapsing: across base/bull/bear scenarios
   the durable business monetises **dollar-denominated flow and credit**, not currency
   collapse — and survives the whipsaw by being the most licensed, compliant, naira-friendly
   operator in the room. The upside, like the deleveraging itself, ultimately turns on the
   six **governance** variables — so watch those, inflation, and the naira.
4. **(The models close the loop)** The quantitative stack independently confirms the story from
   the data up: the graph finds the **current account** is the system hub, the VAR times the
   **oil→FX→inflation** chain, and the stock-flow model *generates* the **dollarization loop**
   that is precisely the stablecoin demand the application layer sets out to serve — so the
   macro engine and the business opportunity are two views of one mechanism.

*No 5-year macro path is certain; the analysis is built as scenarios with explicit triggers so
probabilities can be updated as the gauges move. Scenario probabilities are ojies'
judgement; all data is attributed in the respective folders, and the application-layer reports
carry ~200 inline-cited web sources.*
