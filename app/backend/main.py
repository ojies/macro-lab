"""
macro-lab API — serves the model outputs (the debt_cycle CSVs) as JSON for the dashboard frontend.
Run (from app/backend/):  uv run uvicorn main:app --reload --port 8000
Docs at http://localhost:8000/docs
"""
import os
from pathlib import Path
import numpy as np
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Model data dir: env override (used in Docker) else the in-repo path.
DATA = Path(os.environ.get(
    "MODEL_DATA_DIR",
    Path(__file__).resolve().parents[2] / "informal_economy_ai_bitcoin" / "debt_cycle",
))

app = FastAPI(title="macro-lab API", version="0.1.0",
              description="Serves the macro-lab quantitative models as JSON.")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


def rows(path, **read_kwargs):
    """Read a CSV under DATA into a list of dict rows (NaN -> None). Empty list if missing."""
    p = DATA / path
    if not p.exists():
        return []
    df = pd.read_csv(p, **read_kwargs)
    return df.replace({np.nan: None}).to_dict("records")


def last_valid(path, col, filt=None):
    p = DATA / path
    if not p.exists():
        return None
    df = pd.read_csv(p)
    if filt:
        df = df[df[filt[0]] == filt[1]]
    df = df.dropna(subset=[col]).sort_values("year")
    return None if df.empty else df.iloc[-1]


# ---- qualitative layer (single source of truth for the narrative cells) ----
POLES_META = {
    "Nigeria":       dict(order=0, color="#eb6834", space=10, cycle="mid inflationary EM",
                          lever="almost none", risk="FX / rollover default", trap="no privilege to begin with",
                          own="USD / stablecoins + hard assets; avoid unhedged naira & local bonds"),
    "China":         dict(order=1, color="#e34948", space=70, cycle="mid — model exhaustion",
                          lever="managed (state banks, capital controls)", risk="deflation / slow stagnation",
                          trap="debt-property-demographic trilemma",
                          own="deflation hedges: duration, gold, quality cashflow; managed-weaker CNY"),
    "Euro area":     dict(order=2, color="#1baf7a", space=50, cycle="late stagnation",
                          lever="UK own-currency / periphery none", risk="fragmentation (Bund spread)",
                          trap="union without fiscal union",
                          own="quality / defensives; core over periphery; EUR debases less than USD"),
    "United States": dict(order=3, color="#2a78d6", space=92, cycle="late (reserve power)",
                          lever="the Fed — vast", risk="inflation / debasement", trap="exorbitant privilege eroding",
                          own="real assets + gold/BTC debasement hedge, TIPS; term-premium risk in long bonds"),
    "Japan":         dict(order=4, color="#8b909b", space=60, cycle="very late (precedent)",
                          lever="BoJ (own currency, exited YCC 2024)", risk="stagnation / demographics",
                          trap="30-year deleveraging",
                          own="the template: JGBs & deflation now normalizing — BoJ exit = a regime shift"),
}


@app.get("/api/health")
def health():
    return {"ok": True, "data_dir": str(DATA), "data_present": DATA.exists()}


@app.get("/api/index")
def macro_index():
    """Composite resilience/fragility index (macro_index_scores.csv)."""
    return {"pillars": {"buffer": 0.40, "sustainability": 0.30, "vitality": 0.30},
            "poles": rows("macro_index_scores.csv")}


@app.get("/api/poles")
def poles():
    """Five-pole matrix: debt/GDP + growth + inflation pulled live, plus the qualitative cells."""
    specs = [
        ("Nigeria", "nigeria_debt_cycle_gauges.csv", "debt_to_gdp_dmo_pct", None, "inflation_avg_pct", None, 3.4),
        ("China", "china/china_macro.csv", "govt_debt_pct_gdp", "gdp_growth", "cpi_inflation", None, None),
        ("Euro area", "europe/europe_macro.csv", "debt_gdp_pct", "gdp_growth", "cpi_inflation", ("country", "Euro area"), None),
        ("United States", "usa/usa_debt_cycle_gauges.csv", "federal_debt_held_by_public_pct_gdp", None, None, None, None),
        ("Japan", "japan/japan_macro.csv", "govt_debt_gross_pct_gdp", "gdp_growth", "cpi_inflation", None, None),
    ]
    out = []
    for name, csv, dcol, gcol, icol, filt, gfix in specs:
        r = last_valid(csv, dcol, filt)
        debt = float(r[dcol]) if r is not None else None
        growth = gfix
        infl = None
        if r is not None:
            if gcol and pd.notna(r.get(gcol)):
                growth = float(r[gcol])
            if icol and pd.notna(r.get(icol)):
                infl = float(r[icol])
        if name == "United States":  # growth/inflation from the monetary panel
            m = last_valid("usa/usa_monetary_macro.csv", "real_gdp_growth")
            if m is not None:
                growth, infl = float(m["real_gdp_growth"]), float(m["cpi_inflation"])
        meta = POLES_META[name]
        out.append({"name": name, "debt_gdp": debt, "growth": growth, "inflation": infl,
                    "year": int(r["year"]) if r is not None else None, **meta})
    out.sort(key=lambda x: x["order"])
    return {"poles": out}


@app.get("/api/development-age")
def development_age():
    return {
        "summary": rows("development_age_summary.csv"),
        "trajectories": rows("countries_gdp_pc_ppp.csv"),
        "divergence": rows("countries_divergence_factors.csv"),
        "montecarlo": rows("montecarlo_summary.csv"),
        "nigeria_level_ppp": 2207,
        # per-dimension "Korea-equivalent year" (from development_age.py [1b])
        "dimensions": [
            {"dim": "Health (life expectancy)", "korea_year": 1961},
            {"dim": "Structure (agriculture share)", "korea_year": 1969},
            {"dim": "Income (GDP/capita)", "korea_year": 1970},
            {"dim": "Demography (fertility)", "korea_year": 1970},
            {"dim": "Urbanization", "korea_year": 1983},
        ],
    }


@app.get("/api/us")
def usa():
    return {
        "gauges": rows("usa/usa_debt_cycle_gauges.csv"),
        "irf": rows("usa/usa_var_irf_ratehike.csv"),
        "cycles": rows("usa/usa_fed_cycles.csv"),
        "presidents": rows("usa/usa_presidents.csv"),
        "monetary": rows("usa/usa_monetary_macro.csv"),
    }


@app.get("/api/reserves")
def reserves():
    df = pd.read_csv(DATA / "usa/usa_debt_cycle_gauges.csv")
    keep = ["year", "usd_share_global_reserves_pct", "foreign_held_treasury_pct"]
    df = df[keep].dropna(how="all", subset=keep[1:])
    return {"series": df.replace({np.nan: None}).to_dict("records")}


@app.get("/api/demographics")
def demographics():
    data = rows("demographics.csv")
    return {"available": bool(data), "countries": data}


@app.get("/")
def root():
    return {"service": "macro-lab API",
            "endpoints": ["/api/health", "/api/index", "/api/poles", "/api/development-age",
                          "/api/us", "/api/reserves", "/api/demographics", "/docs"]}
