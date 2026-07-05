#!/usr/bin/env python3
"""
EUROPE — The Stagnation Pole    (macro-lab, Europe module)
==========================================================
The UK and the euro area: aging, low-productivity, high-debt advanced economies — plus the euro's
defining structural fragility. The third pole of macro-lab.

  1. STAGNATION — growth ground down from ~4% (2000) to ~0-1.4% (2024-25); Germany in outright
     recession (2023-24) as the 2022 energy shock hit its industrial model (a terms-of-trade blow
     the energy-exporting US escaped). Aging (Italy median age ~49) + the Draghi productivity gap.
  2. THE EURO'S FRAGILITY — a monetary union WITHOUT a fiscal union: members issue debt in a
     currency they cannot print. The BTP/OAT–Bund SPREAD (Italy/France 10y minus Germany 10y) is
     the market price of that fragility — it blew out in the 2011-12 sovereign crisis and the ECB
     has backstopped it ever since (OMT 'whatever it takes' 2012, PEPP 2020, TPI 2022).
  3. THE UK-vs-PERIPHERY SPLIT — the UK has its OWN currency + central bank (the BoE could and did
     halt the Sep-2022 gilt/LDI crisis unilaterally): its risk is inflation/currency, like a smaller
     US. The euro periphery (Italy ~137% debt) lacks currency control — its risk is categorically
     closer to EM fragility, dependent on the ECB's conditional backstop.

Data: europe_macro.csv (Eurostat, ECB, ONS, BoE, IMF; staging 32).
Run (from debt_cycle/):  uv run python europe/europe_stagnation.py
"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    d = pd.read_csv(os.path.join(HERE, "europe_macro.csv"))
    y10 = d.pivot(index="year", columns="country", values="gov_10y_yield")
    grw = d.pivot(index="year", columns="country", values="gdp_growth")
    print("="*84)
    print("EUROPE — the stagnation pole (aging · low-growth · high-debt · union without fiscal union)")
    print("="*84)

    print("\n[1] 2025 SNAPSHOT vs 2000:")
    print(f"    {'entity':<11}{'growth00':>9}{'growth25':>9}{'CPI22':>7}{'debt25':>8}{'defc25':>8}{'10y25':>7}")
    for c in ["UK", "Euro area", "Germany", "France", "Italy"]:
        g = d[d.country == c].set_index("year")
        print(f"    {c:<11}{g.loc[2000,'gdp_growth']:>9.1f}{g.loc[2025,'gdp_growth']:>9.1f}"
              f"{g.loc[2022,'cpi_inflation']:>7.1f}{g.loc[2025,'debt_gdp_pct']:>8.0f}"
              f"{g.loc[2025,'deficit_gdp_pct']:>8.1f}{g.loc[2025,'gov_10y_yield']:>7.1f}")
    print("    (Germany 2023/24 growth −0.9%/−0.5% — industrial recession on the energy shock)")

    print("\n[2] THE EURO FRAGILITY GAUGE — 10y spread OVER the German Bund (pp):")
    print(f"    {'year':<6}{'Italy–Bund':>12}{'France–Bund':>13}   note")
    notes = {2000:"pre-euro-crisis, tight", 2011:"sovereign crisis", 2012:"'whatever it takes'",
             2022:"TPI announced", 2025:"structurally elevated"}
    for y in [2000, 2011, 2012, 2022, 2025]:
        if y in y10.index:
            it = y10.loc[y, "Italy"] - y10.loc[y, "Germany"]
            fr = y10.loc[y, "France"] - y10.loc[y, "Germany"]
            print(f"    {y:<6}{it:>12.2f}{fr:>13.2f}   {notes.get(y,'')}")
    print("    The spread IS the 'no fiscal union' premium: periphery debt in a currency it can't print.")

    print("\n[3] GROWTH GROUND DOWN (avg real GDP growth):")
    for c in ["UK", "Euro area", "Germany", "France", "Italy"]:
        g = d[d.country == c].set_index("year")["gdp_growth"]
        early, late = g.loc[2000:2007].mean(), g.loc[2018:2025].mean()
        print(f"    {c:<11} 2000-07 {early:>4.1f}%   →   2018-25 {late:>4.1f}%")

    print("\n[4] DIAGNOSIS: a slow 'Japanification' — aging demographics, a widening productivity gap")
    print("    vs the US (Draghi: ~70% of the per-capita gap is productivity), high debt, and little")
    print("    growth to inflate it away. The UK (own currency) can debase or backstop; the euro")
    print("    PERIPHERY cannot — its fragility is structural, priced daily in the Bund spread, and")
    print("    contained only by the ECB's conditional promises. High income, low momentum.")

    print("\n" + "-"*84)
    print("FIVE POLES:  Nigeria (early inflationary EM, no space) · US (late reserve power, vast space)")
    print("Europe (aging stagnation, union w/o fiscal union) · China (state-directed workout) ·")
    print("Japan (the precedent: the balance-sheet recession the others are measured against).")


if __name__ == "__main__":
    main()
