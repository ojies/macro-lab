#!/usr/bin/env python3
"""
Nigeria Debt-Cycle — Stock-Flow / System-Dynamics Model  (Phase 2c)
===================================================================
A small, transparent stock-flow simulation that ENDOGENIZES the transmission the VAR
measured and the graph mapped. Where scenario_model.py takes FX and inflation as scenario
*inputs*, this model GENERATES them from the oil -> reserves -> FX -> inflation -> debt feedback:

  STOCKS:  external reserves (USD), public debt (NGN, split external/domestic)
  FLOWS:   oil export earnings, imports, fiscal deficit, interest, FX intervention
  FEEDBACK LOOPS (the whole point):
    R1  oil down  -> current account down -> reserves drain -> naira depreciates
    R2  naira depreciates -> imported inflation up  AND  external-debt naira value up
    R3  higher debt + higher rates -> debt-service/revenue up -> less fiscal space
    B1  depreciation -> import compression -> current account partially self-corrects

This is a STYLIZED, illustrative model (not a calibrated national SFC): the parameters are
plausible and reproduce Nigeria's qualitative dynamics, but it is a mechanism-demonstrator,
not a forecast. Its job is to show *how* an oil shock becomes a household shock, with feedback.
Run:  uv run python sfc_model.py
"""
import os, csv
HERE = os.path.dirname(os.path.abspath(__file__))

# ---- 2025 initial state (from the strengthened dataset) --------------------
INIT = dict(
    reserves_usd=40.0,      # $bn (gross, usable proxy)
    debt_ngn=159.28,        # ₦tn total public debt
    ext_share=0.47,         # external share
    fx=1500.0,              # NGN/USD
    cpi=541.3,              # index 2015=100
    ngdp=441.5,             # ₦tn nominal GDP
    revenue=38.0,           # ₦tn FGN retained revenue
)
# ---- structural parameters (illustrative, plausible) -----------------------
P = dict(
    production=1.5,         # mbpd (held flat; could be scenario-driven)
    imports_usd_base=55.0,  # $bn baseline imports at base GDP
    nonoil_fx_usd=25.0,     # $bn structural inflows (remittances + non-oil exports - services)
    capital_flows_usd=3.0,  # $bn net (portfolio/FDI), confidence-sensitive
    reserves_target_months=6.0,
    fx_sensitivity=0.45,    # how hard FX moves when reserves fall below target (R1)
    fx_passthrough=0.35,    # share of depreciation passed to inflation (R2)
    base_inflation=0.09,    # structural/non-FX inflation floor
    import_elast_fx=0.25,   # import compression per unit depreciation (B1)
    real_growth=0.038,      # baseline real growth
    interest_rate=0.13,     # effective rate on debt (R3)
    primary_deficit_gdp=0.025,
    us_inflation=0.03,
)


def simulate(oil_path, label):
    s = INIT.copy(); p = P.copy()
    rows = []
    for yr, oil in zip(range(2026, 2026+len(oil_path)), oil_path):
        ngdp_usd = s["ngdp"]*1000/s["fx"]                       # $bn
        imports = p["imports_usd_base"]*(ngdp_usd/294.0)        # scales with USD GDP
        # --- current account (R1) ---
        oil_export = oil * p["production"] * 365 / 1000         # $bn
        # B1: depreciation since base compresses imports
        dep_cum = max(0.0, (s["fx"]-INIT["fx"])/INIT["fx"])
        imports *= (1 - p["import_elast_fx"]*dep_cum)
        ca = oil_export + p["nonoil_fx_usd"] - imports          # $bn
        # --- reserves stock update ---
        s["reserves_usd"] = max(1.0, s["reserves_usd"] + ca + p["capital_flows_usd"])
        # --- FX (R1): depreciate when reserves below target cover + PPP drift ---
        months_cover = s["reserves_usd"] / (imports/12)
        reserve_gap = max(0.0, (p["reserves_target_months"]-months_cover)/p["reserves_target_months"])
        ppp_drift = 0.0  # set after inflation known; approximate with prior inflation
        fx_dep = reserve_gap*p["fx_sensitivity"]
        # --- inflation (R2): structural + FX pass-through ---
        infl = p["base_inflation"] + p["fx_passthrough"]*fx_dep
        # add PPP component to FX (inflation differential) -> next-year drift
        fx_dep += max(0.0, (infl - p["us_inflation"]))*0.5
        new_fx = s["fx"]*(1+fx_dep)
        fx_change = (new_fx - s["fx"])/s["fx"]
        # --- nominal GDP, revenue ---
        s["ngdp"] *= (1+p["real_growth"])*(1+infl)
        s["cpi"] *= (1+infl)
        oil_rev_ngn = oil_export*new_fx/1000                    # ₦tn from oil at new FX
        s["revenue"] = s["revenue"]*(1+p["real_growth"])*(1+infl)
        # --- debt stock (R3): deficit + FX revaluation of external ---
        deficit = p["primary_deficit_gdp"]*s["ngdp"] + p["interest_rate"]*s["debt_ngn"]*0.4
        s["debt_ngn"] = s["debt_ngn"]*(1+s["ext_share"]*fx_change) + deficit
        debt_service = p["interest_rate"]*s["debt_ngn"]
        dsr = debt_service/s["revenue"]*100
        s["fx"] = new_fx
        real_wage_idx = (70000/s["cpi"])*(100/18000)*100
        rows.append(dict(scenario=label, year=yr, oil=oil,
                         reserves_usd=round(s["reserves_usd"],1), months_cover=round(months_cover,1),
                         fx=round(s["fx"]), inflation_pct=round(infl*100,1),
                         debt_to_gdp=round(s["debt_ngn"]/s["ngdp"]*100,1),
                         dsr_pct=round(dsr,1), real_wage_idx=round(real_wage_idx,1),
                         current_acct_usd=round(ca,1)))
    return rows


def main():
    stable = [72,74,75,76,78]          # oil ~ base
    shock  = [45,40,48,55,60]          # bear: oil collapse then partial recovery
    boom   = [95,98,95,92,90]          # bull: oil strong

    print("="*78)
    print("NIGERIA DEBT-CYCLE STOCK-FLOW MODEL — oil shock -> household shock, with feedback")
    print("="*78)
    all_rows = []
    for path, lab in [(stable,"base_oil"),(shock,"oil_collapse"),(boom,"oil_boom")]:
        rows = simulate(path, lab); all_rows += rows
        print(f"\n--- {lab} (oil path {path}) ---")
        print(f"  {'yr':<5}{'oil':>5}{'reserves$':>11}{'cover_m':>9}{'FX':>8}{'infl%':>7}{'debt/GDP':>10}{'DSR%':>7}{'realwage':>10}")
        for r in rows:
            print(f"  {r['year']:<5}{r['oil']:>5}{r['reserves_usd']:>11}{r['months_cover']:>9}"
                  f"{r['fx']:>8}{r['inflation_pct']:>7}{r['debt_to_gdp']:>10}{r['dsr_pct']:>7}{r['real_wage_idx']:>10}")

    out = os.path.join(HERE, "sfc_simulation.csv")
    with open(out,"w",newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys())); w.writeheader(); w.writerows(all_rows)
    print(f"\nWrote {out}")
    print("\nReading: under oil_collapse, reserves drain -> import cover falls -> the naira")
    print("depreciates -> inflation jumps and the external-debt naira value balloons -> debt/GDP")
    print("and DSR rise while the real wage erodes. The model GENERATES (not assumes) that chain")
    print("from one oil-price input — the feedback the scenario engine takes as given.")


if __name__ == "__main__":
    main()
