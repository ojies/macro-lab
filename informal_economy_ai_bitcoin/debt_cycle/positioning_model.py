#!/usr/bin/env python3
"""
Nigeria Debt-Cycle — Positioning Model  (Phase 4)
=================================================
Translates the calibrated base/bull/bear scenarios (55/20/25) into asset-class implications.
All returns are expressed in USD total return (annualized, ~2026-2029 horizon) — because for a
Nigerian saver, an SME, or a foreign allocator the binding question is the dollar outcome after
FX, which is exactly what the debt cycle drives.

Computes per asset: probability-weighted expected USD return, scenario dispersion (downside risk),
and a simple risk-adjusted score (excess return over the USD/stablecoin 'safe' leg / dispersion).

The scenario return assumptions are illustrative-but-reasoned (see POSITIONING.md for the logic
behind each cell) and tie to the model outputs: base FX drifts to ~1880, bull appreciates,
bear slides to ~3000; disinflation rallies duration in base/bull and crashes it in bear; the
naira destroys NGX USD returns except when the currency is stable.
Run:  uv run python positioning_model.py
"""
import os, csv
HERE = os.path.dirname(os.path.abspath(__file__))

WEIGHTS = {"base": 0.55, "bull": 0.20, "bear": 0.25}   # from ANALOGUE_CALIBRATION.md

# asset -> {scenario: USD total return % p.a.}   (see POSITIONING.md §per-asset for rationale)
ASSETS = {
    "NGN T-bills (1yr)":        {"base": 11, "bull": 15, "bear":  2},
    "FGN bonds (10yr, NGN)":    {"base": 14, "bull": 24, "bear": -12},
    "FGN Eurobonds (USD)":      {"base":  9, "bull": 13, "bear": -8},
    "NGX equities (USD)":       {"base":  8, "bull": 22, "bear": -18},
    "NGX banks (USD)":          {"base": 12, "bull": 28, "bear": -16},
    "USD / stablecoin (yield)": {"base":  5, "bull":  4, "bear":  6},
    "Lagos real estate (USD)":  {"base":  3, "bull":  8, "bear": -5},
    "Gold / BTC (tail hedge)":  {"base":  6, "bull":  2, "bear": 18},
}
SAFE = "USD / stablecoin (yield)"


def stats(ret):
    mu = sum(WEIGHTS[s]*ret[s] for s in WEIGHTS)
    var = sum(WEIGHTS[s]*(ret[s]-mu)**2 for s in WEIGHTS)
    downside = sum(WEIGHTS[s]*min(0, ret[s])**2 for s in WEIGHTS) ** 0.5  # downside semi-dev
    return mu, var**0.5, downside


def main():
    safe_mu = stats(ASSETS[SAFE])[0]
    rows = []
    for a, ret in ASSETS.items():
        mu, sd, dn = stats(ret)
        sharpe = (mu - safe_mu) / sd if sd > 0 else float("inf")
        rows.append(dict(asset=a, base=ret["base"], bull=ret["bull"], bear=ret["bear"],
                         exp_usd_return=round(mu, 1), dispersion=round(sd, 1),
                         downside=round(dn, 1), risk_adj=round(sharpe, 2)))

    print("="*92)
    print("NIGERIA DEBT-CYCLE POSITIONING MODEL — USD total return by scenario  (weights 55/20/25)")
    print("="*92)
    hdr = f"{'asset':<26}{'base':>6}{'bull':>6}{'bear':>7}{'E[USD]':>8}{'disp':>7}{'downsd':>8}{'risk-adj':>9}"
    print(hdr); print("-"*92)
    for r in sorted(rows, key=lambda x: -x["exp_usd_return"]):
        print(f"{r['asset']:<26}{r['base']:>6}{r['bull']:>6}{r['bear']:>7}"
              f"{r['exp_usd_return']:>8}{r['dispersion']:>7}{r['downside']:>8}{r['risk_adj']:>9}")
    print("-"*92)

    out = os.path.join(HERE, "positioning_returns.csv")
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(f"Wrote {out}\n")

    # barbell verdict
    best_ret = max(rows, key=lambda x: x["exp_usd_return"])
    best_radj = max(rows, key=lambda x: x["risk_adj"])
    print("READ:")
    print(f"  Highest expected USD return : {best_ret['asset']} (E={best_ret['exp_usd_return']}%)")
    print(f"  Best risk-adjusted          : {best_radj['asset']} (risk-adj={best_radj['risk_adj']})")
    print("  The 55/20/25 (fat bear tail) world favours a BARBELL: carry/short-duration NGN + USD-")
    print("  stablecoin & gold/BTC as the bear hedge. Long-duration FGN bonds & broad equities are")
    print("  high-beta bets on the 20% bull. Eurobonds are the moderate USD-carry middle.")


if __name__ == "__main__":
    main()
