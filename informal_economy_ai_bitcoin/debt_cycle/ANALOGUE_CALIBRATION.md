# Nigeria Debt-Cycle — Historical Analogue Calibration (Phase 3)

**Compiled:** 2026-06-30 · **Sources:** `_staging/18_analogue_argentina.md`, `19_analogue_turkey_egypt.md`, `20_analogue_ghana_synthesis.md`

Phase 3 backtests the base/bull/bear scenarios against real inflationary deleveragings — to replace judgment-set probabilities with **analogue-anchored** ones, and to see how these episodes actually resolved *for households*.

---

## 1. The analogue panel

| Episode | Trigger | Peak inflation | FX collapse | How it deleveraged | Household real-wage hit / recovery | Verdict |
|---|---|---|---|---|---|---|
| **Argentina 1980s** | oil/debt + monetization | ~5,000% (1989) | hyperinflation | austerity→1991 currency board | real wage ~halved vs 1974; **never fully recovered** | **ugly / lost decade** |
| **Argentina 2001–02** | FX-debt + peg break | ~41% | 1:1→~4:1 | **default (~75% haircut)** + float | poverty→57.5%, wages −24%; recover ~4–5 yrs | ugly→recover |
| **Argentina 2018–24** | FX-debt + failed IMF | 211% (2023) | peso collapse | orthodox shock (Milei 2024) | poverty 52.9%→31.6%; wages recover ~1.5–2 yrs | provisionally beautiful (brutal) |
| **Turkey 2018–25** | local-debt, **heterodox** | 85.5% (2022) | lira −80%+ | rate-cuts-into-inflation, then 2023 U-turn | incomes still below pre-crisis; recover **~5–7 yrs** | **ugly grind** |
| **Egypt 2016 / 2022–24** | FX shortage | ~38% (2023) | pound floats, ~−70% | **orthodox + $35bn UAE windfall** + IMF | poverty rising into 2024; recover **~3–4 yrs (bought)** | beautiful-ish (sponsored) |
| **Ghana 2022–25** | lost market access | 54.1% | cedi −45–50% | **dual default (DDEP + Eurobond −37%)** + $3bn IMF | wages −43% (2022), still climbing | ugly→beautiful (reset) |
| **Nigeria 2005–06** *(own)* | Paris Club exit | — | n/a (relief) | **$18bn write-off + oil-windfall buy-back** | debt/GDP 52%→7% | beautiful (one-off) |

---

## 2. Base rates from the evidence

- **"Beautiful" deleveragings are the minority: ~30–40%.** Most inflationary deleveragings are ugly (lost decade, serial relapse, or default) before — if ever — they resolve.
- **Typical time for household real income to regain pre-crisis levels: ~6.5-year median / ~8-year mean** (Reinhart–Rogoff ~100-episode evidence), range ~3 to 15–20+ years — *well beyond* the ~5-year "beautiful" bar.
- **The household shock lands fast** (a 20–50% real-wage hit + double-digit poverty jump within ~12 months) in *every* case; it is the *recovery* that varies enormously.
- **Three factors separate good from bad outcomes:** (1) sustained **orthodox policy** with a credible fiscal anchor; (2) **external support / windfall** (IMF + relief, FDI, or a sponsor cheque); (3) **governance / reform durability**. *Default itself is not decisive* — a clean IMF-covered default (Ghana) can *speed* recovery.

---

## 3. Where Nigeria sits

Nigeria's current episode = **orthodox float (Jun 2023) + aggressive tightening (MPR to 27.5%) + IMF engagement + NO default + an oil windfall** — structurally the **better-than-median** side of the distribution (closest to **Egypt's orthodox direction** and **Ghana's destination**). **But:**
- It is executing at **Turkey's gradualist pace**, not Egypt's decisive one.
- It **lacks Ghana's mechanical debt reset** (no default → no automatic stock reduction) **and Egypt's $35bn sponsor cheque** (no mega-windfall to close the gap in one move).
- Its **weak governance and rising insecurity** (ACLED fatalities at a decade high) are *exactly* the variable that sorts countries into the ugly tail.

**Net read:** the base case is "**Egypt's destination on a Turkey-length timetable**" — household real incomes bottoming 2024–25 and not fully recovering until ~**2027–29**. A fast/"beautiful" recovery requires an external catalyst Nigeria does not currently have.

---

## 4. Calibration decision

| Scenario | Before (judgment) | **After (analogue-calibrated)** | Why |
|---|---|---|---|
| Base — "grinding stabilization" | 55% | **55%** | The central Egypt-on-a-Turkey-timetable path; unchanged |
| Bull — "beautiful deleveraging completes" | 25% | **20% ▼** | Empirically, fast/beautiful recovery is a **sub-25% event**; Nigeria lacks the reset/windfall that bought it elsewhere |
| Bear — "reform fatigue / ugly relapse" | 20% | **25% ▲** | Governance/security fattens the left tail; Turkey shows how premature loosening or fiscal slippage stretches recovery past 7 years |

**Applied in `scenario_model.py`** (prob fields). Effect on the probability-weighted 2030 outlook: GDP/capita ≈ $2,000 (was $2,036), real-wage index ≈ 51.9 (was 54.6), extreme poverty ≈ 45.5% (was 44.8) — i.e. the calibrated expectation is modestly *worse*, driven by the heavier bear weight.

> The probabilities remain a judgement — but now an **evidence-anchored** one: a ~55/20/25 split puts ~25% on the ugly tail and only ~20% on a fast household recovery, consistent with the ~30–40% "beautiful" base rate *discounted* for Nigeria's missing debt-reset/windfall and its governance risk. Re-weight again if the tracker's security gauge or the external catalysts change.
