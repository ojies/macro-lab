# Nigeria Debt-Cycle Dataset — Data Notes, Sources & Rebasing Reconciliation

**Compiled:** 2026-06-30 · **Coverage:** annual 2015–2026 + quarterly 2020Q1–2026Q2 (historical pre-2015 in a separate file once available).

This note is the **read-me-first** for the strengthened debt-cycle data. It documents (1) the file inventory, (2) the **four statistical breaks** that make naive time-series comparison wrong, (3) a do/don't table, (4) flag conventions, and (5) corrections applied to earlier drafts. Every figure in the CSVs is sourced from the per-cluster staging files in `_staging/` (16 thematic files + 1 historical), each of which carries per-cell source URLs and confidence flags.

---

## 1. File inventory

| File | Contents |
|---|---|
| `nigeria_debt_cycle_gauges.csv` | **Core annual gauges** 2015–2026, 31 columns (debt, debt-service, W&M, reserves, FX, REER, MPR, inflation, oil price, terms of trade, real min wage, poverty) |
| `nigeria_debt_cycle_quarterly.csv` | **High-frequency gauges** 2020Q1–2026Q2 (debt, FX official+parallel, reserves, MPR, inflation, Bonny Light) — the early-warning series |
| `nigeria_external_debt_profile.csv` | External-debt **creditor composition** (multilateral/bilateral/commercial), 2025 quarterly snapshots |
| `nigeria_eurobond_maturity_wall.csv` | FGN **Eurobond maturity schedule** 2025–2051 |
| `imf_weo_nigeria_projections.csv` | IMF WEO actuals + forecasts to 2031 (GDP, growth, deficit, debt/GDP-WEO, per-capita USD & PPP, population) — *unchanged* |
| *(thematic CSVs)* | monetary/credit/banking · markets/capital · real-economy/welfare · sectoral activity · social/security/humandev · financial inclusion · migration/japa · private capital — built from staging files 05, 07–16 |
| `_staging/01–17_*.md` | Fully-sourced working files (per-cell URLs + flags) behind every CSV |

The IMF WEO CSV is the cleanest source for **GDP level, real growth, fiscal balance, and the IMF debt/GDP series** — those are deliberately *not* duplicated in the gauges file (which carries the DMO debt/GDP instead, as the more debt-cycle-relevant measure).

---

## 2. The four statistical breaks (critical)

Nigeria's statistics agency and central bank introduced **four** discontinuities in 2023–2025. Reading any of them as real economic change is the single biggest analytical trap in this dataset.

### Break 1 — Naira float / unification (14 June 2023)
The naira moved from a managed ~₦460/$ to a float (~₦750→₦1,535 by end-2024). Consequences:
- **USD-denominated series fall while NGN series rise** — e.g. total public debt rose ₦97tn→₦145tn (2023→24) but *fell* in USD ($108bn→$94bn). External-debt *share* jumped to 48.6% purely from revaluing the USD stock, not new borrowing.
- **NGN revenue roughly tripled** in nominal terms (federation revenue ₦16.8tn→₦31.9tn), which **mechanically improves every debt-service and interest ratio from 2024 without real cash-flow relief.** Flag any post-2023 ratio improvement as partly a valuation effect.

### Break 2 — Ways & Means securitization (May 2023)
CBN overdraft ("Ways & Means") peaked at **₦26.95tn (May 2023)**, then was securitized into 40-year FGN bonds and the stock reset low (₦7.94tn end-2023 → ₦3.27tn 2024 → ₦2.84tn Jan-2026). The W&M column is therefore **non-monotonic by design** — the drop is an accounting reclassification (the debt moved into the bond stock), not repayment.

### Break 3 — CPI rebasing (January 2025 data, published 18 Feb 2025)
Base year 2009→2024; basket reweighted (food weight **51.8%→40.0%**, meals-out moved to a new Restaurants division). Headline y/y fell **34.80% (Dec-2024, old series) → 24.48% (Jan-2025, new series)** — **~10 points of that drop is mechanical, not disinflation.**
- A **second, smaller revision in late 2025** switched the y/y reference to a 12-month-average base, retroactively lifting Nov-2025 from 14.45%→17.33%.
- **Inflation *levels* are not comparable across the break; y/y *rates* still chain** (the real-minimum-wage index in the gauges file is built from chained rates and is valid across the break).

### Break 4 — GDP rebasing (published 21 July 2025)
Base year 2010→2019; 2024 nominal GDP revised **+34.4%** (₦277.49tn→₦372.82tn), reweighting digital/fintech/creative/real-estate/informal up. **This alone cut debt/GDP from 52.13%→38.80% with no change in debt** — *not* deleveraging. Affects every ratio with GDP in the denominator (debt/GDP, deficit/GDP, tax/GDP) and every GDP level/ per-capita figure. Does **not** affect debt-service-to-revenue, reserves, FX, or oil volumes.

### Break (bonus) — Unemployment methodology (2023)
NBS adopted a new ILO-aligned Labour Force Survey: old methodology showed ~33% unemployment (Q4-2020); new shows ~4–5%. **The two series are not comparable** — both are reported in the labour data, clearly labelled.

---

## 3. Do / don't — safe time-series comparisons

| Series | Compare across 2023–2025 breaks? | How to bridge |
|---|---|---|
| Debt in **NGN** | ⚠️ Watch the float | Read alongside the USD column; the 2023 jump includes W&M securitization |
| Debt in **USD** | ✅ | Clean (FX-revaluation is the real signal) |
| Debt-service-to-revenue | ⚠️ | Improvement from 2024 is partly revenue-inflation; tag the basis (gross vs retained) |
| Debt/GDP, deficit/GDP, tax/GDP | ❌ | Restate one side onto the same GDP base year (post-rebasing GDP ~34% larger) |
| CPI / food inflation **level** | ❌ | Use chained y/y *rates*, not index levels |
| Real-wage / chained deflator | ✅ | Built from rates — already bridges the CPI break |
| Reserves (USD), FX, REER, MPR, oil mbpd, Bonny Light | ✅ | No rebasing touches these |
| Unemployment | ❌ | Old vs new LFS methodology — never splice |

---

## 4. Flag conventions (in staging files)

`[SOURCED]` primary/official or credible secondary citing official · `[ESTIMATED]` derived by the analyst (method stated) · `[PROVISIONAL]` latest/incomplete/forecast, may revise · blank = not reliably sourceable, **left empty rather than guessed**. CSV cells are left blank on the same principle.

---

## 5. Corrections applied (vs earlier drafts / the original gauges file)

1. **Ways & Means peak = ₦26.95tn (May 2023)**, not ₦22.7tn (the ₦22.7tn was the end-2022 stock that got securitized).
2. **"~109× the legal cap" is UNVERIFIED** and was removed. Sourced breach multiples are ~21–28× on annual flow and ~70–83× on the stock vs the 5%-of-prior-revenue cap (CBN Act 2007 §38).
3. **2020 headline inflation corrected to ~13.25% avg / 15.75% Dec** — the original gauges file carried 34.8% in the 2020 row, which is the *2024* value (an error).
4. **Reserves backbone:** the World Bank "total reserves incl. gold" column is the internally-consistent annual series; the CBN daily-headline and audited-accounts "gross" definitions diverge ~$1–4bn in 2023–24 (both noted in staging 03). Net reserves ($3.99bn 2023 → $23.11bn 2024 → $34.80bn 2025) are CBN-disclosed.
5. **Debt/GDP** in the gauges file is the **DMO total-public-debt basis** (more debt-cycle-relevant); the IMF WEO general-government series lives in `imf_weo_nigeria_projections.csv`. They differ by coverage (IMF includes AMCON/CBN items) and GDP vintage — treat as parallel, not interchangeable.
6. **Oil production** is the crude+condensate (NUPRC/EIA) basis; OPEC quota figures are crude-only (excl. condensate), which is why Nigeria reports ~1.64 vs its 1.5 quota.

---

## 6. Headline debt-cycle reading (unchanged conclusion, now better evidenced)

Nigeria is ~3 years into an **inflationary "beautiful deleveraging"**: the sovereign gauges are healing (net reserves $4bn→$35bn, current account to +6.8% GDP, parallel premium ~62%→~2%, debt-service-to-revenue gross 96%→44%) **but much of the ratio improvement is FX-valuation and GDP-rebasing arithmetic, not real relief** — while the household gauges deteriorated (real minimum wage index 100→50.5 by 2023, only ~62 by 2026; extreme poverty 41.8%→50.9%; food still ~57% of the budget). The data strengthening confirms the split-screen: green sovereign, red household.
