# Nigeria — Fiscal Composition & Tax Detail, 2015–2026

**Purpose:** Composition/tax-detail layer for a Big-Debt-Cycle dataset (FGN/federal basis unless noted "states"/"general government"). Companion to `02_fiscal_debtservice_waysmeans.md` (headline debt-service/deficit/revenue covered there).
**Compiled:** 2026-06-30 · **Currency:** NGN (₦) unless USD noted.
**Flags:** `[S]` = SOURCED (primary/official or credible secondary citing official) · `[E]` = ESTIMATED (derivation noted) · `[P]` = PROVISIONAL/unaudited · `[F]` = FORECAST/BUDGET (appropriation, not actual) · `BLANK` = not reliably sourced (left empty by design, not guessed).

---

## READ-FIRST: two artifacts that distort every naira/ratio series

1. **Naira-float inflation [CRITICAL].** The June-2023 float (≈₦460→₦1,500/$) roughly tripled the naira value of oil tax, customs, and FX-linked revenue. **Tax collections jump from ₦12.4tn (2023) to ₦21.7tn (2024) to ₦28.3tn (2025) is largely nominal/devaluation, not real broadening.** Do NOT read post-2023 naira growth as real-terms revenue gains; deflate by CPI (≈+30–35%/yr) and FX before any real comparison.

2. **GDP-rebasing [CRITICAL].** NBS rebased GDP (base 2010→2019, released Jul-2025), raising 2024 nominal GDP ₦277.5tn→₦372.82tn (+34.4%). Every **tax-to-GDP** and **IGR/GDP** ratio across the 2025 break is non-comparable: the same 2024 tax take reads ~13.5% on old GDP but mechanically lower on rebased GDP. FIRS/Tinubu quote **13.5% (2024, pre-rebasing denominator)**; independent estimates on the rebased base run nearer **~9–10%**.

3. **Institutional rename.** FIRS (Federal Inland Revenue Service) was renamed **Nigeria Revenue Service (NRS)** under the 2025 Tax Reform Acts (effective 2026). 2025 collection is reported under NRS but is the same body/series.

---

## TABLE 1 — FGN Budget Composition, APPROPRIATION basis (₦ trillion, signed/approved)

Splits = Capital Expenditure (capex, incl. Development Fund) · Recurrent Non-Debt (mostly personnel/overheads) · Debt Service · Statutory Transfers. "Recurrent (total)" = Non-Debt + Debt Service.

| Year | Total | Capex | Recurrent Non-Debt | Debt Service | Stat. Transfers | Capex % of total | Flag | Source (period) |
|---|---|---|---|---|---|---|---|---|
| 2015–2021 | BLANK | BLANK | BLANK | BLANK | BLANK | — | — | not pulled this pass (capex historically ~25–30%; see note) |
| 2022 | 17.13 | 5.96 | 6.91 | 3.61 | ~0.87 | ~35% | [S] | Statehouse/BudgIT (Buhari signed ₦17.127tn; +₦0.27tn bond retirement) |
| 2023 | 21.83 | 5.97 | 8.33 | 6.56 | 0.97 | ~27% | [S] | National Assembly approved ₦21.827tn (ThisDay/Channels) |
| 2024 (approved) | 28.78 | 9.99 | 8.76 | 8.27 | 1.70 | ~35% | [S] | NASS-revised appropriation (NISER/Guardian); later supplementary raised total to ~₦35.05tn, then ₦43.5tn revised |
| 2025 | 54.99 | 23.96 | 13.06 | 14.32 | 3.65 | ~44% | [S][F] | Tinubu signed 28-Feb-2025 (Nairametrics/Channels; Development Fund capex = ₦23.963tn) |
| 2026 (proposed Dec-2025) | 58.18 | 26.08 | 15.25 | ~13 | ~3.6 | ~45% | [F] | Tinubu 2026 Appropriation Bill (Statehouse) |
| 2026 (signed Apr-2026) | 68.32 | 32.20 | 15.40 | 15.80 | 4.80 | ~47% | [S] | Tinubu assent (Guardian/ICIR; +2025 capital-spend extension to Jun-2026) |

> **Caveat:** appropriation ≠ execution. Capex release rates in Nigeria historically run well below 100%, so the rising headline capex % overstates real investment delivery. See Table 1b.

## TABLE 1b — 2024 ACTUAL execution (₦ trillion) — the gap vs budget

| Item | 2024 Budget (approved) | 2024 Actual | Flag | Source |
|---|---|---|---|---|
| Capital expenditure | 9.99 | 7.789 | [S] | Budget Office 2024 Budget Implementation (via Guardian) |
| Recurrent non-debt | 8.76 | 7.312 | [S] | same |
| Debt service | 8.27 | 11.887 | [S] | same — debt service OVERSHOT budget by ₦3.6tn, took 69% of revenue |

> Pattern: debt service over-executes while capex under-executes — the classic late-stage debt-cycle squeeze.

---

## TABLE 2 — Total tax collections, FIRS/NRS (₦ trillion, full-year)

Oil = PPT/Hydrocarbon + upstream CIT. Non-oil = CIT + VAT + EDT + stamp/EMTL/other. (Excludes Customs — see Table 3.)

| Year | FIRS/NRS Total | Oil | Non-Oil | Flag | Source (period) |
|---|---|---|---|---|---|
| 2015 | BLANK | | | — | not reliably sourced this pass |
| 2016 | 3.30 | | | [S] | FIRS via Nairametrics |
| 2017 | 4.027 | | | [S] | FIRS via Nairametrics |
| 2018 | 5.320 | | | [S] | FIRS via Nairametrics (all-time high then) |
| 2019 | 5.26 | | | [S] | FIRS via Nairametrics |
| 2020 | 4.95 | | | [S] | FIRS (98% of ₦5.076tn target) via Leadership |
| 2021 | 6.405 | 2.008 | 4.396 | [S] | FIRS (Nami) via Vanguard/TheCable (target ₦6.401tn) |
| 2022 | 10.1 | 4.09 | 5.96 | [S] | FIRS via Premium Times/Nairametrics (first >₦10tn) |
| 2023 | 12.37 | 3.17 (25.6%) | 9.20 (74.4%) | [S] | FIRS via Nairametrics/TheCable (target ₦11.5tn, +₦0.82tn) |
| 2024 | ~21.6–21.7 | 5.8 | 15.9 | [S] | FIRS via Intelpoint/Businessday (record; non-oil 2.7× oil) |
| 2025 | 28.3 | 6.8 | 21.5 | [S][P] | NRS via Businessday (Jun-2026; +30% YoY, 112% of ₦25.2tn target); H1-2025 was ₦14.27tn (Punch/ThisDay) |

> Naira-float caveat applies acutely 2024–25: ~75% of the 2023→2024 jump is devaluation/inflation, not real broadening.

---

## TABLE 3 — Tax collections BY TYPE (₦ trillion, full-year)

| Year | VAT | CIT | PPT/Hydrocarbon (+upstream CIT) | Education Tax | Customs/Excise (NCS) | Flag | Source |
|---|---|---|---|---|---|---|---|
| 2021 | 2.07 | 1.896 | 2.00 | 0.209 (earmarked) | BLANK | [S] | FIRS (Nami) via Vanguard; EMTL ₦0.114tn also |
| 2023 | 3.64 | ~4.47 (≈36.1% of ₦12.37tn) | 3.17 | BLANK | 3.206 | [S] | FIRS via Nairametrics (CIT = top tax, 36.14%); NCS via Arise/Blueprint |
| 2024 | 6.72 (+84.6% YoY) | 6.78 (102.5% YoY) | 5.76 | 1.64 (+127.8% YoY) | 6.105 | [S] | FIRS via Nairametrics/Daily Post/Tekedia; NCS via Sahara/Ships&Ports |
| 2025 | ~9+ (Q3 alone ₦2.28tn, NBS) | exceeded target | ~6.8 (oil total) | BLANK | ~6.58 target (actual pending) | [S][P] | NBS (VAT Q3) / NRS via Businessday; full-type breakdown not yet published |

**Notes:** PIT (Personal Income Tax) is **collected by states**, not FIRS — it is the PAYE-dominated bulk of state IGR (Table 5), not a federal FIRS line. 2024 VAT split: non-import VAT ₦5.13tn, import VAT ₦1.59tn. 2024 PPT delivered only 82.3% of ₦7tn target (oil-theft/under-production). EMTL = Electronic Money Transfer Levy. CIT 2023 precise naira figure not cleanly printed; ~₦4.47tn is the 36.14%-of-total derivation [E].

---

## TABLE 4 — Tax-to-GDP ratio (%) — among world's lowest

| Year | Tax/GDP % | Basis / denominator | Flag | Source |
|---|---|---|---|---|
| 2021 | 10.86 | revised NBS/FIRS computation (incl. previously-omitted agency revenue), old (2010-base) GDP | [S] | NBS/FIRS May-2023 via Nairametrics/Daily Post |
| 2010–2020 | ~5–9 | World Bank / OECD Revenue Statistics Africa (varies by definition; among lowest globally) | [S] | OECD Rev. Stats Africa / World Bank |
| 2024 (pre-rebasing) | 13.5 | FGN/FIRS figure vs OLD GDP denominator | [S] | FIRS Chair Adedeji / Tinubu (ThisDay/Daily Post, Sep–Oct 2025) — claims rise from "10%" at admin inception |
| 2024 (rebased GDP) | ~9–10 | same tax take ÷ rebased ₦372.82tn GDP | [E] | PwC outlook ~9.5%; Agusto/NESG note rebasing mechanically lowers the ratio |

> **Critical:** the official "13.5%" headline and the "~9–10%" rebased figure describe the **same year** on **different denominators**. Post-rebasing, Nigeria's tax/GDP remains far below the African average (~15–16%) and global lows. FIRS target: 18% by 2026/27.

---

## TABLE 5 — State-level Internally Generated Revenue (IGR) & FAAC

### 5a — Total state IGR (36 states + FCT, ₦ trillion)
PAYE (Personal Income Tax) dominates — 64–70% of the total. This is where "PIT" lives.

| Year | Total IGR | YoY | PAYE share | Top earners | Flag | Source (NBS, period) |
|---|---|---|---|---|---|---|
| 2021 | 1.89 | — | — | Lagos, FCT, Rivers | [S] | NBS via Nairametrics |
| 2022 | 1.93 | +1.6% | — | Lagos ₦651bn (34%), Rivers ₦173bn, FCT ₦124bn | [S] | NBS via TheCable/Vanguard |
| 2023 | 2.43 | +26.0% | ₦1.24tn (63.8%) | Lagos ₦815.9bn, FCT ₦211.1bn, Rivers ₦195.4bn | [S] | NBS IGR-2023 report (Oct-2024) |
| 2024 | 3.63 | +49.7% | ₦1.86tn (69.8%) | Lagos ₦1.26tn (~35%), Rivers ₦317.3bn, FCT ₦282.4bn | [S] | NBS IGR-2024 report (Oct-2025) via Nairametrics/Leadership |

> Naira-float caveat: the 2023→2024 +49.7% jump is partly inflation; Lagos alone ~35% of all subnational IGR — extreme concentration.

### 5b — FAAC allocations (Federation Account, ₦ trillion, full-year, all three tiers + derivation)

| Year | Total FAAC disbursed | To States | To FG | To LGCs | Flag | Source |
|---|---|---|---|---|---|---|
| 2023 | ~10.7 (states' share ₦3.58tn) | 3.58 | 3.99 | ~3.1 | [S] | NEITI via Telegraph/Channels (2024 figures cite these as base) |
| 2024 | 15.26 | 5.81 | 4.95 | ~4.5 | [S] | NEITI CMS via Blueprint/Channels (+43% YoY; states +62%) |

> FAAC surge driven by subsidy removal + naira-float boosting oil/FX remittances — same nominal-vs-real caveat. Monthly 2024 disbursements ran ₦1.1–1.4tn (e.g. July ₦1.358tn of ₦2.614tn gross).

---

## TABLE 6 — Pension fund assets (PenCom, ₦ trillion, year-end net asset value)

| Year-end | Pension AUM/NAV | YoY | FGN-securities share | Flag | Source |
|---|---|---|---|---|---|
| 2015 | 5.3 | — | — | [S] | PenCom via Intelpoint |
| 2016 | 6.16 | +16% | — | [S] | PenCom via Intelpoint |
| 2017 | ~7.5 | | — | [E] | interpolated (not cleanly sourced) — treat as gap |
| 2018 | ~8.6 | | — | [E] | interpolated — treat as gap |
| 2019 | ~10.2 (Q3 ₦9.58tn) | | — | [S][P] | PenCom Q3-2019 via Intelpoint |
| 2020 | 12.3 | +21% | — | [S] | PenCom (31-Dec-2020) |
| 2021 | 13.42 | +9% | — | [S] | PenCom (31-Dec-2021) |
| 2022 | 14.99 | +12% | — | [S] | PenCom via Nairametrics |
| 2023 | 18.36 | +22.4% (record) | ₦11.92tn (64.9%) | [S][P] | PenCom unaudited Q4-2023 via Nairametrics |
| 2024 | 22.51 | +22.6% | ₦14.309tn (62.6%, Jan-25) | [S] | PenCom Q4-2024 Dashboard |
| 2025 | 27.45 | +22% | ~62% | [S][P] | PenCom via Business Post (Jun-2026); intra-year: ₦22.86tn Jan, ₦24.1tn May, ₦26.09tn Sep |

> Pension assets are heavily FGN-paper (~62–65%) — a major **captive domestic financing base for the deficit**; relevant to debt-cycle "who holds the debt" mechanics. Naira-float caveat: real-dollar value of the fund FELL sharply post-2023 despite naira growth.

---

## TABLE 7 — Fuel subsidy fiscal-side (₦ trillion / USD)

| Year | Subsidy cost | Flag | Source |
|---|---|---|---|
| 2022 | 4.39 (~$10bn) | [S] | NNPCL via Al Jazeera/Guardian |
| 2023 | 3.6 (Jan–May pre-removal; subsidy formally "ended" 29-May-2023 but partial costs continued) | [S] | Premium Times (NNPC owed ₦2.8tn/$6bn at removal) |
| 2024 | 7.1 ("energy security expense") | [S][P] | NNPC report via Sahara Reporters (Nov-2025) — flags de-facto subsidy re-emergence despite "removal" |

> Tinubu announced removal at 29-May-2023 inauguration; World Bank had estimated ₦3.9tn potential 2023 saving. The 2024 ₦7.1tn "energy security expense" indicates subsidy did not fully disappear — material for the fiscal-relief narrative.

---

## SOURCES (publication — URL)

**Budget composition**
- Statehouse (2022 ₦17.127tn signed) — https://statehouse.gov.ng/news/president-buhari-signs-n17-127tr-2022-budget-into-law-directs-mdas-to-commence-early-preparation-of-2023-transition-budget/
- BudgIT 2022 FG Approved Budget — https://budgit.org/post_infographics/2022-fg-approved-budget/
- ThisDay (2023 ₦21.82tn passed) — https://www.thisdaylive.com/index.php/2022/12/29/nassembly-passes-2023-budget-raises-proposed-spending-by-n1-32trn-to-n21-82trn
- Channels (2023 budget passed) — https://www.channelstv.com/2022/12/28/national-assembly-passes-n21-8trn-2023-budget/
- NISER 2024 Federal Budget Analysis — https://niser.gov.ng/v2/wp-content/uploads/2024/02/2024-Federal-Budget-Analysis.pdf
- Punch (2024 high recurrent low capital) — https://punchng.com/budget-2024-high-on-recurrent-low-on-capital/
- Guardian (2024 actuals; debt service 69%) — https://guardian.ng/business-services/debt-service-takes-69-of-2024-revenue-as-fg-releases-budget-performance/
- Nairametrics (2025 ₦54.99tn passed) — https://nairametrics.com/2025/02/13/senate-passes-n54-99-trillion-2025-budget/
- Channels (Tinubu signs ₦54.99tn) — https://www.channelstv.com/2025/02/28/just-in-tinubu-signs-2025-supplementary-budget/
- Statehouse (2026 ₦58.18tn bill) — https://statehouse.gov.ng/president-tinubu-presents-%E2%82%A658-18-trillion-2026-appropriation-bill-vows-stronger-discipline-in-budget-execution/
- Guardian (2026 ₦68.32tn signed) — https://guardian.ng/featured/tinubu-signs-n68-32tn-2026-budget-extends-2025-capital-spending-to-june/
- ICIR (2026 ₦68.32tn) — https://www.icirnigeria.org/tinubu-signs-n68-32tn-2026-budget-approves-extension-of-2025-implementation/

**Tax collections (FIRS/NRS, Customs)**
- Nairametrics (FIRS 2016–2019 series; 2018 high) — https://nairametrics.com/2019/01/08/how-nigeria-made-an-all-time-high-tax-revenue-in-2018/
- Leadership (FIRS 2020 ₦4.95tn / 4-yr growth) — https://leadership.ng/firs-4-years-of-sustained-tax-revenue-growth/
- Vanguard (FIRS 2021 ₦6.405tn, Nami breakdown) — https://www.vanguardngr.com/2022/01/firs-recorded-n6-405-trn-revenue-in-2021-nami/
- TheCable (FIRS 2021 ₦6.4tn) — https://thecable.ng/firs-generates-n6-4trn-revenue-in-2021/amp
- Premium Times (FIRS 2022 ₦10.1tn) — https://www.premiumtimesng.com/news/top-news/577391-firs-breaks-2021-record-collects-n10-1-trillion-in-2022.html
- Nairametrics (FIRS 2022 ₦10.1tn, oil/non-oil) — https://nairametrics.com/2023/01/23/firs-shatters-2021-record-collects-n10-1-trillion-in-2022/
- Nairametrics (FIRS 2023 ₦12.37tn) — https://nairametrics.com/2024/01/24/nigerians-paid-n12-37-trillion-taxes-in-2023-as-firs-surpassed-revenue-target-by-n816-billion/
- TheCable (FIRS 2023 non-oil 74%) — https://www.thecable.ng/adedeji-firs-collected-n12-3trn-in-2023-non-oil-sector-accounted-for-74/
- Intelpoint (FIRS 2024 record ₦15.9tn non-oil vs ₦5.8tn oil) — https://intelpoint.co/insights/nigerias-non-oil-tax-revenue-solidified-its-dominance-over-oil-in-firs-collections-reaching-a-record-of-%E2%82%A615-9t-in-2024-more-than-2-7x-the-%E2%82%A65-8t-from-oil/
- Nairametrics (VAT 2024 ₦6.72tn +84.6%) — https://nairametrics.com/2025/01/31/nigerias-vat-revenue-hits-n6-72-trillion-in-2024-surges-by-84-62/
- Tekedia (VAT 2024 ₦6.72tn; CIT/PPT/EDT) — https://www.tekedia.com/nigerias-vat-collection-surges-to-n6-72tn-in-2024-amid-economic-struggles-and-tax-expansion/
- Daily Post (VAT 2024 +84.62%) — https://dailypost.ng/2025/01/31/nigerias-vat-surged-by-84-62-to-n6-72trn-in-2024-firs/
- Punch (FIRS H1-2025 ₦14.27tn) — https://punchng.com/firs-posts-n14-27tn-revenue-surge-exceeds-h1-target/
- ThisDay (H1-2025 ₦14.27tn) — https://www.thisdaylive.com/2025/07/24/fgs-half-year-tax-revenues-jump-43-to-n14-27-trillion/
- Businessday (NRS 2025 ₦28.3tn, +30%) — https://businessday.ng/news/article/nigeria-revenue-service-grew-income-by-30-to-n28-3trn-in-2025/
- Punch (FIRS ₦47.39tn Oct-2023→Sep-2025) — https://punchng.com/firs-grows-tax-collection-to-n47-39tn/
- Premium Times (VAT Q3-2025 ₦2.28tn, NBS) — https://www.premiumtimesng.com/business/business-news/861084-nigerias-vat-revenue-rises-to-%E2%82%A62-28-trillion-in-q3-2025-nbs.html
- Arise (NCS 2023 ₦3.206tn) — https://www.arise.tv/amid-headwinds-nigeria-customs-reveals-record-n3-2-trillion-revenue-in-2023/
- Sahara Reporters (NCS 2024 ₦6.1tn) — https://saharareporters.com/2025/01/14/nigerian-customs-records-904-increment-revenue-hits-n61trillion-2024
- Ships&Ports (NCS 2024 ₦6.1tn; 2025 ₦6.58tn target) — https://shipsandports.com.ng/nigeria-customs-service-generates-%E2%82%A66-01-trillion-in-2024-targets-%E2%82%A66-58-trillion-for-2025/

**Tax-to-GDP**
- Nairametrics/FIRS (10.86% revised, 2021) — https://nairametrics.com/2023/05/31/nigerias-tax-to-gdp-ratio-rises-to-10-86-firs/
- NBS revised tax-to-GDP computation 2021 — https://www.nigerianstat.gov.ng/pdfuploads/TAX-TO-GDP%20RATIO%20REVISED%20COMPUTATION-2021.pdf
- ThisDay (Adedeji 13.5% from 10%) — https://www.thisdaylive.com/2025/09/30/adedeji-weve-increased-tax-to-gdp-ratio-to-13-5-from-10/
- KSBC (13.5% in 2024) — https://ksbcjournal.com/2025/05/30/nigerias-tax-revenue-to-gdp-ratio-rose-to-13-5-in-2024/
- OECD Revenue Statistics in Africa — Nigeria — https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/global-tax-revenues/revenue-statistics-africa-nigeria.pdf
- World Bank tax revenue %GDP (Nigeria) — https://data.worldbank.org/indicator/GC.TAX.TOTL.GD.ZS?locations=NG
- Agusto (rebased GDP, old problems) — https://www.agusto.com/publications/nigerias-rebased-gdp-new-numbers-old-problems/

**State IGR & FAAC**
- NBS IGR 2023 report (PDF) — https://www.nigerianstat.gov.ng/pdfuploads/IGR_2023.pdf
- TheCable (2023 ₦2.43tn) — https://www.thecable.ng/nbs-36-states-fct-recorded-n2-43trn-igr-in-2023-up-by-26/
- Nairametrics (2024 ₦3.63tn) — https://nairametrics.com/2025/10/07/lagos-rivers-fct-lead-nigerias-n3-63-trillion-igr-in-2024/
- TheCable (2022 ₦1.93tn) — https://www.thecable.ng/nbs-36-states-fct-recorded-n1-93trn-igr-in-2022-lagos-accounted-for-34/
- Nairametrics (2021 ₦1.89tn) — https://nairametrics.com/2022/10/16/nigerian-states-grow-igr-to-n1-89-trillion-in-2021-as-lagos-abuja-dwarf-others/
- NEITI CMS (FAAC +43% 2024 ₦15.26tn) — https://neiti.gov.ng/cms/faac-allocations-soar-by-43-in-2024/
- Blueprint (FAAC ₦15.26tn 2024, NEITI) — https://blueprint.ng/how-faac-disbursed-n15-26trn-to-federal-states-lgs-in-2024-neiti/
- Channels (FAAC ₦15tn 2024) — https://www.channelstv.com/2025/03/19/faac-disbursement-to-fg-states-lg-jumps-by-43-to-n15tn-in-2024/
- Min. of Finance (Aug-2024 FAAC monthly) — https://finance.gov.ng/faac-fg-states-lgcs-share-n1-203-trillion-from-a-gross-total-of-n2-278-trillion-for-the-month-of-august-2024/

**Pension fund assets**
- PenCom Q4-2024 Dashboard (PDF) — https://www.pencom.gov.ng/wp-content/uploads/2025/01/Q4-2024-PENSION-INDUSTRY-INFORMATION-DASHBOARD-3-APRIL.pdf
- PenCom Q4-2023 Report (PDF) — https://www.pencom.gov.ng/wp-content/uploads/2024/04/FOURTH-QUARTER-REPORT-2023.pdf
- Nairametrics (2023 ₦18.36tn) — https://nairametrics.com/2024/01/30/nigerias-pension-industry-gains-n3-36-trillion-in-2023-fastest-growth-on-record/
- Nairametrics (Jan-2025 ₦22.86tn) — https://nairametrics.com/2025/03/30/nigerias-pension-fund-assets-hit-n22-86-trillion-in-january-2025-pencom/
- Business Post (2025 ₦27.45tn) — https://businesspost.ng/economy/nigerias-pension-fund-assets-jump-22-to-n27-45trn-in-2025/
- Intelpoint (historical 2015–2024 series) — https://intelpoint.co/blogs/best-performing-pension-funds-nigeria/

**Fuel subsidy**
- Al Jazeera (2022 ₦4.39tn/$10bn) — https://www.aljazeera.com/news/2023/5/31/nigeria-fuel-subsidy-cut-spiralling-costs-all-you-need-to-know
- Premium Times (2023 ₦3.6tn) — https://www.premiumtimesng.com/news/headlines/701270-despite-tinubus-pronouncement-nigerian-govt-spent-n3-6-trillion-on-subsidy-in-2023.html
- Sahara Reporters (2024 ₦7.1tn "energy security expense") — https://saharareporters.com/2025/11/25/nnpc-report-shows-tinubu-government-spent-n71trillion-subsidies-2024-captured-energy

---

## GAPS (left blank by design, not guessed)
- **Budget composition 2015–2021** (only 2022–2026 pulled this pass; capex historically ~25–30%).
- **FIRS 2015** total; **2017/2018 pension** year-end NAV (interpolated only).
- **PIT as a standalone federal line** — does not exist; PIT is state-collected (≈PAYE bulk of IGR, Table 5a).
- **Tax-by-type full 2025 breakdown** — only VAT (Q3) and oil/non-oil totals published as of pull date; CIT/PPT/EDT year-end naira splits pending.
- **FAAC full-year 2025 total** — not yet published; **State IGR 2025** — not yet published (NBS reports lag ~10 months).
- **Customs 2025 actual** — only ₦6.58tn target confirmed.
