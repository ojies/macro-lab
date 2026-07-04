#!/usr/bin/env python3
"""
USA — Big Debt Cycle Diagnosis + the "two poles" comparison    (macro-lab, US module)
=====================================================================================
Applies Ray Dalio's Big-Debt-Cycle template (the same lens used on Nigeria) to the US — the
LEADING RESERVE POWER late in its long-term debt cycle — and puts the two economies side by side.

The decisive difference the whole comparison turns on:
  • Nigeria borrows partly in hard currency with NO reserve status -> genuine FX/rollover/default
    risk; its deleveraging is inflation + devaluation, ALREADY underway, with no policy space.
  • The US borrows in its OWN reserve currency -> it cannot be forced into external default; its
    risk is slow currency debasement + a gradual loss of 'exorbitant privilege'. Late, not acute.

Data: usa_debt_cycle_gauges.csv (FRED/IMF/BEA/Treasury) + the Nigeria gauges (parent module).
Run (from debt_cycle/):  uv run python usa/usa_debt_cycle.py
"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DC = os.path.dirname(HERE)   # debt_cycle/


def main():
    us = pd.read_csv(os.path.join(HERE, "usa_debt_cycle_gauges.csv")).set_index("year")
    print("="*90)
    print("USA — BIG DEBT CYCLE DIAGNOSIS (Dalio lens): the late-stage reserve power")
    print("="*90)

    print("\n[1] US DEBT-CYCLE GAUGES over time:")
    cols = ["federal_debt_held_by_public_pct_gdp", "fiscal_deficit_pct_gdp", "net_interest_pct_revenue",
            "foreign_held_treasury_pct", "usd_share_global_reserves_pct", "niip_pct_gdp"]
    hdr = ["debt/GDP", "deficit", "int/rev", "foreign%", "USD-res%", "NIIP"]
    print(f"    {'year':<6}" + "".join(f"{h:>11}" for h in hdr))
    for y in [1980, 2000, 2007, 2010, 2020, 2024, 2025]:
        r = us.loc[y]
        print(f"    {y:<6}" + "".join(
            f"{(r[c] if pd.notna(r[c]) else float('nan')):>11.1f}" if pd.notna(r[c]) else f"{'—':>11}"
            for c in cols))

    r25 = us.loc[2025]
    print("\n[2] LATE-CYCLE MARKERS (Dalio) — what's flashing:")
    flags = [
        ("Debt held by public near post-WWII record", f"{r25['federal_debt_held_by_public_pct_gdp']:.0f}% of GDP (gross ~120%+)", True),
        ("Structural deficit with NO war/recession", f"{-r25['fiscal_deficit_pct_gdp']:.1f}% of GDP", True),
        ("Interest/revenue rising into the danger zone", f"{r25['net_interest_pct_revenue']:.0f}% — interest now exceeds defense", True),
        ("Real 10y yield positive → r rising vs g", f"{r25['10y_real_yield_pct']:.1f}% (from −0.6% in 2020)", True),
        ("Foreign appetite for Treasuries thinning", f"{r25['foreign_held_treasury_pct']:.0f}% (was ~34% c.2013)", True),
        ("Reserve privilege slowly eroding", f"USD {r25['usd_share_global_reserves_pct']:.0f}% of reserves (was 72% in 2000)", True),
        ("Net international investment position deeply negative", f"{r25['niip_pct_gdp']:.0f}% of GDP — the US owes the world", True),
    ]
    for name, val, on in flags:
        print(f"    {'🔴' if on else '🟡'} {name:<46} {val}")

    print("\n[3] DIAGNOSIS: The US is LATE in the big debt cycle of the leading reserve power —")
    print("    high and rising debt, a structural (peacetime) deficit, an interest bill that now")
    print("    compounds faster than growth, and a reserve privilege that is eroding at the margin.")
    print("    But because it prints the world's reserve currency, the resolution is NOT an external")
    print("    default (as it can be for an EM) — it is some mix of inflation, financial repression,")
    print("    and a slow, negotiated decline of privilege. Late-stage, chronic — not acute.")

    # ---- Two poles comparison ----
    ng = pd.read_csv(os.path.join(DC, "nigeria_debt_cycle_gauges.csv")).set_index("year")
    n25 = ng.loc[2025]
    print("\n" + "="*90)
    print("THE TWO POLES OF THE DEBT CYCLE — same Dalio template, opposite ends")
    print("="*90)
    rows = [
        ("Position in the big debt cycle", "LATE (reserve power)", "MID inflationary deleveraging"),
        ("Debt currency", "own reserve currency", f"~{n25['external_debt_share_pct']:.0f}% external + local"),
        ("Reserve-currency status", f"yes — {r25['usd_share_global_reserves_pct']:.0f}% of world reserves (eroding)", "none"),
        ("Deleveraging type", "printing / debasement (latent)", "inflation + devaluation (underway)"),
        ("Debt / GDP", f"{r25['federal_debt_held_by_public_pct_gdp']:.0f}% public (~120% gross)", f"~{n25['debt_to_gdp_dmo_pct']:.0f}% (rebased)"),
        ("Debt-service / revenue", f"~{r25['net_interest_pct_revenue']:.0f}% (interest only)", f"~{n25['debt_service_rev_gross_pct']:.0f}% gross / >100% retained"),
        ("Central-bank lever / policy space", "the Fed — vast", "almost none"),
        ("Household shock arrives via", "inflation, rates, unemployment", "naira collapse / dollarization"),
        ("External-default risk", "≈ nil (own currency)", "real (FX / rollover)"),
        ("The trap", "exorbitant privilege eroding", "no privilege to begin with"),
    ]
    w = max(len(a) for a, _, _ in rows)
    print(f"    {'dimension':<{w}}   {'UNITED STATES':<40}NIGERIA")
    print("    " + "-"*(w+3+40+24))
    for a, u, n in rows:
        print(f"    {a:<{w}}   {u:<40}{n}")
    print("\n    One line: the US is running DOWN its exorbitant privilege slowly; Nigeria never had it.")
    print("    Same template, opposite ends — the two poles of macro-lab.")


if __name__ == "__main__":
    main()
