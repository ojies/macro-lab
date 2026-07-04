# Nigeria — External Sector & Monetary Indicators (2015–2026)

**Dataset:** Big-Debt-Cycle / Nigeria
**Compiled:** 2026-06-29
**Coverage:** Annual (year-end) + quarterly (end-of-quarter) where the underlying series is monthly/quarterly.
**Source priority:** Central Bank of Nigeria (CBN), IMF, World Bank, FMDQ Exchange, BIS.

**Flag legend:** `[SOURCED]` = taken directly from a cited primary/secondary source for the stated period · `[PROVISIONAL]` = sourced but period/precision uncertain, or a projection/estimate vintage · `[ESTIMATED]` = derived/computed (method noted) · blank = not reliably sourceable, left blank rather than guessed.

---

## CRITICAL METHODOLOGY NOTES (read first)

**1. Series breaks in the FX regime.** Nigeria ran a *multiple-exchange-rate* regime for most of 2015–2023, so "the official rate" is ambiguous before mid-2023. Two structural breaks:
- **14 Jun 2023 — FLOAT / unification** (Tinubu reform). I&E window last closed ₦471.67 (13 Jun) → ₦664.04 close on 14 Jun (intraday ~₦755), ~41% one-day depreciation. Window later renamed **NAFEM** (Oct 2023).
- **Jan–Feb 2024 — second devaluation / deeper unification.** Official fell from ~₦900 (Jan) to a weakest close of **₦1,665.50 (23 Feb 2024)** (intraday spike ~₦1,805). Parallel peaked ~₦1,880–1,900. By 9 Mar 2024 the official–parallel gap hit a then-record low (<2%).
- **2 Dec 2024 — EFEMS launch** (Bloomberg BMatch electronic matching); market renamed **NFEM**; rate = volume-weighted average of matched trades.

**2. Official-window naming over time** (the continuous market-determined window — I&E ≈ NAFEX ≈ NAFEM ≈ NFEM — is the relevant series for a debt-cycle dataset):

| Era | Window name | Notes |
|---|---|---|
| 2015 – Jun 2016 | CBN official interbank **peg** | Hard peg ~₦197 |
| Jun 2016 – Apr 2017 | CBN managed float / interbank | Peg abandoned 20 Jun 2016, settled ~₦305 |
| Apr 2017 – Jun 2023 | **I&E (Investors & Exporters) window** / NAFEX (FMDQ fixing) | Ran *alongside* a separate, cheaper pegged CBN "official rate" (~₦306→₦460). **Dual rate.** |
| 14 Jun 2023 → | "Willing-buyer-willing-seller"; renamed **NAFEM** (Oct 2023) | Float / unification |
| 2 Dec 2024 → | **NFEM + EFEMS** | Rate = wtd-avg of matched trades |

**3. Reserves — two competing "gross" definitions for 2023–2024.** The CBN *daily headline* series (30-day moving average) vs CBN *audited financial-statements* basis diverge: end-2023 $33.2bn (headline) vs $36.6bn (accounts); end-2024 $40.2bn (headline) vs $38.8bn (accounts). The **World Bank "total reserves incl. gold"** series (IMF/IFS-derived, end-period) is used as the single internally-consistent annual backbone and runs ~$1.5–2.7bn above the CBN FX-only headline.

**4. REER — BIS does NOT cover Nigeria.** Nigeria is not in the BIS effective-exchange-rate basket. Best citable index with a stated base year is **World Bank WDI `PX.REX.REER`, base 2010 = 100** (underlying source: IMF International Financial Statistics).

---

## 1–2. EXTERNAL RESERVES & IMPORT COVER — ANNUAL (year-end)

| Year-end | Gross FX reserves, CBN headline (USD bn) | Total reserves incl. gold, WB end-Dec (USD bn) | Net external reserves (USD bn) | Import cover (months) | Flag |
|---|---|---|---|---|---|
| 31 Dec 2015 | 28.28 | 29.01 | — | 4.07 (WB) | [SOURCED] |
| 31 Dec 2016 | 26.99 | 28.02 | — | 6.17 (WB) | [SOURCED] |
| 31 Dec 2017 | 38.77 | 40.50 | — | 8.00 (WB) | [SOURCED] |
| 31 Dec 2018 | 43.12 | 42.84 | — | 6.05 (WB) | [SOURCED] |
| 31 Dec 2019 | ~38.6 | 39.38 | — | 4.21 (WB) | [SOURCED] |
| 31 Dec 2020 | ~35.37 | 38.03 | — | 5.80 (WB) | gross headline [PROVISIONAL]; WB & cover [SOURCED] |
| 31 Dec 2021 | 40.23 | 41.73 | ~14.0 (JPM est.) | 6.42 (WB) | gross/WB/cover [SOURCED]; net [PROVISIONAL — JP Morgan estimate] |
| 31 Dec 2022 | 36.61 | 36.81 | ~3.7 (JPM est.) | 4.82 (WB) | gross/WB/cover [SOURCED]; net [PROVISIONAL — JP Morgan estimate] |
| 31 Dec 2023 | 33.22 (headline); 36.6 (CBN accounts) | 33.45 | **3.99** (CBN, disclosed 2025) | 5.12 (WB) | [SOURCED] |
| 31 Dec 2024 | 40.19 (headline); 38.8 (CBN accounts) | 40.41 | **23.11** (CBN) | 7.11 (WB) | [SOURCED] |
| 31 Dec 2025 | 45.71 (headline; ~45.5 close per Proshare) | n/a (WB not released) | **34.80** (CBN) | ~8 (implied) | gross/net [SOURCED]; cover [PROVISIONAL] |
| Latest 2026 | **51.04** (18 Jun 2026); 49.58 (May 2026) | n/a | — (not yet published) | — | gross [SOURCED] |

**Net-reserves narrative (debt-cycle relevant):** JP Morgan (Aug 2023) estimated net FX reserves fell from **~$14.0bn (end-2021) to ~$3.7bn (end-2022)** after adjusting gross for FX forwards (~$6.84bn), securities lending (~$5.5bn) and swaps (~$21.3bn). CBN later officially disclosed net reserves of **$3.99bn (end-2023) → $23.11bn (end-2024) → $34.80bn (end-2025)** — confirming the near-depletion then rapid rebuild.

## 1. GROSS RESERVES — QUARTERLY (end-of-quarter, USD bn)

*Q1–Q3 for 2015–2022 are NOT reliably sourceable from open sources (require the CBN Statistical Bulletin monthly external-reserves .xlsx or CEIC). Left blank rather than guessed. Q4 = year-end values above.*

| Year | Q1 (end-Mar) | Q2 (end-Jun) | Q3 (end-Sep) | Q4 (end-Dec) | Flag |
|---|---|---|---|---|---|
| 2015 | — | — | — | 28.28 | Q4 [SOURCED] |
| 2016 | — | — | — | 26.99 | Q4 [SOURCED] |
| 2017 | — | — | — | 38.77 | Q4 [SOURCED] |
| 2018 | — | — | — | 43.12 | Q4 [SOURCED] |
| 2019 | — | — | — | ~38.6 | Q4 [SOURCED] |
| 2020 | — | — | — | ~35.37 | Q4 [PROVISIONAL] |
| 2021 | — | — | — | 40.23 | Q4 [SOURCED] |
| 2022 | — | — | — | 36.61 | Q4 [SOURCED] |
| 2023 | — | — | 33.28 (18 Sep) | 33.22 | Q3/Q4 [SOURCED] |
| 2024 | — | — | 37.31 (23 Sep) / 39.07 (19 Sep, diff. basis) | 40.19 | Q3/Q4 [SOURCED] |
| 2025 | — | 37.71 (Jun) | 42.03 (19 Sep) | 45.71 | Q2/Q3/Q4 [SOURCED] |
| 2026 | — | 51.04 (18 Jun) | — | — | [SOURCED] |

*Note 2024 Q3: $37.31bn ("22-month high," CBN 23 Sep) and $39.07bn (Gov. Cardoso, 19 Sep) reported within days reflect different reserve concepts the CBN was reconciling.*

---

## 3. EXCHANGE RATE NGN/USD — ANNUAL (year-end ≈ 31 Dec)

Premium = (parallel ÷ official window) − 1, computed `[ESTIMATED]` from the two rates in the row. In the 2017–2019 dual-rate era the parallel ≈ I&E window, so the *meaningful* distortion was vs the cheaper pegged CBN official rate (shown in the "vs CBN peg" note).

| Year-end | Official rate (NGN/USD) | Official window | Parallel rate (NGN/USD) | Premium % (parallel vs official window) | Flag |
|---|---|---|---|---|---|
| 2015 | ~197 (peg) | CBN official interbank peg | ~266–268 | **~35.5%** | official 31-Dec [PROVISIONAL]; parallel [SOURCED]; premium [ESTIMATED] |
| 2016 | ~305 | CBN managed float | ~490–495 | **~61%** | official [PROVISIONAL]; parallel [SOURCED]; premium [ESTIMATED] |
| 2017 | ~360–363 | I&E/NAFEX (separate CBN peg ~₦306) | ~363 | **~1%** vs I&E (**~18%** vs CBN peg ₦306) | [PROVISIONAL]; premium [ESTIMATED] |
| 2018 | ~364 | I&E/NAFEX (peg ~₦306–307) | ~364 | **~0%** vs I&E (**~19%** vs peg) | [PROVISIONAL]; premium [ESTIMATED] |
| 2019 | ~362–364 | I&E/NAFEX (peg ~₦307) | ~362 | **~0%** vs I&E (**~18%** vs peg) | levels [SOURCED], 31-Dec [PROVISIONAL]; premium [ESTIMATED] |
| 2020 | 410.25 (31 Dec) | NAFEX/I&E (peg ~₦379–381) | 470 (30 Dec) | **~14.6%** | [SOURCED]; premium [ESTIMATED] |
| 2021 | 435.00 (31 Dec) | NAFEX/I&E | 570 | **~31.0%** | [SOURCED]; premium [ESTIMATED] |
| 2022 | 461.50 (30 Dec) | I&E | 735–736 (30 Dec) | **~59.3%** | [SOURCED]; premium [ESTIMATED] |
| 2023 | 907.11 (29 Dec) | NAFEM (post-float) | ~1,205–1,215 | **~33.4%** | [SOURCED]; premium [ESTIMATED] |
| 2024 | 1,535.8 (31 Dec) | NFEM/EFEMS | 1,660 | **~8.1%** | [SOURCED]; premium [ESTIMATED] |
| 2025 | 1,429 (31 Dec; IMF cites 1,435) | NFEM/EFEMS | ~1,477 | **~3.4%** | [SOURCED]; premium [ESTIMATED] |
| 2026 (latest) | 1,379.22 (29 Jun 2026) | NFEM | 1,400 (29 Jun) | **~1.5%** | [PROVISIONAL]; premium [ESTIMATED] |

## 3. EXCHANGE RATE — QUARTERLY (end-of-quarter)

**Official window (I&E / NAFEX / NAFEM / NFEM):** *2015–2019 quarter-ends not pinnable to exact dates — pegged rate ~flat at annual levels; FMDQ daily archive required, left blank.*

| Quarter | Date | Official (NGN/USD) | Window | Flag |
|---|---|---|---|---|
| Q1 2020 | 31 Mar 2020 | ~385 (post 20-Mar deval.) | NAFEX | [PROVISIONAL] |
| Q2 2020 | 30 Jun 2020 | ~386 | NAFEX | [PROVISIONAL] |
| Q3 2020 | 30 Sep 2020 | ~386 | NAFEX | [PROVISIONAL] |
| Q4 2020 | 31 Dec 2020 | 410.25 | NAFEX | [SOURCED] |
| Q1 2021 | 31 Mar 2021 | 408.67 | NAFEX | [SOURCED] |
| Q2 2021 | 30 Jun 2021 | ~411 | NAFEX | [PROVISIONAL] |
| Q3 2021 | 30 Sep 2021 | ~411.67 | NAFEX | [PROVISIONAL] |
| Q4 2021 | 31 Dec 2021 | 435.00 | NAFEX | [SOURCED] |
| Q1 2022 | 31 Mar 2022 | 417 | I&E | [SOURCED] |
| Q2 2022 | 30 Jun 2022 | 425.05 | I&E | [SOURCED] |
| Q3 2022 | 30 Sep 2022 | 437.03 | I&E | [SOURCED] |
| Q4 2022 | 30 Dec 2022 | 461.50 | I&E | [SOURCED] |
| Q1 2023 | 31 Mar 2023 | ~461.5 | I&E | [PROVISIONAL] |
| **Q2 2023** | 30 Jun 2023 | **769.25** (float 14 Jun) | I&E (post-float) | [SOURCED] — series break |
| Q3 2023 | 29–30 Sep 2023 | 755.27 | NAFEM | [SOURCED] |
| Q4 2023 | 29 Dec 2023 | 907.11 | NAFEM | [SOURCED] |
| Q1 2024 | 28 Mar 2024 | 1,309.39 | NAFEM | [SOURCED] |
| Q2 2024 | 30 Jun 2024 | 1,505.30 | NAFEM | [SOURCED] |
| Q3 2024 | 30 Sep 2024 | ~1,541 | NAFEM | [SOURCED] |
| Q4 2024 | 31 Dec 2024 | 1,535.8 | NFEM/EFEMS | [SOURCED] |
| Q1 2025 | 31 Mar 2025 | 1,536.82 | NFEM | [SOURCED] |
| Q2 2025 | 30 Jun 2025 | ~1,532 | NFEM | [SOURCED] |
| Q3 2025 | 30 Sep 2025 | 1,480.15 | NFEM | [SOURCED] |
| Q4 2025 | 31 Dec 2025 | 1,429 | NFEM/EFEMS | [SOURCED] |
| Q1 2026 | 31 Mar 2026 | ~1,383–1,386 (intraday) | NFEM | [PROVISIONAL] |
| Q2 2026 | 29 Jun 2026 | 1,379.22 (30-Jun close unpublished) | NFEM | [PROVISIONAL] |

**Parallel / black-market quarter-ends (only where reliably date-pinnable):** *2015–2022 and some 2024 cells not pinnable (AbokiFX historical CSV no longer freely retrievable) — left blank.*

| Quarter | Date | Parallel (NGN/USD) | Flag |
|---|---|---|---|
| Q3 2023 | ~end-Sep 2023 | ~1,000 (milestone) | [PROVISIONAL] |
| Q4 2023 | 31 Dec 2023 | ~1,210 | [SOURCED] |
| *(peak)* | ~Feb 2024 | ~1,880–1,900 (record low) | [PROVISIONAL] |
| Q1 2024 | end-Mar 2024 | ~1,250 | [SOURCED] |
| Q3 2024 | 30 Sep 2024 | 1,700 | [SOURCED] |
| Q4 2024 | 31 Dec 2024 | 1,660 | [SOURCED] |
| Q1 2025 | ~28 Mar 2025 | ~1,560 | [SOURCED] |
| Q3 2025 | ~end-Sep 2025 | ~1,495–1,515 | [SOURCED] |
| Q4 2025 | Dec 2025 | ~1,477 | [SOURCED] |
| Q2 2026 | 28–29 Jun 2026 | 1,400 | [SOURCED] |

---

## 4. REER — Real Effective Exchange Rate index (annual)

**Base: 2010 = 100. Source: World Bank WDI `PX.REX.REER` (underlying IMF IFS). Higher = real appreciation/overvaluation.**

| Year | REER (2010=100) | Flag | Note |
|---|---|---|---|
| 2015 | 119.86 | [SOURCED] | |
| 2016 | 110.86 | [SOURCED] | |
| 2017 | 101.45 | [SOURCED] | |
| 2018 | 109.90 | [SOURCED] | |
| 2019 | 124.18 | [SOURCED] | |
| 2020 | 119.52 | [SOURCED] | |
| 2021 | 117.05 | [SOURCED] | |
| 2022 | 133.33 | [SOURCED] | **peak real overvaluation** (pre-float, tightly managed naira) |
| 2023 | 115.58 | [SOURCED] | June 2023 float begins; partial real depreciation |
| 2024 | 63.93 | [SOURCED] | **sharp real depreciation (~45% below 2022)** after full float |
| 2025 | — | | WDI series ends 2024; not yet published |
| 2026 | — | | Not available |

**Qualitative IMF model-based REER assessments:** end-2022 naira assessed overvalued (basis for reform) `[SOURCED]`; end-2023 overvalued ~6% `[SOURCED]`; 2025 naira ~25.6% *undervalued*, model fair value ~₦1,142/$ (IMF CR 25/157) `[SOURCED]`.

---

## 5. CURRENT ACCOUNT BALANCE (annual)

**Source: IMF WEO (Apr-2026 vintage) `BCA`/`BCA_NGDPD`, cross-checked vs World Bank WDI & CBN BoP. WEO USD and WB USD are identical (WB ingests IMF).**

| Year | CA (USD bn) | CA (% of GDP, IMF WEO) | Flag | Note |
|---|---|---|---|---|
| 2015 | −15.44 | −2.2% | [SOURCED] | deficit |
| 2016 | +5.08 | +0.9% | [SOURCED] | |
| 2017 | +13.56 | +2.6% | [SOURCED] | |
| 2018 | +7.28 | +1.2% | [SOURCED] | |
| 2019 | −13.69 | −2.0% | [SOURCED] | deficit |
| 2020 | −15.99 | −2.7% | [SOURCED] | COVID-year deficit |
| 2021 | −3.25 | −0.5% | [SOURCED] | deficit |
| 2022 | +1.02 | +0.2% | [SOURCED] | near balance |
| 2023 | +6.42 | +1.3% | [SOURCED] | |
| 2024 | +17.22 | **+6.8%** | [SOURCED] | large surplus; CBN BoP confirms current+capital surplus $17.22bn. *IMF Article IV narrative cites ~9% of GDP (different GDP denominator/vintage).* |
| 2025 | +14.88 | +5.1% | [PROVISIONAL] | IMF WEO Apr-2026 estimate (AfDB projects ~4.7%) |
| 2026 | +21.93 | +5.8% | [PROVISIONAL] | IMF WEO Apr-2026 projection (AfDB projects ~3.9%) |

**Note on 2024 % of GDP:** IMF WEO +6.8% / WB WDI +6.82% (essentially identical) vs IMF 2025 Article IV staff-report narrative ~9% — not an error, a denominator/vintage difference. Headline uses IMF WEO +6.8% per brief.

---

## 6. MONETARY POLICY RATE (MPR) — every MPC decision/change

**Primary source: CBN "Monetary Policy Decisions" register. All [SOURCED].**

| Meeting date | MPC # | Decision | MPR after | Δ |
|---|---|---|---|---|
| 23–24 Nov 2015 | — | cut from 13.0 | **11.00%** | −200bp |
| 21–22 Mar 2016 | — | hike | **12.00%** | +100bp |
| 25–26 Jul 2016 | — | hike | **14.00%** | +200bp |
| (held through 2017–2018) | — | retain | 14.00% | — |
| 25–26 Mar 2019 | — | cut | **13.50%** | −50bp |
| 28 May 2020 | — | cut | **12.50%** | −100bp |
| 21–22 Sep 2020 | — | cut | **11.50%** | −100bp |
| (held through 2021–Mar 2022) | — | retain | 11.50% | — |
| 23–24 May 2022 | 284th | hike | **13.00%** | +150bp |
| 18–19 Jul 2022 | 286th | hike | **14.00%** | +100bp |
| 26–27 Sep 2022 | 287th | hike | **15.50%** | +150bp |
| 21–22 Nov 2022 | 288th | hike | **16.50%** | +100bp |
| 21–22 Jan 2023 | 289th | hike | **17.50%** | +100bp |
| 20–21 Mar 2023 | 290th | hike | **18.00%** | +50bp |
| 23–24 May 2023 | 291st | hike | **18.50%** | +50bp |
| 24–25 Jul 2023 | 292nd | hike | **18.75%** | +25bp |
| (held — leadership transition to Gov. Cardoso) | — | — | 18.75% | — |
| 26–27 Feb 2024 | 293rd | hike | **22.75%** | +400bp |
| 25–26 Mar 2024 | 294th | hike | **24.75%** | +200bp |
| 20–21 May 2024 | 295th | hike | **26.25%** | +150bp |
| 22–23 Jul 2024 | 296th | hike | **26.75%** | +50bp |
| 23–24 Sep 2024 | 297th | hike | **27.25%** | +50bp |
| 25–26 Nov 2024 | 298th | hike | **27.50%** | +25bp |
| 19–20 Feb 2025 | 299th | retain | 27.50% | — |
| 19–20 May 2025 | 300th | retain | 27.50% | — |
| 21–22 Jul 2025 | 301st | retain | 27.50% | — |
| 22–23 Sep 2025 | 302nd | cut | **27.00%** | −50bp |
| 24–25 Nov 2025 | 303rd | retain | 27.00% | — |
| 23–24 Feb 2026 | 304th | cut | **26.50%** | −50bp |
| 19–20 May 2026 | 305th | retain | 26.50% | — |

### MPR — quarter-end (rate prevailing on last day of quarter), all [SOURCED]

| Year | Q1 (Mar 31) | Q2 (Jun 30) | Q3 (Sep 30) | Q4 (Dec 31) |
|---|---|---|---|---|
| 2015 | 13.00% | 13.00% | 13.00% | 11.00% |
| 2016 | 12.00% | 12.00% | 14.00% | 14.00% |
| 2017 | 14.00% | 14.00% | 14.00% | 14.00% |
| 2018 | 14.00% | 14.00% | 14.00% | 14.00% |
| 2019 | 13.50% | 13.50% | 13.50% | 13.50% |
| 2020 | 13.50% | 12.50% | 11.50% | 11.50% |
| 2021 | 11.50% | 11.50% | 11.50% | 11.50% |
| 2022 | 11.50% | 13.00% | 15.50% | 16.50% |
| 2023 | 18.00% | 18.50% | 18.75% | 18.75% |
| 2024 | 24.75% | 26.25% | 27.25% | 27.50% |
| 2025 | 27.50% | 27.50% | 27.00% | 27.00% |
| 2026 | 26.50% | 26.50% | *(future)* | *(future)* |

---

## SOURCES

### Reserves & import cover
- World Bank Open Data — Total reserves incl. gold (`FI.RES.TOTL.CD`) & months of imports (`FI.RES.TOTL.MO`), Nigeria: https://data.worldbank.org/indicator/FI.RES.TOTL.CD?locations=NG · https://data.worldbank.org/indicator/FI.RES.TOTL.MO?locations=NG
- CBN — Movement in Foreign Reserves (daily headline): https://www.cbn.gov.ng/intops/reserve.html
- CBN — 2022 Annual Economic Report (import cover): https://www.cbn.gov.ng/Out/2024/RSD/2022%20ANNUAL%20REPORT.pdf
- CBN — 2021 Annual Economic Report: https://www.cbn.gov.ng/Out/2023/RSD/2021%20CBN%20ANNUAL%20ECONOMIC%20REPORT.a.pdf
- IMF — 2024 Post-Financing Assessment with Nigeria: https://www.imf.org/en/News/Articles/2024/02/09/pr2443-nigeria-imf-exec-board-concludes-pfa
- Vanguard — JP Morgan: net FX reserves $3.7bn end-2022 (Aug 2023): https://www.vanguardngr.com/2023/08/nigerias-net-foreign-reserves-fell-to-3-7bn-at-end-of-2022-jp-morgan/
- TheCable — JP Morgan net FX reserves $3.7bn: https://www.thecable.ng/nigerias-net-fx-reserves-likely-fell-to-3-7bn-at-end-of-2022-says-jp-morgan/
- Nairametrics — net reserves $34.80bn by Dec 2025 (net: 2023 $3.99bn, 2024 $23.11bn, 2025 $34.80bn): https://nairametrics.com/2026/03/02/nigerias-net-reserves-surge-to-34-80-billion-by-december-2025-cbn/
- Daily Post — external reserves grew 5.6% to $38.8bn in 2024, CBN accounts basis: https://dailypost.ng/2025/05/03/nigerias-external-reserves-grew-by-5-6-to-38-8bn-in-2024-cbn/
- Proshare — gross reserves close 2025 at ~$45.5bn: https://www.proshare.co/articles/nigerias-gross-external-reserves-rose-by-us834.2m-mom-closes-2025-at-45.5bn
- Nairametrics — reserves $39.07bn, Cardoso (Sep 2024): https://nairametrics.com/2024/09/24/nigerias-external-reserves-hit-39-07-billion-cardoso/
- Channels TV — reserves $37.31bn 22-month high (23 Sep 2024): https://www.channelstv.com/2024/09/23/external-reserves-hit-22-month-high-to-37-31bn-cbn/
- Businessday — reserves $33.28bn (18 Sep 2023): https://businessday.ng/news/article/nigerias-external-reserve-dropped-to-33bn-in-september-2023/
- Nairametrics — reserves $42.03bn 6-year high (Sep 2025): https://nairametrics.com/2025/09/29/why-nigerias-external-reserves-is-at-a-6-year-high/
- Businessday — reserves $51.04bn (18 Jun 2026): https://businessday.ng/news/article/external-reserves-hit-cbns-51-04bn-target-as-naira-posts-weekly-loss/
- TradingEconomics — Nigeria FX reserves: https://tradingeconomics.com/nigeria/foreign-exchange-reserves
- Brandspur — gross reserves 2015–2019 series: https://brandspurng.com/2020/08/11/nigerias-gross-external-reserves-an-historical-perspective/
- CEIC (full monthly history, paywalled): https://www.ceicdata.com/en/indicator/nigeria/foreign-exchange-reserves

### Exchange rate (primary fixings — query directly for audit-grade dates)
- CBN exchange-rate portal: https://www.cbn.gov.ng/rates/ExchRateByCurrency.html · monthly avg: https://www.cbn.gov.ng/rates/exrate.html
- CBN — EFEMS FAQ: https://www.cbn.gov.ng/Out/2024/FMD/FREQUENTLY%20ASKED%20QUESTIONS%20(FAQS)%20ON%20THE%20ELECTRONIC%20FOREIGN%20EXCHANGE%20MATCHING%20SYSTEM%20(EFEMS)%20.pdf
- FMDQ Exchange (NAFEX/NAFEM fixings): https://fmdqgroup.com/exchange/ · NAFEM methodology: https://fmdqgroup.com/exchange/wp-content/uploads/2023/10/FMDQ-Exchange-NAFEM-Spot-Rates-Methodology-October-2023.pdf
- World Bank — official rate period avg (`PA.NUS.FCRF`): https://api.worldbank.org/v2/country/NGA/indicator/PA.NUS.FCRF?date=2015:2019&format=json
- Nairametrics — end-2020 ₦410.25: https://nairametrics.com/2020/12/31/updated-naira-devalues-to-n410-25-1-at-the-official-nafex-window-as-of-dec-31-2020/
- Nairametrics — end-2021 ₦435: https://nairametrics.com/2021/12/31/official-nafex-exchange-rate-closes-at-n435-1-in-2021/
- Nairametrics — Q2 2022 ₦425.05: https://nairametrics.com/2022/07/01/naira-falls-to-n420-1-at-ie-window-despite-moderations-at-parallel-market/
- Peoples Gazette — Q3 2022 ₦437.03: https://gazettengr.com/ie-window-naira-constant-exchanges-at-437-03-to-dollar/
- Nairametrics — end-2022 ₦461.5 / parallel ₦735: https://nairametrics.com/2023/01/01/nigerias-exchange-rate-depreciates-23-to-close-2022-at-n735-1-at-black-market/
- Vanguard — float 14 Jun 2023 ₦664.04: https://www.vanguardngr.com/2023/06/naira-depreciates-to-n664-04-as-cbn-lifts-restrictions/
- Nairametrics — Q2 2023 ₦769.25: https://nairametrics.com/2023/06/30/ie-window-exchange-rate-closes-at-n769-25-1-depreciates-39-in-one-month-june-2023/
- Nairametrics — end-2023 NAFEM ₦907.11: https://nairametrics.com/2023/12/29/nafem-exchange-rate-ends-2023-at-n907-11-26-8-depreciation-since-unification/
- Nairametrics — Feb 2024 peak ₦1,665.50: https://nairametrics.com/2024/02/24/official-exchange-rate-closes-week-at-n1665-50-1-amidst-demand-pressure-and-forex-decline/
- Business Post — Q1 2024 ₦1,309.39: https://businesspost.ng/economy/naira-falls-to-n1309-1-as-official-market-amid-107-surge-in-fx-sales/
- Businessday — Q2 2024 ₦1,505.30 / 2024 review: https://businessday.ng/news/article/naira-ends-2024-with-40-9-loss-amid-external-reserves-growth/
- Nairametrics — end-2024 ₦1,535: https://nairametrics.com/2024/12/31/exchange-rate-ends-2024-at-n1535-1-marking-a-40-9-depreciation/
- Nairametrics — Sep 2024 parallel ₦1,700: https://nairametrics.com/2024/10/01/naira-ends-september-at-lowest-exchange-rate-in-seven-months-at-parallel-market/
- Channels TV — Q1 2025 ₦1,536.82: https://www.channelstv.com/2025/04/07/naira-weakens-by-3-q1-2025/
- Vanguard — Q3 2025 ₦1,480.15: https://www.vanguardngr.com/2025/09/dollar-to-naira-exchange-rate-today-september-30-2025/
- Nairametrics — end-2025 ₦1,429 (first annual gain in 13 yrs): http://nairametrics.com/2026/01/01/naira-ends-2025-at-n1429-first-annual-gain-in-13-years/
- Vanguard — Dec 2025 parallel ₦1,477: https://www.vanguardngr.com/2025/12/naira-appreciates-to-n1477-in-parallel-market/
- Channels TV — 29 Jun 2026 ₦1,379.22: https://www.channelstv.com/2026/06/29/naira-to-dollar-exchange-rate-today-june-29-2026/
- Leadership — Cardoso: parallel premium <2% in 2025: https://leadership.ng/parallel-market-premium-shrinks-by-48-in-3-years-cardoso/
- AbokiFX year-end parallel series (via StatiSense): https://x.com/StatiSense/status/1571244664501538816

### REER
- World Bank WDI — REER index 2010=100 (`PX.REX.REER`), Nigeria: https://data.worldbank.org/indicator/PX.REX.REER?locations=NG
- Bruegel/Darvas REER database (alt source): https://www.bruegel.org/publications/datasets/real-effective-exchange-rates-for-178-countries-a-new-database
- BIS Effective Exchange Rates (confirms Nigeria NOT covered): https://www.bis.org/statistics/eer.htm
- IMF — 2024 Article IV (REER overvaluation assessment): https://www.elibrary.imf.org/view/journals/002/2024/102/article-A001-en.xml
- IMF — naira ~25% undervalued (2025): https://www.thecable.ng/imf-says-naira-is-25-undervalued-despite-fx-reforms/

### Current account
- IMF DataMapper — Nigeria (`BCA`, `BCA_NGDPD`), WEO Apr-2026: https://www.imf.org/external/datamapper/profile/NGA
- IMF — Country Report 25/157, Nigeria 2025 Article IV: https://www.imf.org/en/publications/cr/issues/2025/07/01/nigeria-2025-article-iv-consultation-press-release-staff-report-and-statement-by-the-568220
- IMF — 2026 Article IV press release (PR26/190): https://www.imf.org/en/news/articles/2026/06/09/pr26190-nigeria-imf-executive-board-concludes-2026-article-iv-consultation-with-nigeria
- World Bank WDI — CA % GDP (`BN.CAB.XOKA.GD.ZS`): https://data.worldbank.org/indicator/BN.CAB.XOKA.GD.ZS?locations=NG
- CBN — 2024 Annual Balance of Payments Highlights (current+capital surplus $17.22bn; overall BoP $6.83bn): https://www.cbn.gov.ng/Out/2025/CCD/2024%20Annual%20Balance%20of%20Payments%20Highlights_08_04_2025_FINAL.pdf
- AfDB — Nigeria Economic Outlook: https://www.afdb.org/en/countries-west-africa-nigeria/nigeria-economic-outlook

### Monetary Policy Rate
- CBN — Monetary Policy Decisions register (all MPR figures): https://www.cbn.gov.ng/MonetaryPolicy/decisions.html
- CBN — MPC Communiqué No. 155 (26 Nov 2024, 27.50%): https://www.cbn.gov.ng/Out/2024/CCD/FINAL%20MPC%20Communique%20No.%20155%20November%2026%202024%2015.08pm.pdf
- CBN — MPC Communiqué No. 156 (20 Feb 2025, retain 27.50%): https://www.cbn.gov.ng/Out/2025/CCD/Central_Bank_of_Nigeria_Comminique_No.156_20_February_2025.pdf
- CBN — MPC Communiqué No. 160 (25 Nov 2025, retain 27.00%): https://www.cbn.gov.ng/Out/2025/CCD/MPC%20Communique%20No.%20160%20%20November%2025%202025.pdf
- Vanguard — May 2026 retain 26.5%: https://www.vanguardngr.com/2026/05/breaking-cbn-retains-monetary-policy-rate-at-26-5/
- TradingEconomics — Nigeria interest rate (cross-check): https://tradingeconomics.com/nigeria/interest-rate

---

## KNOWN GAPS / CAVEATS

1. **Reserves Q1–Q3 2015–2022** not reliably sourceable from open web — require CBN Statistical Bulletin monthly external-reserves .xlsx or CEIC.
2. **Two gross-reserve definitions 2023–2024** (daily headline vs audited accounts) diverge ~$1–4bn; pick one basis consistently. World Bank total-reserves recommended as the consistent annual backbone.
3. **2020 year-end CBN headline (~$35.37bn)** is [PROVISIONAL]; the sourced figure is World Bank $38.03bn (incl. gold).
4. **FX 2015–2019 quarter-ends** (official I&E and parallel) not pinnable to exact dates; pegged rate ~flat so annual levels stand in. 2017–2019 I&E year-ends rest on AbokiFX/StatiSense (parallel≈I&E then), hence [PROVISIONAL].
5. **Premium %** is [ESTIMATED] from the two rates in each row; in the dual-rate era (2017–2019) the parallel ≈ I&E so the real distortion was vs the cheaper CBN peg (noted).
6. **REER 2025–2026 blank** — WDI/IFS series ends 2024.
7. **Current account 2025–2026** are IMF WEO projections [PROVISIONAL], not outturns.
8. **2026 FX & reserves** are [PROVISIONAL] / latest-available (30 Jun 2026 quarter close not yet published; latest confirmed FX ₦1,379.22 on 29 Jun 2026; reserves $51.04bn on 18 Jun 2026).
