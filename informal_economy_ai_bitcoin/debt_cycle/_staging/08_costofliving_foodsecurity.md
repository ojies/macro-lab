# Nigeria — Cost of Living & Food Security (2015–2026)

**Dataset:** Big-Debt-Cycle / Nigeria
**Compiled:** 2026-06-29
**Coverage:** Annual 2015–2026, plus recent monthly anchors (2022–2026) where the underlying NBS series is monthly.
**Source priority:** NBS (CPI / Selected Food Prices Watch / PMS, Diesel & Cooking-Gas Price Watch), NMDPRA/NNPC, NERC (electricity tariffs), Cadre Harmonisé / FEWS NET / FAO-WFP-OCHA / IPC.

**Flag legend:** `[SOURCED]` = taken directly from a cited primary/secondary source for the stated period · `[PROVISIONAL]` = sourced but period/precision uncertain, partial-year, or a single illustrative figure rather than a true average · `[ESTIMATED]` = derived/computed (method noted) · blank / "not sourceable" = left blank rather than guessed.

---

## CRITICAL METHODOLOGY NOTES (read first)

**1. NBS publishes MONTHLY price watches, not annual averages.** For petrol (PMS), diesel (AGO), cooking gas (LPG) and the Selected Food Prices, NBS releases a national-average figure each month. Every **annual average** in this file is *my computation* (mean of available NBS monthly anchors) and is flagged `[ESTIMATED]` — it is **not** an official NBS annual release. Individual monthly figures are `[SOURCED]`.

**2. Two structural breaks in petrol, not one.** (a) **June 2023 subsidy removal** — Tinubu "subsidy is gone" (29 May 2023); NBS national PMS jumped ~₦264 (Feb 2023) → **₦545.83 (Jun 2023)** → ~₦620–630 (H2 2023). (b) **Sep 2024 second hike** — PMS crossed ₦1,000 for the first time (**₦1,030.46, Sep 2024**), peaked ~₦1,262 (Mar 2025), eased to ~₦1,025 (Dangote-refinery effect, mid-2025), then **surged again in 2026 to ₦1,596.25 (May 2026)**.

**3. The Naira float masks the real price story (see §5 USD-equivalent).** In USD terms petrol was ~$0.40–0.47/litre across 2015–early-2023 because each nominal hike was matched by devaluation. Post-float the USD price rose to ~$0.70+ and by May 2026 ~$1.07/litre — i.e. the post-2023 increases are a *real* price rise (subsidy withdrawal), not merely devaluation.

**4. January-2025 CPI rebasing break.** NBS rebased the CPI in Jan 2025 (new base year 2024, weights 2023). Food inflation appears to drop from ~40% (2024, old base) to ~26% (early 2025, new base) — this is **methodological, not real disinflation** (prices kept rising). Old-base (≤Dec 2024) and new-base (≥Jan 2025) are kept as separate series below.

**5. Food prices are NBS national-average PER KG (loose), not branded bags.** A "50kg bag of rice" is shown as the per-kg figure ×50; this implied bag runs broadly consistent with (slightly above) reported market wholesale bags (₦80k–112k in 2025–26). NBS food price-watch series only began **June 2016** — there is **no NBS per-kg figure for 2015** (2015 = anecdotal only).

**6. There is no single official national "average electricity tariff."** Tariffs vary by DisCo (11), customer class, and — since Nov 2020 — service band (A–E). The annual average column is indicative; the load-bearing, well-sourced event is the **April 2024 Band-A hike (₦66 → ₦225/kWh)**.

**7. Cadre Harmonisé runs twice yearly.** The **October** analysis of year X gives a "current" (Oct–Dec X) figure and a "projected" figure for the **June–August lean season of X+1**; the **March** analysis of X+1 revises that same lean-season projection. Most lean seasons therefore have two projections. Geographic scope expanded over time: 16 states+FCT (2019–21) → 20 (Oct 2021) → 26 (Nov 2022–2024) → 27 (Oct 2025).

---

## 1. PETROL (PMS) — pump price NGN/litre

### 1a. Annual averages

| Year | PMS NGN/litre (annual avg) | Basis | Flag |
|---|---|---|---|
| 2015 | ~87 | Govt-regulated cap; cut ₦97→₦87, Jan 2015 | [SOURCED] (cap = price) |
| 2016 | ~120 | Cap ₦86.5 Jan–early May, then ₦87→₦145 on 11 May 2016 | [ESTIMATED] (mid-year cap change) |
| 2017 | ~145 | Regulated cap ₦145 | [SOURCED] (cap) |
| 2018 | ~145 | Regulated cap ₦145 | [SOURCED] (cap) |
| 2019 | ~145 | Regulated cap ₦145 (NBS Jan 2019 ≈ ₦145.7) | [SOURCED] (cap) |
| 2020 | ~148–150 | Deregulated Mar 2020; range ₦123.50 (Jun) – ₦162.44 (Dec) | [ESTIMATED] (range midpoint) |
| 2021 | ~165 | NBS monthly ₦164.09 (Jan) – ₦165.77 (Dec) | [ESTIMATED] (mean of NBS months) |
| 2022 | ~190 | NBS ₦166.40 (Jan) → ₦191.65 (Sep) → ~₦206 (Dec) | [ESTIMATED] (mean of NBS anchors) |
| 2023 | ~480–510 | ~₦264 Jan–May → ₦545.83 (Jun) → ~₦620–630 (H2) | [ESTIMATED] (subsidy split-year) |
| 2024 | ~860–870 | NBS ₦668.30 (Jan) → ₦1,189.12 (Dec) | [ESTIMATED] (mean of 12 NBS months) |
| 2025 | ~1,090–1,110 | ~₦1,262 (Q1) → ~₦1,025–1,060 (H2) | [ESTIMATED] (mean of NBS months) |
| 2026 (Jan–May, partial) | ~1,350, rising to ₦1,596 by May | NBS Apr ₦1,532.93 / May ₦1,596.25 | [PROVISIONAL] (partial year) |

### 1b. Monthly NBS anchors (the load-bearing subsidy-removal series)

| Period | PMS NGN/litre | Note | Flag |
|---|---|---|---|
| Jan 2021 | 164.09 | | [SOURCED] |
| Jan 2022 | 166.40 | | [SOURCED] |
| Sep 2022 | 191.65 | | [SOURCED] |
| Dec 2022 | ~206 | | [SOURCED] |
| **Feb 2023 (pre-removal)** | **263.76** | already scarcity-inflated above ~₦185–195 cap | [SOURCED] |
| **Jun 2023 (post-removal)** | **545.83** | +210% YoY; Naira floated 14 Jun 2023 | [SOURCED] |
| Aug 2023 | 626.70 | | [SOURCED] |
| Oct 2023 | 630.63 | | [SOURCED] |
| Jan 2024 | 668.30 | | [SOURCED] |
| Aug 2024 | 830.46 | | [SOURCED] |
| **Sep 2024 (crosses ₦1,000)** | **1,030.46** | first time ever | [SOURCED] |
| Oct 2024 | 1,184.83 | | [SOURCED] |
| Dec 2024 | 1,189.12 | | [SOURCED] |
| Mar 2025 | 1,261.65 | period peak | [SOURCED] |
| **May 2025 (Dangote drop)** | **1,027.76** | | [SOURCED] |
| Jul 2025 | 1,024.99 | | [SOURCED] |
| Dec 2025 | 1,048.63 | | [SOURCED] |
| Apr 2026 | 1,532.93 | | [SOURCED] |
| **May 2026** | **1,596.25** | +55.31% YoY | [SOURCED] |

---

## 2. DIESEL (AGO) & COOKING GAS (LPG)

### 2a. Diesel (AGO / Automotive Gas Oil) — NGN/litre

| Year | AGO NGN/litre (annual avg) | Basis | Flag |
|---|---|---|---|
| 2021 | ~250–270 | only Oct 2021 (₦254.07) firmly anchored | [ESTIMATED] (sparse — low confidence) |
| 2022 | ~650–700 | **spike**: ₦288 (Jan) → ₦671 (May) → ₦800–818 (Q4) | [ESTIMATED] |
| 2023 | ~850–900 | ₦828.82 (Jan) → mid-year dip → ₦1,126.69 (Dec) | [ESTIMATED] |
| 2024 | ~1,250–1,350 | ₦1,153.01 (Jan) → ₦1,403.96 (May), eased H2 | [ESTIMATED] |
| 2025 | ~1,500–1,600 | ₦1,758.26 (May) → ₦1,409.61 (Nov) — volatile | [ESTIMATED] (low-moderate confidence) |
| 2026 (partial) | rising sharply | ₦2,474.69 (Apr) → **₦3,277.47 (May, +86.40% YoY)** | [PROVISIONAL] (partial; surge) |

Diesel monthly anchors: ₦254.07 (Oct 2021); ₦671.08 (May 2022); ₦817.86 (Dec 2022); ₦844.28 (May 2023); ₦1,126.69 (Dec 2023); ₦1,403.96 (May 2024); ₦1,758.26 (May 2025); ₦1,409.61 (Nov 2025); **₦3,277.47 (May 2026)**. All [SOURCED]. Diesel is fully deregulated (no subsidy) — it tracks crude/FX directly, hence the 2022 and 2026 spikes.

### 2b. Cooking gas (LPG) — 12.5kg & 5kg refill, NGN

| Year | 12.5kg refill (annual avg) | 5kg anchor | Flag |
|---|---|---|---|
| 2021 | ~5,000–5,500 | — | [ESTIMATED] (₦4,514.82 Aug → ₦7,332.04 Dec) |
| 2022 | ~8,800–9,500 | — | [ESTIMATED] (₦7,413.25 Jan → ₦9,899.34 Aug) |
| 2023 | ~9,000–10,000 | ₦4,115.32 (Aug) | [ESTIMATED] (₦9,194.41 Aug; retail ~₦11,000) |
| 2024 | ~14,500–15,800 | ₦6,430.02 (Aug) | [ESTIMATED] (₦14,261.57 Jul → ₦15,552 Aug) |
| 2025 | ~18,000–19,000 | ₦8,323.95 (Jun, peak) | [ESTIMATED] (peak ~₦21,010 Jun, then collapse H2) |

LPG monthly anchors (12.5kg): ₦4,514.82 (Aug 2021); ₦7,413.25 (Jan 2022); ₦9,899.34 (Aug 2022); ₦9,194.41 (Aug 2023); ₦14,261.57 (Jul 2024); ₦15,552 (Aug 2024); ₦20,268.06 (Apr 2025); **₦21,010.56 (Jun 2025, peak)**; ₦20,609.48 (Jul 2025). All [SOURCED]. **Notable:** LPG collapsed in H2 2025 (5kg ₦8,323.95 Jun → ₦5,360.43 Dec, −36%; −25.31% YoY), rebounding to 5kg ₦7,655 by Mar 2026.

---

## 3. ELECTRICITY TARIFFS — NGN/kWh

> Caveat: no single official national average exists (varies by DisCo/class/band). Annual column is indicative; the Band-A 2024 event (Table 3b) is the robust series.

### 3a. Indicative average end-user tariff

| Year | Avg tariff NGN/kWh | Note | Flag |
|---|---|---|---|
| 2015 | ~23.5 (range ₦16–31) | pre-MYTO-2015 baseline | [SOURCED] |
| 2016 | ~24–31 | MYTO 2015 order, eff. 1 Feb 2016 (~45% rise; R2 ₦14→₦23.6) | [PROVISIONAL] (examples, not nat'l avg) |
| 2017 | — | tariffs largely frozen post-2016 | not reliably sourceable |
| 2018 | — | | not reliably sourceable |
| 2019 | — | | not reliably sourceable |
| 2020 | ~30–55 | Service-Based Tariff (SBT) from 1 Nov 2020; charged ~₦31 vs cost ~₦53 | [ESTIMATED] (illustrative) |
| 2021 | — | Jan 2021 FX/inflation adjustment (+₦2–4/kWh by band) | [PROVISIONAL] |
| 2022 | Band C ~₦100 | MYTO 2022 (FX ₦441/$) | [PROVISIONAL] |
| 2023 | ~63 (range ₦55–71) | as of Jan 2023 | [SOURCED] |
| 2024 | allowed avg **₦100.27**; cost-reflective **₦175.31** (gap ₦75.04 = subsidy) | NERC 2024 annual report | [SOURCED] |
| 2025 | allowed avg ≈ ₦100–116 (no clean nat'l avg) | Band A ~₦209; Enugu (EERC) cut to ₦160 from 1 Aug 2025 | [PROVISIONAL] |
| 2026 | no new general order yet (~₦209 Band A prevailing) | NERC reviewing all bands (mid-2026) | [PROVISIONAL] |

### 3b. Band-A 2024 hike — the core event (before/after)

| Date | Band A NGN/kWh | Change | Flag |
|---|---|---|---|
| to 2 Apr 2024 (pre-hike) | **66** (some cite ₦66–68) | baseline | [SOURCED] |
| **3 Apr 2024 (hike)** | **225** | +~240% | [SOURCED] |
| 6 May 2024 (cut) | **206.8** | −8.1% (Naira appreciation; FX input cut 16.03%) | [SOURCED] |
| Jul 2024 | **209.5** | small FX uptick | [SOURCED] |
| 2025–2026 | ~**209** prevailing (some DisCos quoted to ~₦230) | broadly stable | [PROVISIONAL] |
| 1 Aug 2025 (Enugu/EERC only) | **160** (from ₦209) | −23.4%, first sub-national regulator divergence | [SOURCED] |

**Bands B–E:** NOT raised in April 2024; remain frozen near pre-2024 ~₦60–66/kWh and all subsidised. Band A (feeders with 20+ hrs/day; ~15% of customers, ~40% of consumption) is the only roughly cost-reflective band. **Electricity subsidy 2024 = ₦1.94 trillion** (NERC; avg ₦75.04/kWh gap), up ~220% YoY despite the hike; ~₦1.98tn over the 12 months to Q3 2025 (BusinessDay). All [SOURCED].

---

## 4. STAPLE FOOD PRICES — NBS national average, nominal NGN

> NBS reports per kg / per loaf / per litre. "50kg bag rice" = per-kg ×50 [ESTIMATED]. No NBS data for 2015 (series began Jun 2016).

### 4a. Rice (local, loose) — per kg & implied 50kg bag

| Period | ₦/kg | Implied 50kg (×50) | Flag |
|---|---|---|---|
| 2015 | ~250–300 | ~12,500–15,000 | [ESTIMATED] (anecdotal, not NBS) |
| Dec 2022 | 506.17 | 25,309 | [SOURCED] |
| Dec 2023 | 917.93 | 45,897 | [SOURCED] |
| Dec 2024 | 1,944.40 | 97,220 | [SOURCED] |
| Oct 2025 | 1,913.78 | 95,689 | [SOURCED] |
| Mar 2026 (local short-grain) | 1,876.36 | 93,818 | [SOURCED] |
| Mar 2026 (imported long-grain) | 2,223.83 | 111,192 | [SOURCED] |

Market cross-check: local-rice 50kg bag reported ~₦80,000–112,000 in late-2025/2026 (Legit.ng). NBS also: rice +134.81% in the 12 months to mid-2024 (Guardian).

### 4b. Other staples — per kg / per unit (key anchors)

| Commodity | Dec 2022 | Dec 2023 | 2024 | 2025/26 | Flag |
|---|---|---|---|---|---|
| Garri (white) /kg | — | — | 749.89 (Mar) → 1,198.05 (Oct) | 846.69 (Oct 2025) | [SOURCED] |
| Garri (yellow) /kg | — | — | 1,170.65 (Aug) | — | [SOURCED] |
| Beans (brown) /kg | 586.14 | 870.67 | 2,501.32 (Dec) | 1,760.53 (Oct 2025); 1,325.85 (Mar 2026) | [SOURCED] |
| Bread (sliced 500g) | — | — | 1,047.86 (Feb) → 1,550.24 (Oct) | — | [SOURCED] |
| Bread (unsliced 500g) | — | 736.68 (Oct) | — | — | [SOURCED] |
| Tomato /kg | 458.42 | 814.16 | 1,465.99 (Oct) | 1,269.17 (Oct 2025); 1,104.95 (Mar 2026) | [SOURCED] |
| Onion /kg | 435.93 | 971.86 | 2,057.81 (Dec) | — | [SOURCED] |
| Palm oil (1 litre) | — | 1,425.32 | 2,582.35 (Dec) | — | [SOURCED] |
| Yam (per tuber) | — | — | — | 2,144.70 (Mar 2026) | [SOURCED] |

Context: NBS ~40-item food basket average rose to **₦2,920.13 in Dec 2024, +91.6% YoY** (Nairametrics/NBS). National "mudu/congo" measures exist regionally but no reliable national series — not sourceable. Imported-rice/yellow-garri/yam earlier-year series are present in NBS PDFs but thin in secondary coverage — pull from NBS report PDFs if every year is needed.

---

## 5. PETROL — USD-equivalent (devaluation effect)

> USD = PMS ÷ approximate prevailing official NGN/USD (World Bank period-average / CBN). All [ESTIMATED].

| Period | PMS NGN/litre | Approx NGN/USD | USD/litre |
|---|---|---|---|
| 2015 | 87 | ~193 | ~$0.45 |
| 2016 (post-May) | 145 | ~253 | ~$0.57 |
| 2017–2019 | 145 | ~306 | ~$0.47 |
| 2020 | ~148 | ~359 | ~$0.41 |
| 2021 | ~165 | ~401 | ~$0.41 |
| 2022 | ~190 | ~426 | ~$0.45 |
| early 2023 (pre-removal) | ~190 (cap) / 264 (NBS) | ~461 | ~$0.41 / $0.57 |
| **Jun 2023 (post-removal)** | 545.83 | ~750 | **~$0.73** |
| Dec 2023 | ~625 | ~900 | ~$0.69 |
| 2024 (annual) | ~868 | ~1,479 | ~$0.59 |
| Dec 2024 | 1,189 | ~1,535 | ~$0.77 |
| 2025 (annual) | ~1,100 | ~1,535 | ~$0.72 |
| **May 2026** | 1,596 | ~1,490 | **~$1.07** |

**Insight:** flat ~$0.40–0.47/litre across 2015–early-2023 (devaluation absorbed each nominal hike) → ~$0.70+ post-float → ~$1.07 by 2026. The USD price has roughly doubled vs the subsidy era: post-2023 hikes are a real price rise, not just devaluation.

---

## 6. FOOD INFLATION — annual (year-on-year, %)

| Year | Annual avg | Dec YoY | Flag |
|---|---|---|---|
| 2015 | ~9.8% | ~10.6% | [ESTIMATED] (verify NBS Dec-2015 CPI) |
| 2016 | ~14.9% | 15.70% (Dec) | Dec [SOURCED]; annual [ESTIMATED] |
| 2017 | ~19.5% (peak 20.32% Oct) | ~19.4% | [ESTIMATED] |
| 2018 | ~14.4% | ~13.6% | [ESTIMATED] (verify NBS) |
| 2019 | ~13.7% | ~14.7% | [ESTIMATED] (verify NBS) |
| 2020 | **16.17%** (12-mo avg) | ~19.6% | annual avg [SOURCED] |
| 2021 | ~20.4% | ~17.4% | [ESTIMATED] (verify NBS) |
| 2022 | ~18.7–20.5% | **23.75%** | Dec [SOURCED]; annual [ESTIMATED] |
| 2023 | ~24–27% | **33.93%** | Dec [SOURCED]; annual [ESTIMATED] |
| 2024 (old base) | high-30s (**peak 40.87%, Jun 2024, all-time high**) | **39.84%** | Dec & peak [SOURCED] |
| 2025 (new base) | declining ~26% (Jan) → **10.84%** (Dec) | **10.84%** | [SOURCED] |
| 2026 (YTD) | Jan **8.89%** → May **16.96%** | n/a | [SOURCED] |

**2025 monthly (new base, [SOURCED]):** ~26% (Jan), 23.51% (Feb), 25.22% (Mar), 24.55% (May), 20.16% (Sep), 16.30% (Oct), 14.21% (Nov), **10.84% (Dec)**.
**2026 monthly ([SOURCED]):** **8.89% (Jan, lowest since Aug 2011)**, 15.06% (Feb), 14.32% (Mar), 16.06% (Apr), **16.96% (May)**.

**⚠ Rebasing hazard (Jan 2025):** the ~40%→~26% drop is methodological (new base 2024 / weights 2023), **not** real disinflation — prices kept rising into 2025. Keep old-base (≤Dec 2024) and new-base (≥Jan 2025) separate. **Live discrepancy:** a Feb-2026 Nairametrics retrospective cites 29.63% for "Jan 2025" vs the ~26% in the original release — confirm against the NBS Jan-2025 CPI report before locking. Years flagged [ESTIMATED] (2015, 2017–19, 2021, and annual-avg 2016/2022/2023) were not directly sourced — verify in NBS December CPI reports.

---

## 7. FOOD SECURITY — Cadre Harmonisé / IPC Phase 3+ (crisis or worse)

| Lean season | Analysis cycle | Current Phase 3+ (at analysis) | Projected Jun–Aug lean-season Phase 3+ | States | Flag |
|---|---|---|---|---|---|
| 2020 | Oct 2019 | BAY only 2.9m (Oct–Dec 2019) | BAY ~3.6–3.8m; **national not cleanly sourced** | 16+FCT | [PROVISIONAL] (national unverified) |
| 2021 | Oct 2020 | 9.8m (Oct–Dec 2020) | 13.8m | 16+FCT | [SOURCED]; states [PROVISIONAL] |
| 2022 | Oct 2021 | 12.9m (Oct–Dec 2021) | 18.0m | 20+FCT | [SOURCED] |
| 2022 | Mar 2022 (revised) | 14.5m (Mar–May 2022) | 19.5m | ~26+FCT | [SOURCED] (the "14.4m" anchor = Mar-2022 current) |
| 2023 | Oct/Nov 2022 | ~17m (Oct–Dec 2022) | **25.3m** ("nearly 25m") | 26+FCT | [SOURCED] |
| 2024 | Oct 2023 | 18.6m (Oct–Dec 2023) | **26.5m** | 26+FCT | [SOURCED] |
| 2025 | Oct 2024 | 25.1m (Oct–Dec 2024) | **33.1m** | 26+FCT | [SOURCED] |
| 2025 | Mar 2025 (revised) | 24.9m (Mar–May 2025) | **30.6m** (30,624,499; revised down from 33.1m) | 26+FCT (548 LGAs) | [SOURCED] (confirms "30.6m" anchor) |
| 2026 | Oct/Nov 2025 | 27.2m (Oct–Dec 2025, incl. ~485k IDPs) | **34.7m** | 27+FCT | [SOURCED] |

**Anchor clarifications:** the ~7m "2020" figure could NOT be verified as a national CH Phase 3+ number (only BAY-states 2.9m→3.6–3.8m are sourced — likely conflated with broader humanitarian-needs). 2021's "9–13m" = the Oct-2020 analysis (9.8m current / 13.8m projected). 2025's two figures (33.1m vs 30.6m) are both correct — Oct-2024 forecast vs Mar-2025 revision of the same lean season.

**Phase 4 (Emergency) / Phase 5 (famine-risk):** Phase 4 ~1m (2024 lean peak) → 1.8m projected for 2025 lean (Oct 2024), revised ~1.18m (Mar 2025). **Phase 5 risk flagged in Borno** — ~15,000 at risk of Catastrophe in Dikwa/Kaga/Kalabalge (Oct-2025 analysis for the 2026 projection); inaccessible Borno LGAs (Abadam, Guzamala, Kukawa, Marte) repeatedly flagged (178,000 of 295,000 residents severe, 2025 lean projection). No area *currently* classified Phase 5 per the 2026 regional FAO bulletin.

**Regional context (do not mix into Nigeria totals):** West Africa & Sahel — 41.8m Phase 3+ current (Oct–Dec 2025), **52.8m** projected for the 2026 lean season; Nigeria is ~two-thirds of this.

---

## SOURCES (full URLs)

### Fuel — NBS primary
- PMS Price Watch catalog: https://microdata.nigerianstat.gov.ng/index.php/catalog/157 · Diesel: https://microdata.nigerianstat.gov.ng/index.php/catalog/158 · LPG: https://microdata.nigerianstat.gov.ng/index.php/catalog/160
- PMS Feb 2023: https://nigerianstat.gov.ng/elibrary/read/1241299 · Aug 2023: https://www.nigerianstat.gov.ng/elibrary/read/1241383 · Oct 2024: https://www.nigerianstat.gov.ng/elibrary/read/1241584
- Diesel Jan 2023: https://nigerianstat.gov.ng/elibrary/read/1241287 · May 2023: https://nigerianstat.gov.ng/elibrary/read/1241341 · Jan 2024: https://www.nigerianstat.gov.ng/elibrary/read/1241456 · May 2024: https://www.nigerianstat.gov.ng/elibrary/read/1241517
- LPG May 2024: https://www.nigerianstat.gov.ng/elibrary/read/1241519 · NBS X (LPG 5kg Dec 2025): https://x.com/NBS_Nigeria/status/2018607394037604479

### Fuel — reporting citing NBS
- PMS Jul 2025: https://nairametrics.com/2025/08/21/average-petrol-price-slips-to-n1024-99-litre-in-july-2025-nbs/
- PMS crosses ₦1,000 (Sep 2024): https://nairametrics.com/2024/10/17/petrol-price-crosses-n1000-benchmark-for-the-first-time-ever-rises-by-24-08-in-september-2024-nbs/
- PMS Apr 2025: https://nairametrics.com/2025/05/21/pms-prices-surge-by-76-73-year-on-year-in-april-2025-south-east-residents-paid-n1341-71-nbs/
- PMS May 2026 (Premium Times): https://www.premiumtimesng.com/business/business-news/890568-nigerias-petrol-price-climbs-to-%E2%82%A61596-per-litre-in-may-nbs.html · (Legit): https://www.legit.ng/business-economy/energy/1716120-nbs-reports-petrol-price-climbs-5531-n1596litre-2026/
- PMS Feb 2023→2024 (₦263.76→₦679.37): https://www.thecable.ng/from-n263-to-n679-nbs-says-petrol-price-surged-by-157-in-one-year/ · subsidy-removal +210% (Jun 2023 ₦545.83): https://www.thecable.ng/subsidy-removal-petrol-price-soared-by-210-in-one-year-says-nbs/
- PMS Sep 2022 (₦191.65): https://nairametrics.com/2022/10/24/petrol-price-rises-to-n191-65-for-september-2022-nbs/ · Dec 2024 decline: https://guardian.ng/news/petrol-prices-decline-11-81-in-december-nbs/ · Nov 2025: https://www.channelstv.com/2025/12/23/consumers-paid-%E2%82%A61061-average-petrol-price-in-november-nbs/
- Diesel Mar 2024: https://nairametrics.com/2024/04/18/diesel-prices-increased-to-n1341-litre-in-march-2024-nbs/ · Oct 2022 (₦801.09): https://nairametrics.com/2022/11/24/nigerians-paid-on-average-n801-09-per-litre-for-diesel-in-october/ · Nov 2025: https://nairametrics.com/2025/12/23/diesel-price-drops-2-57-to-n1409-61-in-november-nbs/
- Diesel May 2026 (₦3,277.47, +86.40%): https://www.legit.ng/business-economy/energy/1716140-nbs-diesel-price-rises-8640-n3277litre-2026/ · (Tribune): https://tribuneonlineng.com/diesel-price-rose-by-86-in-may-2026-as-kerosene-sold-for-n2971-94-per-litre-nbs/amp/
- LPG Aug 2024 (5kg ₦6,430.02 / 12.5kg ₦15,552): https://nairametrics.com/2024/09/23/average-price-of-12-5kg-cooking-gas-hits-n16500-in-niger-delta-states-highest-across-nigeria/ · May 2025: https://naija247news.com/2025/07/04/cooking-gas-prices-surge-nationwide-5kg-refill-hits-%E2%82%A68167-12-5kg-tops-%E2%82%A620709-nbs-report/ · Jun 2025 peak: https://nairametrics.com/2025/07/31/average-price-of-5kg-cooking-gas-rises-to-n8323-in-june-2025-nbs/ · Jul 2025 (12.5kg ₦20,609): https://www.tv360nigeria.com/cooking-gas-price-soars-by-44-5-year-on-year-hits-%E2%82%A620609-for-12-5kg-in-july-nbs/ · Dec 2025 5kg ₦5,360.43: https://www.facebook.com/NBSNigeria/posts/1210886291232991/ · Mar 2026 (5kg ₦7,655): https://nairametrics.com/2026/04/29/cooking-gas-prices-jump-as-5kg-hits-n7655-in-march-2026/
- Regulated-era & FX: Vanguard (₦87→₦145, 2016): https://www.vanguardngr.com/2016/05/petrol-price-hike-buharis-1st-year-anniversary-gift-to-nigerians/ · FIJ pump-price timeline: https://fij.ng/article/timeline-from-n20-to-n617-how-pump-price-evolved-in-24-years/ · WB exchange rate: https://data.worldbank.org/indicator/PA.NUS.FCRF?locations=NG · CBN rates: https://www.cbn.gov.ng/rates/ExchRateByCurrency.html · Statista NGN/USD: https://www.statista.com/statistics/1304053/usd-to-nigerian-naira-annual-average-exchange-rate/

### Electricity — NERC & reporting
- NERC FAQ (band definitions, SBT 1 Nov 2020): https://nerc.gov.ng/faq/electricity-tariffs/
- Punch (168% hike; 2015 ₦23.5 / 2023 ₦63): https://punchng.com/cheap-electricity-nigeria-ranks-109-amid-168-tariff-hike-in-eight-years/
- Ventures Africa (MYTO 2015, eff. 1 Feb 2016): http://venturesafrica.com/is-the-new-electricity-tariff-justifiabe/
- Proshare (300% Band A hike): https://www.proshare.co/articles/nerc-approves-300-tariff-increase-for-band-a-nigerian-electricity-consumers
- Vanguard (₦225→₦206.8, −8%): https://www.vanguardngr.com/2024/05/electricity-nerc-reduces-band-a-tariff-by-8-to-n206-8-kwh/ · Nairametrics (8.1% cut, 6 May 2024): https://nairametrics.com/2024/05/06/naira-appreciation-nerc-approves-8-1-electricity-tariff-cut-for-band-a-customers-for-all-discos/ · (FX cut 16.03%): https://nairametrics.com/2024/05/07/nerc-reduces-fx-rate-for-calculating-new-tariff-for-band-a-customers-by-16-03/
- Stears (Band A ₦209.5, Jul 2024): https://www.stears.co/article/electricity-data-bulletin-nigerian-band-a-electricity-tariff-reaches-2095kwh-in-july-2024/
- Premium Times (Enugu Band A ₦209→₦160, Aug 2025): https://www.premiumtimesng.com/news/top-news/808513-electricity-regulator-slashes-band-a-tariff-gives-reason.html
- Guardian (₦1.94tn subsidy 2024): https://guardian.ng/news/electricity-subsidies-cost-fg-%E2%82%A61-94-trillion-in-2024-nerc/ · BusinessDay (₦1.98tn 12-mo): https://businessday.ng/energy/article/nigerias-electricity-subsidy-hits-%E2%82%A61-98tn-in-12-months-despite-tariff-hikes/ · Punch (subsidy +220%): https://punchng.com/shocking-surge-electricity-subsidy-jumps-220-to-nearly-n2tn/
- Pulse (2026 tariff review): https://www.pulse.ng/story/nigerians-brace-for-another-electricity-tariff-hike-as-nerc-reviews-power-costs-2026051209451771562 · ICIR (tariff regime / Q1-2025 subsidy): https://www.icirnigeria.org/inside-nerc-electricity-tariff-regime/

### Food prices & inflation — NBS & reporting
- NBS Selected Food Prices Watch catalog: https://microdata.nigerianstat.gov.ng/index.php/catalog/162 · CPI & Inflation catalog: https://microdata.nigerianstat.gov.ng/index.php/catalog/154
- NBS Food Price Watch Dec 2023 (read): https://www.nigerianstat.gov.ng/elibrary/read/1241445 · Mar 2024 PDF: https://www.nigerianstat.gov.ng/pdfuploads/SELECTED_FOOD_MARCH_2024.pdf · Jun 2024 PDF: https://www.nigerianstat.gov.ng/pdfuploads/Selected_Food_Report_June_2024.pdf · Oct 2024 PDF: https://www.nigerianstat.gov.ng/pdfuploads/Selected_Food_Report_Oct_2024.pdf
- NBS reads: Feb 2024 https://www.nigerianstat.gov.ng/elibrary/read/1241477 · Apr 2024 https://www.nigerianstat.gov.ng/elibrary/read/1241505 · May 2024 https://www.nigerianstat.gov.ng/elibrary/read/1241520 · Sep 2024 https://www.nigerianstat.gov.ng/elibrary/read/1241575
- NBS CPI: Dec 2022 https://www.nigerianstat.gov.ng/elibrary/read/1241274 · Jun 2024 https://www.nigerianstat.gov.ng/elibrary/read/1241533 · NBS X (Dec-2024 food 39.84% / headline 34.80%): https://x.com/NBS_Nigeria/status/1879498504340644100
- Nairametrics Dec-2024 food (+91.6% YoY; rice ₦1,944.40; beans ₦2,501.32): https://nairametrics.com/2025/01/25/average-food-prices-rise-to-n2920-13-in-december-2024-marking-91-6-yoy-increase-nbs/
- 21st Century Chronicle Oct-2025 (rice ₦1,913.78; beans ₦1,760.53; garri ₦846.69): https://21stcenturychronicle.com/nbs-rice-beans-garri-and-tomato-prices-fall-nationwide-in-october-2025/
- Nairametrics Feb-2026 (food 8.89% Jan 2026 + 2025 monthly series): https://nairametrics.com/2026/02/16/nigerias-food-inflation-drops-to-single-digit-of-8-89-lowest-in-over-14-years/ · Punch Dec-2025 headline 15.15%: https://punchng.com/nigerias-headline-inflation-eases-to-15-15-in-december-2025-nbs/ · Ecofin Feb-2025 food 23.51%: https://www.ecofinagency.com/public-management/1803-46513-nigerias-food-inflation-drops-to-23-51-in-february-2025
- Vanguard Jun-2026 (Mar-2026 prices: imported rice ₦2,223.83, local ₦1,876.36, yam ₦2,144.70): https://www.vanguardngr.com/2026/06/how-high-pricesre-degrading-quality-of-food-nigerians-eat/ · Legit (local rice 50kg ₦112,000): https://www.legit.ng/business-economy/economy/1709017-local-rice-costs-n112000-50kg-bag-food-prices-surge-nationwide/ · Guardian (rice +134.81%): https://guardian.ng/business-services/prices-of-rice-rise-by-134-81-per-cent-in-12-months-says-nbs/
- TradingEconomics food inflation (all-time high 40.87% Jun 2024): https://tradingeconomics.com/nigeria/food-inflation · CBN inflation rates: https://www.cbn.gov.ng/rates/inflrates.html

### Food security — Cadre Harmonisé / FAO-WFP-OCHA
- CH Oct 2019 (16 states, proj. 2020): https://reliefweb.int/report/nigeria/cadre-harmonis-identification-risk-areas-and-vulnerable-populations-sixteen-16-0
- Oct 2020 fiche: https://fscluster.org/nigeria/document/october-2020-cadre-harmonize-ch-fiche · Mar 2021 fiche: https://fscluster.org/nigeria/document/final-fiche-report-march-2021-cadre
- Oct 2021 (20 states, proj. 2022): https://reliefweb.int/report/nigeria/cadre-harmonis-identification-risk-areas-and-vulnerable-populations-twenty-20-states · fiche: https://fscluster.org/lakechad/document/final-fiche-report-october-2021-cadre
- Nov 2022 fiche (26 states): https://fscluster.org/nigeria/document/final-fiche-report-november-2022-cadre · Mar 2023 fiche: https://fscluster.org/nigeria/document/fiche-cadre-harmonise-identification
- Oct 2024 CH results: https://fscluster.org/nigeria/document/cadre-harmonise-results-food-and · AGRHYMET/CILSS Nov 2024: https://agrhymet.cilss.int/2024/11/01/publication-des-resultats-de-la-consolidation-nationale-du-cadre-harmonise-ch-au-nigeria/
- **Mar 2025 Fiche PDF (exact numbers, 30,624,499):** https://fscluster.org/sites/default/files/2025-03/FINAL_2025%20_March_Fiche-Nigeria.pdf
- Oct 2025 (34.7m, proj. 2026, 27 states): https://agrhymet.cilss.int/2025/10/31/bout-34-7-million-nigerians-across-27-states-and-the-federal-capital-territory-fct-are-projected-to-face-a-severe-food-and-nutrition-crisis-between-june-and-august-2026/
- IPC Cadre Harmonisé portal: https://www.ipcinfo.org/ch/ · HDX CH dataset (raw by phase/year): https://data.humdata.org/dataset/cadre-harmonise
- 25m for 2023 (UNICEF/FAO): https://www.unicef.org/wca/press-releases/joint-press-release-25-million-nigerians-high-risk-food-insecurity-2023 · FAO: https://www.fao.org/nigeria/news/detail-events/en/c/1630260/
- 26.5m for 2024 (FAO): https://www.fao.org/nigeria/news/detail-events/en/c/1661923 · OCHA: https://www.unocha.org/publications/report/nigeria/265-million-nigerians-projected-be-food-insecure-2024
- 33.1m for 2025 (FAO): https://www.fao.org/nigeria/news/detail-events/en/c/1720792/ · WFP: https://www.wfp.org/news/economic-hardship-climate-crisis-and-violence-northeast-projected-push-331-million-nigerians
- 34.7m by mid-2026 (BusinessDay): https://businessday.ng/news/article/over-34-million-nigerians-to-face-acute-food-insecurity-by-mid-2026-fao-report/ · Guardian: https://guardian.ng/news/34-7-million-nigerians-projected-to-face-food-insecurity-by-june-2026/
- W.Africa/Sahel 52.8m (2026 regional): https://www.fao.org/africa/news-stories/news-detail/west-africa-and-the-sahel--nearly-52.8-million-people-could-face-acute-food-insecurity-during-the-2026-lean-season-(june-august)/en

---

## KEY GAPS / CONFIDENCE NOTES

- **Electricity:** a clean national-average NGN/kWh series for **2017–2022 and 2025–2026** is not reliably sourceable (left blank). Defensible anchors: ₦23.5 (2015), ₦63 (Jan 2023), ₦100.27 allowed-avg (2024, NERC). The Band-A event is solid.
- **Fuel annual averages** are computed from NBS monthly figures (not official NBS annual releases); 2015–2020 are regulated caps, not survey averages. 2026 is partial-year and surging.
- **Food prices:** no NBS data for 2015 (series began Jun 2016); imported-rice/yellow-garri/yam earlier-year lines need direct NBS PDF extraction.
- **Food inflation:** 2015, 2017–19, 2021 annual figures flagged [ESTIMATED] — verify in NBS December CPI reports. Live discrepancy on the Jan-2025 rebased value (26% vs 29.63%).
- **Food security:** the ~7m "2020" anchor is **unconfirmed** as a national CH Phase 3+ number (only BAY-states figures sourced). Exact March-cycle totals for 2020/2021/2024 sit behind fiche PDFs that block automated fetch — open the HDX CH dataset / fiche PDFs in a browser for LGA-level precision.
