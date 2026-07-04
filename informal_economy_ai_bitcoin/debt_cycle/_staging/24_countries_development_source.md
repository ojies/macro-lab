# 24 — Cross-Country Development-Trajectory Indicators (11 countries)

**Deliverable:** `../countries_development_indicators.csv` (long format, one row per country-year)
**Built:** 2026-07-04
**Purpose:** Composite "development index" inputs + structural/demographic path comparison at equivalent development stages.

## Countries (11)
United States (USA), United Kingdom (GBR), Germany (DEU), Japan (JPN), South Korea (KOR),
China (CHN), India (IND), Brazil (BRA), Indonesia (IDN), Vietnam (VNM), Nigeria (NGA).

## Benchmark years
1900, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2023.
(1900 rows written only where any value exists — UK & Japan life-expectancy only. 1900 dropped for all others.)

## Indicators, sources & WB codes

| Column | Indicator | Primary source | Code / dataset |
|---|---|---|---|
| life_expectancy | Life expectancy at birth (yrs) | World Bank WDI (1960-2023); OWID for 1900 & 1950 | `SP.DYN.LE00.IN` / OWID `life-expectancy` |
| urban_pct | Urban population (% of total) | World Bank WDI (1960-2023); OWID for 1950 | `SP.URB.TOTL.IN.ZS` / OWID `share-of-population-urban` |
| agriculture_pct_gdp | Agriculture, forestry & fishing value added (% GDP) | World Bank WDI | `NV.AGR.TOTL.ZS` |
| industry_pct_gdp | Industry (incl. construction) value added (% GDP) | World Bank WDI | `NV.IND.TOTL.ZS` |
| services_pct_gdp | Services value added (% GDP) | World Bank WDI | `NV.SRV.TOTL.ZS` |
| fertility_rate | Total fertility rate (births/woman) | World Bank WDI | `SP.DYN.TFRT.IN` |
| median_age | Median age (years) | UN World Population Prospects 2024, via OWID | OWID `median-age` (variant = estimates) |

## URLs / API calls (all [SOURCED], fetched 2026-07-04; WB lastupdated 2026-07-01)

World Bank (one call per indicator, all 11 countries at once):
```
https://api.worldbank.org/v2/country/NGA;USA;GBR;DEU;JPN;KOR;CHN;IND;BRA;IDN;VNM/indicator/<CODE>?format=json&per_page=20000&date=1960:2023
```
CODEs: SP.DYN.LE00.IN, SP.URB.TOTL.IN.ZS, NV.AGR.TOTL.ZS, NV.IND.TOTL.ZS, NV.SRV.TOTL.ZS, SP.DYN.TFRT.IN

Our World in Data (full CSV downloads):
- Median age (UN WPP 2024): `https://ourworldindata.org/grapher/median-age.csv?csvType=full&useColumnShortNames=true`
- Historical life expectancy: `https://ourworldindata.org/grapher/life-expectancy.csv?csvType=full&useColumnShortNames=true`
- Historical urban share: `https://ourworldindata.org/grapher/share-of-population-urban.csv?csvType=full&useColumnShortNames=true`

## Coverage
- **Rows written:** 102 country-years.
- **Overall cell fill:** 577 / 714 = **80.8%** of value cells populated.
- Per field (count of values across all country-years):
  - life_expectancy: 102 (full — every row) [SOURCED]
  - urban_pct: 99 [SOURCED]
  - median_age: 99 (1950-2023 for all 11; no 1900) [SOURCED, UN WPP]
  - fertility_rate: 88 (1960-2023 full for all 11) [SOURCED]
  - agriculture / industry / services: 63 each [SOURCED]

## Known gaps (all genuine source absences — left BLANK, none estimated)
1. **Sector value-added (agri/ind/serv), early years for high-income countries.** WB WDI series start dates (SNA methodology): USA 1997, Japan 1994, Germany 1991, UK 1990. So 1960-1990 sector cells are blank for USA/GBR/JPN, and 1960-1990 for DEU. Emerging markets that also start late: Indonesia 1983, Vietnam 1986, Nigeria 1981. → Nigeria/Indonesia/Vietnam sectors blank 1960-1980; KOR/CHN/IND/BRA have full 1960-2023.
2. **USA sector 2023:** WB reports no 2023 (or 2022) value-added split for the US yet (latest US = 2021). Blank.
3. **1900 row:** OWID historical life-expectancy has 1900 only for Brazil(29.0), Japan(38.6), UK(45.62). No 1900 urbanization or median age for any of the 11. All other 1900 rows omitted entirely.
4. **1950 sectors & fertility:** WB series begin 1960, so 1950 has only life_expectancy, urban_pct, median_age (from OWID/UN). Blank otherwise.

## Data-quality notes
- **Germany (DEU):** WB pre-1990 series are sparse; reunified-Germany basis from 1991. Life expectancy/urban from 1960 reflect WB's DEU aggregate.
- **China 1960 life expectancy = 33.4 yrs** — correctly reflects the Great Leap Forward famine trough (not an error).
- All numeric values rounded: life-exp / urban / sectors / fertility to 2 dp, median_age to 1 dp.
- No interpolation, no estimation. Every populated cell is directly sourced. Flags: all [SOURCED]; zero [ESTIMATED].

## Reproduce
Script: fetch 6 WB JSONs via curl + 3 OWID CSVs; parse & join on (ISO3, year) filtered to benchmark years; write long CSV. (See scratchpad `build.py`.)
