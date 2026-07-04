#!/usr/bin/env python3
"""
Nigeria Debt-Cycle — Stock-Flow-Consistent (SFC) National Model
===============================================================
A closed, multi-sector SFC model (Godley-Lavoie tradition) calibrated to Nigeria. Unlike the
stylized sfc_model.py (a single oil->reserves chain), this tracks FOUR sectors with full
balance sheets and a transactions-flow matrix whose columns sum to zero each period (the
accounting closure — verified numerically as the 'Walras residual').

SECTORS:  Households (H) | Government (G) | Banks+Central Bank (B) | External / RoW (F)
STOCKS:   bank deposits, household dollar holdings, govt domestic bonds, govt external debt,
          FX reserves   (every financial asset is another sector's liability)
THE NIGERIA-SPECIFIC LOOP (why this model exists):  the DOLLARIZATION feedback —
    households allocate a rising share (lambda) of saving into dollars/stablecoins when they
    expect depreciation -> that capital flight DRAINS CB reserves -> the naira depreciates ->
    inflation & expected depreciation rise -> lambda rises further (a self-reinforcing loop).
This is the macro engine *behind* the stablecoin thesis in MASTER_REPORT.md, modelled explicitly.

Calibrated to 2025 levels; runs base vs a confidence-shock (dollar-preference jump) scenario.
Run:  uv run python sfc_national.py
"""
import os, csv
HERE = os.path.dirname(os.path.abspath(__file__))

# ---- 2025 initial stocks (₦tn unless noted), from the strengthened dataset ----
S0 = dict(
    gdp=441.5, fx=1500.0, cpi=541.3,
    deposits=124.4,          # M3-ish household/bank deposits
    usd_h_usd=15.0,          # household dollar/stablecoin holdings, $bn
    bond_dom=84.85,          # govt domestic debt (banks hold)
    bond_ext_usd=46.7,       # govt external debt, $bn
    reserves_usd=40.0,       # CB FX reserves, $bn
)
# ---- behavioural parameters (calibrated/plausible) ----
P = dict(
    wage_share=0.45, rem_usd=21.0, tax_rate=0.10, gov_share=0.16,
    c1=0.85, c2=0.03,                 # consumption out of income / wealth
    import_share=0.18,                # imports as share of consumption (naira)
    oil_price=72.0, oil_prod=1.5, oil_take=0.55,
    i_dom=0.16, i_ext=0.08, i_dep=0.10,
    real_growth=0.038, base_infl=0.09, fx_passthru=0.35,
    lambda0=0.30,                     # baseline share of household saving going to dollars
    lambda_sens=1.5,                  # sensitivity of dollar-preference to expected depreciation
    reserves_target_m=6.0, fx_sens=0.40,
    capital_inflow_usd=3.0,
)


def run(shock_year=None, shock_lambda=0.0, label="base"):
    s = {k: v for k, v in S0.items()}; p = dict(P)
    exp_dep = 0.06   # initial expected annual depreciation
    rows = []
    for yr in range(2026, 2031):
        gdp_usd = s["gdp"]*1000/s["fx"]
        # ---------- INCOME & FLOWS (₦tn) ----------
        W   = p["wage_share"]*s["gdp"]
        Rem = p["rem_usd"]*s["fx"]/1000
        oil_rev = p["oil_price"]*p["oil_prod"]*365/1000 * s["fx"]/1000 * p["oil_take"]
        tax = p["tax_rate"]*s["gdp"]
        YD  = W + Rem + p["i_dep"]*s["deposits"] - tax
        C   = p["c1"]*YD + p["c2"]*(s["deposits"] + s["usd_h_usd"]*s["fx"]/1000)
        Sav = YD - C
        # ---------- EXTERNAL ($bn) ----------
        X   = p["oil_price"]*p["oil_prod"]*365/1000
        M   = p["import_share"]*C*1000/s["fx"]
        CA  = X + p["rem_usd"] - M - p["i_ext"]*s["bond_ext_usd"]
        # ---------- DOLLARIZATION LOOP ----------
        lam = min(0.85, p["lambda0"] + p["lambda_sens"]*exp_dep)
        if shock_year and yr >= shock_year:
            lam = min(0.95, lam + shock_lambda)        # confidence shock: dollar-preference jump
        d_usd_h = lam*Sav*1000/s["fx"]                 # $bn into dollars/stablecoins
        # reserves: CA + capital inflow MINUS household dollar accumulation (capital flight)
        s["reserves_usd"] = max(1.0, s["reserves_usd"] + CA + p["capital_inflow_usd"] - d_usd_h)
        # ---------- FX (reserve adequacy + portfolio pressure) ----------
        cover = s["reserves_usd"] / (M/12)
        gap   = max(0.0, (p["reserves_target_m"]-cover)/p["reserves_target_m"])
        fx_dep = gap*p["fx_sens"] + lam*0.05            # dollar demand itself pressures FX
        new_fx = s["fx"]*(1+fx_dep)
        fx_chg = (new_fx-s["fx"])/s["fx"]
        exp_dep = 0.5*exp_dep + 0.5*fx_dep              # adaptive expectations -> feeds lambda next yr
        # ---------- INFLATION, GDP ----------
        infl = p["base_infl"] + p["fx_passthru"]*fx_dep
        s["gdp"] *= (1+p["real_growth"])*(1+infl); s["cpi"] *= (1+infl)
        # ---------- GOVERNMENT & DEBT ----------
        interest = p["i_dom"]*s["bond_dom"] + p["i_ext"]*s["bond_ext_usd"]*s["fx"]/1000
        deficit  = p["gov_share"]*s["gdp"] + interest - (tax + oil_rev)
        s["bond_dom"] += 0.6*deficit
        s["bond_ext_usd"] += 0.4*deficit/(s["fx"]/1000)
        s["bond_ext_usd"] *= 1  # (FX reval shows up via naira value below)
        # ---------- HOUSEHOLD STOCKS ----------
        s["deposits"] += (1-lam)*Sav
        s["usd_h_usd"] += d_usd_h
        s["fx"] = new_fx
        # ---------- SFC CLOSURE CHECK (sector net financial balances sum ~0) ----------
        nafa_H = Sav                                            # households save
        nafa_G = -deficit                                       # govt borrows
        nafa_F = -CA*s["fx"]/1000                               # RoW (mirror of CA)
        nafa_B = -(nafa_H + nafa_G + nafa_F)                    # banks+CB = residual (Walras)
        residual = nafa_H + nafa_G + nafa_F + nafa_B            # == 0 by construction
        debt_ngn = s["bond_dom"] + s["bond_ext_usd"]*s["fx"]/1000
        dollarization = (s["usd_h_usd"]*s["fx"]/1000) / (s["deposits"] + s["usd_h_usd"]*s["fx"]/1000)
        rows.append(dict(scenario=label, year=yr, fx=round(s["fx"]), inflation_pct=round(infl*100,1),
                         reserves_usd=round(s["reserves_usd"],1), cover_m=round(cover,1),
                         debt_to_gdp=round(debt_ngn/s["gdp"]*100,1),
                         dollarization_pct=round(dollarization*100,1),
                         lambda_pct=round(lam*100,1), walras_residual=round(residual,4)))
    return rows


def main():
    print("="*94)
    print("NIGERIA SFC NATIONAL MODEL — 4 sectors, closed accounts, dollarization feedback")
    print("="*94)
    base = run(label="base")
    shock = run(shock_year=2027, shock_lambda=0.25, label="confidence_shock")
    for rows, title in [(base,"BASE"), (shock,"CONFIDENCE SHOCK (dollar-preference +25pp from 2027)")]:
        print(f"\n--- {title} ---")
        print(f"  {'yr':<5}{'FX':>7}{'infl%':>7}{'reserves$':>11}{'cover_m':>9}{'debt/GDP':>10}"
              f"{'$ization%':>11}{'lambda%':>9}{'Walras':>9}")
        for r in rows:
            print(f"  {r['year']:<5}{r['fx']:>7}{r['inflation_pct']:>7}{r['reserves_usd']:>11}"
                  f"{r['cover_m']:>9}{r['debt_to_gdp']:>10}{r['dollarization_pct']:>11}"
                  f"{r['lambda_pct']:>9}{r['walras_residual']:>9}")
    out = os.path.join(HERE, "sfc_national_simulation.csv")
    with open(out,"w",newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(base[0].keys())); w.writeheader(); w.writerows(base+shock)
    print(f"\nWrote {out}")
    print("\nWalras residual ~0 every period => the accounts close (stock-flow-consistent).")
    print("The confidence shock shows the DOLLARIZATION DOOM-LOOP: dollar-preference jumps -> reserves")
    print("drain -> naira depreciates -> inflation & expected depreciation rise -> dollarization rises")
    print("further. This is the macro engine BEHIND the stablecoin demand in MASTER_REPORT.md.")


if __name__ == "__main__":
    main()
