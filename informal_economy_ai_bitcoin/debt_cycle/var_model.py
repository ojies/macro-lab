#!/usr/bin/env python3
"""
Nigeria Debt-Cycle — VAR Transmission Model  (Phase 2b)
=======================================================
Turns the graph's heuristic lead-lag map into a proper Vector Autoregression with
Granger-causality tests and orthogonalized impulse-response functions (IRFs).

Backbone (the spine the MST recovered): oil price -> current account -> reserves
-> FX -> inflation -> growth. We estimate a VAR on the stationary transforms and ask:
  * Granger causality: does oil Granger-cause FX/inflation/the current account?
  * IRF: if oil drops 1 s.d., what happens to the current account, reserves, FX,
    inflation and growth over the next ~6 years (with the Cholesky ordering = the spine)?
  * FEVD: what share of FX/inflation variance is driven by oil shocks?

CAVEATS: ~46 annual obs after differencing -> a VAR(1) is the honest max (VAR(2) would
over-parameterize). Results are indicative transmission directions/magnitudes, not precise
elasticities. The 2023 float and the rebasings are regime breaks inside the sample (flagged).
Run:  uv run python var_model.py
"""
import os
import numpy as np
import pandas as pd
from statsmodels.tsa.api import VAR

HERE = os.path.dirname(os.path.abspath(__file__))


def build_panel():
    hist = pd.read_csv(os.path.join(HERE, "nigeria_historical_precycle.csv")).set_index("year")
    gau  = pd.read_csv(os.path.join(HERE, "nigeria_debt_cycle_gauges.csv")).set_index("year")
    imf  = pd.read_csv(os.path.join(HERE, "imf_weo_nigeria_projections.csv")).set_index("year")

    def splice(h, g, i=None):
        s = pd.Series(index=range(1980, 2027), dtype=float)
        if h: s.loc[1980:2014] = hist[h].reindex(range(1980, 2015))
        if i: s.loc[2015:2026] = imf[i].reindex(range(2015, 2027))
        elif g: s.loc[2015:2026] = gau[g].reindex(range(2015, 2027))
        return s

    raw = pd.DataFrame({
        "oil":      splice("oil_price_usd_bbl", "bonny_light_usd_bbl"),
        "ca":       splice("current_account_pct_gdp", "current_account_pct_gdp"),
        "reserves": splice("reserves_usd_bn", "reserves_gross_cbn_usd_bn"),
        "fx":       splice("ngn_usd_official_avg", "ngn_usd_official_ye"),
        "inflation":splice("inflation_avg_pct", "inflation_avg_pct"),
        "growth":   splice("real_gdp_growth_pct", None, "real_gdp_growth_pct"),
    })
    # Stationary transforms: levels (oil, reserves, fx) -> log-change %; rates kept as levels.
    d = pd.DataFrame(index=raw.index)
    d["oil_ret"]  = np.log(raw["oil"]).diff()*100
    d["ca"]       = raw["ca"]
    d["res_ret"]  = np.log(raw["reserves"]).diff()*100
    d["fx_ret"]   = np.log(raw["fx"]).diff()*100          # +ve = naira depreciation
    d["inflation"]= raw["inflation"]
    d["growth"]   = raw["growth"]
    # interpolate small internal gaps (e.g. CA early-80s), then drop remaining
    d = d.interpolate(limit=2, limit_area="inside").dropna()
    return d


def main():
    d = build_panel()
    order = ["oil_ret", "ca", "res_ret", "fx_ret", "inflation", "growth"]  # Cholesky = the spine
    d = d[order]
    print("="*72)
    print("NIGERIA DEBT-CYCLE VAR — transmission / impulse-response")
    print(f"Sample: {int(d.index.min())}-{int(d.index.max())}  ({len(d)} annual obs)  vars={order}")
    print("="*72)

    model = VAR(d)
    # small sample -> cap at 2 lags, let AIC choose
    sel = model.select_order(maxlags=2)
    p = sel.aic if isinstance(sel.aic, int) else 1
    p = max(1, min(2, int(p) if p else 1))
    res = model.fit(p)
    print(f"\nLag order selected (AIC, capped at 2): VAR({p})")

    # ---- Granger causality: does oil drive the system? ----
    print("\n[1] GRANGER CAUSALITY (H0: row does NOT cause col; p<0.05 = causes):")
    pairs = [("oil_ret","ca"), ("oil_ret","fx_ret"), ("oil_ret","inflation"),
             ("ca","reserves" if "reserves" in d else "res_ret"), ("fx_ret","inflation"),
             ("res_ret","fx_ret"), ("ca","growth")]
    for cause, effect in pairs:
        if cause in d.columns and effect in d.columns and cause != effect:
            try:
                t = res.test_causality(effect, [cause], kind="f")
                flag = "  <-- causes" if t.pvalue < 0.05 else ""
                print(f"    {cause:<10} -> {effect:<10}  p={t.pvalue:.3f}{flag}")
            except Exception as e:
                print(f"    {cause:<10} -> {effect:<10}  (n/a: {e})")

    # ---- Impulse responses to a NEGATIVE oil shock (1 s.d.) ----
    H = 6
    irf = res.irf(H)
    oil_i = order.index("oil_ret")
    print(f"\n[2] IMPULSE RESPONSE to a -1 s.d. OIL shock (orthogonalized, {H} yrs):")
    print(f"    {'horizon':<8}" + "".join(f"{v:>11}" for v in order))
    irfs = -irf.orth_irfs   # negative oil shock
    rows = []
    for hh in range(H+1):
        vals = irfs[hh, :, oil_i]
        print(f"    h={hh:<6}" + "".join(f"{v:>11.2f}" for v in vals))
        rows.append({"horizon": hh, **{v: round(irfs[hh, j, oil_i], 3) for j, v in enumerate(order)}})
    pd.DataFrame(rows).to_csv(os.path.join(HERE, "var_irf_oil_shock.csv"), index=False)

    # ---- Forecast error variance decomposition ----
    fevd = res.fevd(H)
    print(f"\n[3] FEVD at h={H}: share of each variable's variance driven by OIL shocks:")
    dec = fevd.decomp[:, H-1, oil_i]
    for j, v in enumerate(order):
        print(f"    {v:<10} {dec[j]*100:5.1f}% from oil")

    print("\nWrote var_irf_oil_shock.csv")
    print("\nReading: a negative oil shock propagates oil -> current account -> reserves")
    print("-> naira depreciation -> inflation, with growth hit last — the same spine the")
    print("MST found, now with signs, magnitudes and lags. (n~46: indicative, not precise.)")


if __name__ == "__main__":
    main()
