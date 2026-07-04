#!/usr/bin/env python3
"""
USA — Monetary-Policy VAR + Fed-Cycle Event Study   (macro-lab, US module)
==========================================================================
The US pole of macro-lab. Where Nigeria is an inflationary EM cycle with no policy space,
the US is a reserve-currency economy whose central lever is the Fed. This models that lever:

  1. MONETARY-TRANSMISSION VAR (Christiano-Eichenbaum-Evans recursive identification):
     order [GDP growth, inflation, unemployment, fed funds] with fed funds LAST, so the
     monetary-policy shock is the orthogonal innovation to the funds rate. We trace a +100bp
     rate shock through GDP, unemployment and inflation, with Granger tests and a variance
     decomposition. (Annual data 1960-2025, ~66 obs -> indicative magnitudes, not precise.)

  2. FED-CYCLE EVENT STUDY: every tightening cycle since 1970 tagged hard-landing (recession)
     vs soft-landing -> the base rate that a soft landing is historically rare.

Data: usa_monetary_macro.csv, usa_fed_cycles.csv (FRED / NBER / Fed, staging 27-28).
Run (from debt_cycle/):  uv run python usa/usa_monetary_var.py
"""
import os
import numpy as np
import pandas as pd
from statsmodels.tsa.api import VAR

HERE = os.path.dirname(os.path.abspath(__file__))
ORDER = ["real_gdp_growth", "cpi_inflation", "unemployment_rate", "fed_funds_rate"]  # Cholesky: funds last


def main():
    df = pd.read_csv(os.path.join(HERE, "usa_monetary_macro.csv")).set_index("year")
    d = df[ORDER].dropna()
    print("="*76)
    print("USA MONETARY-POLICY VAR — how a Fed rate shock transmits to the economy")
    print(f"Sample {int(d.index.min())}-{int(d.index.max())} ({len(d)} annual obs) · "
          "recursive ID, funds rate ordered last")
    print("="*76)

    model = VAR(d)
    sel = model.select_order(maxlags=2)
    p = 2 if (sel.aic is None or int(sel.aic) >= 2) else max(1, int(sel.aic))
    res = model.fit(p)
    print(f"\nLag order: VAR({p})")

    ff = ORDER.index("fed_funds_rate")
    print("\n[1] GRANGER CAUSALITY — does the fed funds rate drive the macro variables?")
    for eff in ["real_gdp_growth", "unemployment_rate", "cpi_inflation"]:
        t = res.test_causality(eff, ["fed_funds_rate"], kind="f")
        flag = "  <-- causes" if t.pvalue < 0.05 else ""
        print(f"    fed_funds -> {eff:<20} p={t.pvalue:.3f}{flag}")

    H = 6
    irf = res.irf(H)
    orth = irf.orth_irfs                      # [h, response, shock]
    norm = orth[0, ff, ff]                    # h0 response of funds to its own shock = 1 s.d.
    scaled = orth[:, :, ff] / norm            # responses per +100bp funds shock
    print(f"\n[2] IMPULSE RESPONSE to a +100bp FED FUNDS shock (annual horizon, pp deviation):")
    print(f"    {'horizon':<9}" + "".join(f"{v.split('_')[0][:9]:>11}" for v in ORDER))
    rows = []
    for h in range(H+1):
        print(f"    h={h:<7}" + "".join(f"{scaled[h, j]:>11.2f}" for j in range(len(ORDER))))
        rows.append({"horizon": h, **{v: round(scaled[h, j], 3) for j, v in enumerate(ORDER)}})
    pd.DataFrame(rows).to_csv(os.path.join(HERE, "usa_var_irf_ratehike.csv"), index=False)

    ue = scaled[:, ORDER.index("unemployment_rate")]
    gd = scaled[:, ORDER.index("real_gdp_growth")]
    print(f"\n    Read: a +100bp hike lifts unemployment by ~{ue.max():.2f}pp (peak h={ue.argmax()}) and")
    print(f"    knocks ~{-gd.min():.2f}pp off GDP growth (trough h={gd.argmin()}). Inflation may tick UP")
    print("    first (the 'price puzzle' — a known VAR artifact from omitting commodity prices).")

    fevd = res.fevd(H)
    dec = fevd.decomp[:, H-1, ff]
    print(f"\n[3] FEVD at h={H}: share of each variable's variance driven by MONETARY shocks:")
    for j, v in enumerate(ORDER):
        print(f"    {v:<22}{dec[j]*100:5.1f}%")

    # ---- Event study ----
    cyc = pd.read_csv(os.path.join(HERE, "usa_fed_cycles.csv"))
    print("\n" + "="*76)
    print("FED-CYCLE EVENT STUDY — does tightening end in recession?  (cycles since 1970)")
    print("="*76)
    print(f"    {'cycle':<16}{'start%':>7}{'peak%':>7}{'+bp':>6}   {'landing':<14}recession?")
    for _, r in cyc.iterrows():
        print(f"    {r['cycle_label']:<16}{r['start_rate_pct']:>7.2f}{r['peak_rate_pct']:>7.2f}"
              f"{int(r['total_hike_bp']):>6}   {r['landing']:<14}{r['followed_by_recession']}")
    hard = (cyc.landing == "hard").sum(); soft = cyc.landing.str.startswith("soft").sum()
    exo = (cyc.landing == "exogenous").sum()
    policy = hard + soft
    print(f"\n    Base rate (policy-linked cycles, excl. the 2020 COVID/exogenous case):")
    print(f"      hard landings (recession): {hard}   soft landings: {soft}   -> soft-landing rate ~{soft/policy*100:.0f}%")
    print("    A clean soft landing is historically RARE — 1994-95 is the only universally-agreed case")
    print("    (1983-84 the other strong one). The 2022-23 cycle (+525bp, fastest in 4 decades) shows")
    print("    no recession ~3yr on — a provisional 3rd soft landing, but the historical prior sits against it.")

    print("\n" + "-"*76)
    print("MACRO-LAB TWO POLES:  US = reserve-currency cycle, the Fed is the lever (this model);")
    print("Nigeria = inflationary EM cycle, no policy space (the debt_cycle stack). Same toolkit,")
    print("opposite ends of the debt-cycle spectrum.")


if __name__ == "__main__":
    main()
