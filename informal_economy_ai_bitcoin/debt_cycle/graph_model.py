#!/usr/bin/env python3
"""
Nigeria Debt-Cycle — Graph / Network Model (Mantegna MST + directed lead-lag)
============================================================================
Unsupervised structure discovery over the macro gauges, adapting the Mantegna (1999)
correlation-network + Minimum-Spanning-Tree idea from asset networks to a small macro panel.

THREE outputs:
  1. MST (undirected): distance d_ij = sqrt(2*(1-corr_ij)); keep each variable's strongest links.
     -> recovers the economic blocs (external / price / real / policy) with NO labels.
  2. Centrality + informative-neighbour: the hub variables, and the single best-correlated
     gauge for each target (the "informative neighbour" -> what to watch for each target).
  3. Directed lead-lag network: for each pair, compare corr(x_{t-1}, y_t) vs corr(y_{t-1}, x_t)
     to infer which variable LEADS -> an approximate transmission map (oil -> FX -> inflation -> ...).

HONEST CAVEATS (see MODEL_AND_TRACKER.md / graph section of README):
  - Annual data: ~47 obs for long variables (1980-2026), only ~11 for 2015-only variables.
    Correlations on n~11 are noisy -> exploratory, not inferential. Long-panel results are the
    reliable ones; short-variable links are flagged.
  - Level vs rate handling: stock/level series (FX, reserves, oil price, debt) use YoY % change;
    rate/ratio series (growth, inflation, CA%GDP, MPR, DSR, poverty) use levels. Mixing is standard
    in macro but documented here for transparency.
  - Undirected MST != causation; the directed lead-lag layer is a heuristic, not formal Granger.

Dependencies: pandas, numpy only (MST via hand-rolled Prim; no scipy needed).
"""
import os, math
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------
# 1. Build a harmonised annual panel 1980-2026 from the strengthened CSVs.
#    Long variables splice historical (<=2014) + gauges/imf (>=2015).
# ----------------------------------------------------------------------------
def load():
    hist = pd.read_csv(os.path.join(HERE, "nigeria_historical_precycle.csv")).set_index("year")
    gau  = pd.read_csv(os.path.join(HERE, "nigeria_debt_cycle_gauges.csv")).set_index("year")
    imf  = pd.read_csv(os.path.join(HERE, "imf_weo_nigeria_projections.csv")).set_index("year")

    def splice(hist_col, gau_col, imf_col=None):
        s = pd.Series(index=range(1980, 2027), dtype=float)
        if hist_col: s.loc[1980:2014] = hist[hist_col].reindex(range(1980, 2015))
        if gau_col:  s.loc[2015:2026] = gau[gau_col].reindex(range(2015, 2027))
        if imf_col:  s.loc[2015:2026] = imf[imf_col].reindex(range(2015, 2027))
        return s

    p = pd.DataFrame({
        "gdp_growth":     splice("real_gdp_growth_pct", None, imf_col="real_gdp_growth_pct"),
        "inflation":      splice("inflation_avg_pct", "inflation_avg_pct"),
        "fx":             splice("ngn_usd_official_avg", "ngn_usd_official_ye"),
        "reserves":       splice("reserves_usd_bn", "reserves_gross_cbn_usd_bn"),
        "oil_price":      splice("oil_price_usd_bbl", "bonny_light_usd_bbl"),
        "current_acct":   splice("current_account_pct_gdp", "current_account_pct_gdp"),
        "ext_debt_usd":   splice("external_debt_wdi_usd_bn", "total_debt_usd_bn"),
        # short variables (2015+ only) — flagged downstream as low-n
        "mpr":            splice(None, "mpr_ye_pct"),
        "debt_service":   splice(None, "debt_service_rev_gross_pct"),
        "real_wage":      splice(None, "real_min_wage_idx_2015"),
        "poverty":        splice(None, "extreme_poverty_3usd_pct"),
    })
    return p

# Stock/level series -> YoY % change; rate/ratio series -> level.
LEVELS = {"fx", "reserves", "oil_price", "ext_debt_usd"}
RATES  = {"gdp_growth", "inflation", "current_acct", "mpr", "debt_service", "real_wage", "poverty"}
SHORT  = {"mpr", "debt_service", "real_wage", "poverty"}   # ~11 obs -> flag as low-n

def change_panel(p):
    out = pd.DataFrame(index=p.index)
    for c in p.columns:
        out[c] = p[c].pct_change(fill_method=None)*100 if c in LEVELS else p[c]
    return out

# The reliable backbone: long variables only (~40+ annual obs, 1980-2026).
LONG = ["gdp_growth", "inflation", "fx", "reserves", "oil_price", "current_acct", "ext_debt_usd"]

# ----------------------------------------------------------------------------
# 2. Correlation, Mantegna distance, MST (Prim), centrality, neighbours.
# ----------------------------------------------------------------------------
def corr_and_distance(panel, method="pearson", min_overlap=8):
    cols = list(panel.columns)
    n = len(cols)
    C = pd.DataFrame(np.eye(n), index=cols, columns=cols)
    for i in range(n):
        for j in range(i+1, n):
            a, b = panel[cols[i]], panel[cols[j]]
            mask = a.notna() & b.notna()
            if mask.sum() >= min_overlap:
                r = a[mask].corr(b[mask], method=method)
            else:
                r = np.nan
            C.iloc[i, j] = C.iloc[j, i] = r
    D = np.sqrt(2*(1 - C))   # Mantegna distance
    return C, D

def mst_prim(D):
    cols = list(D.columns); n = len(cols)
    # only connect nodes reachable via non-NaN distances
    visited = [0]; edges = []
    Dv = D.values.copy()
    np.fill_diagonal(Dv, np.inf)
    Dv = np.where(np.isnan(Dv), np.inf, Dv)
    while len(visited) < n:
        best = (None, None, np.inf)
        for u in visited:
            for v in range(n):
                if v not in visited and Dv[u, v] < best[2]:
                    best = (u, v, Dv[u, v])
        if best[0] is None: break   # disconnected (NaN gaps)
        edges.append((cols[best[0]], cols[best[1]], round(best[2], 3)))
        visited.append(best[1])
    return edges

def informative_neighbours(C):
    """For each variable, the single most-correlated other variable (|corr|)."""
    res = {}
    for t in C.columns:
        s = C[t].drop(t).dropna()
        if len(s):
            best = s.abs().idxmax()
            res[t] = (best, round(C.loc[t, best], 2))
    return res

# ----------------------------------------------------------------------------
# 3. Directed lead-lag: does x lead y, or y lead x?
# ----------------------------------------------------------------------------
def lead_lag(panel, min_overlap=8):
    cols = list(panel.columns); links = []
    for i in range(len(cols)):
        for j in range(len(cols)):
            if i == j: continue
            x, y = panel[cols[i]], panel[cols[j]]
            m = x.shift(1).notna() & y.notna()
            if m.sum() < min_overlap: continue
            r = x.shift(1)[m].corr(y[m])
            if pd.notna(r):
                links.append((cols[i], cols[j], round(r, 2)))   # x_{t-1} -> y_t
    return links


def main():
    p = load()
    panel = change_panel(p)

    # --- (A) RELIABLE BACKBONE: long variables only, ~40+ obs ------------------
    longpanel = panel[LONG]
    Cl, Dl = corr_and_distance(longpanel, min_overlap=20)

    print("="*72)
    print("NIGERIA DEBT-CYCLE GRAPH MODEL  (Mantegna MST + directed lead-lag)")
    print("="*72)
    print("\n### A. RELIABLE BACKBONE — 7 long variables, 1980-2026 (~40+ obs) ###")

    print("\n[A1] MINIMUM SPANNING TREE (unlabeled bloc structure):")
    edges_l = mst_prim(Dl)
    for a, b, d in edges_l:
        print(f"    {a:<14} --- {b:<14}  d={d}")

    print("\n[A2] HUB CENTRALITY (MST degree = system hubs):")
    deg = {}
    for a, b, _ in edges_l:
        deg[a] = deg.get(a, 0)+1; deg[b] = deg.get(b, 0)+1
    for k, v in sorted(deg.items(), key=lambda x: -x[1]):
        print(f"    {k:<14} degree {v}")

    print("\n[A3] INFORMATIVE NEIGHBOUR (best gauge to watch for each):")
    for t, (nb, r) in informative_neighbours(Cl).items():
        print(f"    {t:<14} <- {nb:<14} (corr {r})")

    print("\n[A4] DIRECTED LEAD-LAG (|r|>=0.45, x_t-1 -> y_t):")
    ll = [e for e in lead_lag(longpanel, min_overlap=20) if abs(e[2]) >= 0.45]
    for a, b, r in sorted(ll, key=lambda x: -abs(x[2]))[:12]:
        print(f"    {a:<14} -> {b:<14} (lead-corr {r})")

    # --- (B) EXPLORATORY: include the 2015+ household/policy variables ----------
    Cf, _ = corr_and_distance(panel, min_overlap=9)
    print("\n### B. EXPLORATORY — household/policy targets (2015+, n~11, WEAK) ###")
    print("[B1] INFORMATIVE NEIGHBOUR for the short targets (treat as hypotheses):")
    for t in SHORT:
        s = Cf[t].drop(t).dropna()
        if len(s):
            nb = s.abs().idxmax()
            print(f"    {t:<14} <- {nb:<14} (corr {round(Cf.loc[t, nb],2)})  [n~11, weak]")

    # persist
    pd.DataFrame(edges_l, columns=["node_a","node_b","distance"]).to_csv(
        os.path.join(HERE, "graph_mst_edges.csv"), index=False)
    Cl.round(3).to_csv(os.path.join(HERE, "graph_correlation_matrix.csv"))
    print("\nWrote graph_mst_edges.csv and graph_correlation_matrix.csv (backbone)")


if __name__ == "__main__":
    main()
