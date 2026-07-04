# Nigeria — Development-Age Model (comparative macro / catch-up)

**Engine:** `development_age.py` → `development_age_summary.csv`
**Data:** `countries_gdp_pc_ppp.csv` · `countries_development_indicators.csv` · `countries_catchup_macro.csv` · `countries_divergence_factors.csv` (staging 23–26)
**Sources:** Maddison Project Database 2023 (2011$ PPP), World Bank WDI, IMF Historical Public Debt, UN, ACLED, WGI.

Compares countries by **development level, not calendar year**. Nigeria isn't "behind in 2026" — it's at an *economic age* the US/UK/Korea/China passed through decades ago. The model lines them up on that axis, shows what came next, and — critically — **conditions the analogy on Nigeria's initial conditions** so it never claims "Nigeria = Korea-1970 → Nigeria becomes Korea."

---

## 1. Nigeria's economic age — the frontier-equivalent year

On Maddison's consistent 2011$ PPP base, **Nigeria (2022) = $2,207/capita**. That income level was reached by:

| Country | was at Nigeria's level in… | "years behind" |
|---|---|---|
| **South Korea** | **~1970** (near-exact anchor) | 52 |
| China | ~1983 | 39 |
| India | ~2000 | 22 · Vietnam ~1996 · Indonesia ~1988 |
| Brazil | ~1950 | 72 |
| Japan | ~1919 | 103 |
| United States | ~1862 | 160 · Germany ~1860 · UK ~1823 |

**Korea-1970 is the tightest match** — so the question the model answers is *"can Nigeria do from here what Korea did?"* And a sobering fact frames it: **Nigeria's per-capita income peaked c.2010 ($2,269) and has *fallen* to $2,207** — it has spent a lost decade going backwards, not forwards.

## 1b. Development is *uneven* — a 22-year spread across dimensions

The composite index (income + health + urbanization + structure + demography) nets to **Korea-1970**, but mapping each dimension onto Korea's timeline shows Nigeria is at very different "ages" on different axes:

| Dimension | Nigeria ≈ Korea in… |
|---|---|
| Income (GDP/capita) | ~1970 |
| Demography (fertility) | ~1970 |
| Structure (agriculture share) | ~1969 |
| **Health (life expectancy)** | **~1961** (behind) |
| **Urbanization** | **~1983** (ahead) |

**A ~22-year spread.** Urbanization has run ~22 years *ahead* of health and structure — Nigeria **built cities before jobs, health, or industry caught up**. That incoherence is itself a warning: the escapers developed these dimensions roughly *together* (industrial jobs pulled people into cities as health and skills rose); Nigeria's urbanization is running on informal services, not a rising-productivity base.

## 2. The structural anomaly — urbanizing *without* industrializing

At the **same income**, Nigeria looks structurally unlike the East-Asian escapers:

| (same ~$2.2k income) | life exp | urban % | industry % GDP | fertility |
|---|---|---|---|---|
| **Nigeria 2023** | 54 | **62** | **19** (falling) | 4.5 |
| South Korea 1970 | 62 | 41 | 25 (rising) | 4.5 |
| China 1980 | 64 | 19 | 48 (rising) | 2.7 |

Nigeria is **far more urban but far less industrial** (manufacturing only ~8–9% of GDP, and *falling*), with lower life expectancy. It is packing people into cities *without* the manufacturing ladder that carried the tigers — Rodrik's **premature deindustrialization**.

## 3. The catch-up path menu — and what separates escape from stall

From this income level, over the next ~40 years:

| Case | growth | savings | debt/GDP | exports | outcome |
|---|---|---|---|---|---|
| Japan 1960s | 10.4% | 35% | 8% | 10% | **escaped, doubled in ~8yr** |
| S. Korea 1980s | 8.6% | 34% | 18% | 32% | **escaped, doubled in ~10yr** |
| China 2005–14 | 9.5% | 49% | 34% | 30% | escaped (debt overhang the open risk) |
| US 1890s | 3.8% | 20% | 8% | 7% | escaped slowly (~40yr, internal market) |
| **Brazil 1975–80** | 6.5% | **20%** | 30% | 8% | ***STALLED 40yr+*** (low savings, weak exports, inflation/debt) |

**Escaper template:** 35–45% savings + export manufacturing + **low public debt** → double income in ~8–10 years. **Stall:** ~18–20% savings, weak export upgrading, inflation/debt crises → 40yr+ to barely double.

**Nigeria's actual trajectory is worse than the stall:** −0.2%/yr per-capita since 2010. Years to double from here — 8%/yr → 9 yrs; 3%/yr → 23 yrs; 1.5%/yr → 47 yrs; at Nigeria's recent −0.2% → **never (diverging).**

## 4. The conditioning layer — same income, different odds

The raw income parallel is **arithmetic**; the *outcome* depends on initial conditions. The 7-factor divergence scorecard (`countries_divergence_factors.csv`):

| Factor | tilt | why it differs from the escapers |
|---|---|---|
| Security / conflict | **adverse** | insurgency + banditry *concurrent* with takeoff (US/Korea/China grew *after* order was restored) |
| Institutions | **adverse** | rule-of-law −1.0, extractive corruption on weak state capacity (vs Korea's disciplined bureaucracy) |
| Resource dependence | **adverse** | oil ~88% of exports (Dutch-disease rentier trap) vs the *resource-poor* tigers forced to export |
| Human capital | **adverse** | ~18m out-of-school, 74% below basic skills (vs Korea/China near-universally schooled at takeoff) |
| Premature deindustrialization | **adverse** | manufacturing ~8–9% and falling; the escalator peaks earlier now |
| Global context | **adverse** | deglobalization + automation + climate (vs the tigers' hyper-globalization tailwind) |
| Demographics | **adverse** (latent upside) | slow fertility decline squanders the dividend — but the youth bulge + 240m market *could* flip favourable |

**Structural-readiness index: 0/100** (7/7 factors currently adverse). Crucially the adverse factors **compound** — oil rents both corrode institutions *and* crowd out manufacturing.

---

## Conditioned verdict

- **Arithmetic:** Nigeria today sits at Korea-1970 / China-1983 / US-1860s income.
- **Structural:** it lacks the escaper preconditions — urbanizing without industry, savings ~15–20% (vs 35–45%), and every conditioning factor currently adverse.
- **Odds:** the income parallel is **structurally unearned** — Nigeria's path sits far closer to the **Brazil stall than the Korea escape**, and it isn't even matching Brazil yet (per-capita income has *fallen* since 2010). Escape requires security + institutions + fertility + human capital + a manufacturing jobs-ladder to flip **together** — the same **governance** swing-factor the debt-cycle tracker already flags as the top **bear** trigger.

> The development-age lens and the debt-cycle model converge: Nigeria's constraint is not its income level (that just says "early-middle-income, like Korea-1970") — it's the **initial conditions** (security, institutions, oil, human capital, structure) that decide whether the next 40 years look like Seoul or like a stall. *"Nigeria is at Korea-1970's income, but not Korea-1970's conditions."*
