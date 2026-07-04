# 23 — Cross-Country Real GDP per Capita (PPP), Long-Run "Development-Age" Axis

**Deliverable:** `../countries_gdp_pc_ppp.csv` (long format: `country, year, gdp_pc_ppp`)
**Built:** 2026-07-04

---

## 1. Source, release, and price base

- **Source:** Maddison Project Database (MPD) **2023 release** — Bolt, J. and van Zanden, J.L. (2024),
  *"Maddison style estimates of the evolution of the world economy: A new 2023 update"*, Journal of Economic Surveys, 1–41.
- **Series used:** `gdppc` — real GDP per capita, the multiple-benchmark composite series designed for cross-country *and* over-time comparison.
- **PRICE BASE — STATE EXPLICITLY:** **international dollars at 2011 prices (2011 int'l $, PPP-adjusted).**
  MPD 2023 splices 1990 PPPs (used through 1990) onto 2011 PPPs (used from 2011 onward), with the intervening years
  adjusted to connect the two benchmarks smoothly. Every value in the CSV is on this single 2011-int'l-$ base.
- **Access route:** Our World in Data grapher CSV mirror of MPD 2023 (clean, faithful reproduction of the `gdppc` series).
  Confirmed release = 2023 and unit = "international-$ in 2011 prices" from the OWID variable metadata.

### URLs
- Data CSV: https://ourworldindata.org/grapher/gdp-per-capita-maddison.csv
- Variable metadata (release + unit confirmation): https://ourworldindata.org/grapher/gdp-per-capita-maddison.metadata.json
- Original database (Groningen / GGDC): https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2023
- OWID chart page: https://ourworldindata.org/grapher/gdp-per-capita-maddison-project-database
- World Bank cross-check API (Nigeria): https://api.worldbank.org/v2/country/NGA/indicator/NY.GDP.PCAP.PP.KD?date=2020:2022&format=json
- World Bank cross-check API (multi-country): https://api.worldbank.org/v2/country/NGA;USA;CHN;KOR/indicator/NY.GDP.PCAP.PP.KD?format=json

---

## 2. ⚠️ DO NOT MIX BASES

Maddison PPP (2011 int'l $) is **NOT** interchangeable with World Bank / IMF PPP (currently a 2021-int'l-$ base
built on the 2021 ICP round). They differ by both PPP benchmark year and methodology. Illustration for the *same*
country and year (Nigeria, 2022):

| Series | Base | Nigeria 2022 GDP p.c. (PPP) |
|---|---|---|
| **Maddison 2023 (used in CSV)** | 2011 int'l $ | **$2,207** |
| World Bank WDI (`NY.GDP.PCAP.PP.KD`) | 2021 int'l $ | ~$7,752 |

The ~3.5× gap is base/methodology, not real-income change. **The CSV column is 100% Maddison 2011-int'l-$.**
World Bank figures above are for context only and are NOT in the deliverable.

---

## 3. Per-country coverage (benchmark years, all [SOURCED] from MPD 2023)

Benchmark years requested: 1820, 1870, 1900, 1913, 1929, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2022.
MPD 2023 returns a value for **all 11 countries in all 15 benchmark years** — the 2023 update back-projected
late-starting countries, so none are blank.

| Country | Coverage in CSV | Flag / confidence note |
|---|---|---|
| United States | 1820–2022, all years | [SOURCED], high confidence throughout |
| United Kingdom | 1820–2022, all years | [SOURCED], high confidence throughout |
| Germany | 1820–2022, all years | [SOURCED]. 1950 = 3,881 reflects post-WWII trough (within-borders) |
| Japan | 1820–2022, all years | [SOURCED]. 1950 = 1,921 reflects post-war trough |
| South Korea | 1820–2022, all years | [SOURCED]. **Pre-1911 values are MPD conjectural back-projections — low confidence** |
| China | 1820–2022, all years | [SOURCED], reasonable confidence; pre-1950 sparse/conjectural |
| India | 1820–2022, all years | [SOURCED], reasonable confidence |
| Brazil | 1820–2022, all years | [SOURCED] |
| Indonesia | 1820–2022, all years | [SOURCED] |
| Vietnam | 1820–2022, all years | [SOURCED]. **Pre-1950 values are MPD conjectural back-projections — low confidence** |
| Nigeria | 1820–2022, all years | [SOURCED]. **Pre-1950 values are MPD conjectural/colonial-era estimates — low confidence** |

**Provenance flag:** Nothing in the CSV is [ESTIMATED] by this analyst — every cell is [SOURCED] directly
from MPD 2023. However, MPD's own **pre-1950 estimates for Nigeria, South Korea and Vietnam are conjectural
back-projections** (the original user brief expected these to be blank). They are retained because they are
genuine database values, but should be treated as low-confidence and NOT over-interpreted. The
industrial-era figures (1950→2022) that drive the crossover analysis below are high/medium confidence.

---

## 4. HEADLINE — Nigeria's frontier-equivalent ("development-age") years

**Nigeria's most recent Maddison value: 2022 = $2,207 (2011 int'l $).**
(2010 = $2,269 was Nigeria's Maddison peak; the level has drifted *down* since — a lost decade.)

Using the **same MPD 2023 series and 2011-int'l-$ base**, the calendar year each frontier economy last stood at
Nigeria's current ~$2,207 level (linear interpolation between bracketing benchmark years):

| Frontier country | Bracketing benchmarks | **Frontier-equivalent year for Nigeria-2022** |
|---|---|---|
| **United States** | 1820 ($1,287) → 1870 ($2,445) | **≈ 1860** |
| **United Kingdom** | already above by 1820 ($2,126) → 1870 ($4,131) | **≈ 1822** (early 1820s) |
| **Germany** | 1820 ($1,528) → 1870 ($2,428) | **≈ 1858** |
| **Japan** | 1913 ($1,889) → 1929 ($2,857) | **≈ 1918** |
| **South Korea** | 1970 = $2,208 (near-exact match) | **≈ 1970** |
| **China** | 1980 ($1,930) → 1990 ($2,982) | **≈ 1983** |

**One-line headline:** *Nigeria today (2022, ≈ $2,207 in 2011 int'l $) sits where the US was around 1860,
the UK in the early 1820s, Germany around 1858, Japan around 1918, South Korea in 1970, and China in 1983.*

The tightest and most striking anchor: **South Korea in 1970 had essentially the identical level ($2,208)** —
Korea then multiplied that ~15× in 52 years. That is the "development-age gap" the module is built around.

---

## 5. Cross-checks performed

- **Release/base confirmation:** OWID variable metadata explicitly returns source = "Maddison Project Database 2023"
  and unit = "international-$ in 2011 prices". Matches the GGDC 2023 release page (169 countries, through 2022).
- **World Bank PPP sanity check (recent years):** WB `NY.GDP.PCAP.PP.KD` (2021 int'l $) — Nigeria 2020/2021/2022 =
  $7,664 / $7,588 / $7,752. Directionally consistent with Maddison (flat-to-declining post-2019) but on a higher
  base; used ONLY to confirm the trend and to document the base gap, not merged into the CSV.
- **Internal consistency:** Korea 1970 ($2,208) independently corroborates the Nigeria-2022 crossover; US/UK/Germany
  1820–1870 slopes are the well-known Maddison frontier values.
