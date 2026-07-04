# Nigeria — Fiscal, Debt-Service & Ways-and-Means Data, 2015–2026

**Purpose:** Cash-flow-squeeze gauges for a Big-Debt-Cycle dataset (Federal Government / FGN basis unless noted).
**Compiled:** 2026-06-29 · **Basis:** FGN-only unless flagged "general government".
**Flags:** `[S]` = SOURCED (primary/official or credible secondary citing official) · `[E]` = ESTIMATED (derivation noted) · `[P]` = PROVISIONAL · `[F]` = FORECAST/BUDGET · `BLANK` = not reliably sourced (left empty by design, not guessed).

---

## READ-FIRST: why the same year shows very different ratios

Three official bodies use three different **revenue denominators**, so a single year can read 65% or 116% depending on the basis:

- **DMO** (Market-Access-Country Debt Sustainability Analysis) uses a broad, general-government-style revenue base → **lower** ratios (e.g. 80.6% for 2022).
- **Budget Office / CBN** use **FGN retained revenue** (cash the FG keeps after statutory transfers/derivation) → the **higher** ratios that breach 100%.
- **IMF Article IV** reports **interest only** (no amortization) over FGN revenue — a narrower numerator; not directly comparable to "debt-service" ratios.

**Naira-float artifact [CRITICAL]:** the June-2023 float (≈₦460→₦1,500/$) inflated naira oil/customs/FX-gain revenue. From 2024 the denominator balloons faster than naira interest costs, **mechanically shrinking every ratio without real relief**. The IMF interest-to-revenue fall from 88% (2022) to 40.8% (2024) is largely this revenue-inflation effect; it re-rises to ~53% in 2025–26 once the one-off 2024 FX windfall normalizes.

**GDP-rebasing artifact [CRITICAL]:** NBS rebased GDP (base 2010→2019, released Jul-2025), raising 2024 nominal GDP ₦277.5tn→₦372.82tn (+34%). Deficit/GDP and tax/GDP ratios are **not comparable across the 2025 break**; the 2026 MTEF uses a ₦557tn rebased denominator.

---

## TABLE 1 — Debt-service-to-revenue, GROSS / broader-revenue basis (%)

| Year | Gross DSR % | Flag | Source (period) |
|---|---|---|---|
| 2015 | BLANK | — | not reliably sourced |
| 2016 | BLANK | — | not reliably sourced |
| 2017 | 57 | [S] | DMO via Vanguard (full-year, DMO basis) |
| 2018 | 51 | [S] | DMO via Vanguard (full-year, DMO basis) |
| 2019 | BLANK | — | not reliably sourced |
| 2020 | 81.1 | [S] | Budget Office MTFF/FSP via Nairametrics (full-year; gross≈retained this year) |
| 2021 | ~96 | [S] | World Bank Macro Poverty Outlook / Budget Office (full-year, "worst on record") |
| 2022 | 80.6 | [S] | DMO MAC-DSA 2022 via Guardian (full-year, DMO/gross basis) |
| 2023 | ~64.5–65 | [S] | total-federal-revenue basis via Nairametrics (full-year) |
| 2024 | ~61 | [E] | = ₦11.89tn debt service ÷ ~₦19.35tn total revenue (Budget Office 2024 BIR); 69% headline uses the narrower ₦17.2tn retained denominator |
| 2025 | 39.4 (budget) / ~44 (flattered) | [F] | 2025 Budget: ₦14.32tn ÷ ~₦36.35tn projected revenue; "~44%" is the post-float-flattered family figure. No confirmed full-year actual |
| 2026 | 48 (budget) | [F] | 2026 Budget: ₦15.9tn ÷ ₦33.39tn via Nairametrics (analyst flags as optimistic) |

---

## TABLE 2 — Debt-service-to-revenue, RETAINED / NET-revenue basis (%) — the >100% series

Uses **FGN retained revenue** (Budget Office BIR / CBN). NESG publishes a stricter measure that runs higher.

| Year | Retained DSR % | Flag | Source (period) |
|---|---|---|---|
| 2015–2019 | BLANK | — | no clean retained-basis print (DMO 2017/2018 = 57%/51% are nearest official anchors) |
| 2020 | 81.1 | [S] | Budget Office / MTFF (full-year) via Nairametrics |
| 2021 | 96 | [S] | Budget Office: debt service ₦4.22tn ÷ retained ₦4.39tn (full-year) |
| 2022 (Jan–Apr) | 118 | [S][P] | Min. of Finance 2023-25 MTFF/FSP: ₦1.94tn ÷ ₦1.63tn — **4-month print, not full year** |
| 2022 (full year) | 106 / 111.8 | [S] | Businessday ₦5.65tn÷₦5.30tn = 106%; **CBN 2022 Statistical Bulletin = 111.8/112%** (narrower retained denom) |
| 2023 | 78 (BIR); NESG >100 | [S] | Budget Office 2023 BIR = 78%; NESG/independent stricter measure puts it above 100% |
| 2024 | 69 (BIR); 116.8 (NESG) | [S] | Budget Office 2024 BIR: ₦11.887tn ÷ ~₦17.2tn retained = 69%; **NESG = 116.8%** |
| 2025 (partial) | 144 (Jan) / ~113 (Q1) / 105 (Jan–Jul, incl. wages) | [S][P] | CBN Jan-2025 ₦696bn÷₦483bn = 144% (single month); NESG Q1 ~113%; Punch Jan–Jul 105% is debt-service+personnel combined (debt service alone ₦9.81tn vs ₦8.35tn target) |
| 2026 | BLANK (retained actual) | — | year in progress; budget projects 48% gross (Table 1) |

> Note: the ANALYSIS.md "still >110% retained (2025)" is consistent with the NESG Q1 ~113% and CBN single-month 144% prints, but no **full-year 2025 retained actual** exists yet.

---

## TABLE 3 — Interest-payments-to-revenue, IMF Article IV (FGN, interest only) (%)

| Year | Interest/revenue % | Flag | Source |
|---|---|---|---|
| 2022 | 88 | [S] | IMF 2024 Article IV (CR 24/102, May-2024), actual. (Earlier 2022 IMF projection had ~92%) |
| 2023 | ~48.7 | [E] | anchor consistent with 88%→40.8% trajectory; **not confirmable** from accessible IMF PDFs (all returned HTTP 403). Treat as estimate; verify in CR 25/157 |
| 2024 | 40.8 | [S] | IMF 2026 Article IV (PR 26/190, publ. 2026-06-09), actual — via TheCable/Businessday/The Sun |
| 2025 | 53.2 | [S][P] | IMF 2026 Article IV, projected |
| 2026 | 53.7 | [S][F] | IMF 2026 Article IV, forecast |
| 2027 | 52.4 | [S][F] | IMF 2026 Article IV, forecast (IMF: interest/revenue ~50% across 2025–28) |

> The 40.8% (2024) → 53.2% (2025) rebound reflects the **fading one-off 2024 FX-revenue windfall** plus rising naira interest costs — once the post-float surge normalized, the ratio re-deteriorated.

---

## TABLE 4 — FGN fiscal aggregates (NGN trillion): retained revenue, expenditure, deficit, debt service

Cleanest internally-consistent 2015–2023 series = **CBN Statistical Bulletin "Summary of FG Finances" (Table B.1.1)** + "Public Debt Servicing" (B.1.2), which reconcile (Expenditure − Retained Revenue = Deficit). 2024–2026 = **Budget Office 2026–2028 MTEF/FSP** + signed 2026 Appropriation Act. CBN debt-service line is **interest/debt-charges only**; DMO actual-paid (incl. principal) shown where available.

| Year | Retained rev. | Expenditure | Deficit | Deficit %GDP | Debt service | Flag | Source / notes |
|---|---|---|---|---|---|---|---|
| 2015 | 3.43 | 4.99 | 1.56 | ~1.6 [E] | 1.06 | [S] | CBN 2022 Bulletin (final) |
| 2016 | 3.18 | 5.86 | 2.67 | ~2.6 [E] | 1.43 | [S] | CBN 2022 Bulletin (final) |
| 2017 | 2.85 | 6.46 | 3.61 | ~3.1 [E] | 1.82 | [S] | CBN 2022 Bulletin (final; provisional ₦4.62tn revenue revised down to ₦2.85tn) |
| 2018 | 4.19 (CBN) / 3.48 (BIR) | 7.81 (CBN) / 7.51 (BIR) | 3.63 (CBN) / 3.64 (BIR) | 2.81 (CBN) / 2.85 (BIR) | 2.16 | [S] | CBN revised vs Budget Office BIR (both shown; debt service agrees) |
| 2019 | 4.84 (CBN) / 4.12 (BIR) | 9.71 (CBN) / 8.30 (BIR) | 4.87 (CBN) / 4.18 (BIR) | 3.35 (CBN) / 2.9 (BIR) | 2.45 | [S] | CBN revised vs Budget Office BIR |
| 2020 | 3.94 | 10.23 | 6.29 (CBN) / 6.60 (Annual Rep.) | 4.08 / ~4.3 | 2.4–3.27 | [S][P] | CBN; debt service range: ₦2.43tn (Annual Report, provisional) to ₦3.27tn (revised, adds W&M/promissory-note interest); external ~₦553bn firm |
| 2021 | 5.04 | 12.16 | 7.12 | 4.04 | 4.22 (CBN) / 2.93 (DMO paid) | [S][P] | CBN 2023 Bulletin revised; DMO actual-paid lower |
| 2022 | 5.63 | 14.95 | 9.32 | 4.61 | 5.66 (CBN) / 3.76 (DMO paid) | [S][P] | CBN 2023 Bulletin revised |
| 2023 | 7.44 (CBN) / 5.99 (OAGF) | 19.81 (CBN) / 19.50 (OAGF) | 12.37 (CBN) / 11.34–13.50 (OAGF) | 5.28 (CBN) / ~5.0 (OAGF) | 8.56 (CBN) / 7.66 (DMO paid) | [P] | CBN flags 2023 provisional; **naira float inflates all naira figures from H2-2023** |
| 2024 | 20.98 (incl GOEs) / 19.88 (excl) | 34.49 | ~13.51 | ~3.6–3.7 | 12.63 | [P][E] | Budget Office 2026–28 MTEF "Actual"; deficit = rev−exp (no single FGN deficit line printed); debt service = 152.7% of budget, ~60% of revenue. DMO total public debt service 2024 ≈₦12.62tn |
| 2025 | 40.89 (incl GOEs) / 38.02 (excl) | 54.99 | 14.10 | 4.17 | 13.94 + 0.38 sinking ≈ 14.32 | [F] | NASS-approved 2025 Appropriation / MTEF; deficit %GDP on pre-rebasing GDP ₦338tn |
| 2026 (a) MTEF/FSP proposal | 34.33 | 54.46 | 20.12 | 3.61 (rebased GDP ₦557tn) | 15.52 + 0.39 sinking | [F] | Budget Office MTEF/FSP (Dec-2025), FGN basis |
| 2026 (b) signed Approp. Act | 36.87 | 68.32 | 31.45 | 6.41 | 15.81 (dom 10.16 + for 5.36) | [S]/[F] | Expenditure & debt service [S] State House (assent 17-Apr-2026); revenue & deficit [F] from BudgIT analysis |

> **2024 fiscal jump is largely valuation:** retained revenue ~₦7.4tn (2023) → ~₦21tn (2024) is mostly the FX/float effect, not real relief — foreign debt service simultaneously overran the 2024 budget by ~242% on naira depreciation.
> **IMF vs FGN basis:** IMF figures are consolidated/general government (deficit 4.8%/4.1%/4.7% GDP for 2023/24/25) and are **not** the FGN lines above — used only for context.

---

## TABLE 5 — CBN Ways & Means stock (NGN trillion, year-end overdraft / deficit-monetization)

**Two series diverge for 2015–2020** (gross vs net; CBN financial-statement basis vs reported overdraft; point-in-year vs year-end). 2021–2024 are consistent across sources and solid. The series is **non-monotonic** because of the May-2023 securitization reset.

| Year-end | W&M stock (₦tn) | Flag | Source / notes |
|---|---|---|---|
| 2015 | 1.75 (Coronation) / 0.86 (Dataphyte) | [S] | two competing bases (Coronation Research vs Dataphyte/Buhari-start series) |
| 2016 | 2.63 (~2.6% GDP) | [S] | Coronation Research |
| 2017 | BLANK | — | ₦1.1tn figure cited is a single-year flow (37.2% of prior-year revenue), not a cumulative stock |
| 2018 | 5.40 | [S] | Coronation Research |
| 2019 | 9.04 (alt 8.72 / 6.0% GDP) | [S] | Coronation Research; Govt & Business Journal |
| 2020 | 11.9 (year-end; gross peaked ~13.8 in H2) | [S] | Coronation Research; Nairametrics. (gauges CSV shows 13.11 — within the gross/net range) |
| 2021 | 17.46 | [S] | Multiple (Nairametrics/Businessday) |
| 2022 | 22.70 | [S] | the figure later securitized (= end-2022 stock) |
| **Peak (May 2023)** | **26.95** | [S] | Guardian / Businessday — the absolute peak |
| 2023 (year-end) | 7.94 (CBN monthly showed 8.21 at Dec) | [S][P] | re-accumulated after May-2023 securitization reset (Legit.ng citing CBN) |
| 2024 (year-end) | 3.27 (−58.9% YoY) | [S] | CBN 2024 financials via Legit.ng |
| 2025 (year-end) | BLANK | — | no clean year-end figure found |
| Jan 2026 | 2.84 | [P] | Guardian |

### Legal cap & breach (Section 38, CBN Act 2007)
- **Rule [S]:** W&M "temporary advances" must not exceed **5% of the previous year's actual collected revenue**, repayable by year-end. (CBN Act 2007 §38; Nairametrics; Punch; DG Onanuga.)
- **Breach evidence [S]:** single-year W&M flows ran 107% (2020), 106.4% (2021), 138% (2022) of prior-year revenue vs the 5% cap → ~21–28× the annual cap in a single year; on a **stock** basis the ₦22.7–26.95tn dwarfs the ~₦325bn that 5% of 2022 revenue would permit → roughly **70–83× the cap**.
- **The "~109× the cap" claim: UNVERIFIED / BLANK** — could not source it from any primary outlet. Sourced breach multiples are ~21–28× (annual flow) and ~70–83× (stock). Do not state "109×" as sourced.
- **Aftermath:** CBN retained the 5% limit (Sep-2024, defying NASS push to 10%); NASS proposed amending §38 to 10% with a 21-year-imprisonment penalty for breach.

### Securitization
- **First / main tranche [S]:** **₦22.7tn** (₦23.7tn House version incl. a ₦1tn 2022 supplementary). Senate 3-May-2023, House 4-May-2023. **40-year** tenor, **9%** coupon, **3-year** principal moratorium. Issued as long-dated FGN bonds to the CBN (not sold to public), added to DMO domestic debt; replaced the prior ~20.5% (MPR+3%) rate; pushed reported public debt to ~₦69tn.
- **Second tranche [S]:** **₦7.3tn** (outstanding balance at 11-Dec-2023; exceeded the statutory limit by ~₦3.577tn). Senate **30-Dec-2023**. **40-year** tenor, **5%** coupon (lower than the first), **3-year** moratorium. Min. Edun (Jun-2024) said the government had repaid ₦7.3tn of securitized W&M.

> **Correction to common framing:** the **peak is ₦26.95tn (May 2023)**, not ₦22.7tn — the ₦22.7tn is the *securitized amount* (end-2022 stock). The "₦23.8tn" figure is the cumulative Buhari-era total (₦856bn→₦23.8tn, +2,635% over 7 years).

---

## TABLE 6 — Revenue context: federally-collected revenue & oil/non-oil split (NGN trillion)

**Primary series:** CBN Statistical Bulletin, Table B.1.1 (federally-collected, gross; net of some upstream oil costs). Oil + Non-oil = Total in every row. All [S], actuals (2018–23 footnoted provisional/revised).

| Year | Total fed-collected | Oil | Non-oil | Oil share | Flag |
|---|---|---|---|---|---|
| 2015 | 6.91 | 3.83 | 3.08 | 55.4% | [S] |
| 2016 | 5.62 | 2.69 | 2.92 | 48.0% | [S] |
| 2017 | 7.44 | 4.11 | 3.34 | 55.2% | [S] |
| 2018 | 9.59 | 5.55 | 4.04 | 57.9% | [S] |
| 2019 | 9.83 | 5.11 | 4.72 | 52.0% | [S] |
| 2020 | 8.77 | 4.16 | 4.62 | 47.4% | [S] |
| 2021 | 10.47 | 4.15 | 6.32 | 39.6% | [S] |
| 2022 | 13.87 | 4.67 | 9.21 | 33.6% | [S] |
| 2023 | 19.25 | 5.66 | 13.59 | 29.4% | [S] |
| 2024 | BLANK (CBN 2024 Excel is debt-only) | — | — | oil ~25.8% / non-oil ~74.2% (CBN via Legit.ng) | [S] (share only) |
| 2025 | 78.08 gross-collectable (budget) | 51.04 gross o&g | ~27.0 | 65.4% (budget concept) | [F] |
| 2026 | 34.33 (FG revenue, not gross fed.) | — | non-oil ~⅔ | — | [F] |

**Cross-reference (different concepts, NOT comparable to CBN series):**
- Budget Office **gross oil revenue**: 2023 ₦8.35tn → 2024 ₦15.07tn (+80.3%) [S].
- NEITI **FAAC distributed** to 3 tiers: 2022 ₦9.18tn · 2023 ₦10.9tn · 2024 ₦15.26tn (+43%) [S].
- FIRS total collections: 2015 3.71 · 2016 3.3 · 2017 4.03 · 2018 5.32 · 2019 5.26 · 2020 4.95 · 2021 6.41 · 2022 10.18 · 2023 12.37 · 2024 ~21.6–21.7 (non-oil 15.9 + oil 5.8) [S].

> **2025 actual (partial) [P]:** oil badly missed — gross oil only ₦4.87tn in one quarter (~62% below target); non-oil ₦20.59tn Jan–Aug 2025 (Budget Office).

---

## TABLE 7 — Tax-to-GDP (%) — three non-interchangeable measures

The "famous low" number depends entirely on definition. ~6% = old FIRS-only narrow federal; ~8–10% = broad all-levels (NBS/IMF/OECD); the gap is mainly whether **oil rents/royalties count as tax** (NBS yes, OECD no) and the **GDP base** used.

### Measure 1 — NBS "Revised" (all levels, includes oil taxes; OLD pre-rebasing GDP)
Source: NBS "Tax-to-GDP Ratio Revised Computation" (Jun-2023). All [S].

| Year | Tax/GDP % |
|---|---|
| 2015 | 9.78 |
| 2016 | 8.28 |
| 2017 | 9.02 |
| 2018 | 10.36 |
| 2019 | 10.20 |
| 2020 | 8.40 |
| 2021 | 10.86 |

This 10.86% (2021) replaced the old FIRS-only ~6% narrow measure. 2022–26 not covered.

### Measure 2 — OECD Revenue Statistics in Africa 2025 (international, EXCLUDES oil rents → lower; old GDP)
- 2022 **7.9** [S] · 2023 **8.2** [S] · (ref: 2016 5.3 lowest, 2011 9.7 highest). 2015/2017–2021 exact values BLANK (only chart points published; live in OECD Data Explorer). OECD reclassifies oil rents/royalties (5.93% of GDP in 2023) as **non-tax**, explaining the ~2–3pt gap vs NBS.

### Measure 3 — IMF (general-government tax revenue/GDP)
- 2023 **9.4** [S] (IMF via TheCable; CR 25/157). Old GDP basis.

### Government 2024 figure (methodology-flagged)
- **13.5% (2024)** [S] — Presidency/Fiscal Policy Committee (Oyedele), broad all-levels, **on OLD pre-rebasing GDP ~₦277.5tn**. On the **rebased 2024 GDP ₦372.82tn the same taxes imply ≈10%** (PwC ~9.5%). This old-vs-rebased gap is the single biggest source of confusion.

---

## Key cross-cutting flags (for the dataset)

1. **Post-June-2023 naira float** roughly doubled naira oil/federation revenue (gross oil ₦8.35tn→₦15.07tn 2023→24; FAAC +43% to ₦15.26tn; NEITI mineral revenue +>400%). This **mechanically improves every debt-service / interest ratio from 2024** without real cash-flow relief — flag any ratio improvement after 2023 as partly a valuation effect.
2. **2024 GDP rebasing** (₦277.5tn→₦372.82tn) breaks comparability of all %-of-GDP ratios across 2024/2025; the 2026 MTEF uses ₦557tn.
3. **Denominator choice** (DMO gross vs Budget-Office/CBN retained vs IMF interest-only) explains 65% vs 116% for the same year — always tag the basis.
4. **CBN revises provisionals heavily** (e.g. 2017 retained revenue ₦4.62tn provisional → ₦2.85tn final). Budget Office BIR (cash) differs from CBN revised actuals; both shown for 2018–19.
5. **W&M peak = ₦26.95tn (May 2023)**, not ₦22.7tn; "109× the cap" is **unverified** (sourced breach is ~21–28× annual flow / ~70–83× stock).

---

## Sources

**Primary / official**
- CBN 2022 Statistical Bulletin — Public Finance (XLSX, 2015–17 final): https://www.cbn.gov.ng/Out/2023/STD/2022%20Statistics%20Bulletin_Public%20Finance.xlsx
- CBN 2023 Statistical Bulletin — Public Finance (XLSX, 2018–23): https://www.cbn.gov.ng/Out/2024/STD/2023%20Statistics%20Bulletin_Public%20Finance.xlsx (index: https://www.cbn.gov.ng/documents/Statbulletin.html)
- CBN 2020 Annual Economic Report (PDF): https://www.cbn.gov.ng/out/2023/rsd/2020%20cbn%20annual%20report....pdf
- CBN 2024 Summary Financial Statements (W&M, PDF): https://www.cbn.gov.ng/Out/2025/CCD/Year%202024%20Summary%20Financial%20Statements.pdf
- CBN Act 2007 (§38, primary): https://www.cbn.gov.ng/OUT/CIRCULARS/CSD/2007/CBN%20ACT%202007.PDF
- Budget Office 2018 Q4 BIR: https://budgetoffice.gov.ng/index.php/resources/internal-resources/reports/quarterly-budget-implementation/2018-fourth-quarter-budget-implementation-report/download
- Budget Office 2019 Q4 BIR: https://budgetoffice.gov.ng/index.php/resources/internal-resources/reports/quarterly-budget-implementation/2019-fourth-quarter-budget-implementation-report/download
- Budget Office 2026–2028 MTEF/FSP (2024 actuals, 2025 approval, 2026 proposal): https://budgetoffice.gov.ng/index.php/2026-2028-mtef-fsp/2026-2028-mtef-fsp/viewdocument/1000
- State House, 2026 Appropriation assent (17-Apr-2026): https://statehouse.gov.ng/president-tinubu-assents-to-2026-appropriation-bill-and-2025-budget-extension/
- State House, 2026 Appropriation Bill presentation (₦58.18tn): https://statehouse.gov.ng/president-tinubu-presents-%E2%82%A658-18-trillion-2026-appropriation-bill-vows-stronger-discipline-in-budget-execution/
- DMO debt service: https://www.dmo.gov.ng/debt-profile/external-debts/debt-service
- NBS Tax-to-GDP Revised Computation (Jun-2023): https://www.nigerianstat.gov.ng/pdfuploads/TAX-TO-GDP%20RATIO%20REVISED%20COMPUTATION-2021.pdf
- NEITI, FAAC allocations 2024: https://neiti.gov.ng/cms/faac-allocations-soar-by-43-in-2024/
- OECD Revenue Statistics in Africa 2025 — Nigeria: https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/11/revenue-statistics-in-africa-2025-country-notes_ee0ba7f7/nigeria_798060d4/fc80552b-en.pdf
- IMF Nigeria 2024 Article IV (CR 24/102): https://www.imf.org/en/Publications/CR/Issues/2024/05/08/Nigeria-2024-Article-IV-Consultation-Press-Release-Staff-Report-Staff-Statement-and-548726
- IMF Nigeria 2025 Article IV (CR 25/157): https://www.imf.org/en/publications/cr/issues/2025/07/01/nigeria-2025-article-iv-consultation-press-release-staff-report-and-statement-by-the-568220
- IMF Nigeria 2026 Article IV (PR 26/190, publ. 2026-06-09): reported via TheCable/Businessday/The Sun (IMF PDFs returned HTTP 403)

**Secondary (citing official data)**
- Vanguard, DMO 2017/2018 DSR (57%/51%): https://www.vanguardngr.com/2019/12/dmo-clarifies-nigerias-external-debt/amp/
- Nairametrics, "118% of revenue on debt service" (2020 81.1%, Jan–Apr 2022 118%): https://nairametrics.com/2022/07/21/nigeria-spends-118-of-revenue-on-debt-service/
- Nairametrics, 2021 96% "worst on record": https://nairametrics.com/2022/05/05/nigeria-spends-96-of-its-revenue-on-debt-servicing-in-2021-worst-on-record/
- Businessday, "96% of 2022 revenue / 106% of FG revenue 2022": https://businessday.ng/news/article/96-of-nigerias-revenue-spent-on-debt-servicing-in-2022-world-bank/ ; https://businessday.ng/news/article/debt-servicing-gulped-106-of-fgs-revenue-in-2022/
- Guardian, DMO MAC-DSA 80.6% (2022): https://guardian.ng/news/debt-service-gulps-80-6-of-2022-revenue-fg-seeks-fresh-n8-8tr-loans/
- Nairametrics, CBN 112% (2022): https://nairametrics.com/2023/05/17/nigerias-debt-service-to-revenue-ratio-rises-to-112-in-2022-cbn/
- Guardian / Leadership, 2024 BIR 69%: https://guardian.ng/business-services/debt-service-takes-69-of-2024-revenue-as-fg-releases-budget-performance/ ; https://leadership.ng/nigeria-spends-69-of-2024-revenues-on-debt-service-budget-office-report/
- CNBC Africa, Jan-2025 144%: https://www.cnbcafrica.com/media/6372064852112/nigerias-debt-service-obligations-hit-69627bn-in-january-2025--cbn
- Punch, "salaries + debt service 105%" (Jan–Jul 2025): https://punchng.com/salaries-debt-service-gulp-105-of-govt-revenue/
- Nairametrics, "Is Nigeria sliding into a debt trap?" (2023/2026 gross, NESG Q1 2025): http://nairametrics.com/2026/05/24/is-nigeria-sliding-into-a-debt-trap/
- TheCable, IMF interest-to-revenue 2024/25/26 (40.8/53.2/53.7): https://www.thecable.ng/imf-nigeria-to-spend-over-half-of-revenue-on-debt-servicing-in-2026/
- TheCable, IMF tax/GDP 9.4% (2023): https://www.thecable.ng/imf-at-9-4-in-2023-nigerias-tax-revenue-to-gdp-ratio-among-lowest-in-the-world/
- Nairametrics, securitization ₦22.7tn (May-2023): https://nairametrics.com/2023/05/05/ways-and-means-national-assembly-securitizes-n22-7-trillion-cbn-loan-public-debt-now-n69-trillion/
- Nairametrics, second securitization ₦7.3tn (Dec-2023): https://nairametrics.com/2023/12/30/senate-approves-securitization-of-n7-3-trillion-ways-and-means-outstanding-debt/
- Nairametrics, end-2023 W&M re-accumulation: https://nairametrics.com/2024/04/26/ways-means-fg-borrows-additional-n3-8-trillion-from-cbn-in-6-months/
- Guardian, W&M ₦26.95tn peak → ₦2.84tn: https://guardian.ng/news/cbn-slashes-ways-and-means-to-n2-84tr-from-n26-95tr-in-2023/
- Legit.ng, W&M 2023 ₦7.94tn → 2024 ₦3.27tn: https://www.legit.ng/business-economy/industry/1653308-cbn-reduces-ways-means-advances-by-59-reinforce-fiscal-discipline/
- Coronation Research, W&M 2015–2020 series: https://www.coronationmb.com/cbn-funding-the-government/
- Punch, CBN keeps 5% W&M cap: https://punchng.com/just-in-cbn-defies-nassembly-maintains-5-ways-and-means-advance-limit/
- Legit.ng, 2024 oil share ~25.8%: https://www.legit.ng/business-economy/economy/1657937-nigeria-grew-oil-gas-revenue-by-70-year-cbn-report/
- NEITI / Nation, FAAC ₦15.26tn (2024): https://thenationonlineng.net/neiti-puts-faac-disbursements-to-three-tiers-of-govt-in-2024-at-n15-26tr/
- Nairametrics, gross oil revenue 2024 / 2025 H1 miss: https://nairametrics.com/2025/10/24/oil-revenue-declines-22-to-n3-9-trillion-in-q4-2024-budget-office/ ; https://nairametrics.com/2025/12/24/nigerias-gross-oil-revenue-misses-2025-budget-target-in-h1-2025-budget-office/
- KSBC Journal / Businessday, tax/GDP 13.5% (2024): https://ksbcjournal.com/2025/05/30/nigerias-tax-revenue-to-gdp-ratio-rose-to-13-5-in-2024/
- Nairametrics, rebased GDP ₦372.82tn (2024): https://nairametrics.com/2025/07/21/rebased-gdp-report-shows-nigerias-economy-hits-n372-82-trillion-in-2024-nbs/
- BudgIT, 2026 budget deficit ₦31.45tn: https://budgit.org/post_publications/2026-fg-proposed-budget/ ; Businessday: https://businessday.ng/business-economy/article/nigeria-to-borrow-for-nearly-half-of-2026-budget-as-deficit-hits-n31-45tn-budgit-warns/

---

*Compiled 2026-06-29 from four parallel primary-source research passes (CBN, DMO, Budget Office, NBS, NEITI, OECD, IMF Article IV, plus credible secondary outlets citing official data). Values left BLANK where no reliable source was found — not guessed. IMF.org/elibrary PDFs returned HTTP 403 to automated fetch; IMF figures confirmed via secondary outlets quoting the reports and should be verified against CR 25/157 and the 2026 Article IV (PR 26/190).*
