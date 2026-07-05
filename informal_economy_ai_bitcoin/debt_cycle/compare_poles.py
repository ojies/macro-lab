#!/usr/bin/env python3
"""
COMPARE POLES — the five-pole debt-cycle matrix, from each module's real gauges
===============================================================================
Reads the latest gauges out of every country module (Nigeria + usa/ + europe/ + china/ + japan/)
and prints (1) a side-by-side matrix and (2) a cross-pole POSITIONING read — what each regime
implies about what to own. The quantitative cells are pulled live from the CSVs; the qualitative
cells (policy space, cycle position, the trap, positioning) are the analytical layer.

The thesis this table encodes: the debt RATIO is not the danger — the POLICY SPACE to manage it is.
Nigeria carries the least debt and the most acute risk; Japan the most debt and a managed grind.

Run (from debt_cycle/):  uv run python compare_poles.py
"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))


def load(csv, debt_col, growth_col=None, infl_col=None, filt=None, macro=None,
         mgrowth=None, minfl=None, growth_fixed=None):
    """Pull latest-year debt / growth / inflation from a module CSV (filt = (col,val) row filter)."""
    try:
        d = pd.read_csv(os.path.join(HERE, csv))
    except FileNotFoundError:
        return None
    if filt:
        d = d[d[filt[0]] == filt[1]]
    d = d.dropna(subset=[debt_col]).sort_values("year")
    last = d.iloc[-1]
    out = {"debt": last[debt_col], "year": int(last["year"])}
    out["infl"] = last[infl_col] if infl_col and pd.notna(last.get(infl_col)) else None
    out["growth"] = growth_fixed
    if growth_col and pd.notna(last.get(growth_col)):
        out["growth"] = last[growth_col]
    if macro:  # growth/inflation from a separate macro CSV (US)
        m = pd.read_csv(os.path.join(HERE, macro)).sort_values("year").iloc[-1]
        if mgrowth: out["growth"] = m[mgrowth]
        if minfl: out["infl"] = m[minfl]
    return out


POLES = [
    dict(name="Nigeria", csv="nigeria_debt_cycle_gauges.csv", debt_col="debt_to_gdp_dmo_pct",
         infl_col="inflation_avg_pct", growth_fixed=3.4, dnote="",
         space=10, cyc="mid inflationary EM", lever="almost none", risk="FX / rollover default",
         trap="no privilege to begin with",
         own="USD / stablecoins + hard assets + dollar-linked cashflows; avoid unhedged naira & local bonds"),
    dict(name="China", csv="china/china_macro.csv", debt_col="govt_debt_pct_gdp",
         growth_col="gdp_growth", infl_col="cpi_inflation", dnote="~300 total",
         space=70, cyc="mid — model exhaustion", lever="managed (state banks, capital controls)",
         risk="deflation / slow stagnation", trap="debt-property-demographic trilemma",
         own="deflation hedges: duration, gold, quality cashflow; avoid property-linked; managed-weaker CNY"),
    dict(name="Euro area", csv="europe/europe_macro.csv", debt_col="debt_gdp_pct",
         growth_col="gdp_growth", infl_col="cpi_inflation", filt=("country", "Euro area"), dnote="Italy 137",
         space=50, cyc="late stagnation", lever="UK own-currency / periphery none",
         risk="fragmentation (Bund spread)", trap="union without fiscal union",
         own="quality / defensives; core over periphery on spread risk; EUR debases less than USD"),
    dict(name="United States", csv="usa/usa_debt_cycle_gauges.csv", debt_col="federal_debt_held_by_public_pct_gdp",
         macro="usa/usa_monetary_macro.csv", mgrowth="real_gdp_growth", minfl="cpi_inflation", dnote="~120 gross",
         space=92, cyc="late (reserve power)", lever="the Fed — vast", risk="inflation / debasement",
         trap="exorbitant privilege eroding",
         own="real assets + gold/BTC as debasement hedge, TIPS; term-premium risk in long Treasuries"),
    dict(name="Japan", csv="japan/japan_macro.csv", debt_col="govt_debt_gross_pct_gdp",
         growth_col="gdp_growth", infl_col="cpi_inflation", dnote="net ~137",
         space=60, cyc="very late (precedent)", lever="BoJ (own currency, exited YCC 2024)",
         risk="stagnation / demographics", trap="30-year deleveraging",
         own="the template: decades of JGBs & deflation now normalizing — BoJ exit = a yen & rate regime shift"),
]


def main():
    print("="*100)
    print("MACRO-LAB — FIVE POLES OF THE DEBT CYCLE   (debt ratio ≠ danger; policy space does)")
    print("="*100)
    data = {p["name"]: load(**{k: p[k] for k in ("csv", "debt_col") if k in p},
                            growth_col=p.get("growth_col"), infl_col=p.get("infl_col"),
                            filt=p.get("filt"), macro=p.get("macro"), mgrowth=p.get("mgrowth"),
                            minfl=p.get("minfl"), growth_fixed=p.get("growth_fixed")) for p in POLES}

    print(f"\n[1] SNAPSHOT — pulled live from each module's gauges:")
    print(f"    {'pole':<15}{'debt/GDP':>10}{'growth':>8}{'inflation':>11}   note")
    for p in POLES:
        d = data[p["name"]]
        if d is None:
            print(f"    {p['name']:<15}{'(pending data — run after japan/ lands)':>44}")
            continue
        g = f"{d['growth']:.1f}%" if d["growth"] is not None else "—"
        i = f"{d['infl']:.1f}%" if d["infl"] is not None else "—"
        note = f"govt gross; {p['dnote']}" if p["dnote"] else "govt"
        print(f"    {p['name']:<15}{d['debt']:>9.0f}%{g:>8}{i:>11}   {note}  ({d['year']})")

    print(f"\n[2] THE MATRIX — same Dalio template, five regimes:")
    print(f"    {'pole':<15}{'space':>6}  {'cycle position':<24}{'central-bank lever':<42}risk")
    for p in POLES:
        print(f"    {p['name']:<15}{p['space']:>5}/100  {p['cyc']:<24}{p['lever']:<42}{p['risk']}")

    print(f"\n[3] POSITIONING READ — what each regime implies to own:")
    for p in POLES:
        print(f"    • {p['name']:<14} {p['own']}")
    print(f"\n    The through-line: dollar-scarcity regimes (Nigeria) reward hard-currency access; debasement")
    print("    regimes (US) reward real assets; deflation/stagnation regimes (China, Japan, Europe core)")
    print("    reward duration & quality. Same cycle, opposite trades at each pole.")

    print("\n" + "-"*100)
    print("Danger is not the debt RATIO (Nigeria 39% is the most acute; Japan 250% the most managed) —")
    print("it is the POLICY SPACE behind it: currency sovereignty, reserve status, who owns the debt.")


if __name__ == "__main__":
    main()
