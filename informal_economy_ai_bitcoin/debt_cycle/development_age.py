#!/usr/bin/env python3
"""
Nigeria — Development-Age Model  (comparative macro / catch-up analysis)
=======================================================================
Compares countries by DEVELOPMENT LEVEL, not calendar year. Answers: "Nigeria today is at
the income the US/UK/Korea/China passed through decades ago — where were they, what happened
next, and — crucially — do Nigeria's INITIAL CONDITIONS let it follow the good path or not?"

Four layers (data from the countries_*.csv panels, Maddison 2011$ PPP + WB/IMF):
  1. FRONTIER-EQUIVALENT YEAR  — the calendar year each country was at Nigeria's current
     GDP/capita (log-linear interpolation between benchmarks). Nigeria's "economic age".
  2. STRUCTURAL ANOMALY        — Nigeria-now vs the escapers AT THE SAME INCOME: Nigeria is
     urbanizing WITHOUT industrializing (the key deviation from the East-Asian template).
  3. CATCH-UP PATH MENU        — what the escapers (Korea/China/Japan) vs the stall (Brazil)
     did over the next ~40 years (growth, savings, debt, years-to-double).
  4. DIVERGENCE CONDITIONING   — the 7-factor scorecard that TILTS the raw analogy: same income
     level, very different odds. Prevents naive "Nigeria = Korea-1970 -> Nigeria becomes Korea".

Honest stance: the income parallel is arithmetic; the *outcome* is conditional on initial
conditions. This model reports both, and never claims Nigeria WILL follow any analogue.
Run:  uv run python development_age.py
"""
import os
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
NIG = "Nigeria"


def load():
    g = pd.read_csv(os.path.join(HERE, "countries_gdp_pc_ppp.csv"))
    d = pd.read_csv(os.path.join(HERE, "countries_development_indicators.csv"))
    c = pd.read_csv(os.path.join(HERE, "countries_catchup_macro.csv"))
    v = pd.read_csv(os.path.join(HERE, "countries_divergence_factors.csv"))
    return g, d, c, v


def crossover_year(cg, target):
    """First calendar year a country reached `target` GDP/capita (log-linear interp)."""
    cg = cg.sort_values("year")
    ys, gs = cg["year"].values, cg["gdp_pc_ppp"].values
    if gs.max() < target:
        return None                                   # never reached it (still below)
    for i in range(1, len(ys)):
        if gs[i-1] < target <= gs[i]:
            f = (np.log(target)-np.log(gs[i-1]))/(np.log(gs[i])-np.log(gs[i-1]))
            return ys[i-1] + f*(ys[i]-ys[i-1])
    return ys[0] if gs[0] >= target else None


def main():
    g, d, c, v = load()
    nig_now = g[(g.country == NIG)].sort_values("year").iloc[-1]
    LEVEL = nig_now["gdp_pc_ppp"]; YEAR = int(nig_now["year"])
    nig_peak = g[g.country == NIG]["gdp_pc_ppp"].max()

    print("="*78)
    print("NIGERIA DEVELOPMENT-AGE MODEL — comparison by development level, not calendar year")
    print("="*78)
    print(f"\nNigeria {YEAR}: ${LEVEL:,.0f}/capita (Maddison 2011$ PPP) — its 'economic age'.")
    print(f"  (Peaked at ${nig_peak:,.0f} c.2010 and has DECLINED since — a lost ~decade, going backwards.)")

    # ---- 1. FRONTIER-EQUIVALENT YEAR ----
    print(f"\n[1] FRONTIER-EQUIVALENT YEAR — when each country was at Nigeria's ${LEVEL:,.0f} level:")
    rows = []
    for ctry in ["United States", "United Kingdom", "Germany", "Japan", "South Korea",
                 "China", "Brazil", "Indonesia", "Vietnam", "India"]:
        yr = crossover_year(g[g.country == ctry], LEVEL)
        if yr:
            print(f"    Nigeria {YEAR}  ≈  {ctry:<15} in ~{yr:.0f}   ({YEAR-yr:.0f} years 'behind')")
            rows.append({"country": ctry, "frontier_equiv_year": round(yr),
                         "years_behind": round(YEAR-yr)})

    # ---- 2. STRUCTURAL ANOMALY vs the escapers at the SAME income ----
    print("\n[2] STRUCTURAL ANOMALY — Nigeria vs the East-Asian escapers AT THE SAME INCOME:")
    def ind(ctry, yr):
        row = d[(d.country == ctry) & (d.year == yr)]
        return row.iloc[0] if len(row) else None
    anchors = [("Nigeria", 2023), ("South Korea", 1970), ("China", 1980)]
    print(f"    {'(same ~$2.2k income)':<22}{'life exp':>9}{'urban %':>9}{'industry%':>10}{'fertility':>10}")
    for ctry, yr in anchors:
        r = ind(ctry, yr)
        if r is not None:
            print(f"    {ctry+' '+str(yr):<22}{r['life_expectancy']:>9.0f}{r['urban_pct']:>9.0f}"
                  f"{r['industry_pct_gdp']:>10.0f}{r['fertility_rate']:>10.1f}")
    print("    -> Nigeria is FAR more urban (62% vs Korea's 41%) but LESS industrial (19% vs 25% and")
    print("       falling, not rising) and lower life-expectancy: urbanization WITHOUT industrialization.")

    # ---- 3. CATCH-UP PATH MENU ----
    print("\n[3] CATCH-UP PATH MENU — from this income level, what happened over ~40 years:")
    first = c[c.decade_from_nigeria_level == "0-10yr"]
    print(f"    {'case':<14}{'decade':>9}{'growth%':>8}{'savings%':>9}{'debt/GDP':>9}{'exports%':>9}  verdict")
    verdicts = {"Japan": "ESCAPED ~8yr-double", "South Korea": "ESCAPED ~10yr-double",
                "China": "ESCAPED (debt risk)", "United States": "escaped (slow,~40yr)",
                "United Kingdom": "leader, slow", "Germany": "reset 60yr by wars",
                "Brazil": "*** STALLED 40yr+"}
    for _, r in first.iterrows():
        print(f"    {r['country']:<14}{r['stage_decade']:>9}{r['real_growth_pct']:>8.1f}"
              f"{r['savings_rate_pct']:>9.0f}{r['debt_gdp_pct']:>9.0f}{r['exports_pct_gdp']:>9.0f}"
              f"  {verdicts.get(r['country'],'')}")
    print("    Escaper template: 35-45% savings + export manufacturing + LOW debt -> double in ~8-10yr.")
    print("    Stall (Brazil): ~18-20% savings, weak exports, inflation/debt -> 40yr+ to barely double.")

    # ---- Nigeria's ACTUAL trajectory -> years to double ----
    g10 = g[(g.country == NIG) & (g.year == 2010)]["gdp_pc_ppp"].iloc[0]
    nig_cagr = (LEVEL/g10)**(1/(YEAR-2010)) - 1
    print(f"\n    Nigeria's ACTUAL 2010->{YEAR} per-capita growth: {nig_cagr*100:+.1f}%/yr (going backwards).")
    print(f"    Years to DOUBLE income from here at various rates:")
    for rate in [0.08, 0.05, 0.03, 0.015]:
        print(f"        at {rate*100:>4.1f}%/yr : {np.log(2)/np.log(1+rate):>4.0f} yrs")
    print(f"        at Nigeria's recent {nig_cagr*100:+.1f}%/yr : never (diverging)")

    # ---- 4. DIVERGENCE CONDITIONING ----
    tmap = {"favourable": 1, "neutral": 0, "adverse": -1}
    v["t"] = v["tilt"].map(tmap)
    score = (v["t"]*v["weight_1to3"]).sum(); wmax = v["weight_1to3"].sum()
    readiness = (score + wmax)/(2*wmax)*100
    print("\n[4] DIVERGENCE CONDITIONING — same income, different odds (the invariance guardrail):")
    print(f"    {'factor':<28}{'tilt':>11}{'weight':>8}")
    for _, r in v.iterrows():
        print(f"    {r['factor']:<28}{r['tilt']:>11}{r['weight_1to3']:>8}")
    print(f"\n    Structural-readiness index: {readiness:.0f}/100  "
          f"({int((v.tilt=='adverse').sum())}/{len(v)} factors adverse, "
          f"{int((v.tilt=='favourable').sum())} favourable)")

    print("\n" + "="*78)
    print("CONDITIONED VERDICT")
    print("="*78)
    print(f"  • ARITHMETIC: Nigeria today sits at Korea-1970 / China-1983 / US-1860s income.")
    print(f"  • STRUCTURAL: it lacks the escaper preconditions — urbanizing without industry,")
    print(f"    manufacturing ~8-9% (falling), savings ~15-20% (vs 35-45%), and all 7 conditioning")
    print(f"    factors currently adverse (security, institutions, oil-curse, human capital,")
    print(f"    premature deindustrialization, global headwinds, demographics) — though demographics")
    print(f"    is the one with latent upside if fertility falls and a jobs engine appears.")
    print(f"  • ODDS: the income parallel is UNEARNED — on initial conditions Nigeria's path sits")
    print(f"    far closer to the Brazil STALL than the Korea ESCAPE. It is not even matching Brazil")
    print(f"    yet: per-capita income has FALLEN since 2010. Escape requires security + institutions")
    print(f"    + fertility + human capital + a manufacturing jobs-ladder to flip together — the same")
    print(f"    governance swing-factor the debt-cycle tracker already flags as the top bear trigger.")

    # persist
    summ = pd.DataFrame(rows)
    summ["nigeria_level_2011ppp"] = round(LEVEL)
    summ.to_csv(os.path.join(HERE, "development_age_summary.csv"), index=False)
    print(f"\nWrote development_age_summary.csv  (readiness index: {readiness:.0f}/100)")


if __name__ == "__main__":
    main()
