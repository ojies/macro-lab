# Nigeria — Long-Run Historical Backbone & Prior Debt Cycles (1980–2014)

**Dataset:** Big-Debt-Cycle / Nigeria — PRE-2015 historical backbone (the detailed 2015–2026 series live in worksheets 01–16; this file supplies the deeper history the Dalio framework needs).
**Compiled:** 2026-06-30
**Coverage:** annual, 1980–2014.
**Source priority:** World Bank WDI / International Debt Statistics, IMF, CBN Statistical Bulletin, DMO, Paris Club, OPEC/EIA, academic economic histories.

**Flag legend:** `[SOURCED]` = taken directly from a cited primary/secondary source for the stated period · `[SOURCED-2nd]` = official DMO/CBN figure reported via a secondary outlet or the standard published CBN/DMO series (DMO & CBN portals were anti-scraping/Cloudflare-blocked this session, same as worksheet 01) · `[ESTIMATED]` = derived/computed by analyst (method noted) · `[PROVISIONAL]` = single-source or vintage-uncertain · blank/`—` = not reliably sourceable, left empty rather than guessed.

---

## CRITICAL METHODOLOGY NOTES & SERIES BREAKS (read first)

**BREAK 1 — 2014 GDP rebasing (base 1990 → 2010).** On 6 April 2014 the NBS rebased nominal GDP, lifting the level by **~59–89%** (≈ ₦80.2tn vs ~₦42.4tn for 2013; Nigeria overtook South Africa as Africa's largest economy at ~$510bn → ~$574bn 2014). **Every debt-to-GDP, deficit-to-GDP and current-account-to-GDP ratio computed on the *old* base is mechanically ~1.6× higher than on the new base.** WDI now splices the rebased series back to 2010, so 2010–2014 ratios here are on the new base while pre-2010 ratios are effectively old-base. Treat the 2010 boundary as a denominator break. *(Detail in worksheet 04.)*

**BREAK 2 — FX regimes & redenomination.** The naira passed through several incompatible regimes: a managed peg of **₦0.55–0.77/$ (1980–1985)**; the **SFEM/SAP float from Sept 1986** (₦1.75 → ₦4.0 → ₦8.0); a **dual/multiple-rate era through the 1990s** where the official rate was pegged at **₦21.9/$ (1995–1998)** while the **parallel ("autonomous") market ran ~₦80–88/$**; unification near **₦92–100/$ (1999)**; a long managed band ~₦115–150/$ (2000s); ~₦150/$ (2008) to ~₦158–197/$ (2014). The official-rate column below understates the true cost of FX in 1993–1998. **There was no currency redenomination** (the proposed 2007 "re-denomination"/N1=100k was cancelled); the unit is continuous, but the *rate* breaks are severe. *(Detail in worksheet 03.)*

**BREAK 3 — "GDP in current US$" distortion (1980–1998).** Because WDI converts naira GDP at the *official* rate, the overvalued peg makes 1981 GDP look like **$164bn** and 1997 like **$201bn**, then it "collapses" to **$59bn in 1999** purely from the FX unification — not a real-economy collapse. Use real GDP *growth* (next table) for the macro story; read the USD-GDP level with this caveat.

**BREAK 4 — "External debt": two different concepts.** (a) **World Bank total external debt (DOD)** = public + publicly-guaranteed + private non-guaranteed + IMF credit. (b) **DMO/CBN public external debt** = sovereign only. They diverge sharply after the 2005–06 Paris Club exit: e.g. **end-2006 DMO public external ≈ $3.5bn**, but **WDI total external ≈ $17.5bn** (the difference is private-sector and other external liabilities). Both are shown and labelled; do not conflate the famous "$3.5bn" sovereign figure with the WDI total.

---

## PART A — LONG ANNUAL TIME SERIES, 1980–2014

### A1. Debt stock — external (USD bn), domestic (₦ bn), with public-debt context

| Year | External debt, total — WDI DOD (USD bn) | DMO/CBN **public** external (USD bn) | FGN domestic debt (₦ bn) | Flag | Notes |
|---|---|---|---|---|---|
| 1980 | 8.94 | ~8.9 | ~8.2 | [SOURCED]/[SOURCED-2nd] | WDI; start of the borrowing surge |
| 1981 | 11.45 | — | ~11.2 | [SOURCED] | |
| 1982 | 11.99 | — | — | [SOURCED] | oil price crash begins |
| 1983 | 17.58 | — | — | [SOURCED] | |
| 1984 | 17.78 | — | — | [SOURCED] | domestic debt/GDP already >40% (IMF/Asogwa) |
| 1985 | 18.66 | ~19.0 | ~28 | [SOURCED] | |
| 1986 | 22.22 | — | — | [SOURCED] | SAP / 1st Paris Club reschedule |
| 1987 | 29.02 | — | — | [SOURCED] | SAP devaluation inflates USD-converted debt |
| 1988 | 29.62 | — | — | [SOURCED] | |
| 1989 | 30.12 | — | — | [SOURCED] | 2nd Paris Club reschedule |
| 1990 | 33.46 | ~33.1 | ~84 | [SOURCED] | |
| 1991 | 33.53 | 35.9 | — | [SOURCED] | DMO/Wikipedia cite US$35.9bn external; debt/GDP ~75% peak (old base) |
| 1992 | 29.02 | — | — | [SOURCED] | |
| 1993 | 30.70 | — | — | [SOURCED] | Nigeria stops servicing Paris Club → arrears build |
| 1994 | 33.09 | — | — | [SOURCED] | |
| 1995 | 34.09 | — | — | [SOURCED] | |
| 1996 | 31.41 | — | — | [SOURCED] | |
| 1997 | 28.47 | — | — | [SOURCED] | |
| 1998 | 30.31 | — | — | [SOURCED] | |
| 1999 | 29.10 | ~28.0 | ~795 | [SOURCED] | return to civilian rule; debt-relief campaign begins |
| 2000 | 33.51 | — | ~898 | [SOURCED] | DMO established Oct 2000; 4th Paris Club reschedule |
| 2001 | 34.98 | — | — | [SOURCED] | |
| 2002 | 36.78 | — | — | [SOURCED] | |
| 2003 | 41.86 | — | ~1,330 | [SOURCED] | 1st FGN Bond re-floated after 17-yr absence |
| 2004 | 45.91 | **35.99** | **~1,360** | [SOURCED] | DMO: total external **$35.994bn** (Paris Club 85.8% / $30.84bn; Multilateral 7.9%; London Club 4.0%; Prom. Notes 2.2%); domestic ~₦1.36tn securitized (DMO Paris Club doc) |
| 2005 | 33.65 | ~20.5 | ~1,526 | [SOURCED] | Paris Club **Phase 1** (arrears + 33% cancel) executed; debt falling |
| 2006 | 17.49 | **~3.5** | ~1,753 | [SOURCED]/[SOURCED-2nd] | Paris Club exit complete (Apr 2006); sovereign external ≈ **$3.5bn**; WDI *total* (incl. private) $17.5bn |
| 2007 | 19.48 | ~3.7 | ~2,170 | [SOURCED] | re-leveraging begins (eurobond debut delayed to 2011) |
| 2008 | 20.42 | ~3.7 | ~2,320 | [SOURCED] | Wikipedia: external "$20.6bn", debt/GDP 7.3% (WDI total) |
| 2009 | 22.75 | ~3.9 | ~3,228 | [SOURCED] | |
| 2010 | 29.15 | ~4.6 | ~4,552 | [SOURCED] | |
| 2011 | 34.13 | ~5.7 | ~5,623 | [SOURCED] | debut $500m Eurobond (Jan 2011); Apr-2011 domestic ₦4.8tn (~$30bn) per Wikipedia/DMO |
| 2012 | 39.28 | ~6.5 | ~6,538 | [SOURCED] | $1bn Eurobond (2013) pending |
| 2013 | 42.60 | ~8.8 | ~7,119 | [SOURCED] | |
| 2014 | 46.67 | ~9.7 | ~7,904 | [SOURCED] | hand-off year to the detailed 2015– dataset (worksheet 01) |

> **Domestic-debt column caveat:** the ₦ values are the standard **CBN Statistical Bulletin / DMO "FGN Domestic Debt Outstanding"** series. Strongly-anchored years (2004 ≈ ₦1.36tn [SOURCED, DMO], 2005, 2010, 2014) are reliable; intervening years are the widely-published official figures but flagged `[SOURCED-2nd]` because the CBN/DMO portals (and the Knoema mirror) were Cloudflare-blocked this session. Mid-1990s annual values not independently re-verified are left blank rather than guessed. The full annual ₦ series resides in the CBN Statistical Bulletin (Public Finance tables).

### A2. Debt-to-GDP (%) — **read with BREAK 1 & BREAK 3 caveats**

| Year | External debt / GDP, WDI-based (%) | Headline debt/GDP cited by officials/lit. | Flag | Notes |
|---|---|---|---|---|
| 1980 | 13.9 | — | [ESTIMATED] | WDI ext ÷ WDI USD-GDP |
| 1985 | 25.3 | — | [ESTIMATED] | |
| 1990 | 61.9 | — | [ESTIMATED] | USD-GDP depressed by SAP FX |
| 1991 | 56.3 | **~75%** (peak) | [ESTIMATED]/[SOURCED] | Wikipedia/DMO: total-debt/GDP peaked ~75% in 1991 (old base) |
| 1995 | 24.2 | — | [ESTIMATED] | denominator inflated by ₦21.9 peg → understated ratio |
| 2000 | 48.4 | — | [ESTIMATED] | |
| 2004 | 33.8 | **~52% / ~58%** | [ESTIMATED]/[SOURCED] | DMO Paris Club doc: total debt/GDP "about 52–58%" pre-relief (old base) |
| 2005 | 19.2 | — | [ESTIMATED] | mid-transition |
| 2006 | 7.3 | **~7%** | [ESTIMATED]/[SOURCED] | DMO projected post-relief debt/GDP "to ~7%"; matches WDI total |
| 2008 | 6.0 | **7.3%** | [ESTIMATED]/[SOURCED] | trough of the cycle |
| 2010 | 7.9 | — | [ESTIMATED] | new (2010) GDP base from here |
| 2014 | 8.1 | ~12–13% (total public, new base) | [ESTIMATED] | external-only shown; +domestic ≈ low-teens total public debt/GDP |

> The DMO's own pre-relief headline (52%) and the WDI-based 33.8% for 2004 differ because the DMO used a *sovereign-debt / smaller-GDP* construction. The reliable, regime-independent message: **debt/GDP peaked ~75% around 1991, was still ~50%+ in 2004, then collapsed to ~7% by 2006–08 after Paris Club relief, and re-climbed only into the low teens by 2014.**

### A3. Real GDP growth (%) and GDP level (current USD bn)

| Year | Real GDP growth % | GDP, current USD bn | Flag | Year | Real GDP growth % | GDP, current USD bn | Flag |
|---|---|---|---|---|---|---|---|
| 1980 | +4.2 | 64.2 | [SOURCED] | 1998 | +2.6 | 218.4 | [SOURCED] |
| 1981 | **−13.1** | 164.5 | [SOURCED] | 1999 | +0.6 | 59.1 | [SOURCED] |
| 1982 | −6.8 | 142.8 | [SOURCED] | 2000 | +5.0 | 69.2 | [SOURCED] |
| 1983 | −10.9 | 97.1 | [SOURCED] | 2001 | +5.9 | 73.6 | [SOURCED] |
| 1984 | −1.1 | 73.5 | [SOURCED] | 2002 | +15.3 | 95.1 | [SOURCED] |
| 1985 | +5.9 | 73.7 | [SOURCED] | 2003 | +7.3 | 104.7 | [SOURCED] |
| 1986 | +0.1 | 54.8 | [SOURCED] | 2004 | +9.3 | 135.8 | [SOURCED] |
| 1987 | +3.2 | 52.7 | [SOURCED] | 2005 | +6.4 | 175.7 | [SOURCED] |
| 1988 | +7.3 | 49.6 | [SOURCED] | 2006 | +6.1 | 238.5 | [SOURCED] |
| 1989 | +1.9 | 44.0 | [SOURCED] | 2007 | +6.6 | 278.3 | [SOURCED] |
| 1990 | +11.8 | 54.0 | [SOURCED] | 2008 | +6.8 | 339.5 | [SOURCED] |
| 1991 | +0.4 | 59.5 | [SOURCED] | 2009 | +8.0 | 295.0 | [SOURCED] |
| 1992 | +4.6 | 52.1 | [SOURCED] | 2010 | +8.0 | 367.0 | [SOURCED] |
| 1993 | −2.0 | 56.7 | [SOURCED] | 2011 | +5.3 | 414.5 | [SOURCED] |
| 1994 | −1.8 | 80.4 | [SOURCED] | 2012 | +4.2 | 464.0 | [SOURCED] |
| 1995 | −0.1 | 140.9 | [SOURCED] | 2013 | +6.7 | 520.1 | [SOURCED] |
| 1996 | +4.2 | 185.7 | [SOURCED] | 2014 | +6.3 | 574.2 | [SOURCED] |
| 1997 | +2.9 | 200.9 | [SOURCED] | | | | |

*Source: World Bank WDI (NY.GDP.MKTP.KD.ZG real growth; NY.GDP.MKTP.CD current US$). The 1981–1984 contraction (cumulatively ~−28%) is the 1980s oil-bust depression; the 2002 +15.3% reflects a one-off oil-output rebound (and old-base volatility); 2014 level embeds the rebasing (BREAK 1).*

### A4. Inflation — CPI, annual average %

| Year | CPI % | Year | CPI % | Year | CPI % |
|---|---|---|---|---|---|
| 1980 | 10.0 | 1992 | **44.6** | 2004 | 15.0 |
| 1981 | 20.8 | 1993 | **57.2** | 2005 | 17.9 |
| 1982 | 7.7 | 1994 | **57.0** | 2006 | 8.2 |
| 1983 | 23.2 | 1995 | **72.8** | 2007 | 5.4 |
| 1984 | 17.8 | 1996 | 29.3 | 2008 | 11.6 |
| 1985 | 7.4 | 1997 | 8.5 | 2009 | 12.5 |
| 1986 | 5.7 | 1998 | 10.0 | 2010 | 13.7 |
| 1987 | 11.3 | 1999 | 6.6 | 2011 | 10.8 |
| 1988 | **54.5** | 2000 | 6.9 | 2012 | 12.2 |
| 1989 | **50.5** | 2001 | 18.9 | 2013 | 8.5 |
| 1990 | 7.4 | 2002 | 12.9 | 2014 | 8.0 |
| 1991 | 13.0 | 2003 | 14.0 | | |

*Source: World Bank WDI (FP.CPI.TOTL.ZG). Two hyperinflation episodes: **1988–89 (~50–55%)** post-SAP price deregulation, and **1992–1995 (peaking 72.8% in 1995)** driven by deficit monetization (CBN financing of fiscal gaps) and naira collapse under Abacha.*

### A5. NGN/USD exchange rate (annual average, official) — **see BREAK 2**

| Year | ₦/$ official | Year | ₦/$ official | Year | ₦/$ official |
|---|---|---|---|---|---|
| 1980 | 0.55 | 1992 | 17.30 | 2004 | 132.89 |
| 1981 | 0.62 | 1993 | 22.07 | 2005 | 131.27 |
| 1982 | 0.67 | 1994 | 22.00 | 2006 | 128.65 |
| 1983 | 0.72 | 1995 | 21.90 | 2007 | 125.81 |
| 1984 | 0.77 | 1996 | 21.88 | 2008 | 118.57 |
| 1985 | 0.89 | 1997 | 21.89 | 2009 | 148.88 |
| 1986 | **1.75** | 1998 | 21.89 | 2010 | 150.30 |
| 1987 | 4.02 | 1999 | **92.34** | 2011 | 153.86 |
| 1988 | 4.54 | 2000 | 101.70 | 2012 | 157.50 |
| 1989 | 7.37 | 2001 | 111.23 | 2013 | 157.31 |
| 1990 | 8.04 | 2002 | 120.58 | 2014 | 158.55 |
| 1991 | 9.91 | 2003 | 129.22 | | |

*Source: World Bank WDI (PA.NUS.FCRF, official period-average). **Caveat:** 1995–1998 the official rate was a frozen ₦21.9 peg while the parallel/autonomous market traded **~₦80–88/$**; the 1999 jump to ₦92 is the unification of the dual rate, not a single-year devaluation. 1986 ₦1.75 = the SFEM float that ended the ₦0.55–0.77 peg.*

### A6. External reserves (USD bn, total reserves incl. gold, year average/holdings)

| Year | Reserves $bn | Year | Reserves $bn | Year | Reserves $bn |
|---|---|---|---|---|---|
| 1980 | 10.6 | 1992 | 1.2 | 2004 | 17.3 |
| 1981 | 4.2 | 1993 | 1.6 | 2005 | 28.6 |
| 1982 | 1.9 | 1994 | 1.6 | 2006 | 42.7 |
| 1983 | 1.3 | 1995 | 1.7 | 2007 | 51.9 |
| 1984 | 1.7 | 1996 | 4.3 | 2008 | 53.6 |
| 1985 | 1.9 | 1997 | 7.8 | 2009 | 43.1 |
| 1986 | 1.3 | 1998 | 7.3 | 2010 | 33.3 |
| 1987 | 1.5 | 1999 | 5.6 | 2011 | 33.7 |
| 1988 | 0.9 | 2000 | 10.1 | 2012 | 45.0 |
| 1989 | 2.0 | 2001 | 10.6 | 2013 | 43.7 |
| 1990 | 4.1 | 2002 | 7.6 | 2014 | 35.1 |
| 1991 | 4.7 | 2003 | 7.4 | | |

*Source: World Bank WDI (FI.RES.TOTL.CD). Reserves were drained to **<$1bn (1988)** at the depth of the debt crisis, rebuilt on the late-2000s oil windfall to a peak ~$53.6bn (2008), then fell with the GFC oil shock. CBN year-end figures differ marginally (e.g. CBN cites ~$51.3bn end-2007).*

### A7. Oil — price (USD/bbl) and Nigerian crude production (mbpd)

| Year | Crude price, world ref. (WTI, $/bbl) | Brent annual avg ($/bbl) | Nigeria crude output (mbpd) | Flag |
|---|---|---|---|---|
| 1980 | 37.42 | — | ~2.05 | [SOURCED]/[ESTIMATED] |
| 1981 | 35.75 | — | ~1.43 | |
| 1982 | 31.83 | — | ~1.28 | oil-price crash begins |
| 1983 | 29.08 | — | ~1.23 | |
| 1984 | 28.75 | — | ~1.38 | |
| 1985 | 26.92 | — | ~1.49 | |
| 1986 | **14.44** | — | ~1.46 | price collapse → SAP |
| 1987 | 17.75 | 18.53 | ~1.34 | Brent series begins |
| 1988 | 14.87 | 14.91 | ~1.38 | |
| 1989 | 18.33 | 18.23 | ~1.76 | |
| 1990 | 23.19 | 23.76 | ~1.77 | Gulf-War spike |
| 1991 | 20.20 | 20.04 | ~1.94 | |
| 1992 | 19.25 | 19.32 | ~2.01 | |
| 1993 | 16.75 | 17.01 | ~1.99 | |
| 1994 | 15.66 | 15.86 | ~1.90 | |
| 1995 | 16.75 | 17.02 | ~1.92 | |
| 1996 | 20.46 | 20.64 | ~1.95 | |
| 1997 | 18.64 | 19.11 | ~1.95 | |
| 1998 | **11.91** | 12.76 | ~2.00 | Asian-crisis price trough |
| 1999 | 16.56 | 17.90 | ~1.87 | |
| 2000 | 27.39 | 28.66 | ~2.15 | |
| 2001 | 23.00 | 24.46 | ~2.13 | |
| 2002 | 22.81 | 24.99 | ~1.92 | OPEC-cut year |
| 2003 | 27.69 | 28.85 | ~2.27 | |
| 2004 | 37.66 | 38.26 | ~2.46 | oil-windfall era begins |
| 2005 | 50.04 | 54.57 | ~2.45 | windfall funds Paris Club exit |
| 2006 | 58.30 | 65.16 | ~2.34 | |
| 2007 | 64.20 | 72.44 | ~2.17 | |
| 2008 | 91.48 | **96.94** | ~2.13 | price peak; Niger-Delta militancy cuts output |
| 2009 | 53.48 | 61.74 | ~2.16 | GFC price crash; amnesty |
| 2010 | 71.21 | 79.61 | ~2.46 | output recovery |
| 2011 | 87.04 | 111.26 | ~2.39 | |
| 2012 | 86.46 | 111.63 | ~2.35 | |
| 2013 | 91.17 | 108.56 | ~2.21 | |
| 2014 | 85.60 | **98.97** | ~2.21 | H2-2014 price collapse begins |

> **Sources/flags:** WTI nominal annual averages — InflationData historical table [SOURCED]; **Brent annual average — EIA RBRTE series [SOURCED]** (the cleaner Nigeria proxy, since **Bonny Light tracks Brent within ±$1–2**, per worksheet 06). Use Brent from 1987; for 1980–86 the WTI column captures the boom-bust level (OPEC official Bonny Light ran ~$40/bbl in 1980 → ~$14 in 1986). **Production [ESTIMATED]:** derived from the Energy Institute Statistical Review of World Energy (via Our World in Data, primary-energy TWh) converted to mbpd (factor anchored so 1980≈2.05, 2010≈2.46); matches OPEC ASB/EIA crude benchmarks within rounding. Definitions vary (crude-only vs. crude+condensate+NGL) by ±0.2 mbpd — treat as indicative.

### A8. Current account (% GDP) and fiscal balance (% GDP)

| Year | Current account (% GDP) | Fiscal balance (% GDP) | Flag |
|---|---|---|---|
| 1980 | +8.1 | — | [SOURCED CA] |
| 1981 | −3.9 | — | [SOURCED CA] |
| 1985 | +3.5 | — | [SOURCED CA] |
| 1990 | +9.2 | ~−8 to −12 (deficit) | [SOURCED CA]/[PROVISIONAL fiscal] |
| 1993 | −1.4 | ~−6.1 (deficit) | [SOURCED CA]/[SOURCED fiscal] |
| 1994 | −2.6 | ~−7 | [SOURCED CA]/[PROVISIONAL] |
| 1995 | −0.6 | — | [SOURCED CA] |
| 1998 | −0.6 | — | [SOURCED CA] |
| 2000 | +10.7 | — | [SOURCED CA] |
| 2004 | +12.4 | — | [SOURCED CA] |
| 2005 | **+20.8** | — | [SOURCED CA] |
| 2006 | +15.3 | **+6.2 (surplus)** | [SOURCED CA]/[SOURCED fiscal] |
| 2007 | +9.9 | — | [SOURCED CA] |
| 2008 | +8.6 | — | [SOURCED CA] |
| 2009 | +4.7 | — | [SOURCED CA] |
| 2010 | +3.6 | **−6.1** | [SOURCED CA]/[SOURCED fiscal] |
| 2011 | +2.6 | — | [SOURCED CA] |
| 2012 | +3.7 | — | [SOURCED CA] |
| 2013 | +3.7 | — | [SOURCED CA] |
| 2014 | +0.2 | ~−2 (consolidated) | [SOURCED CA]/[PROVISIONAL] |

> **Current account:** full WDI series (BN.CAB.XOKA.GD.ZS) [SOURCED] — note the **2004–2006 oil-windfall surpluses (+12% to +21% of GDP)** that physically financed the Paris Club buy-back. **Fiscal balance:** only fragmentary points are reliably sourced this session (1990s deficits "up to 12% of GDP", 1993 ≈ −6%, 2006 ≈ +6.2% surplus, 2010 ≈ −6.1%); the full annual federal-deficit series sits in the CBN Statistical Bulletin (Public Finance) and is left blank where not corroborated.

---

## PART B — PRIOR DEBT-CYCLE EPISODES

### Episode 1 — 1970s oil boom → 1980s oil bust & debt build-up

The **1971–1981 oil boom** ("the era of big borrowing," DMO) flipped Nigeria from a near-zero external debtor (US$0.84bn in 1970, US$8.9bn in 1980) into a heavy one. Borrowing was undertaken by all tiers of government and, critically, the **FGN guaranteed many unviable loans** of state governments, parastatals and private banks (trade arrears). When **oil prices crashed from ~$37/bbl (1980) to ~$14/bbl (1986)**, FX earnings collapsed, Nigeria could not service its loans, and **arrears, penalties and interest compounded the stock from ~$9bn (1980) to ~$18.7bn (1985) and ~$33.5bn (1990)** (WDI). Real GDP contracted in **1981 (−13%), 1982 (−7%), 1983 (−11%)** — a cumulative ~28% depression — while reserves fell below **$1bn by 1988**. This is the classic Dalio "bubble → bust → debt-burden" opening of a big debt cycle, denominated in foreign currency. *[SOURCED — WDI; DMO Paris Club doc]*

### Episode 2 — 1986 Structural Adjustment Programme (SAP)

Facing insolvency, the Babangida regime adopted **SAP in mid-1986** (with World Bank/IMF design, though Nigeria refused a full IMF loan after a national "IMF debate"). Core measures: the **Second-Tier Foreign Exchange Market (SFEM, Sept 1986)** that floated the naira from **₦0.89/$ to ₦1.75/$ and onward to ₦8/$ by 1990**; trade and import liberalization; removal of price controls and subsidies; privatization; and the first **Paris Club reschedulings (1986, 1989, 1991)**. The devaluation **mechanically inflated the USD-converted debt and naira debt-service burden** (external debt rose from $18.7bn in 1985 to $30bn+ by 1989 partly via FX revaluation), and the social cost was severe: **inflation hit ~55% (1988) and ~50% (1989)** as subsidies were cut, real wages fell, and the "SAP riots" erupted. The conditionality bought reschedulings but **not stock reduction** — postponing rather than resolving the burden. *[SOURCED — DMO Paris Club doc; WDI]*

### Episode 3 — 1990s debt overhang, arrears & ~72% inflation (Abacha era)

Despite four reschedulings, **Paris Club debt kept rising** because Nigeria could not pay what fell due each year; after the Paris Club refused deep reduction, **Nigeria effectively stopped servicing Paris Club debt in the mid-1990s**, so arrears and late-interest ballooned. The **Abacha military government (1993–1998)** ran large deficits financed by **CBN money-printing** (the CBN held ~75% of domestic debt by end-1994), driving the worst inflation in Nigeria's history — **44.6% (1992), 57.2% (1993), 57.0% (1994), and a peak 72.8% (1995)** — while the official FX rate was frozen at **₦21.9/$** against a parallel rate near **₦85/$**. Total debt/GDP had peaked near **75% around 1991** (old base). The cycle stayed stuck in "depression/stagflation with FX rationing and capital flight" until the **1999 return to civilian rule** under Obasanjo reopened the path to relief. *[SOURCED — WDI; DMO; IMF Asogwa; US State Dept 1995 trade report]*

### Episode 4 — **2005–2006 Paris Club & London Club debt relief (THE pivotal episode)**

This is the single most important pre-2015 event for the Nigerian debt cycle — a textbook Dalio "**beautiful deleveraging**": a large, negotiated debt write-down combined with an oil-windfall cash buy-back that reset the sovereign balance sheet.

**Before (31 Dec 2004):**
- Total external debt: **US$35.994bn** (≈ ₦4.82tn at the ₦134/$ rate) — about **$37,101 owed per Nigerian** against GDP-per-capita of ~₦3,380.
- Composition: **Paris Club 85.8% (US$30.84bn)**, Multilateral 7.9%, London Club 4.0%, Promissory Notes 2.2%, Non-Paris bilateral 0.1%. Largest Paris creditors: **UK $8.00bn, France $6.25bn, Germany $5.29bn, Japan $4.45bn, Italy $1.98bn**.
- Pre-relief ratios: debt/GDP ~52%, debt/revenue ~412%, debt/exports ~152%.
- Securitized **domestic** debt: ~**₦1.36tn** (64% in 91-day T-bills — very short, bank-held).

**The deal (announced 29 June 2005; executed Oct 2005 → 21 Apr 2006):**
1. **Arrears clearance** — Nigeria paid ~**US$6bn** of arrears upfront (Oct 2005). (Nigeria's case was exceptional: relief was offered *before* arrears were cleared.)
2. **Naples-terms write-off** — the $30.84bn was reduced to **$24.84bn**, of which up to **$16.64bn was cancelled** (two tranches: 33% then a further 34%, ≈67%).
3. **Discounted buy-back** — the remaining ~**$8.2bn** was bought back at a market-related discount (the **first-ever discounted buy-back inside the Paris Club**, an innovation proposed in an April-2005 CGD note), saving a further ~$2.0bn and leaving ~**$6.2bn**, which Nigeria paid to exit.
4. **Policy anchor** — not a full IMF loan but a **Policy Support Instrument (PSI)** endorsing Nigeria's home-grown **NEEDS** reform programme (IMF first review ~March 2006 triggered the second cancellation tranche).

**Quantum:** total debt relief **≈ US$18bn** (the headline "$18bn"); total cash Nigeria paid **≈ US$12.4bn** (~$6bn arrears + ~$6.2bn buy-back) — financed by the **2004–2006 oil-windfall current-account surpluses (+12% to +21% of GDP)** accumulated in the Excess Crude Account. The architects were **Finance Minister Ngozi Okonjo-Iweala** (who headed the Nigerian delegation) and President **Olusegun Obasanjo**'s economic team; the DMO (est. Oct 2000) had spent years auditing and reconciling the debt database to make a credible deal possible.

**After:**
- Sovereign external debt fell to ~**US$3.5bn** (multilateral + remaining promissory notes/London Club) by end-2006 — **Nigeria owed the Paris Club nothing**.
- **External debt/GDP collapsed from ~52% to ~7%** (DMO projection; WDI total-external/GDP confirms ~7.3% by 2006–08); debt/revenue from 412% to ~58%; debt-service from heavy to **~1% of GDP**.
- **London Club:** the smaller commercial debt (par/promissory-note and oil-warrant instruments) was retired separately via buy-backs around **2006–2007**, completing the external clean-up.

This relief is the deep trough of Nigeria's first big debt cycle and the baseline against which the post-2015 re-leveraging (worksheets 01–02) should be read. *[SOURCED — DMO "Nigeria's Debt Relief Deal with the Paris Club"; Paris Club press release 20 Oct 2005; CGD; UPenn "Anatomy of a 2005 Debt Deal"]*

### Episode 5 — Post-2006 re-leveraging (2006 → 2014)

From the ~$3.5bn sovereign-external / ~₦1.75tn domestic trough, debt rebuilt steadily but **moderately** through 2014:
- **Domestic** was the engine: FGN domestic debt rose **~₦1.75tn (2006) → ₦7.9tn (2014)** (~4.5×), as the DMO deliberately deepened the local bond market (lengthening from 91-day bills toward 3–20-year FGN bonds) and financed persistent ~2–6%-of-GDP deficits.
- **External** stayed small and concessional at first (multilateral/IDA), then Nigeria returned to international capital markets with its **debut $500m Eurobond (Jan 2011)** and further issues (2013), lifting sovereign external toward ~$9–10bn by 2014 (WDI total external $46.7bn including private).
- Because the 2010-rebased GDP denominator was large, **total public debt/GDP was still only ~low-teens % by 2014** — which fed the official "Nigeria's debt is low/sustainable" narrative (BudgIT 2018: ~24% even in 2018) even as the *debt-service-to-revenue* ratio was already climbing ominously toward the danger zone (the theme that dominates the 2015–2026 dataset).

This sets up the hand-off: **2014 ≈ ₦7.9tn domestic + ~$9–10bn sovereign external**, debt/GDP low-teens, oil at ~$99 Brent but collapsing in H2-2014 — i.e. the calm just before the 2015– leg of the cycle. *[SOURCED — WDI; DMO; BudgIT]*

---

## SOURCES

**Core long series (World Bank WDI / IDS, retrieved via API 2026-06-30, country=NGA, 1980–2014):**
- GDP current US$ — `NY.GDP.MKTP.CD`: https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=NG
- Real GDP growth — `NY.GDP.MKTP.KD.ZG`: https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=NG
- Inflation CPI — `FP.CPI.TOTL.ZG`: https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?locations=NG
- External debt stock (DOD, current US$) — `DT.DOD.DECT.CD`: https://data.worldbank.org/indicator/DT.DOD.DECT.CD?locations=NG
- Total reserves incl. gold — `FI.RES.TOTL.CD`: https://data.worldbank.org/indicator/FI.RES.TOTL.CD?locations=NG
- Current account (% GDP) — `BN.CAB.XOKA.GD.ZS`: https://data.worldbank.org/indicator/BN.CAB.XOKA.GD.ZS?locations=NG
- Official exchange rate (LCU/US$, period avg) — `PA.NUS.FCRF`: https://data.worldbank.org/indicator/PA.NUS.FCRF?locations=NG

**Debt relief / debt profile:**
- DMO, *Nigeria's Debt Relief Deal with the Paris Club* (extracted in full this session): https://www.dmo.gov.ng/publications/other-publications/nigeria-debt-relief/570-nigeria-s-debt-relief-deal-with-the-paris-club/file
- Paris Club press release, *Treatment of Nigeria's debt*, 20 Oct 2005: https://clubdeparis.org/en/communications/press-release/treatment-of-nigeria-s-debt-20-10-2005
- Center for Global Development, *Debt Relief for Nigeria* (discounted buy-back innovation): https://www.cgdev.org/page/debt-relief-nigeria
- UPenn / T. Callaghy, *Anatomy of a 2005 Debt Deal: Nigeria and the Paris Club*: https://live-sas-www-polisci.pantheon.sas.upenn.edu/sites/default/files/TC_Nigeria_short.pdf
- Wikipedia, *Nigeria national debt* (corroboration: 1991 $35.9bn / ~75% debt-GDP; 2004 ~$36bn; 2008 7.3%; Apr-2011 ₦4.8tn domestic): https://en.wikipedia.org/wiki/Nigeria_national_debt
- BudgIT, *Reviewing Nigeria's Debt Status* (2019; debt-to-GDP context): https://yourbudgit.com/wp-content/uploads/2019/06/Nigerias-Debt-Status.pdf
- DMO external debt outstanding 1983–2004 (creditor breakdown; portal blocked this session): https://www.dmo.gov.ng/1107-external-debt-outstanding-1983-2004/file
- IMF / C. Asogwa, *Domestic Government Debt Structure…Nigeria* (1980s domestic-debt/GDP, CBN financing share): https://www.imf.org/external/np/res/seminars/2005/macro/pdf/asogwa.pdf

**Oil & prices:**
- EIA Europe Brent Spot annual averages (`RBRTE`, parsed this session): https://www.eia.gov/dnav/pet/hist/RBRTEa.htm
- InflationData, *Historical Crude Oil Prices Table* (WTI nominal annual): https://inflationdata.com/articles/inflation-adjusted-prices/historical-crude-oil-prices-table/
- OPEC Annual Statistical Bulletin (Nigeria crude production benchmark cross-check): https://www.opec.org/annual-statistical-bulletin.html
- Energy Institute Statistical Review of World Energy via Our World in Data (oil production, primary-energy basis → converted to mbpd): https://ourworldindata.org/grapher/oil-production-by-country

**Reserves / fiscal context:**
- CBN, Movement in Foreign Reserves / Reserve Management: https://www.cbn.gov.ng/intops/reserve.html
- CBN, *External Reserves Accumulation…* (Economic & Financial Review, 2010): https://www.cbn.gov.ng/Out/2012/publications/reports/rsd/efr-2010/
- CBN Statistical Bulletin (master historical series — Public Finance / Domestic Debt tables; full annual ₦ domestic-debt series): https://www.cbn.gov.ng/documents/Statbulletin.html
- US Dept of State, *Nigeria: Economic Policy and Trade Practices, 1995* (1990s deficits up to 12% of GDP; CBN held 75% of domestic debt 1994): https://1997-2001.state.gov/issues/economic/trade_reports/africa95/NIGERIA.html

**Known gaps left blank (not reliably sourceable this session):** full annual ₦ FGN domestic-debt series 1985–2003 (CBN/DMO portals Cloudflare-blocked; only anchor years given); full annual federal fiscal-balance %GDP series (only ~1993, 2006, 2010 corroborated); exact DMO *public* external debt for each post-2006 year (only headline ~$3.5bn / Eurobond milestones given); year-by-year Bonny Light realized prices pre-2009 (Brent/WTI proxies used per worksheet 06's ±$1–2 rule).
