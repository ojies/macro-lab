#!/usr/bin/env python3
"""
JAPAN — The Precedent: bubble → balance-sheet recession → lost decades   (macro-lab, Japan module)
==================================================================================================
The economy every other pole is measured against. Japan ran the modern playbook FIRST — a 1980s
asset bubble, its 1990 burst, a Richard-Koo balance-sheet recession, mild deflation for ~25 years,
and the world's highest public debt that never triggered a crisis. It also pioneered every tool
(ZIRP → QE → QQE → NIRP/YCC → the 2024 exit) the Fed and ECB later copied.

  THE DEBT PARADOX — the single most important lesson for the other poles: gross debt ~206% of GDP
  coexisted with the WORLD'S LOWEST yields. Why it never became a crisis: the debt is domestically
  owned (~90%+, the BoJ alone holds ~half of all JGBs), yen-denominated with its own backstopping
  central bank, funded by high domestic savings, and Japan is the world's largest net external
  CREDITOR (positive NIIP). WHO owns the debt and in WHAT currency matters more than the ratio.

Data: japan_macro.csv (IMF WEO, BoJ, MOF, World Bank; staging 34).
Run (from debt_cycle/):  uv run python japan/japan_model.py
"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    d = pd.read_csv(os.path.join(HERE, "japan_macro.csv")).set_index("year")
    print("="*86)
    print("JAPAN — the precedent: bubble → balance-sheet recession → lost decades → normalization")
    print("="*86)

    print("\n[1] THE ARC — growth, deflation, and the debt ramp that filled the demand gap:")
    print(f"    {'year':<6}{'growth':>8}{'CPI':>7}{'policy%':>9}{'debt/GDP':>10}{'BoJ%GDP':>9}{'JGB10y':>8}   era")
    eras = {1989:"bubble peak (Nikkei ~38,900)", 1990:"the burst", 1995:"deflation sets in",
            2000:"ZIRP", 2012:"pre-Abenomics", 2016:"NIRP + YCC", 2020:"COVID / max QE",
            2024:"BoJ EXIT (1st hike since '07)", 2025:"normalizing"}
    for y in [1989, 1990, 1995, 2000, 2012, 2016, 2020, 2024, 2025]:
        r = d.loc[y]
        boj = f"{r['boj_balance_sheet_pct_gdp']:>8.0f}" if pd.notna(r["boj_balance_sheet_pct_gdp"]) else f"{'—':>8}"
        print(f"    {y:<6}{r['gdp_growth']:>7.1f}%{r['cpi_inflation']:>7.1f}{r['policy_rate']:>9.2f}"
              f"{r['govt_debt_gross_pct_gdp']:>9.0f}%{boj}{r['jgb_10y_yield']:>8.2f}   {eras.get(y,'')}")

    defl = d.loc[1995:2020, "cpi_inflation"]
    print(f"\n[2] THE DEFLATION STRETCH: CPI averaged {defl.mean():+.1f}% across 1995-2020 — a quarter-century")
    print(f"    near zero. Debt gross {d.loc[1990,'govt_debt_gross_pct_gdp']:.0f}% (1990) → "
          f"{d.loc[2024,'govt_debt_gross_pct_gdp']:.0f}% (2024): private deleveraging offset by public borrowing.")

    print(f"\n[3] THE DEBT PARADOX: {d.loc[2025,'govt_debt_gross_pct_gdp']:.0f}% gross debt (net "
          f"{d.loc[2025,'govt_debt_net_pct_gdp']:.0f}%), BoJ balance sheet {d.loc[2024,'boj_balance_sheet_pct_gdp']:.0f}% of GDP —")
    print("    yet JGB yields stayed the world's lowest. Domestic (~90%+) + yen + own CB + net-creditor")
    print("    status = record debt with no crisis. (Note: IMF revised gross debt down ~25-30pp from the")
    print("    older ~250% basis; the 'highest in the developed world' headline still holds.)")

    print(f"\n[4] THE 2022-24 REGIME CHANGE: inflation returned ({d.loc[2022,'cpi_inflation']:.1f}% → "
          f"{d.loc[2024,'cpi_inflation']:.1f}%), and the BoJ EXITED — ending NIRP/YCC in Mar-2024, its first")
    print(f"    hike since 2007; policy rate {d.loc[2024,'policy_rate']:.2f}% → {d.loc[2025,'policy_rate']:.2f}%. The lost-decades")
    print("    regime may finally be turning — the tightening the other poles will watch closely.")

    print("\n[5] WHAT JAPAN TEACHES THE POLES:")
    print("    • Europe = the vulnerable case: shared currency, NO shared treasury — periphery lacks Japan's")
    print("      'own central bank + own currency' backstop.")
    print("    • China = the most Japan-like: high but domestic debt, closed capital account, property bust,")
    print("      aging — the balance-sheet-recession setup, but at MIDDLE income (Japan was already rich).")
    print("    • US = has the reserve-currency + own-CB backstop, so 'Japanification' is a chronic-drag risk,")
    print("      not a default risk. Nigeria = the opposite pole: none of Japan's cushions.")

    print("\n" + "-"*86)
    print("Japan is the control experiment for the whole lab: it proves the debt RATIO is not destiny —")
    print("currency sovereignty, domestic ownership, and net-creditor status are. The five-pole through-line.")


if __name__ == "__main__":
    main()
