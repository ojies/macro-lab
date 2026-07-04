#!/usr/bin/env python3
"""
USA — Fiscal Multipliers + QE Channel   (macro-lab, US module — final piece)
============================================================================
The two extra levers a reserve-currency issuer can pull that Nigeria structurally cannot:
FISCAL stimulus (deficit spending / tax cuts) and QE (central-bank balance-sheet expansion).

  1. FISCAL MULTIPLIERS — major packages 1981-2022 with size (% GDP), a representative multiplier,
     and the first-year GDP impulse (size × multiplier). The two things that move the multiplier:
       • STATE: deep-recession / zero-lower-bound bills run high (ARRA ~1.5); full-employment
         bills run low (TCJA/JGTRRA ~0.3).
       • COMPOSITION: transfers / UI / infrastructure (~1.0-1.5) >> high-income & corporate tax
         cuts (~0.3-0.5, largely saved).
  2. QE CHANNEL — QE1-3 + COVID QE compressed the 10y ~100-200bp, but with clear DIMINISHING
     returns (QE1 ~-100bp in dysfunctional markets -> QE2 ~-20bp in functioning ones); QT reverses.

THE POINT (ties to the two-poles comparison): this fiscal + monetary space is the reserve-currency
issuer's privilege. Nigeria's FX/BoP and inflation constraints bind long before any US-style
'slack' argument, and it cannot print the currency much of its debt is in. Space the US has; Nigeria doesn't.

Data: usa_fiscal_packages.csv, usa_qe_episodes.csv (CBO/Fed/BEA/academic; staging 31).
Run (from debt_cycle/):  uv run python usa/usa_fiscal_qe.py
"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))


def slack(ctx):
    c = ctx.lower()
    return "recession/ZLB" if any(k in c for k in ["recession", "zlb", "pandemic"]) else "expansion"


def main():
    fp = pd.read_csv(os.path.join(HERE, "usa_fiscal_packages.csv"))
    fp["impulse"] = fp.size_pct_gdp * fp.est_fiscal_multiplier
    fp["state"] = fp.economic_context.map(slack)
    fp["short"] = fp.package.str.extract(r"\(([^)]+)\)")[0].fillna(fp.package.str.slice(0, 14))

    print("="*84)
    print("USA — FISCAL MULTIPLIERS: the packages, and what makes a dollar work (or not)")
    print("="*84)
    print(f"\n    {'package':<9}{'yr':>5}{'pres':>10}{'type':>9}{'%GDP':>7}{'mult':>6}{'GDPimp':>8}   context")
    for _, r in fp.sort_values("year").iterrows():
        print(f"    {r.short[:8]:<9}{r.year:>5}{r.president[:9]:>10}{r.type:>9}{r.size_pct_gdp:>7.1f}"
              f"{r.est_fiscal_multiplier:>6.2f}{r.impulse:>8.1f}   {r.economic_context}")
    print("    (%GDP = annual fiscal impulse; GDPimp = size × multiplier = first-yr GDP boost, pp)")

    print("\n    DRIVER 1 — STATE (avg multiplier):")
    for s, g in fp.groupby("state"):
        print(f"        {s:<14} {g.est_fiscal_multiplier.mean():.2f}   (n={len(g)})")
    print("    DRIVER 2 — COMPOSITION (avg multiplier):")
    fp["comp"] = fp.type.map(lambda t: "tax cut" if t == "tax_cut" else "spending/transfers/mixed")
    for cmp, g in fp.groupby("comp"):
        print(f"        {cmp:<24} {g.est_fiscal_multiplier.mean():.2f}   (n={len(g)})")
    big = fp.nlargest(3, "size_pct_gdp")
    print(f"\n    Biggest by %GDP: " + " · ".join(f"{r.short[:10]} {r.size_pct_gdp:.1f}%" for _, r in big.iterrows())
          + "  — the pandemic bills dwarf everything.")

    # ---- QE ----
    qe = pd.read_csv(os.path.join(HERE, "usa_qe_episodes.csv"))
    print("\n" + "="*84)
    print("USA — QE CHANNEL: balance-sheet expansion and its (diminishing) yield effect")
    print("="*84)
    print(f"\n    {'program':<22}{'BS Δ ($tn)':>11}{'10y bp':>9}   context")
    for _, r in qe.iterrows():
        print(f"    {r.program:<22}{r.balance_sheet_change_usd_tn:>11.1f}{int(r.est_10y_yield_effect_bp):>9}   {r.context}")
    easing = qe[qe.est_10y_yield_effect_bp < 0]
    print(f"\n    Cumulative QE easing (QE1-3 + COVID): ~{int(easing.est_10y_yield_effect_bp.sum())}bp on the 10y —")
    print("    but front-loaded and DIMINISHING: QE1 ~-100bp (dysfunctional markets) -> QE2 ~-20bp")
    print("    (functioning markets). QT (2017-19, 2022-) reverses it, adding term premium back.")

    print("\n" + "-"*84)
    print("PUNCHLINE — the two-poles link:")
    print("  Fiscal (deficit-financed) + QE (printed reserves) are the levers a RESERVE-CURRENCY")
    print("  issuer can pull with slack as the only real constraint. Nigeria hits FX / balance-of-")
    print("  payments and inflation walls first, and borrows in currency it cannot print — so it has")
    print("  almost none of this space. Same debt-cycle template; the US can cushion, Nigeria cannot.")


if __name__ == "__main__":
    main()
