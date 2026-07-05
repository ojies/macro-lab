# 35 — Vital Rates & Population Trajectories (12 countries)

**Deliverable:** `../demographics.csv` (one row per country, latest available ~2023–2024)
**Built:** 2026-07-05
**Purpose:** Model which countries are in natural population decline ("dying off" from low birth rates) vs still growing. Distinguish natural decrease (deaths > births, already happening) from below-replacement fertility (shrinkage once age-structure momentum fades) and from total population change (which adds/subtracts net migration).

## Countries (12)
Japan, South Korea, China, Italy, Germany, United States, United Kingdom, Nigeria, India, Brazil, Indonesia, Vietnam.

## The "dying off" framing
- **TFR < 2.1 (replacement)** → the birth cohort is smaller than the parent cohort. Population will eventually shrink once the current age-structure "momentum" (a still-large number of women of childbearing age) fades. ELEVEN of the 12 are below replacement; only Nigeria (4.48) is above.
- **birth_to_death_ratio < 1.0** (equivalently natural_increase < 0) → deaths already exceed births. The country is ALREADY in natural decrease. This is happening NOW in Italy, Japan, Germany, China, South Korea.
- **annual_pop_growth_pct** = natural change + net migration. A country can be in natural decrease yet still grow if migration more than offsets it (South Korea +0.40% in 2023 despite deaths>births), or shrink faster than its natural rate if it also loses migrants.

## Column definitions & sources

| Column | Definition | Primary source | Flag |
|---|---|---|---|
| total_fertility_rate | Births per woman, 2023 | World Bank WDI `SP.DYN.TFRT.IN` (Italy cross-checked to Istat 2023 = 1.20) | [SOURCED] |
| crude_birth_rate | Births per 1,000 pop, 2023 | UN WPP 2024 via OWID grapher `crude-birth-rate` | [SOURCED] |
| crude_death_rate | Deaths per 1,000 pop, 2023 | UN WPP 2024 via OWID grapher `crude-death-rate` | [SOURCED] |
| natural_increase_per_1000 | crude_birth_rate − crude_death_rate | Derived | [DERIVED] |
| birth_to_death_ratio | crude_birth_rate ÷ crude_death_rate | Derived | [DERIVED] |
| median_age_years | Median age, 2023 | UN WPP 2024 via OWID grapher `median-age` | [SOURCED] |
| old_age_dependency_pct | Pop 65+ per 100 aged 15–64, 2023 | UN WPP 2024 via OWID grapher `age-dependency-ratio-old` | [SOURCED] |
| pop_millions_2024 | Total population ~mid-2024 | UN WPP 2024 (mid-2023 estimate carried on 2023→2025 trajectory) | [SOURCED] |
| pop_peak_year | Year population peaked / is projected to peak | UN WPP 2024 + national offices | [SOURCED] historical / [ESTIMATED] future |
| pop_millions_2050 | UN medium-variant projection | UN WPP 2024 medium | [SOURCED] |
| pop_millions_2100 | UN medium-variant projection | UN WPP 2024 medium | [SOURCED] |
| annual_pop_growth_pct | Annual population growth %, 2023 | UN WPP 2024 via OWID grapher `population-growth-rate` | [SOURCED] |

All vital-rate columns (CBR, CDR, median age, old-age dependency, growth) are from a single consistent framework — **UN World Population Prospects 2024** — so they are internally comparable. Note UN WPP model values differ slightly from national civil-registration counts (e.g. Japan's registered CDR ~13 vs WPP 6.9/11.7 birth/death); WPP is used throughout for cross-country consistency.

## Source URLs (fetched 2026-07-05)
- OWID / UN WPP 2024 graphers (CSV, `?csvType=full&useColumnShortNames=true`):
  `crude-birth-rate`, `crude-death-rate`, `median-age`, `age-dependency-ratio-old`, `population-growth-rate`, `population-with-un-projections`.
- World Bank WDI `SP.DYN.TFRT.IN` (TFR 2023), already staged in `../countries_development_indicators.csv` (doc 24).
- UN WPP 2024 Summary of Results: https://population.un.org/wpp/ ; OWID digest: https://ourworldindata.org/un-population-2024-revision
- Cross-checks for 2050/2100 medium projections: populationpyramids.org (UN WPP 2024), Wikipedia "Human population projections" (WPP 2024 table). Istat (Italy TFR/peak), Statistics Korea, Japan Statistics Bureau for national peaks.

## Data-quality notes & judgement calls
1. **Projection extraction.** The OWID `population-with-un-projections` CSV filter behaved unreliably through the CDN (intermittently served the full unfiltered file). Clean, precise cell reads were obtained for Japan (2100), Italy, Germany, Brazil, Indonesia; the remaining countries' 2050/2100 were reconciled across ≥2 UN WPP 2024 sources. Where sources disagreed, the value consistent with the WPP2022→WPP2024 revision DIRECTION was chosen (WPP2024 revised Italy/Germany/US/UK UP on migration, and China/Indonesia/Nigeria DOWN on lower fertility).
2. **Nigeria revised down.** WPP2024 medium for Nigeria = 359M (2050) / **477M** (2100) — a large downward revision from WPP2022 (377M / 546M) and WPP2012 (914M). The task's "~375m (2050) / 500m+ (2100)" anchor reflects the older revision; the 2024-revision figures are used here. Nigeria's 2024 population is genuinely uncertain (no recent census); WPP2024 puts it ~232.7M (World Bank ~227M for 2023).
3. **China 2050 = 1,313M** (UN: "1.426bn → 1.313bn by 2050"), 2100 = 633M (medium; low-fertility variant is far lower, ~630–770M is the medium-to-optimistic band cited in the brief).
4. **Peak years:** historical peaks are sourced (Japan 2008 national census 128.08M / UN ~2010; South Korea 2020 ~51.8M; China 2021 ~1,426M; Italy 2014 Istat 60.79M; Germany ~2023, migration-propped). US and Nigeria are still growing at 2100 (peak >2100). UK/India/Brazil/Indonesia/Vietnam peak mid-century then decline — those peak years are [ESTIMATED] (±5 yr) from the medium-variant trajectory.
5. TFR and median age are 2023; population and growth are 2023–2024. Rounding: rates to 1 dp, ratio to 2 dp, populations to 0.1M (China/India to 1M).

## Ranking — fastest natural SHRINKAGE → fastest natural GROWTH (by natural_increase_per_1000)

| Rank | Country | Nat. incr. /1000 | Birth:Death | TFR | Total growth % | Status |
|---|---|---|---|---|---|---|
| 1 | Italy | −6.4 | 0.50 | 1.20 | −0.27 | Natural decrease (deaths ≈ 2× births) |
| 2 | Japan | −4.7 | 0.59 | 1.20 | −0.63 | Natural decrease since ~2007; fastest TOTAL decline |
| 3 | Germany | −3.4 | 0.71 | 1.39 | −0.13 | Natural decrease, propped by migration |
| 4 | China | −2.0 | 0.76 | 1.00 | −0.08 | Peaked 2021; now shrinking |
| 5 | South Korea | −1.8 | 0.72 | 0.72 | +0.40 | Natural decrease since ~2020, but total pop still +0.4% (migration) |
| — | — | — | — | — | — | replacement line (ratio = 1.0) |
| 6 | United Kingdom | +1.6 | 1.17 | 1.56 | +0.64 | Near-flat natural change; growth is migration |
| 7 | United States | +2.8 | 1.33 | 1.62 | +0.49 | Modest natural surplus + migration |
| 8 | Brazil | +5.2 | 1.74 | 1.62 | +0.72 | Below replacement; momentum only, peak ~2048 |
| 9 | Indonesia | +9.7 | 2.41 | 2.13 | +0.76 | ~At replacement; still growing to ~2055 |
| 10 | Vietnam | +9.8 | 2.64 | 1.91 | +0.61 | Below replacement; momentum, peak ~2054 |
| 11 | India | +10.8 | 2.47 | 1.98 | +0.81 | Just below replacement; peak ~2061 at ~1.7bn |
| 12 | Nigeria | +28.4 | 3.31 | 4.48 | +2.54 | Above replacement; births >3× deaths; grows past 2100 |

### Key nuance — current rate vs future momentum
The natural-decrease RATE (per 1,000) is currently steepest in **Italy/Japan/Germany** because they are the oldest (median age 45–49, old-age dependency 37–53%), so their death rates are already high. **South Korea's** natural decrease looks mild today (−1.8) only because its population is not yet as old (median 44.5, dependency 24). But Korea's **TFR of 0.72 is the world's lowest** — roughly one-third of replacement — so its future collapse is the most extreme of all: UN WPP medium takes Korea from 51.7M (2024) to **21.8M by 2100 (−58%)**, a halving-plus within one long lifetime. Low TFR is the leading indicator; natural decrease is the lagging one.

## The demographic pivot (North/East → South)
- **Already dying off (birth < death):** Italy, Japan, Germany, China, South Korea — the aging industrial North and East Asia.
- **Below replacement, shrinking soon (momentum masking decline):** US, UK, Brazil, Vietnam, India, Indonesia — all sub-2.1 TFR; India already at 1.98 and will peak ~2061.
- **Still growing strongly:** Nigeria (and Sub-Saharan Africa broadly) — the only country here above replacement, adding people through and beyond 2100.
- Net effect 2024→2100 (medium): East Asia and Southern Europe roughly HALVE (Korea −58%, China −55%, Japan −40%, Italy −29%), while Nigeria roughly DOUBLES (+105%). The weight of humanity shifts from the aging North/East to the young South — a pivot from Asia/Europe toward Africa.
