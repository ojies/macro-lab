#!/usr/bin/env python3
"""
USA — Presidential Economic Scorecard   (macro-lab, US module)
==============================================================
Economic outcomes BY ADMINISTRATION (Truman -> current, 1945-2026): growth, jobs, unemployment,
inflation, the market, and deficits — ranked, with the by-party pattern.

READ THIS FIRST — it is "what happened ON their watch", NOT "what they caused":
  • Presidents INHERIT the economy; a term's early years reflect the predecessor's cycle.
  • Policy acts with ~1-2 year lags, and fiscal-year budgets straddle administrations.
  • The FED sets monetary policy independently; CONGRESS controls spending.
  • EXOGENOUS shocks dominate the sign: the only net job loss (Trump-1) and the near-zero
    gain (G.W. Bush) both end in an exogenous recession (COVID, GFC) — the shock, not the
    president, set the outcome. The academic finding (Blinder-Watson 2016) is that the D>R
    growth gap is real on-watch but mostly LUCK (oil shocks, defense, TFP, world timing), not
    policy. Treat every ranking below as accountability-with-context, not causation.

Data: usa_presidents.csv (FRED, Shiller S&P, NBER; staging 29).
Run (from debt_cycle/):  uv run python usa/usa_presidential.py
"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))


def yrs(a, b):
    ay, am = map(int, a.split("-")); by, bm = map(int, b.split("-"))
    return (by + bm/12) - (ay + am/12)


def main():
    df = pd.read_csv(os.path.join(HERE, "usa_presidents.csv"))
    df["years"] = [yrs(a, b) for a, b in zip(df.term_start, df.term_end)]
    df["jobs_per_yr"] = df.jobs_added_m / df.years
    df["unemp_change"] = df.unemp_end - df.unemp_start

    print("="*94)
    print("USA PRESIDENTIAL ECONOMIC SCORECARD — outcomes ON their watch (1945-2026)")
    print("  NOT causation: presidents inherit the economy; the Fed & Congress & shocks dominate. See header.")
    print("="*94)
    h = f"{'president':<17}{'pty':>4}{'GDP%':>6}{'jobs/yr':>8}{'unemp Δ':>9}{'infl%':>6}{'S&P%':>6}{'defc%':>7}{'rec':>4}"
    print("\n"+h); print("-"*len(h))
    for _, r in df.iterrows():
        star = "*" if r.term_end >= "2026" else " "
        ud = f"{r.unemp_change:>+9.1f}" if pd.notna(r.unemp_change) else f"{'n/a':>9}"
        print(f"{r.president+star:<17}{r.party:>4}{r.avg_gdp_growth:>6.1f}{r.jobs_per_yr:>8.2f}"
              f"{ud}{r.avg_inflation:>6.1f}{r.sp500_annual_return:>6.1f}"
              f"{r.avg_deficit_pct_gdp:>7.1f}{int(r.recessions):>4}")
    print("  * Trump-2 term in progress (through mid-2026); jobs/yr annualized; defc = avg deficit %GDP (neg=deficit)")

    full = df[df.term_end < "2026"]                              # exclude in-progress term from rankings
    def top(col, n=3, asc=False, fmt="{:.2f}"):
        s = full.sort_values(col, ascending=asc).head(n)
        return " · ".join(f"{r.president} ({fmt.format(r[col])})" for _, r in s.iterrows())
    print("\nRANKINGS (completed terms):")
    print(f"  Fastest GDP growth   : {top('avg_gdp_growth', fmt='{:.1f}%')}")
    print(f"  Most jobs/yr         : {top('jobs_per_yr', fmt='{:.2f}m')}")
    print(f"  Best S&P (price) ret : {top('sp500_annual_return', fmt='{:.1f}%')}")
    print(f"  Biggest unemp drop   : {top('unemp_change', asc=True, fmt='{:+.1f}pp')}")
    print(f"  Widest deficits      : {top('avg_deficit_pct_gdp', asc=True, fmt='{:.1f}%')}")
    print(f"  Highest inflation    : {top('avg_inflation', fmt='{:.1f}%')}")

    print("\nBY PARTY (completed terms, simple averages — an ON-WATCH correlation, not causation):")
    for p, name in [("D", "Democrats"), ("R", "Republicans")]:
        g = full[full.party == p]
        print(f"  {name:<12} GDP {g.avg_gdp_growth.mean():.2f}%  jobs/yr {g.jobs_per_yr.mean():.2f}m  "
              f"infl {g.avg_inflation.mean():.1f}%  S&P {g.sp500_annual_return.mean():.1f}%  "
              f"deficit {g.avg_deficit_pct_gdp.mean():.1f}%  (n={len(g)})")
    gap = full[full.party=="D"].avg_gdp_growth.mean() - full[full.party=="R"].avg_gdp_growth.mean()
    print(f"  -> D minus R GDP-growth gap on-watch: {gap:+.1f}pp. This matches Blinder-Watson (2016):")
    print("     the gap is REAL but attributed mostly to LUCK (oil shocks, defense, productivity, world")
    print("     timing) landing under D terms — NOT to party policy. Do not read it as 'Democrats cause growth'.")

    print("\nSHOCK DOMINATES THE SIGN:")
    for _, r in full.sort_values("jobs_per_yr").head(2).iterrows():
        print(f"  {r.president}: {r.jobs_added_m:+.1f}m jobs, {int(r.recessions)} recession(s) — ended in an exogenous")
        print(f"     {'COVID' if 'Trump' in r.president else 'GFC'} shock that set the outcome, not the administration.")

    df.to_csv(os.path.join(HERE, "usa_presidents_scored.csv"), index=False)
    print(f"\nWrote usa_presidents_scored.csv")


if __name__ == "__main__":
    main()
