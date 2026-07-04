# Nigeria 2026–2030: A Big-Debt-Cycle Diagnosis and the Outlook for the Average Household

**Prepared by:** ojies · **Compiled:** 2026-06-28
**Framework:** Ray Dalio, *Principles for Navigating Big Debt Crises*
**Data:** `imf_weo_nigeria_projections.csv`, `nigeria_debt_cycle_gauges.csv`, and the
`../../nigeria_fdi_fpi/` dataset (governance, macro, external, capital flows).

> **Bottom line.** Nigeria is roughly **3 years into an attempted "beautiful deleveraging"**
> — an *inflationary* adjustment in which the cost of fixing the state's finances has been
> pushed onto households through a collapsing currency and high inflation. The macro
> gauges (reserves, current account, debt-service ratio, ratings) are healing. **The
> average Nigerian's finances are not** — and on the central scenario they do **not**
> regain their 2022–23 real level before 2030. Whether the picture turns depends less on
> oil than on **institutions** (the six governance variables) holding the reform line.

---

## 1. Where Nigeria sits in the Big Debt Cycle

Dalio's template: debt builds → top → deleveraging via *austerity / default / money-printing
/ wealth transfers* → reflation → normalization. The decisive question is **what currency
the debt is in.**

**Nigeria's debt is mostly local-currency and "printable":**
- External debt is only **~47% of public debt (~25% of GDP)** — and within that, ~46% is
  cheap, long multilateral money (World Bank/AfDB), IMF fully repaid in 2025. (gauges file)
- So the adjustment did **not** come as outright default. It came as **inflation +
  devaluation** — Dalio's classic *inflationary deleveraging* for a non-reserve-currency
  economy. The real value of naira debt, savings and wages was inflated down.

**The trigger was a cash-flow squeeze, not a debt-stock wall.** The binding constraint was
**debt-service-to-revenue**, which hit **~96% (2022)** on the World Bank basis and **>110%
on a retained-revenue basis** — the state was spending almost everything it earned just to
service debt, while financing the rest by **money-printing** (CBN Ways & Means peaked at
**~₦27tn, ~11% of GDP**, ~109× the legal cap). That is a textbook late-cycle top.

**The 2023–24 policy turn is the "beautiful deleveraging" attempt.** Dalio's "beautiful"
deleveraging balances deflationary forces (austerity, default) with reflationary ones
(printing, devaluation) so debt/GDP falls without a depression. Nigeria did, in sequence:
- **Floated the naira** (Jun 2023) and **unified the FX windows** (Feb 2024) → wealth transfer.
- **Removed the fuel subsidy** → austerity.
- **Ended CBN deficit monetization** and **securitized Ways & Means** into 40-yr bonds → stopped the printing.
- Result: inflation spiked, the naira lost ~⅔ of its value, **but** the current account
  swung to surplus, reserves rebuilt, debt/GDP began falling (WB: 49%→40% in 2025), and all
  three agencies upgraded. (gauges + markets files)

This is **mid-deleveraging, reflation phase** — the dangerous middle where the macro looks
like it's working but the social cost is peaking.

## 2. The gauges — healing on paper, painful in the household

| Gauge (Dalio's diagnostic) | Reading | Direction | What it says |
|---|---|---|---|
| Debt in foreign currency | ~25% of GDP | ✅ favourable | Inflationary, not default, path — manageable |
| Debt-service / revenue (gross) | 96% (2022) → ~44% (2025) | ✅ improving | But flattered by **revenue inflation**, not lower service |
| Debt-service / revenue (retained) | still **>110%** | ⚠️ severe | Cash-flow stress persists |
| Money-printing (Ways & Means) | ~₦27tn → barred | ✅ stopped | Removed the core inflation engine |
| Reserves (gross / net) | $33→$51bn / **$4→$35bn** | ✅ rebuilt | Net was near-zero in 2023 — a real near-miss |
| Current account | +1.3% → +6.8% of GDP | ✅ surplus | External solvency restored |
| Eurobond maturity wall | **none in 2026**, ≤$1.7bn/yr to 2031 | ✅ benign | No rollover crisis pending |
| Exchange rate (₦/$) | 460 → ~1,435, premium ~62%→~2% | ⚠️/✅ | Huge devaluation, but FX market now *functions* |
| Inflation | peak ~35%, ~16% (mid-2026), re-accelerating | ⚠️ | Disinflation real but fragile |
| **Real wages / poverty** | ₦70k min wage ≈ **$48/mo**; extreme poverty **47.7%→50.9%** | ❌ deteriorating | The household is paying for the adjustment |

**The split-screen is the whole story:** sovereign gauges (top of table) are green; the
household gauges (bottom) are red. Dalio explicitly frames this — in an inflationary
deleveraging the *holders of money and the wage-earners* bear the adjustment.

## 3. Institutions are the swing factor (the six governance variables)

Dalio stresses that whether a deleveraging is "beautiful" or "ugly" depends on the
**quality of policy-making and the social/political capacity to sustain reform**. That is
precisely what the six **Worldwide Governance Indicators** measure — and they are the same
governance variables used as FDI/FPI determinants in `../../nigeria_fdi_fpi/`:

| WGI variable (estimate, −2.5…+2.5) | Nigeria latest | Reading |
|---|---|---|
| Political Stability & Absence of Violence | ≈ **−2.0** | among world's weakest — biggest tail risk |
| Control of Corruption | ≈ −1.1 | chronic leakage of reform gains |
| Government Effectiveness | ≈ −1.0 | execution capacity is the binding question |
| Rule of Law | ≈ −1.0 | weak contract/property enforcement deters FDI |
| Regulatory Quality | ≈ −0.6 | improving (FX/financial reforms) |
| Voice & Accountability | ≈ −0.7 | limits political durability of austerity |

Implication: the macro reforms are real, but Nigeria attempts this deleveraging from a
**weak institutional base**. Low government-effectiveness and political-stability scores
*raise execution risk* and *lower the probability of the bull path*. These six are the
variables to watch to update the scenario probabilities below — improvement in
Regulatory Quality / Government Effectiveness would be the early signal the bull case is
winning; a fall in Political Stability is the early warning for the bear case.

## 4. The IMF baseline — and why it understates the household pain

IMF WEO (`imf_weo_nigeria_projections.csv`) projects a benign path: ~4%/yr growth,
inflation to ~10% by 2029, debt easing to ~31% of GDP, current-account surplus. Useful as
the "official optimism" anchor — but note what the IMF's **own** numbers show about people:

| | 2022 | 2023 | 2024 | 2030 (proj) |
|---|---|---|---|---|
| GDP per capita, **US$** | ~2,160 | **2,139** | **1,083** | **~1,763** |
| GDP per capita, **PPP int’l$** | ~8,200 | 8,712 | 9,100 | **~11,679** |

**Dollar income halved on the float and does not regain its 2023 level by 2030.** The
PPP line keeps rising — the gap between the two *is* the devaluation/inflation wealth
transfer. For anyone who earns naira and buys anything imported (fuel, wheat, medicine,
electronics) or who measures wealth in dollars, the loss is the USD line, not the PPP line.

## 5. Scenarios for the average Nigerian's finances, 2026–2030

Not a point forecast — three paths with explicit triggers, so probabilities can be updated
as the gauges move.

### Base case (≈55%) — "grinding stabilization"
Reforms broadly hold; inflation drifts to ~12–15%; naira range-bound ₦1,400–1,700;
growth ~3.5–4%. **Household:** real wages bottomed in 2024 and recover *slowly*, staying
**below the 2022 real level through 2030**; dollar income ~$1,700–1,900 (still under 2023);
extreme poverty plateaus near ~50% then edges down only late. Net: *stops getting worse,
does not visibly get better for most* by 2030.
- *Watch:* inflation sticky-declining, reserves stable, Reg. Quality/Govt Effectiveness flat-to-up.

### Bull case (≈25%) — "beautiful deleveraging completes"
Oil + non-oil revenue rise, tax-to-GDP improves, FX stays liberalized, FDI/FPI return
(see `../../nigeria_fdi_fpi/`), inflation to single digits by 2028–29, naira appreciates.
**Household:** real wages recover toward the 2022 level by ~2029–30; poverty falls
meaningfully; a real middle-class purchasing-power rebound. Requires governance scores to
*improve* — the historically hard part.
- *Watch:* rising Govt Effectiveness/Rule of Law, FDI net inflows turning up, single-digit inflation.

### Bear case (≈20%) — "reform fatigue / ugly inflation"
Oil shock or political pressure → subsidy/FX backsliding or renewed monetization;
inflation re-accelerates (the 2026 food-price uptick is the warning); naira slides past
₦2,000. **Household:** real wages fall further, poverty climbs above ~55%, possible unrest.
Triggered by a drop in **Political Stability** or a return of Ways & Means.
- *Watch:* falling Political Stability, reserves drawdown, inflation re-acceleration, W&M restart.

## 6. So — where will the average Nigerian be by 2030?

**Most likely (base case): better than the 2024 trough, but not yet back to where they
were in 2022.** Concretely:
- **Dollar purchasing power / savings:** still impaired — USD income below 2023 even in
  2030; anyone holding naira savings through 2023–24 took a permanent real loss.
- **Local real wages:** recovering but lagging prices; the ₦70,000 minimum wage is already
  acknowledged as inadequate and will need re-basing.
- **Cost of living:** inflation lower but the *price level* is permanently ~2–3× its 2022
  base — relief is in the *rate*, not a reversal.
- **Poverty:** near a multi-decade high (~50% extreme poverty) early in the window, easing
  only slowly and only if growth outpaces population (~2.4%/yr).
- **The upside is real but institution-dependent:** the macro foundation for a genuine
  household recovery now exists (surplus, reserves, no debt wall). Converting it into rising
  living standards is a **governance** problem, not a balance-sheet one.

**The honest version of "predict with certainty":** the *direction* of the sovereign
balance sheet is up and fairly secure; the *timing and extent* of the household recovery is
genuinely uncertain and hinges on the six governance variables. Track those, inflation, and
the naira — they will tell you, well before the GDP data does, which scenario is winning.

---

*Caveats: figures rest on DMO/CBN/NBS/IMF/World Bank data compiled 2026-06-28; several are
provisional (end-2025 debt) or affected by the 2025 CPI and GDP rebasings (which make some
ratios non-comparable across the break). Full source list in `nigeria_debt_cycle_gauges.csv`
provenance and the sister dataset's README. Scenario probabilities are ojies'
judgement, not data.*
