# US Fed Tightening Cycles Since 1970 — Event-Study of Hard vs Soft Landings

**Compiled:** 2026-07-04 · **Analyst pull/access date:** 2026-07-04
**Deliverable:** `usa/usa_fed_cycles.csv`
**Purpose:** Test the base rate at which Fed tightening (hiking) cycles end in an NBER recession ("hard landing") versus no recession ("soft landing"). Feeds the debt-cycle model's "what does the exit from high rates look like" layer.

**Method.** A "cycle" = a sustained sequence of policy-rate increases from a local trough to a local peak. Fed funds levels are the **monthly effective federal funds rate** (FRED `FEDFUNDS`) for cycles through 2006, and **target-range midpoints** for the two ZIRP-exit cycles (2015-18, 2022-23) where the Fed sets a range not a point. "Followed by recession" = an NBER-dated recession that **began within ~24 months of the rate peak**. Lag = months from rate peak to NBER peak (recession start).

**Flags:** [SOURCED] = date/level confirmed against Fed/FRED/NBER/St. Louis Fed. [ESTIMATED] = rounded or approximated where sources give ranges or intra-month precision differs.

---

## NBER recession chronology used (peak = recession start) [SOURCED]

Source: NBER Business Cycle Dating Committee / FRED `USREC`.

| Recession (NBER peak -> trough) | Notes |
|---|---|
| 1969-12 -> 1970-11 | pre-window |
| 1973-11 -> 1975-03 | oil shock / Burns |
| 1980-01 -> 1980-07 | Volcker I (brief, credit controls) |
| 1981-07 -> 1982-11 | Volcker II (double-dip, deep) |
| 1990-07 -> 1991-03 | S&L / Gulf War oil |
| 2001-03 -> 2001-11 | dot-com bust |
| 2007-12 -> 2009-06 | Global Financial Crisis |
| 2020-02 -> 2020-04 | COVID-19 (exogenous) |

No NBER recession has been declared after 2020-04 as of the 2026-07 compile date. [SOURCED]

---

## Cycle-by-cycle sourcing

### 1. Burns 1972-74 -> HARD [SOURCED / partly ESTIMATED]
Effective funds ~3.29% (Feb-1972) climbing to a peak **12.92% July-1974**; contemporaneous accounts cite ~13%. Tightening ran into the 1973 OPEC embargo (oil $3->$12). The **NBER recession began 1973-11, ~8 months BEFORE the rate peak** — the Fed was still hiking mid-recession (stagflation). Unambiguous hard landing. Sources: FRED `FEDFUNDS`; Richmond Fed "Burns Disinflation of 1974"; Kansas City Fed "Inflation in 1972."

### 2. Volcker I 1977-80 -> HARD [SOURCED / peak ESTIMATED]
Prior easing bottomed ~4.61% (early 1977); rate rose through the Miller period, then the **Oct-1979 "Volcker shock"** (switch to nonborrowed-reserve targeting) drove it up. **Monthly effective peaked ~17.6% Apr-1980**; the daily/target rate spiked toward **~20%** briefly. The short, sharp **NBER recession 1980-01 -> 1980-07** began ~3 months before the monthly-effective peak (Carter credit controls forced an abrupt slump). Hard. Sources: FRED; Fed History "Recession of 1981-82"; Wikipedia/Volcker (20% June-1981 figure); Statista Volcker-shock series.

### 3. Volcker II 1980-81 -> HARD [SOURCED]
After mid-1980 easing to ~9%, Volcker **re-hiked to ~19-20% by June-1981** (monthly effective ~19.1% Jun-1981; 20% target/daily peak). The **NBER recession 1981-07 -> 1982-11** followed within ~1 month — deep, unemployment >10%, but it **broke inflation** (CPI 14.8% Mar-1980 -> <3% by 1983). The 1980 + 1981-82 pair is the "Volcker double-dip." Sources: Fed History; St. Louis Fed Review (Jan-2025) "The Volcker Tightening Cycle: Explaining the 1982 Course Reversal"; FRED.

### 4. 1983-84 -> SOFT [SOURCED]
Volcker raised the nominal funds rate **from 8.5% (Mar-1983) to ~11.5% (early Aug-1984), +300bp** (St. Louis Fed). **No recession followed** (next recession 1990-07, ~71 months later). St. Louis Fed classes it as one of only two post-1980 episodes (with 1994-95) that produced **no yield-curve inversion** — a genuine soft landing. Rates fell below 10% by Nov-1984. Source: St. Louis Fed "A Look at Fed Tightening Episodes since the 1980s" (Kliesen).

### 5. 1988-89 -> HARD [SOURCED]
Greenspan tightened by a **cumulative 331bp in 18 steps**, roughly **6.5% (early 1988) to ~9.75-9.85% (Feb-1989)**, after the 1987 crash and vs rising inflation. **NBER recession 1990-07 -> 1991-03** followed ~17 months after the peak (Gulf-War oil spike compounded). Hard. Sources: St. Louis Fed tightening-episodes paper; NY Fed "Monetary Policy and Open Market Operations During 1989."

### 6. 1994-95 -> SOFT (the classic case) [SOURCED]
Greenspan **doubled the funds rate 3.0% (Feb-1994) -> 6.0% (Feb-1995), +300bp** in 7 moves (incl. a 75bp move Nov-1994), pre-emptively. **No recession** — expansion ran on to 2001 (~72 months). Widely cited as the **only unambiguous textbook soft landing**. Sources: St. Louis Fed; Richmond Fed "A Rate Cycle Unlike Any Other"; FRED.

### 7. 1999-2000 -> HARD [SOURCED]
**4.75% (Jun-1999) -> 6.5% (May-2000), +175bp**, capped by a 50bp move; tightening into the dot-com bubble. **NBER recession 2001-03 -> 2001-11** began ~10 months after the peak (dot-com bust; 9/11 compounded). Hard. Sources: FRB Monetary Policy Report Jul-2000; SF Fed Economic Letter (May-2000); FRED.

### 8. 2004-06 -> HARD (GFC) [SOURCED]
**1.0% (Jun-2004) -> 5.25% (Jun-2006), +425bp** via **17 consecutive 25bp "measured pace" hikes**. Yield curve inverted in 2006. **NBER recession 2007-12 -> 2009-06 = the Global Financial Crisis** (housing/credit), ~18 months after the peak. Hard. Sources: FOMC statement 2004-06-30; CRS "Federal Reserve Interest Rate Changes 2000-2007"; Bankrate/Forbes rate histories; FRED.

### 9. 2015-18 -> EXOGENOUS (flag) [SOURCED]
Slow ZIRP-exit: first hike **Dec-2015**, target **0-0.25% -> 2.25-2.50% (Dec-2018), +225bp** (midpoints 0.13% -> 2.38%). An **NBER recession did begin 2020-02**, ~14 months after the peak — **but its cause was the COVID-19 pandemic (an exogenous shock), not the tightening.** Timing alone would score "hard," but on causation this is neither a policy-induced hard landing nor a clean soft landing; **flagged as exogenous.** The Fed had already reversed (three "insurance" cuts in 2019) before COVID. Sources: FRB Open Market Operations; NBER; Statista "Most Aggressive Tightening Cycle."

### 10. 2022-23 -> SOFT SO FAR (provisional) [SOURCED]
Fastest cycle in four decades: **11 hikes Mar-2022 -> Jul-2023**, target **0-0.25% -> 5.25-5.50%, +525bp** (midpoints 0.13% -> 5.38%). Peak reached Jul-2023 and held. **As of 2026-07 no NBER recession has begun (~36 months on)** while inflation fell back toward target — widely described as a **soft landing / "immaculate disinflation."** Status is **provisional** (a cycle is only definitively "soft" once the next expansion is well established; the Fed began cutting in 2024). Sources: TheStreet Fed timeline; Forbes/Bankrate; Richmond Fed; NBER (no post-2020 recession dated).

---

## Base-rate synthesis

Counting **all 10 distinct hiking cycles since 1970** (Volcker split into its two legs; Burns included):

- **Hard landings (recession within ~2yr, policy-linked): 6** — Burns 1972-74, Volcker I 1977-80, Volcker II 1980-81, 1988-89, 1999-2000, 2004-06.
- **Soft landings (no recession): 3** — 1983-84, 1994-95, and 2022-23 (provisional).
- **Exogenous / ambiguous: 1** — 2015-18 (recession followed, but COVID-caused).

If the Volcker double-dip is counted as one cycle and the pre-Volcker Burns cycle is set aside, you get the **~8 "canonical" modern cycles** the literature usually cites: ~4 hard, ~3 soft, 1 exogenous — the same ~2:1 tilt.

**Base rate:** roughly **two-thirds of Fed tightening cycles have been followed by a recession**, and a clean soft landing is **historically rare** — only **1994-95** is universally agreed, with **1983-84** the other strong case. **2022-23 is the leading modern candidate** and, as of mid-2026, looks like a soft landing — but it would be only the third in ~55 years, so the historical prior sits against it. Two recessions that followed tightenings (1990-91 Gulf oil, 2001 9/11, 2007-09 housing) also had large non-monetary triggers, underscoring that "hard vs soft" is rarely a function of the Fed alone.

---

## Sources (primary/reputable)

- NBER Business Cycle Dating Committee — US business-cycle peaks/troughs: https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions
- FRED `FEDFUNDS` (effective federal funds rate) and `USREC`: https://fred.stlouisfed.org/series/FEDFUNDS , https://fred.stlouisfed.org/series/USREC
- St. Louis Fed, "A Look at Fed Tightening Episodes since the 1980s" (Kliesen): https://www.stlouisfed.org/on-the-economy/2022/apr/fed-tightening-episodes-since-1980s-part-one
- St. Louis Fed Review (Jan-2025), "The Volcker Tightening Cycle: Explaining the 1982 Course Reversal"
- Federal Reserve History, "Recession of 1981-82": https://www.federalreservehistory.org/essays/recession-of-1981-82
- Richmond Fed, "The Burns Disinflation of 1974"; "A Rate Cycle Unlike Any Other" (2023)
- FRB Open Market Operations / FOMC statements (2004-06-30 etc.): https://www.federalreserve.gov/monetarypolicy/openmarket.htm
- CRS, "Federal Reserve Interest Rate Changes: 2000-2007"
- Bankrate / Forbes Advisor federal-funds-rate histories (secondary cross-checks)
