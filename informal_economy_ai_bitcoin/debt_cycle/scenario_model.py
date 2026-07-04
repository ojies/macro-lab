#!/usr/bin/env python3
"""
Nigeria Big-Debt-Cycle — Living Scenario Model (Phase 2)
=========================================================
Projects base / bull / bear paths 2026-2030 for the variables that decide the
"average Nigerian" outcome, off the strengthened gauges dataset.

Transparent, parameterized, and re-runnable: edit the SCENARIOS assumptions or the
2025 STARTING POINT as new data lands, then re-run to refresh scenario_projections.csv.

Outputs:
  - scenario_projections.csv   (long format: scenario, year, variable, value)
  - prints a comparison summary to stdout

Method (deliberately simple & auditable, NOT a DSGE):
  nominal_gdp_t   = nominal_gdp_{t-1} * (1+real_growth) * (1+gdp_deflator)
  fx_t            = scenario path (NGN/USD, period-average)
  usd_gdp_bn      = nominal_gdp_tn * 1000 / fx
  population_t    = population_{t-1} * (1 + pop_growth)
  gdp_pc_usd      = usd_gdp_bn * 1e9 / population
  cpi_index_t     = cpi_index_{t-1} * (1+cpi_inflation)            (2015=100)
  min_wage_t      = step-up in the wage-rebase year, else flat
  real_wage_idx   = (min_wage_t / cpi_index_t) * (cpi_2015=100 / wage_2015) * 100
  debt_t          = debt_{t-1}*(1 + ext_share*fx_change) + deficit_pct_gdp*nominal_gdp_t
  debt_to_gdp     = debt_t / nominal_gdp_t
  revenue_t       = revenue_{t-1} * (1+real_growth) * (1+cpi_inflation)   (elasticity~1)
  debt_service_t  = eff_interest_rate * debt_{t-1} + amort_rate * debt_{t-1}
  dsr_gross       = debt_service_t / revenue_t
  poverty_t       = poverty_{t-1} - elasticity * (real_growth - pop_growth)
"""

import csv, os

# ----------------------------------------------------------------------------
# 2025 STARTING POINT  (from the strengthened dataset; see DATA_NOTES.md)
# ----------------------------------------------------------------------------
START = dict(
    year=2025,
    nominal_gdp_tn=441.5,     # NBS rebased nominal GDP (2019 base), ₦tn
    debt_tn=159.28,           # DMO total public debt, ₦tn
    fx=1500.0,                # NGN/USD period-average proxy (yr-end 1429; avg higher)
    population_m=237.6,       # IMF WEO
    revenue_tn=38.0,          # FGN retained revenue (excl. GOEs), ₦tn
    cpi_index=541.3,          # CPI index, 2015=100 (implied by real-min-wage index 71.8)
    min_wage=70000,           # ₦/month
    poverty=50.9,             # extreme poverty %, $3.00/day (2021 PPP)
    ext_share=0.47,           # external share of public debt
)
WAGE_2015 = 18000            # ₦/month, for the real-wage index base

# ----------------------------------------------------------------------------
# SCENARIO ASSUMPTIONS  (annual, 2026..2030).  Edit these to re-run.
# Probabilities from ANALYSIS.md (base 55% / bull 25% / bear 20%).
# ----------------------------------------------------------------------------
YEARS = [2026, 2027, 2028, 2029, 2030]

SCENARIOS = {
    "base": dict(   # ~55% "grinding stabilization"
        prob=0.55,
        real_growth   =[0.039, 0.040, 0.041, 0.042, 0.042],
        cpi_inflation =[0.16,  0.145, 0.13,  0.12,  0.115],   # disinflation, sticky
        gdp_deflator  =[0.15,  0.14,  0.125, 0.115, 0.11],
        fx            =[1550,  1650,  1740,  1820,  1880],     # PPP-consistent mild depreciation
        deficit_pct   =[0.042, 0.040, 0.038, 0.036, 0.035],
        eff_int_rate  =[0.115, 0.110, 0.105, 0.100, 0.098],
        amort_rate    =[0.045, 0.045, 0.045, 0.045, 0.045],
        wage_rebase   ={2027: 100000},                         # re-based once
        pov_elasticity=0.7,
    ),
    "bull": dict(   # ~20% "beautiful deleveraging completes" (was 25%; cut after analogue calibration —
                    # fast/"beautiful" household recovery is empirically a sub-25% event, Phase 3)
        prob=0.20,
        real_growth   =[0.045, 0.050, 0.052, 0.050, 0.050],
        cpi_inflation =[0.14,  0.105, 0.085, 0.075, 0.07],
        gdp_deflator  =[0.13,  0.10,  0.08,  0.07,  0.065],
        fx            =[1450,  1400,  1360,  1330,  1310],     # stable/appreciating (reform + inflows)
        deficit_pct   =[0.035, 0.030, 0.028, 0.026, 0.025],
        eff_int_rate  =[0.110, 0.100, 0.090, 0.085, 0.080],
        amort_rate    =[0.045, 0.045, 0.045, 0.045, 0.045],
        wage_rebase   ={2027: 120000},
        pov_elasticity=1.0,
    ),
    "bear": dict(   # ~25% "reform fatigue / ugly inflation" (was 20%; raised after analogue calibration —
                    # governance/security fattens the left tail; Turkey-style relapse risk; Phase 3)
        prob=0.25,
        real_growth   =[0.022, 0.018, 0.020, 0.022, 0.024],
        cpi_inflation =[0.20,  0.26,  0.28,  0.25,  0.22],     # re-acceleration
        gdp_deflator  =[0.19,  0.25,  0.27,  0.24,  0.21],
        fx            =[1700,  2050,  2450,  2750,  3000],     # PPP-consistent renewed slide
        deficit_pct   =[0.055, 0.060, 0.058, 0.055, 0.052],
        eff_int_rate  =[0.125, 0.140, 0.150, 0.145, 0.140],
        amort_rate    =[0.045, 0.045, 0.045, 0.045, 0.045],
        wage_rebase   ={},                                     # no re-basing
        pov_elasticity=1.2,
    ),
}
POP_GROWTH = 0.024  # ~2.4%/yr


def project(name, p):
    s = START.copy()
    rows = []
    # emit 2025 baseline
    rows.append(_row(name, s["year"], s, START["nominal_gdp_tn"], _usd_gdp(s["nominal_gdp_tn"], s["fx"]),
                     _pc(s["nominal_gdp_tn"], s["fx"], s["population_m"]),
                     s["debt_tn"]/s["nominal_gdp_tn"]*100, None, _rwi(s["min_wage"], s["cpi_index"]),
                     s["poverty"]))
    prev = s.copy()
    for i, yr in enumerate(YEARS):
        ngdp = prev["nominal_gdp_tn"] * (1+p["real_growth"][i]) * (1+p["gdp_deflator"][i])
        fx = p["fx"][i]
        pop = prev["population_m"] * (1+POP_GROWTH)
        cpi = prev["cpi_index"] * (1+p["cpi_inflation"][i])
        wage = p["wage_rebase"].get(yr, prev["min_wage"])
        fx_change = (fx - prev["fx"]) / prev["fx"]
        debt = prev["debt_tn"] * (1 + prev["ext_share"]*fx_change) + p["deficit_pct"][i]*ngdp
        revenue = prev["revenue_tn"] * (1+p["real_growth"][i]) * (1+p["cpi_inflation"][i])
        debt_service = (p["eff_int_rate"][i] + p["amort_rate"][i]) * prev["debt_tn"]
        dsr = debt_service / revenue * 100
        pov = max(0.0, prev["poverty"] - p["pov_elasticity"]*(p["real_growth"][i]-POP_GROWTH)*100)
        cur = dict(year=yr, nominal_gdp_tn=ngdp, debt_tn=debt, fx=fx, population_m=pop,
                   revenue_tn=revenue, cpi_index=cpi, min_wage=wage, poverty=pov,
                   ext_share=prev["ext_share"])
        rows.append(_row(name, yr, cur, ngdp, _usd_gdp(ngdp, fx), _pc(ngdp, fx, pop),
                         debt/ngdp*100, dsr, _rwi(wage, cpi), pov))
        prev = cur
    return rows


def _usd_gdp(ngdp_tn, fx):           return ngdp_tn * 1000 / fx                 # USD bn
def _pc(ngdp_tn, fx, pop_m):         return _usd_gdp(ngdp_tn, fx)*1e9 / (pop_m*1e6)  # USD/person
def _rwi(wage, cpi):                 return (wage / cpi) * (100.0 / WAGE_2015) * 100  # 2015=100
def _row(scn, yr, s, ngdp, usdgdp, pc, d2g, dsr, rwi, pov):
    return dict(scenario=scn, year=yr,
                nominal_gdp_ngn_trn=round(ngdp,1), usd_gdp_bn=round(usdgdp,1),
                gdp_per_capita_usd=round(pc), debt_to_gdp_pct=round(d2g,1),
                debt_service_to_rev_pct=(round(dsr,1) if dsr is not None else ""),
                real_min_wage_idx_2015=round(rwi,1), extreme_poverty_pct=round(pov,1))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    all_rows = []
    for name, p in SCENARIOS.items():
        all_rows.extend(project(name, p))

    out = os.path.join(here, "scenario_projections.csv")
    cols = ["scenario","year","nominal_gdp_ngn_trn","usd_gdp_bn","gdp_per_capita_usd",
            "debt_to_gdp_pct","debt_service_to_rev_pct","real_min_wage_idx_2015","extreme_poverty_pct"]
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(all_rows)

    # summary: 2030 endpoint by scenario
    print("\nNigeria Debt-Cycle Scenario Model — 2030 endpoints (vs 2025 base)\n" + "="*68)
    base2025 = next(r for r in all_rows if r["scenario"]=="base" and r["year"]==2025)
    print(f"{'2025 actual':<14}  GDP/cap ${base2025['gdp_per_capita_usd']:>5}  "
          f"debt/GDP {base2025['debt_to_gdp_pct']:>4}%  "
          f"realwage {base2025['real_min_wage_idx_2015']:>5}  "
          f"poverty {base2025['extreme_poverty_pct']:>4}%")
    print("-"*68)
    for name in SCENARIOS:
        r = next(x for x in all_rows if x["scenario"]==name and x["year"]==2030)
        print(f"{name+' 2030':<14}  GDP/cap ${r['gdp_per_capita_usd']:>5}  "
              f"debt/GDP {r['debt_to_gdp_pct']:>4}%  "
              f"realwage {r['real_min_wage_idx_2015']:>5}  "
              f"poverty {r['extreme_poverty_pct']:>4}%  "
              f"DSR {r['debt_service_to_rev_pct']}%  (p={SCENARIOS[name]['prob']})")
    print("="*68)
    print(f"Wrote {out}")
    # probability-weighted 2030 expectation
    for var in ["gdp_per_capita_usd","real_min_wage_idx_2015","extreme_poverty_pct"]:
        ev = sum(SCENARIOS[n]["prob"]*next(x for x in all_rows if x["scenario"]==n and x["year"]==2030)[var]
                 for n in SCENARIOS)
        print(f"  prob-weighted 2030 {var}: {round(ev,1)}")


if __name__ == "__main__":
    main()
