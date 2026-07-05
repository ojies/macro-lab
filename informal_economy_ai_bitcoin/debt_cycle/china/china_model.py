#!/usr/bin/env python3
"""
CHINA — State-Directed Growth Model at Exhaustion    (macro-lab, China module)
==============================================================================
The great catch-up (the escaper of the development-age model) now facing its own reckoning:
a debt / property / demographic trilemma. The fourth pole of macro-lab.

  1. THE DEBT RAMP — total non-financial debt 127% -> ~300% of GDP (2000-2025), and the rising
     CREDIT-INTENSITY OF GROWTH: each point of growth now takes ~3x the credit it did in the 2000s
     (diminishing returns to the debt-fuelled-investment model).
  2. THE PROPERTY BUST — real-estate investment ~14% -> ~6% of GDP (more than halved since 2015),
     with CPI near zero (2023-25) flashing balance-sheet-recession / deflation risk.
  3. THE DEMOGRAPHIC CLIFF — working-age share peaked 2010, fertility ~1.0 (among the world's
     lowest), population shrinking since ~2022: 'grows old before rich' at ~$13.7k GNI/capita —
     roughly a THIRD of Japan's income when Japan aged and its bubble burst in 1990.

Policy space (vs the other poles): China is a net external creditor (~$3.2tn reserves), closed
capital account, sovereign currency, state-owned banks — tools to FORCE a slow, forbearing
workout rather than face a market-driven crisis. But none of that resolves the structural
trilemma. Not Nigeria's FX crisis, not the US's reserve privilege — a managed, Japan-style grind.

Data: china_macro.csv (World Bank, BIS, IMF, NBS/PBoC; staging 33).
Run (from debt_cycle/):  uv run python china/china_model.py
"""
import os
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    d = pd.read_csv(os.path.join(HERE, "china_macro.csv")).set_index("year")
    print("="*82)
    print("CHINA — the state-directed growth model at exhaustion (Dalio + development lens)")
    print("="*82)

    print("\n[1] THE DEBT RAMP — growth slows as leverage triples:")
    print(f"    {'year':<6}{'growth%':>8}{'CPI%':>6}{'debt/GDP':>9}{'govt':>7}{'h/hold':>7}{'corp':>7}{'prop%':>7}")
    for y in [2000, 2007, 2010, 2015, 2019, 2022, 2024, 2025]:
        r = d.loc[y]
        g = lambda c: f"{r[c]:>7.1f}" if pd.notna(r[c]) else f"{'—':>7}"
        print(f"    {y:<6}{r.gdp_growth:>8.1f}{r.cpi_inflation:>6.1f}{r.total_nonfinancial_debt_pct_gdp:>9.0f}"
              f"{g('govt_debt_pct_gdp')}{g('household_debt_pct_gdp')}{g('corporate_debt_pct_gdp')}{g('property_investment_pct_gdp')}")

    # credit intensity of growth: debt added per point of cumulative real growth
    def intensity(a, b):
        dd = d.loc[b, "total_nonfinancial_debt_pct_gdp"] - d.loc[a, "total_nonfinancial_debt_pct_gdp"]
        gsum = d.loc[a+1:b, "gdp_growth"].sum()
        return dd / gsum
    i00, i10 = intensity(2000, 2010), intensity(2010, 2024)
    print(f"\n[2] CREDIT-INTENSITY OF GROWTH (debt-%pts added per point of cumulative GDP growth):")
    print(f"    2000s: {i00:.2f}   →   2010-2024: {i10:.2f}   ({i10/i00:.1f}× more credit per unit of growth)")
    print("    The debt-fuelled-investment engine is spinning faster to move the car slower.")

    prop_peak = d["property_investment_pct_gdp"].max()
    print(f"\n[3] THE PROPERTY BUST + DEFLATION RISK:")
    print(f"    Real-estate investment {prop_peak:.0f}% (2015 peak) → {d.loc[2025,'property_investment_pct_gdp']:.0f}% of GDP (2025) — more than halved.")
    print(f"    CPI {d.loc[2023,'cpi_inflation']:.1f}% / {d.loc[2024,'cpi_inflation']:.1f}% / {d.loc[2025,'cpi_inflation']:.1f}% (2023-25) — near-zero: balance-sheet-recession / deflation risk.")

    print(f"\n[4] THE DEMOGRAPHIC CLIFF — 'old before rich':")
    print(f"    Working-age share peaked {d['working_age_pop_pct'].max():.1f}% (2010) → {d.loc[2025,'working_age_pop_pct']:.1f}% (2025).")
    print(f"    Fertility {d.loc[2010,'fertility_rate']:.2f} (2010) → {d.loc[2024,'fertility_rate']:.2f} (2024) — among the world's lowest; population shrinking since ~2022.")
    print("    GNI/capita ~$13.7k sits right at the high-income line — but China is aging at ~1/3 of")
    print("    Japan's 1990 income. The demographic dividend that powered the catch-up is now reversing.")

    print("\n[5] DIAGNOSIS: growth-model exhaustion, not (yet) a crisis. The savings/investment engine")
    print("    (~43% investment, financial repression, land finance, SOE credit) has hit debt saturation")
    print("    just as property deflates and the workforce shrinks — the Japan 'balance-sheet recession'")
    print("    setup, but at middle income with the high-income transition unresolved. China's closed")
    print("    capital account + state banks + $3.2tn reserves let it FORCE a slow, forbearing workout")
    print("    (stretch losses over years) — avoiding a market crash but risking a decade of ~stagnation.")

    print("\n" + "-"*82)
    print("FOUR POLES:  Nigeria = early inflationary EM (no space) · US = late reserve power (vast space)")
    print("Europe = aging stagnation (union without fiscal union) · China = state-directed workout")
    print("(managed space, structural exhaustion). The development-age model's escaper now meets its")
    print("own big-debt-cycle — the catch-up and the debt cycle are two chapters of one story.")


if __name__ == "__main__":
    main()
