# Nigeria — Monetary Aggregates, Credit & Banking-System Health (2015–2026)

**Dataset:** Big-Debt-Cycle / Nigeria
**Compiled:** 2026-06-30
**Coverage:** Annual (year-end) + selected monthly/quarterly anchors where the underlying series is monthly.
**Source priority:** Central Bank of Nigeria (CBN), IMF (Article IV / Financial Soundness Indicators), World Bank, DMO, FMDQ. Secondary trade press (Nairametrics, Vanguard, BusinessDay, ThisDay, Proshare) is used **only where it explicitly quotes a CBN/DMO release** and is flagged as such.

**Flag legend:** `[SOURCED]` = taken directly from a cited primary/official source (or trade press quoting it verbatim) for the stated period · `[PROVISIONAL]` = sourced but period is intra-year (not strictly Dec), preliminary, or a still-moving latest vintage · `[ESTIMATED]` = derived/computed (method noted) or secondary-aggregator value · blank = not reliably sourceable this session, left blank rather than guessed.

---

## CRITICAL METHODOLOGY NOTES (read first)

**1. M2 → M3 headline break (~2021).** CBN historically published **M2** (= M1 + quasi-money) as headline broad money. In its 2021 monetary-statistics revision CBN adopted **M3** as the headline aggregate, where **M3 = M2 + CBN bills / OMO bills held by the money-holding (non-bank) sector**, and reclassified some items. Consequently:
- Pre-2021 "broad money" rows below are **M2** unless marked otherwise.
- 2020–2026 rows are **M3** (CBN current headline). The 2020 value (~₦38.6 trn) is the bridge point where IMF-IFS broad money and the CBN M3 series coincide.
- The **IMF International Financial Statistics (IFS) "broad money"** series (≈ M3 basis throughout) is shown separately as a consistency backbone for 2015–2020.

**2. 2023–2024 credit/money jump is partly a valuation effect.** The naira float (Jun 2023) and second devaluation (Jan–Feb 2024) roughly tripled the naira value of FX-denominated bank loans and FX deposits, mechanically inflating Credit-to-Private-Sector (CPS) and M3 in 2023–2024 independent of new lending. Treat 2023→2024 growth rates as **not like-for-like**.

**3. CPS reclassification (Apr 2024).** CBN's reported CPS "crashed ₦9.65 trn in one month" (Apr 2024) due to a **statistical reclassification** (removing certain CBN/government-directed credit from the private-sector line), not a real contraction. There are therefore two CPS vintages around 2024 (~₦76 trn pre-reclassification vs ~₦75 trn after). Series break flagged.

**4. Credit-to-GDP — two incompatible measures.** The **World Bank** "domestic credit to private sector by banks (% of GDP)" runs ~11–14% (narrow: deposit-money-bank credit only). A **CBN-CPS ÷ nominal-GDP** computation runs ~25–30% recently (broad CPS incl. FX-revalued and CBN-intervention credit). They are not interchangeable; both shown, computed ones flagged `[ESTIMATED]`.

**5. Banking ratios — forbearance distortion (2025).** CBN's COVID-era regulatory forbearance was withdrawn through 2025. This pushed reported **NPLs sharply up** and **CAR down** in H2-2025 as banks reclassified previously-masked bad loans. End-2024 and 2025 figures straddle this break — flagged.

**6. Regulatory minimums (for reference):** CAR ≥ 10% (national/regional licence), ≥ 15% (international licence); Liquidity ratio ≥ 30%; NPL prudential ceiling ≤ 5%; minimum Loan-to-Deposit Ratio (LDR) = 65% (CBN policy effective Dec 2019).

---

## 1. BROAD MONEY SUPPLY — ANNUAL (year-end)

| Year-end | Headline broad money (NGN trn) | Series | y/y growth % | IMF-IFS broad money (NGN trn) | Flag |
|---|---|---|---|---|---|
| Dec 2015 | 18.74 | M2 (CBN) | — | 21.29 | M2 [SOURCED]; IFS [ESTIMATED] |
| Dec 2016 | 20.91 | M2 (CBN) | +11.6% (computed) | 28.08 *(see note)* | M2 [SOURCED]; IFS [ESTIMATED — anomalous, see note] |
| Dec 2017 | — | M2 (CBN) | — | 28.47 | IFS [ESTIMATED] |
| Dec 2018 | — | M2 (CBN) | — | 32.74 | IFS [ESTIMATED] |
| Dec 2019 | — | M2 (CBN) | — | 34.85 | IFS [ESTIMATED] |
| Dec 2020 | 38.63 | M3 (CBN) = IFS | — | 38.63 | [SOURCED] |
| Dec 2021 | 43.82 | M3 (CBN) | +13.4% (computed); CBN stated M3 +12.6% | — | [SOURCED] |
| Dec 2022 | 52.16 | M3 (CBN) | +19.0% (computed) | — | [SOURCED] |
| Dec 2023 | 78.74 | M3 (CBN) | +51.0% (computed) | — | [SOURCED] |
| Dec 2024 | 113.36 | M3 (CBN) | +44.0% (computed) | — | [SOURCED] |
| Dec 2025 | 124.40 | M3 (CBN) | +9.7% (computed) | — | [SOURCED / PROVISIONAL] |
| 2026 | — | M3 (CBN) | — | — | (not yet year-end) |

**Notes:**
- **2016 IFS anomaly:** the IndexMundi/IMF-IFS value (₦28.08 trn) is inconsistent with both the CBN M2 (₦20.91 trn) and the near-flat 2017 IFS value (₦28.47 trn). Likely a row-misalignment in the secondary aggregator — **do not rely on it**; flagged.
- Intra-2025 path (CBN, via Nairametrics): M3 fell to ₦110.32 trn (Feb 2025, first 2025 drop), recovered to ₦122.95 trn (Nov 2025, +12.8% y/y), ₦124.4 trn (Dec 2025). Components Nov 2025: Net Domestic Assets ₦85.57 trn, Net Foreign Assets ₦37.38 trn (NFA more than doubled y/y from ₦17.35 trn Nov 2024 on reserve rebuild). [SOURCED — CBN via Nairametrics]
- 2024 growth driven heavily by naira-devaluation revaluation of FX deposits (see Methodology #2).

---

## 2. CREDIT TO THE PRIVATE SECTOR & CREDIT-TO-GDP

| Year-end | Credit to private sector, CPS (NGN trn) | y/y % | Credit-to-GDP %, World Bank (banks) | Credit-to-GDP %, CBN-CPS÷GDP (computed) | Flag |
|---|---|---|---|---|---|
| Dec 2015 | — | — | — | — | |
| Dec 2016 | — | — | — | — | |
| Dec 2017 | — | — | — | — | |
| Dec 2018 | — | — | — | — | |
| Dec 2019 | ~26.0 | — | 11.16 | — | WB [SOURCED]; CPS [ESTIMATED] |
| Dec 2020 | 26.4 (Nov 2020) | — | 12.13 | — | [PROVISIONAL — Nov, not Dec]; WB [SOURCED] |
| Dec 2021 | ~35.0–35.3 (Nov 2021) | +33% | — | — | [PROVISIONAL]; CBN via Vanguard [SOURCED] |
| Dec 2022 | 41.8 | +18.8% | 14.09 | ~21% | CPS & WB [SOURCED]; ratio [ESTIMATED] |
| Dec 2023 | 62.54 | +51% (incl. FX reval.) | — | ~25% | CPS [SOURCED]; ratio [ESTIMATED] |
| Dec 2024 | ~75.96 (post-reclassification) | ~+21% | — | ~27% | CPS [SOURCED/PROVISIONAL]; ratio [ESTIMATED] |
| 2025 (recent) | 73.66 (Feb 2025); ~77 (late 2025) | — | — | — | [PROVISIONAL — CBN via Nairametrics] |

**Notes:**
- CPS pre-reclassification Jan 2024 spiked to ₦76.48 trn, then "crashed ₦9.65 trn" in Apr 2024 on reclassification (Methodology #3). Both vintages quoted by CBN; treat 2024 as a series break.
- Vanguard (Nov 2025, quoting CBN): private-sector credit "soars 75.9% in 2 years."
- World Bank credit-to-GDP (narrow bank measure) understates effective penetration vs the CBN broad CPS line; the two should not be mixed (Methodology #4).
- CBN's 65% minimum LDR policy (Dec 2019) is the main driver of the 2020–2023 organic CPS expansion; 2023–24 is amplified by FX revaluation.

### 2b. Net domestic credit / credit to government (CBN)

| Period | Net domestic credit (NGN trn) | Credit to government | Flag |
|---|---|---|---|
| Nov 2020 | 35.5 | — | [PROVISIONAL — CBN via Nairametrics] |
| Nov 2021 | 48.3 (+36% y/y) | — | [PROVISIONAL — CBN via Nairametrics] |
| 2022 | — | New credit to govt +₦11.33 trn (+92% vs 2021) | [SOURCED — flow, not stock] |
| 2025 | Banking-sector credit to the economy ≈ ₦111.4 trn (total) | — | [PROVISIONAL — Guardian quoting CBN] |

*Stock levels of net claims on government for 2015–2019 and 2023–2025 were not reliably sourceable this session — left blank rather than guessed. CBN Money & Credit Statistics .xlsx (mnycredit.html) holds the full monthly series.*

---

## 3. POLICY & RETAIL INTEREST RATES (CBN)

### 3a. Monetary Policy Rate (MPR) — year-end

| Year-end | MPR % | Flag |
|---|---|---|
| 2015 | 11.00 | [SOURCED] |
| 2016 | 14.00 | [SOURCED] |
| 2017 | 14.00 | [SOURCED] |
| 2018 | 14.00 | [SOURCED] |
| 2019 | 13.50 | [SOURCED] |
| 2020 | 11.50 | [SOURCED] |
| 2021 | 11.50 | [SOURCED] |
| 2022 | 16.50 | [SOURCED] |
| 2023 | 18.75 | [SOURCED] |
| 2024 | 27.50 | [SOURCED] |
| 2025 | 27.00 | [SOURCED] |
| mid-2026 | <27.00 (marginal cut signalled; exact level TBC) | [PROVISIONAL] |

*Tightening cycle: 11.5% (mid-2022) → 13 → 14 → 15.5 → 16.5 (Nov 2022) → 18.75 (Jul 2023) → 22.75 → 24.75 → 26.25 → 27.25 → 27.50 (Nov 2024); first cut to 27.00% at the 303rd MPC (24–25 Nov 2025); a further marginal reduction signalled by mid-2026.*

### 3b. Bank lending & deposit rates (CBN Money Market Indicators / weekly returns)

| Period | Avg prime lending % | Avg maximum lending % | Avg savings deposit % | Flag |
|---|---|---|---|---|
| Jan 2024 | — | 27.07 | — | [SOURCED] |
| Mar 2024 | — | 29.38 | — | [SOURCED] |
| Dec 2024 | — | 29.71 | — | [SOURCED] |
| Jan 2025 | 18.49 | 29.79 | — | [SOURCED] |
| Jul 2025 | — | 29.31 | — | [SOURCED] |
| Aug 2025 | 18.88 | 29.13 | — | [SOURCED] |
| Oct 2025 | 18.88 | — | — | [SOURCED] |
| 31 Oct 2025 | — | — | 8.25 | [SOURCED — CBN] |
| Dec 2025 | 18.02 | — | — | [SOURCED] |
| Apr 2026 | — | 35.17 | — | [SOURCED] |
| May 2026 | — | 34.78 | — | [SOURCED] |

*Prime rate has been remarkably sticky (~18–19%) through the tightening cycle while the maximum (retail/SME) rate climbed from ~27% (early 2024) toward ~35% (2026) — a widening prime-to-max spread signalling credit-risk repricing. 2015–2023 year-end prime/max levels not pulled this session (available in CBN Money Market Indicators, mnymktind.html). Pre-2022 savings rate was ~3–4% in the low-rate era (2020–21); 8.25% reflects the post-2024 tightening.*

---

## 4. TREASURY-BILL & FGN BOND YIELDS

### 4a. NTB stop rates (primary auction; year-end / nearest)

| Period | 91-day % | 182-day % | 364-day % | Flag |
|---|---|---|---|---|
| Nov 2020 | — | — | 0.233 (record low) | [SOURCED — extreme-liquidity era] |
| Dec 2023 | ~7.0 | ~10.0 | ~12–13 | [SOURCED / PROVISIONAL] |
| Nov 2024 | — | — | 23.5 (2024 peak; ATH 23.26 series) | [SOURCED] |
| Dec 2024 | 18.0 | 18.5 | ~22.6 | [SOURCED] |
| Jan 2025 | 18.0 | 18.5 | 22.62 | [SOURCED] |
| Nov 2025 | 15.3 | — | ~15–18 (easing) | [SOURCED — declining trend] |

*364-day NTB stop rate range Jan 2008–Dec 2025: avg 18.6%, ATH 23.26% (Nov 2024), record low 0.233% (Nov 2020). Stop rates ≠ secondary-market yields.*

### 4b. FGN bond yields (auction stop / secondary)

| Period | ~5yr % | ~10yr % | ~15–20yr % | Basis | Flag |
|---|---|---|---|---|---|
| Dec 2023 | 15.00 (2027) | 15.50–16.00 (2029/2033) | 16.50 (2038) | Auction stop | [SOURCED] |
| Jan 2024 | — | 14.49 (avg secondary) | — | Secondary | [SOURCED] |
| May 2025 | — | ~19.76 (implied) | — | Secondary OTC | [ESTIMATED — back-derived] |
| May 2026 | — | 14.96 | — | Secondary OTC | [SOURCED] |

*The 10yr OTC yield was "4.80 pts lower than a year ago" at 14.96% on 26 May 2026 → implies ~19.76% May 2025. 5yr/20yr year-end secondary levels for most years were not cleanly sourceable this session.*

### 4c. Rough yield-curve snapshots

| Maturity | End-2023 | End-2024 | Mid-2026 (latest) | Flag |
|---|---|---|---|---|
| 91-day | ~7.0 | 18.0 | ~15.3 (Nov'25) | [SOURCED/PROVISIONAL] |
| 182-day | ~10.0 | 18.5 | — | [SOURCED] |
| 364-day | ~12–13 | ~22.6 | ~15–18 | [SOURCED/PROVISIONAL] |
| 5yr | ~15.0 | ~21 (elevated) | — | end-2023 [SOURCED]; end-2024 [ESTIMATED] |
| 10yr | ~15.5–16.0 | ~21–22 | 14.96 | end-2023 [SOURCED]; 2026 [SOURCED]; 2024 [ESTIMATED] |
| 20yr | ~16.5 | ~20 | — | end-2023 [SOURCED]; 2024 [ESTIMATED] |

*Shape: end-2023 a normal upward curve (~7%→16.5%); end-2024 a sharply higher, near-flat/humped curve (front end ~18–23% post-tightening, long end ~20–22%) — effectively flat-to-inverted at the very front; mid-2026 yields falling as easing begins (10yr back below 15%). End-2024 long-end figures are estimates and should be replaced with FMDQ end-of-day marks if precision is needed.*

---

## 5. BANKING-SYSTEM SOUNDNESS (industry, CBN FSR / IMF FSI / WB)

| Period | NPL ratio % | CAR % | Liquidity ratio % | LDR % | Flag |
|---|---|---|---|---|---|
| 2015 | — | — | — | — | |
| 2016 | — | — | — | — | |
| 2017 | 14.8 (cycle peak) | ~10.5 | — | — | NPL [SOURCED]; CAR [ESTIMATED] |
| 2018 | — | — | — | — | |
| 2019 | — | — | — | ≥65 (policy min) | LDR policy [SOURCED] |
| 2020 | — | 15.2 | — | — | CAR [SOURCED] |
| 2021 | 4.93 | — | — | — | [SOURCED — WB] |
| 2022 | 4.01 | <15 (just under) | — | — | NPL [SOURCED-WB]; CAR [SOURCED-IMF] |
| 2023 | ~4.0 (comm. banks) | 13.3 | — | — | [SOURCED — IMF Art. IV] |
| Apr 2024 | — | 10.81 | — | — | [SOURCED] |
| Dec 2024 | 4.50 (CBN FSR); 5.2 (alt.) | 12.52 (Q4) | 40.14 / 43.59 (Q4) | — | [SOURCED — conflicting NPL vintages] |
| Q1 2025 | — | 15.20 | 49.06 | — | [SOURCED] |
| Apr 2025 | 5.62 | 15.55 | 55.4 (Mar) | — | [SOURCED] |
| Jul 2025 | — | 12.0 (post-forbearance withdrawal) | — | — | [SOURCED] |
| End-2025 | ~7–9.85 (forbearance exit) | ~12 | 65 | — | [PROVISIONAL — moving] |

**Notes:**
- **NPLs:** cycle peak **14.8% in 2017** (oil-price crash/recession), down to ~4–5% (2019–2024). The 2025 spike to ~5.6% (Apr) → ~7% → as high as **9.85%** (late 2025) is driven by the **withdrawal of regulatory forbearance** and IFRS Stage-3 reclassifications (11 banks breached the 5% ceiling). Multiple Dec-2024 NPL vintages exist (4.50% CBN FSR vs 5.2% alt.) — both shown.
- **CAR:** dipped to **10.81% (Apr 2024)**, rebuilt to ~15.2–15.6% (Q1–Q2 2025) on recapitalisation, then fell to **~12% (Jul 2025)** once forbearance was withdrawn. Min 10%/15% by licence class.
- **Liquidity ratio:** comfortably above the 30% floor throughout the visible window — 40–43% (2024) rising to 49–55% (Q1 2025) and ~65% (end-2025).
- **LDR:** specific industry actuals were not cleanly sourceable this session; the binding figure is the **CBN 65% minimum LDR policy (effective Dec 2019)**, which most banks operate near/above. 2015–2018, 2023 NPL/CAR and most LDR cells left blank rather than guessed — full series is in CBN Financial Stability Reports and the IMF FSI database.

---

## SOURCES

**Central Bank of Nigeria (CBN):**
- Money & Credit Statistics — https://www.cbn.gov.ng/rates/mnycredit.html
- Money Market Indicators (lending/deposit rates) — https://www.cbn.gov.ng/rates/mnymktind.html
- Macro-Economic Indicators — https://www.cbn.gov.ng/rates/MacroIndicators.html
- Government Securities (NTB/bond) — https://www.cbn.gov.ng/rates/GovtSecurities.html
- Monetary Policy Decisions (MPR) — https://www.cbn.gov.ng/MonetaryPolicy/decisions.html
- Weekly Interest Rates (banks' deposit/lending) — e.g. https://www.cbn.gov.ng/Out/2025/BSD/WEEKLY%20INTEREST%20RATES%20AS%20AT%20FEBRUARY%2021,%202025.pdf
- 2022 Annual Economic Report — https://www.cbn.gov.ng/Out/2024/RSD/2022%20ANNUAL%20REPORT.pdf
- Q4 2021 Economic Report (M3 +12.6%) — https://www.cbn.gov.ng/out/2022/rsd/ecr%202021q4.pdf
- CBN Macroeconomic Outlook 2026 — https://www.cbn.gov.ng/Out/2025/CCD/CBN%20Macroeconomic%20Outlook%20for%20Nigeria%20Report_28_122025_DG.pdf

**IMF:**
- Nigeria 2024 Article IV Consultation (FSIs: CAR 13.3% end-2023, NPL ~4%) — https://www.elibrary.imf.org/view/journals/002/2024/102/article-A001-en.xml
- Nigeria 2022 Article IV Consultation — https://www.imf.org/-/media/Files/Publications/CR/2023/English/1NGAEA2023001.ashx
- IMF International Financial Statistics (broad money, line 35L..ZK) — via IndexMundi mirror https://www.indexmundi.com/facts/nigeria/broad-money
- IMF Financial Soundness Indicators — https://data.imf.org

**World Bank:**
- Broad money (current LCU), NG — https://data.worldbank.org/indicator/FM.LBL.BMNY.CN?locations=NG
- Domestic credit to private sector (% of GDP), NG — https://data.worldbank.org/indicator/FS.AST.PRVT.GD.ZS?locations=NG ; theglobaleconomy.com mirror https://www.theglobaleconomy.com/Nigeria/domestic_credit_private_sector/
- Bank NPLs to gross loans (%), NG — https://data.worldbank.org/indicator/FB.AST.NPER.ZS?locations=NG ; theglobaleconomy.com mirror https://www.theglobaleconomy.com/Nigeria/nonperforming_loans/

**DMO / FMDQ:**
- DMO Nigerian Treasury Bills — https://www.dmo.gov.ng/fgn-bonds/nigerian-treasury-bills
- DMO FGN Bond Auction Results — https://www.dmo.gov.ng/fgn-bonds/bonds-auction-results
- DMO Summary of FGN Bond Auction Results Dec 2024 — https://www.dmo.gov.ng/fgn-bonds/bonds-auction-results/5021-summary-of-fgn-bond-auction-results-for-december-2024

**Secondary press (each quoting CBN/DMO; flagged accordingly):**
- Nairametrics — M3 Dec 2023 ₦78.74 trn: http://nairametrics.com/2024/01/30/nigerias-money-supply-hits-all-time-high-of-n78-74-trillion-in-december-2023/ ; M3 Dec 2025 ₦124.4 trn: http://nairametrics.com/2026/01/24/nigerias-money-supply-hits-n124-4-trillion-in-december-2025/ ; M3 2022 ₦52.14 trn / 2021 ₦43.82 trn: http://nairametrics.com/2023/01/31/money-supply-in-nigeria-rose-to-n52-14-trillion-in-2022-despite-cbns-hawkish-policies/ ; CPS Feb 2025 ₦73.66 trn: https://nairametrics.com/2025/03/26/credit-to-private-sector-declines-to-n73-66-trillion-in-february-2025-cbn/ ; CPS reclassification Apr 2024: https://nairametrics.com/2024/05/04/credit-to-private-sector-crashes-by-n9-65-trillion-in-one-month/ ; 364-day NTB 22.62% Jan 2025: https://nairametrics.com/2025/01/09/cbn-secures-n1-47-trillion-in-subs-for-364-day-treasury-bills-22-6-stop-rate/ ; NPL 5% breach: https://nairametrics.com/2025/07/22/11-banks-breach-non-performing-loan-limit-after-debt-reclassifications-mpc-member/
- Vanguard — CPS +75.9% in 2yrs (Nov 2025): https://www.vanguardngr.com/2025/11/nigerias-private-sector-credit-soars-75-9-in-2-years/ ; banks' credit +33% to ₦35 trn: https://www.vanguardngr.com/2022/01/banks-credit-to-private-sector-rises-33-to-n35trn/ ; CAR drops to 12% post-forbearance: https://www.vanguardngr.com/2025/11/banks-capital-adequacy-drops-to-12-after-forbearance-withdrawal-cbn/
- BusinessDay — NPL 3.9% / forbearance-exit NPL near 10%: https://businessday.ng/banking-finance/article/banks-non-performing-loans-decline-to-3-9-on-cbns-policy-mpc-members/ ; https://businessday.ng/business-economy/article/forbearance-exit-pushes-banking-sector-npl-ratio-near-10/
- ThisDay — max lending 29.79% (Feb 2025): https://www.thisdaylive.com/2025/02/26/cost-of-borrowing-soars-as-maximum-lending-rate-hits-29-79/ ; prime 18.88% / MPR 27% (Oct 2025): https://www.thisdaylive.com/2025/10/20/prime-lending-rate-steady-18-88-amid-27-monetary-policy-rate/ ; max lending 34.78% May 2026: https://www.thisdaylive.com/2026/06/29/interest-rate-banking-sector-maximum-lending-rate-drops-to-34-78/ ; 364-day NTB 23.5% (Dec 2024): https://www.thisdaylive.com/2024/12/02/cbn-raises-n11-29trn-via-ntbs-as-364-day-yield-hit-23-5/ ; 91-day 15.3% (Nov 2025): https://www.thisdaylive.com/2025/11/10/cbn-mops-up-n11-43trn-via-t-bills-as-91-day-rate-slides-to-15-3/
- allAfrica / MFW4A — CAR 15.2%, liquidity 49.06% (Q1 2025): https://allafrica.com/stories/202504020437.html
- Leadership — NPL 9.85% post-forbearance: https://leadership.ng/banks-non-performing-loans-rise-to-9-85-after-cbns-forbearance-withdrawal/
- Guardian — banking-sector credit ₦111.4 trn: https://guardian.ng/news/banking-sector-credit-to-economy-hits-n111-4-trillion/
- worldgovernmentbonds.com (10yr 14.96% May 2026) / tradingeconomics.com / CEIC — secondary market & series ranges.

---

*End of file. Cells left blank are deliberate (not sourceable this session) — the authoritative gap-fillers are the downloadable CBN Statistical Bulletin / Money & Credit .xlsx tables, CBN Financial Stability Reports (half-yearly), and the IMF FSI database, none of which expose clean values via open web fetch.*
