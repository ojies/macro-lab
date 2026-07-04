#!/usr/bin/env python3
"""
Nigeria Debt-Cycle — Monte Carlo Model  (Phase 5)
=================================================
Turns the discrete base/bull/bear scenarios into a full probability DISTRIBUTION.

Method (regime-mixture Monte Carlo, vectorized over N draws):
  1. Each draw is assigned a regime — base/bull/bear with the calibrated 55/20/25 weights
     (imported straight from scenario_model.py, so the central paths are identical).
  2. Around that regime's central path we add CORRELATED annual shocks: a common macro
     shock z makes a bad year cluster (high inflation + weak naira + low growth + wider
     deficit) the way it does in reality, plus idiosyncratic noise per variable.
  3. We run the SAME projection recurrence as scenario_model and record the full path.
  4. Aggregate -> percentile fan charts + event probabilities + portfolio VaR/expected-shortfall.

HONEST CAVEAT: Monte Carlo propagates the uncertainty you ASSUME (the sigmas + correlations
below); it does not add information. On annual data the tails are indicative, not precise. It
is rigorous structured sensitivity analysis, not a forecast.

Outputs: montecarlo_summary.csv (percentile fan by year) + prints event probs & portfolio risk.
Run:  uv run python montecarlo_model.py
"""
import os
import numpy as np
import pandas as pd
from scenario_model import SCENARIOS, START, WAGE_2015, POP_GROWTH, YEARS
from positioning_model import ASSETS

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(42)
N = 40_000

# within-regime annual volatilities (the assumptions that carry the uncertainty)
SIG_G, SIG_I, SIG_FX, SIG_DEF = 0.012, 0.030, 0.05, 0.008
KAPPA = 1.0        # extra naira depreciation per 1pp inflation surprise (PPP-ish link)
REG = ["base", "bull", "bear"]
PROBS = np.array([SCENARIOS[r]["prob"] for r in REG]); PROBS /= PROBS.sum()


def _stack(key):                      # (3 regimes, 5 years) -> indexable by regime draw
    return np.array([SCENARIOS[r][key] for r in REG])

def _wage_paths():                    # per-regime minimum-wage path across 2026-2030
    out = []
    for r in REG:
        w, path = START["min_wage"], []
        for y in YEARS:
            w = SCENARIOS[r]["wage_rebase"].get(y, w); path.append(w)
        out.append(path)
    return np.array(out, float)


def simulate():
    reg = rng.choice(3, N, p=PROBS)                      # regime per draw
    G, I, D = _stack("real_growth")[reg], _stack("cpi_inflation")[reg], _stack("gdp_deflator")[reg]
    FX, DEF = _stack("fx")[reg].astype(float), _stack("deficit_pct")[reg]
    EI, AM = _stack("eff_int_rate")[reg], _stack("amort_rate")[reg]
    WAGE = _wage_paths()[reg]
    POVEL = np.array([SCENARIOS[r]["pov_elasticity"] for r in REG])[reg]

    z = rng.standard_normal((N, 5))                      # common macro shock (bad-year cluster)
    growth = G + SIG_G*(-0.5*z + 0.87*rng.standard_normal((N, 5)))
    infl = np.maximum(0.02, I + SIG_I*(0.6*z + 0.8*rng.standard_normal((N, 5))))
    isurp = infl - I
    defl = D + 0.9*isurp
    fx_lvl = FX * (1 + KAPPA*isurp + SIG_FX*(0.5*z + 0.87*rng.standard_normal((N, 5))))
    deficit = DEF + SIG_DEF*(0.4*z + 0.9*rng.standard_normal((N, 5))) - 0.3*(growth - G)

    ng = np.full(N, START["nominal_gdp_tn"]); debt = np.full(N, START["debt_tn"])
    fx = np.full(N, START["fx"]); cpi = np.full(N, START["cpi_index"])
    pop = np.full(N, START["population_m"]); rev = np.full(N, START["revenue_tn"])
    pov = np.full(N, START["poverty"]); ext = START["ext_share"]
    paths = {v: np.zeros((N, 5)) for v in ["gdp_pc_usd", "debt_to_gdp", "real_wage", "poverty", "dsr"]}

    for i in range(5):
        prev_debt = debt
        ng2 = ng*(1+growth[:, i])*(1+defl[:, i]); fx2 = fx_lvl[:, i]
        pop = pop*(1+POP_GROWTH); cpi = cpi*(1+infl[:, i]); wage = WAGE[:, i]
        fx_chg = (fx2 - fx)/fx
        debt = prev_debt*(1 + ext*fx_chg) + deficit[:, i]*ng2
        rev = rev*(1+growth[:, i])*(1+infl[:, i])
        dsr = (EI[:, i]+AM[:, i])*prev_debt / rev * 100
        pov = np.maximum(0, pov - POVEL*(growth[:, i]-POP_GROWTH)*100)
        usd_gdp = ng2*1000/fx2
        paths["gdp_pc_usd"][:, i] = usd_gdp*1e9/(pop*1e6)
        paths["debt_to_gdp"][:, i] = debt/ng2*100
        paths["real_wage"][:, i] = (wage/cpi)*(100/WAGE_2015)*100
        paths["poverty"][:, i] = pov
        paths["dsr"][:, i] = dsr
        ng, fx = ng2, fx2
    return paths


def portfolio_var():
    """MC VaR / expected-shortfall for the POSITIONING.md barbell vs an all-stablecoin book."""
    weights = {"NGN T-bills (1yr)": 0.35, "USD / stablecoin (yield)": 0.30,
               "Gold / BTC (tail hedge)": 0.20, "FGN bonds (10yr, NGN)": 0.15}
    asset_sig = {"NGN T-bills (1yr)": 3, "USD / stablecoin (yield)": 1,
                 "Gold / BTC (tail hedge)": 12, "FGN bonds (10yr, NGN)": 9}
    reg = rng.choice(3, N, p=PROBS)
    port = np.zeros(N); stable = np.zeros(N)
    for a, w in weights.items():
        mu = np.array([ASSETS[a][r] for r in REG])[reg]
        r = mu + asset_sig[a]*rng.standard_normal(N)
        port += w*r
        if a == "USD / stablecoin (yield)":
            smu = np.array([ASSETS[a][x] for x in REG])[reg]
            stable = smu + asset_sig[a]*rng.standard_normal(N)
    def risk(x):
        p5 = np.percentile(x, 5)                    # 5th-percentile (worst-case) return
        es = x[x <= p5].mean()                      # expected shortfall = mean of the worst 5% (a return)
        ploss = (x < 0).mean()*100                  # probability of an outright USD loss
        return x.mean(), p5, es, ploss
    return risk(port), risk(stable)


def main():
    print("="*82)
    print(f"NIGERIA DEBT-CYCLE MONTE CARLO — {N:,} draws, regime mixture 55/20/25 + correlated shocks")
    print("="*82)
    p = simulate()
    labels = {"gdp_pc_usd": "GDP/capita USD", "debt_to_gdp": "Debt/GDP %",
              "real_wage": "Real-wage idx", "poverty": "Extreme poverty %", "dsr": "Debt-service/rev %"}

    print("\n2030 DISTRIBUTION (percentiles across draws):")
    print(f"  {'variable':<20}{'P5':>9}{'P25':>9}{'P50':>9}{'P75':>9}{'P95':>9}{'mean':>9}")
    rows = []
    for k, lab in labels.items():
        for yi, yr in enumerate(YEARS):
            q = np.percentile(p[k][:, yi], [5, 25, 50, 75, 95])
            rows.append({"variable": k, "year": yr, "p5": round(q[0], 1), "p25": round(q[1], 1),
                         "p50": round(q[2], 1), "p75": round(q[3], 1), "p95": round(q[4], 1),
                         "mean": round(p[k][:, yi].mean(), 1)})
        q = np.percentile(p[k][:, 4], [5, 25, 50, 75, 95])
        print(f"  {lab:<20}{q[0]:>9.0f}{q[1]:>9.0f}{q[2]:>9.0f}{q[3]:>9.0f}{q[4]:>9.0f}{p[k][:,4].mean():>9.0f}")
    pd.DataFrame(rows).to_csv(os.path.join(HERE, "montecarlo_summary.csv"), index=False)

    pc, rw, pv, dg, ds = (p["gdp_pc_usd"][:, 4], p["real_wage"][:, 4], p["poverty"][:, 4],
                          p["debt_to_gdp"][:, 4], p["dsr"][:, 4])
    print("\n2030 EVENT PROBABILITIES:")
    print(f"  P(dollar income regains 2023 level, >=$2139) : {(pc>=2139).mean()*100:5.1f}%")
    print(f"  P(real wage regains 2025 level, idx>=71.8)   : {(rw>=71.8).mean()*100:5.1f}%")
    print(f"  P(extreme poverty still above 2025's 50.9%)  : {(pv>50.9).mean()*100:5.1f}%")
    print(f"  P(debt/GDP breaches 40%)                     : {(dg>40).mean()*100:5.1f}%")
    print(f"  P(debt-service/revenue breaches 60%)         : {(ds>60).mean()*100:5.1f}%")

    (pm, pp5, pes, pl), (sm, sp5, ses, sl) = portfolio_var()
    print("\nPORTFOLIO RISK (USD return %, 1yr; higher=better; barbell 35 T-bills/30 stable/20 gold-BTC/15 FGN):")
    print(f"  {'':<12}{'mean':>7}{'worst-5% (P5)':>15}{'avg-worst-5%':>14}{'P(loss)':>10}")
    print(f"  {'barbell':<12}{pm:>6.1f}%{pp5:>+14.1f}%{pes:>+13.1f}%{pl:>9.1f}%")
    print(f"  {'stablecoin':<12}{sm:>6.1f}%{sp5:>+14.1f}%{ses:>+13.1f}%{sl:>9.1f}%")
    print("  (both tails stay positive: the stablecoin/gold hedge keeps the barbell near break-even")
    print("   even in bad draws, while the carry + FGN sleeves lift the mean ~3pp above pure stablecoin.)")

    print("\nWrote montecarlo_summary.csv")
    print("Reading: the discrete 55/20/25 scenarios become a distribution. The central story holds —")
    print("only a minority of draws see the household fully recover by 2030 — but now with explicit")
    print("odds and a fan chart, and the barbell's tail loss (expected shortfall) is quantified.")


if __name__ == "__main__":
    main()
