# US Fiscal Packages & Fed QE Episodes — Sources, Method, Key Points

**Compiled:** 2026-07-04 · **Analyst pull/access date:** 2026-07-04
**Deliverables:**
- `usa/usa_fiscal_packages.csv` — 10 major fiscal packages since 1980, sizes + representative multipliers
- `usa/usa_qe_episodes.csv` — Fed QE1/QE2/Twist/QE3/COVID-QE + two QT periods, balance-sheet change + est. 10y yield effect
**Purpose:** Quantify the two big US demand-management levers (discretionary FISCAL policy and Fed QE) with representative sizes and effect estimates, to feed the debt-cycle model's "policy space" layer and anchor the US pole of the US-vs-Nigeria two-poles comparison.

**Flags:** [SOURCED] = figure confirmed against CBO / Fed / Treasury / academic source. [ESTIMATED] = representative point value chosen from a published range, or annualized/derived by the analyst. Multipliers and yield effects are INHERENTLY RANGES — each CSV row carries a point value plus the range in its note.

---

## A. Conventions (read before using the numbers)

**Multipliers and yields are ranges, not points.** The CSVs give a defensible representative point value; the `note` field gives the range and its driver.

**size_pct_gdp is NOT one uniform convention** (heterogeneous bills force this — stated per row):
- **Tax bills (ERTA, EGTRRA, JGTRRA, TCJA):** revenue score is multi-year (5- or 10-yr). `size_pct_gdp` is the **annualized / peak-year revenue loss as % of GDP** (the economically comparable "fiscal impulse"), not the raw multi-year total over one year's GDP.
- **Pandemic packages (CARES, Dec-2020, ARP):** appropriations spent largely within ~1 year. `size_pct_gdp` = headline / **enactment-year** nominal GDP (single-year).
- **IIJA & IRA:** disburse over ~5-10 yr. `size_pct_gdp` = **annualized** spending as % of GDP; total-as-%-of-one-year is noted in-row.
- Nominal GDP denominators used ($bn): 1981 ~3,207; 2001 ~10,582; 2003 ~11,458; 2009 ~14,479; 2017 ~19,612; 2020 ~21,060; 2021 ~23,681; 2022 ~25,744 (BEA).

**headline_size_usd_bn** = the most-cited headline; its horizon (5-yr / 10-yr / single-yr / total-authorized) is stated in the `note`.

---

## B. Fiscal package sourcing (row by row)

1. **ERTA 1981 (Reagan, tax_cut).** 5-yr revenue loss ~$750bn (CBO); ~$2tn over 10yr. **Peak revenue loss 2.9% of GDP** — biggest US tax cut since the 1913 income tax (CRFB; Treasury OTA/Tempalski "Revenue Effects of Major Tax Bills"). 23% across-the-board rate cut, top rate 70%->50%, indexing. JCT static first-year (FY82) -$37.6bn, FY83 -$92.7bn. Signed Aug-1981; NBER recession began Jul-1981. Multiplier 0.3-0.5 (high-income marginal-rate cut, high saving). [SOURCED size; ESTIMATED multiplier]
   Sources: CRFB "Reagan tax cut turned 40"; Treasury OTA Paper 81; Wikipedia ERTA (JCT figures).

2. **EGTRRA 2001 (Bush, tax_cut).** 10-yr score $1.35tn (Bush sought $1.6tn). Top rate 39.6%->35%; included 2001 rebate checks. Enacted in the 2001 dot-com recession. Multiplier 0.3-0.7 (rebate portion ~0.6-0.9 MPC-driven; permanent rate cuts lower). [SOURCED size; ESTIMATED multiplier]
   Sources: Wikipedia EGTRRA; CBPP "Legacy of 2001/2003 Bush tax cuts."

3. **JGTRRA 2003 (Bush, tax_cut).** 10-yr score ~$350bn. Cut cap-gains/dividends to 15%, accelerated EGTRRA. Jobless early-expansion. Multiplier 0.2-0.5 (capital-income cut, low MPC). [SOURCED size; ESTIMATED multiplier]
   Sources: Wikipedia Bush tax cuts; CRS RL31907/RL32502.

4. **ARRA 2009 (Obama, mixed).** CBO final cost **$831bn** (originally $787bn), FY2009-19. ~1/3 tax cuts, ~2/3 spending (state aid, UI, infrastructure). Peak effect 2010 (~half the deficit impact), raised real GDP 0.7-4.1% and cut unemployment 0.4-1.8pp (CBO). CBO provision multipliers span **0.4 (tax cuts to high earners) to 2.5 (aid to states / UI / infrastructure)**; aggregate central ~1.5 given deep slack + ZLB. [SOURCED size; SOURCED CBO multiplier range]
   Sources: CBO pub. 24988 & "Estimated Impact of ARRA" (Feb-2015, May-2012); CRFB "CBO closes the book on the 2009 stimulus."

5. **TCJA 2017 (Trump, tax_cut).** 10-yr JCT static ~$1.5tn (~$1.9tn dynamic incl. interest; CBO ~$1.9tn deficit w/ interest). Corporate 35%->21% permanent; individual cuts expiring 2025. ~0.9%/yr of GDP first decade (Tax Foundation 0.88%). Enacted near full employment. Multiplier 0.2-0.5. [SOURCED size; ESTIMATED multiplier]
   Sources: CBO pub. 53312; Tax Foundation TCJA analysis; JCT; Tax Policy Center; Brookings.

6. **CARES Act 2020 (Trump, mixed).** ~$2.2tn authorized (largest single bill at the time). $1200 rebates, $600/wk UI, PPP, state/business aid. Multiplier 0.4-1.5 — high slack argues high, but lockdown supply constraint + high saving of transfers pulled the realized number down. [SOURCED size; ESTIMATED multiplier]
   Sources: CRFB "What's in the $2 trillion package"; USAFacts; Wikipedia CARES Act.

7. **Consolidated Appropriations Act 2021 / Dec-2020 COVID relief (Trump, mixed).** ~$900bn relief portion (~$868bn net); $600 rebates, $300/wk UI, PPP second draw. Mostly disbursed 2021. Multiplier 0.5-1.0. [SOURCED size; ESTIMATED multiplier]
   Sources: CRFB; USAFacts.

8. **ARP 2021 (Biden, mixed).** ~$1.9tn ($1.844tn). $1400 rebates, $300/wk UI, expanded Child Tax Credit, $350bn state/local aid. **PGPF estimated ~$0.73 of GDP per $1 spent (multiplier ~0.73)** — economy already reopening, less slack, much of transfers saved; range 0.3-1.0. Debated inflation contributor. [SOURCED size; SOURCED PGPF multiplier]
   Sources: Wikipedia ARPA; Yale SOM; PGPF "boost economy by 73 cents per dollar"; USAFacts.

9. **IIJA 2021 (Biden, spending).** $1.2tn total, ~$550bn NEW spending over baseline, disbursed ~5-10yr (roads, bridges, broadband, grid, water). Annualized new spending ~0.4%/yr of GDP; total ~5% of one year's GDP spread over a decade. Multiplier 0.5-1.5 — infrastructure typically high (~1.0-1.5) but slow-disbursing and near full employment lowers near-term realized impact. [SOURCED size; ESTIMATED multiplier]
   Sources: GovTech; NACo; USAFacts.

10. **IRA 2022 (Biden, mixed).** ~$891bn total outlays (~$391bn energy/climate; ~$238bn Rx-drug/ACA/other subsidies); raises ~$738bn (15% corporate min tax, Rx pricing, IRS funding) -> **NET DEFICIT-REDUCING ~$238bn over 10yr** (CBO). Clean-energy credits are uncapped (later cost estimates run higher). Multiplier 0.5-1.0 applied to gross outlays (investment/subsidy, slow, full-employment). [SOURCED size; ESTIMATED multiplier]
   Sources: CBO pub. 58366; CRFB "What's in the IRA"; CRS R47262; Senate Democrats summary.

---

## C. Fed QE / QT sourcing (row by row)

Balance-sheet levels: Fed H.4.1 / FRED `WALCL`. Pre-QE base ~$0.9tn; QE1-3 peak $4.473tn; COVID peak ~$9.0tn (May-2022).

1. **QE1 (Nov-2008 to Jun-2010).** Gross purchases ~$1.75tn ($1.25tn MBS + $200bn agency debt + $300bn Treasuries); BS ~$0.9tn->$2.3tn. 10y yield: **Krishnamurthy-Vissing-Jorgensen (2011) ~-107bp; Gagnon et al. (2011) ~-91bp** on the 10y. Representative **-100bp** (range -80 to -120). Biggest per-dollar effect — crisis/safe-asset premium in dysfunctional markets. [SOURCED]
   Sources: KVJ (2011 Brookings/NBER w17555); Gagnon-Raskin-Remache-Sack (2011); Fed/FRED.

2. **QE2 (Nov-2010 to Jun-2011).** $600bn Treasuries; BS ->~$2.9tn. 10y: KVJ ~-18bp (safe-asset channel); Gagnon-type ~-15 to -20bp per $500bn. Representative **-20bp** (range -15 to -30). First clear DIMINISHING returns vs QE1. [SOURCED]
   Sources: KVJ (2011); Fed "Effect of the Fed's Securities Holdings on Longer-term Interest Rates" (2017 FEDS Note).

3. **Operation Twist / MEP (Sep-2011 to Dec-2012).** Sold ~$667bn short-dated, bought equal long-dated -> **no BS expansion** (duration-only). 10y ~-15bp via term-premium/duration channel (range -10 to -25). Demonstrates portfolio-balance channel without new reserves. [SOURCED size; ESTIMATED yield]
   Sources: Fed History MEP; St. Louis Fed; event-study literature.

4. **QE3 (Sep-2012 to Oct-2014).** Open-ended $85bn/mo ($40bn MBS + $45bn Treasuries), ~$1.6tn total; BS ~$2.8tn->$4.5tn. Announcement effect small/hard to isolate (flow vs stock, pre-anticipated); ~-20 to -50bp. Representative **-30bp**. Taper tantrum (May-2013) reversed some. [SOURCED size; ESTIMATED yield]
   Sources: Fed FOMC statements; Fed conference paper "QE1 vs 2 vs 3"; FRED.

5. **COVID QE (Mar-2020 to Mar-2022).** ~$4.6-4.7tn ($120bn/mo: $80bn Treasuries + $40bn MBS); BS ~$4.2tn->$8.9tn (peak ~$9.0tn May-2022, ~35% of GDP). Initial purpose = restore Treasury-market functioning (Mar-2020 dash-for-cash); later stimulus. Yield effect hard to isolate (rates ~0); crisis compression est. -100 to -150bp initially, persistent effect smaller. Representative **-100bp** (wide range). Followed by 2021-22 inflation surge. [SOURCED size; ESTIMATED yield]
   Sources: CRS IF12147; PGPF; Richmond Fed; Fed/FRED.

6. **QT1 (Oct-2017 to Aug-2019).** Passive roll-off, BS ~$4.5tn->$3.8tn (-~$0.7tn). Upward 10y pressure modest ~+10 to +25bp. Representative **+15bp**. Ended early after Sep-2019 repo spike (reserve scarcity). [SOURCED size; ESTIMATED yield]
   Sources: CRS IF12147; Fed balance-sheet trends.

7. **QT2 (Jun-2022 to mid-2026, ongoing).** Largest QT ever, alongside +525bp of hikes; caps up to $95bn/mo (later tapered). BS ~$8.9tn->~$6.6tn by mid-2026 (-~$2.3tn). Term-premium add small/gradual ~+10 to +50bp cumulative. Representative **+30bp**. [SOURCED size; ESTIMATED yield]
   Sources: Richmond Fed; CRS IF12147; Fed/FRED; econ commentary.

**Total QE1-3 yield compression (consensus):** roughly **-100 to -200bp** on the 10y cumulatively (each ~$500bn ≈ -15 to -20bp rule of thumb; QE1 alone ~-100bp). COVID QE added further compression that is harder to isolate.

---

## D. KEY POINTS (for the notes / model)

**(1) Fiscal multipliers are STATE-DEPENDENT and COMPOSITION-DEPENDENT.**
- *State:* Auerbach-Gorodnichenko (2012, NBER w17447) find purchase multipliers much larger in recessions than expansions; at the zero lower bound (ZLB) the offsetting Fed rate hike is absent, so multipliers can reach ~1.5-2.0. Ramey (2019) survey puts average spending multipliers ~0.6-1.0; Ramey (2011) ~0.3 at low unemployment vs ~1.0 at high-unemployment/ZLB; Ramey-Zubairy (2018) are more skeptical multipliers exceed 1 even in slumps. Net: **recession/ZLB multipliers run high, expansion/full-employment multipliers run low.** In this table ARRA (deep recession, ~1.5) and CARES sit high; TCJA/JGTRRA (expansion tax cuts, ~0.3) sit low.
- *Composition:* transfers, UI, and aid to the cash-constrained (high MPC) and productive spending/infrastructure carry HIGHER multipliers (~1.0-1.5+) than tax cuts skewed to high earners / corporations (~0.3-0.5, largely saved). This is why ERTA/JGTRRA/TCJA (~0.3-0.4) < ARRA/IIJA (~1.0-1.5).
- *Caveat:* CARES/ARP show that in a supply-constrained or already-recovering economy even high-MPC transfers can realize LOWER multipliers (much saved; PGPF put ARP at ~0.73), and can spill into inflation rather than real output.

**(2) QE compressed term premia / long yields with DIMINISHING returns across rounds.** QE1 (~-100bp) delivered the largest effect because it operated on dysfunctional, crisis markets via the safe-asset/liquidity premium; QE2 (~-20bp) and QE3 (~-30bp) each did far less per dollar as markets normalized and effects were pre-anticipated. QE works mainly through the portfolio-balance/duration and signaling channels — Operation Twist proved yields can be pushed down (~-15bp) with NO balance-sheet expansion at all. QT partially reverses this (modest upward yield pressure), and the 2019 repo spike showed there is a floor on how far the balance sheet can shrink.

**(3) THE PUNCHLINE — POLICY SPACE (ties to the two-poles US-vs-Nigeria comparison).** Both levers are the exorbitant privilege of the **reserve-currency issuer**. The US could run CARES+ARP (~18% of GDP in two years) and expand the Fed balance sheet by ~$4.7tn to ~35% of GDP — financing enormous deficits at compressed yields **in its own currency**, with global demand for Treasuries as the world's safe asset absorbing the issuance and inflation (not default) as the binding constraint. **Nigeria has essentially NONE of this space:** it cannot QE without triggering capital flight and naira collapse; deficit monetization (CBN Ways-and-Means) fed ~30%+ inflation rather than stimulus; it borrows externally in hard currency it cannot print (Eurobonds), so its fiscal multiplier is throttled by an FX/BOP and inflation constraint that binds long before any US-style slack argument applies. The US debates the *size* of its multiplier; Nigeria is denied the *instrument*. That asymmetry in policy space — not any difference in the textbook mechanics — is the core of the two-poles contrast.

---

## E. Caveats & limitations
- Multiplier point values are analyst-chosen representatives from published ranges; treat the ranges in the CSV notes as the real object. Reasonable economists disagree (Ramey vs. AG vs. CBO).
- Tax-bill headline sizes are 10-yr scores and are NOT directly comparable to single-year pandemic appropriations without the annualization convention in Section A.
- QE 10y-yield effects are event-study/announcement estimates; the persistent (stock) effect and the counterfactual are contested, especially for COVID QE where the policy rate was already ~0 and market-functioning motives dominated early.
- All figures are nominal USD; GDP denominators are BEA nominal annual GDP (rounded).
