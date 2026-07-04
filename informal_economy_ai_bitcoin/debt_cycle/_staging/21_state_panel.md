# Nigeria State-Level Cross-Section Panel (36 states + FCT = 37 units)

Assembled for a spatial graph-neural-network model. Compiled 2026-06-30.
ACCURACY NOTE: Values are filled only where reliably sourced. Blank = not reliably
sourced (NOT guessed). Each column's source + year is documented in the SOURCES
section below. The most authoritative/complete columns are **zone**, **population_m**,
**mpi_headcount_pct**, **igr_ngn_bn (2024)**, and **poverty_rate_pct (WB 2018/19)**.

--------------------------------------------------------------------------------
## 1. MAIN CSV-READY TABLE
--------------------------------------------------------------------------------

Columns: state, zone, population_m, mpi_headcount_pct, igr_ngn_bn, acled_fatalities_2024, poverty_rate_pct

```csv
state,zone,population_m,mpi_headcount_pct,igr_ngn_bn,acled_fatalities_2024,poverty_rate_pct
Abia,South-East,4.84,29.8,40.01,,5.0
Adamawa,North-East,5.24,54.9,20.30,,63.7
Akwa Ibom,South-South,5.78,51.0,75.77,,18.4
Anambra,South-East,7.30,32.1,42.69,,8.8
Bauchi,North-East,7.54,73.9,32.43,,49.7
Bayelsa,South-South,2.39,88.5,64.01,,13.3
Benue,North-Central,6.69,75.0,20.43,,41.6
Borno,North-East,6.65,72.5,27.80,2143,
Cross River,South-South,4.18,75.4,47.02,,25.4
Delta,South-South,6.11,31.1,157.79,,2.9
Ebonyi,South-East,4.01,78.0,13.18,,19.3
Edo,South-South,5.53,35.4,91.15,,8.8
Ekiti,South-West,3.40,36.0,35.21,,26.1
Enugu,South-East,5.40,31.6,180.50,,6.7
FCT,North-Central,4.80,40.4,282.36,,11.7
Gombe,North-East,4.62,86.2,20.72,,47.3
Imo,South-East,6.07,40.7,25.27,,1.3
Jigawa,North-West,6.98,84.3,59.46,,78.8
Kaduna,North-West,8.32,73.9,71.57,813,37.3
Kano,North-West,16.25,66.3,74.77,,40.9
Katsina,North-West,9.30,72.7,39.15,1306,55.3
Kebbi,North-West,6.00,82.2,16.97,,38.9
Kogi,North-Central,5.05,61.3,32.01,,39.9
Kwara,North-Central,4.26,48.3,71.20,,19.6
Lagos,South-West,15.77,29.4,1261.56,,3.8
Nasarawa,North-Central,3.63,60.7,25.52,,44.2
Niger,North-Central,6.72,69.1,34.66,,72.8
Ogun,South-West,6.45,68.1,194.93,,17.7
Ondo,South-West,5.65,27.2,31.25,,21.5
Osun,South-West,4.24,40.7,54.77,,16.2
Oyo,South-West,7.51,48.7,65.29,,5.5
Plateau,North-Central,5.40,84.0,31.14,,43.3
Rivers,South-South,7.23,62.4,317.30,,15.7
Sokoto,North-West,6.16,90.5,20.85,,79.9
Taraba,North-East,4.33,79.4,17.46,,80.4
Yobe,North-East,4.35,83.5,11.08,,59.0
Zamfara,North-West,5.52,78.0,25.46,1347,62.0
```

Notes on specific cells:
- **Ondo population (5.65)** is a 2006-census projection estimate (NBS Wikipedia table
  omitted Ondo); flag as approximate. All other populations are the NBS 2023 projection.
- **Borno poverty_rate_pct blank**: World Bank 2018/19 NLSS excluded Borno (insecurity /
  no survey coverage). Borno's MPI (72.5%) and IGR are available.
- **acled_fatalities_2024**: only the four highest-fatality states could be sourced to
  exact published ACLED 2024 figures (Borno 2,143; Zamfara 1,347; Katsina 1,306;
  Kaduna 813). A full 37-state ACLED export was not obtainable via web; use the
  fragility_tier proxy (Section 3) for the remaining states, or pull the ACLED Data
  Export Tool directly for exact per-state counts.

--------------------------------------------------------------------------------
## 2. PER-COLUMN SOURCES + YEAR
--------------------------------------------------------------------------------

| Column | Source | Year | Coverage | Confidence |
|---|---|---|---|---|
| zone | Standard Nigeria 6 geopolitical zones (constitutional/NBS grouping) | n/a | 37/37 | Definitive |
| population_m | NBS 2023 population projection (2006 census base), via Wikipedia "List of Nigerian states by population" reproducing NBS | 2023 | 37/37 (Ondo est.) | High |
| mpi_headcount_pct | NBS / NBS-UNDP-OPHI Nigeria Multidimensional Poverty Index 2022 (incidence H, % multidimensionally poor) | 2022 | 37/37 | High |
| igr_ngn_bn | NBS "Internally Generated Revenue at State Level" 2024 report (released Oct 2025), ₦ billion | 2024 | 37/37 | High (official) |
| acled_fatalities_2024 | ACLED 2024 Conflict Index / Nigeria 2024 data (political-violence fatalities, Dec 2023–Nov 2024) | 2024 | 4/37 exact | High for the 4; rest blank |
| poverty_rate_pct | World Bank monetary poverty headcount at $2.15/day (2017 PPP), NLSS 2018/19 small-area estimates | 2018/19 | 36/37 (Borno excl.) | High |

Source URLs:
- NBS MPI 2022: https://www.nigerianstat.gov.ng/pdfuploads/NIGERIA%20MULTIDIMENSIONAL%20POVERTY%20INDEX%20SURVEY%20RESULTS%202022.pdf ; OPHI https://ophi.org.uk/publications/Nigeria-MPI-2022 ; ranked list cross-checked via TheCable/ournigerianews/Punch.
- NBS IGR 2024: https://www.nigerianstat.gov.ng/ (IGR at State Level); breakdown via Nairametrics https://nairametrics.com/2025/10/07/lagos-rivers-fct-lead-nigerias-n3-63-trillion-igr-in-2024/ , Leadership, Channels TV (NBS release, 7 Oct 2025). National total ₦3.63tn.
- NBS IGR 2023 (alt year): ₦2.43tn total; https://www.nigerianstat.gov.ng/elibrary/read/1241579 (top: Lagos 815.86, FCT 211.10, Rivers 195.41, Ogun 146.88, Delta 114.09; bottom: Taraba 10.87, Yobe 11.19, Kebbi 11.74). 2024 used as the primary column (more recent + complete).
- Population: https://en.wikipedia.org/wiki/List_of_Nigerian_states_by_population (NBS projection) ; citypopulation.de.
- World Bank monetary poverty by state: https://en.wikipedia.org/wiki/List_of_Nigerian_states_by_poverty_rate (WB Nigeria Poverty Assessment 2022, NLSS 2018/19; $3.65 and $6.85 lines also available there — see Section 5).
- ACLED 2024: https://acleddata.com/infographic/nigeria-2024-conflict-index-infographic ; https://acleddata.com/country/nigeria .

--------------------------------------------------------------------------------
## 3. FRAGILITY PROXY (for ACLED gaps) + auxiliary flags
--------------------------------------------------------------------------------

Analyst-assigned fragility tier derived from ACLED 2024 documented patterns
(86% of national political-violence fatalities occurred in the North in 2024:
North-West 41%, North-East 25.9%, North-Central 19.3%, South 13.8%). Use as a
proxy node feature where exact ACLED counts are blank. NOT a precise count.

```csv
state,fragility_tier,food_insecurity_flag
Borno,High,Y
Zamfara,High,Y
Katsina,High,Y
Kaduna,High,Y
Sokoto,High,Y
Niger,High,Y
Benue,High,Y
Plateau,High,Y
Taraba,High,Y
Adamawa,High,Y
Yobe,High,Y
Kebbi,Medium,Y
Bauchi,Medium,Y
Gombe,Medium,Y
Jigawa,Medium,Y
Kano,Medium,
Nasarawa,Medium,
Kogi,Medium,
Enugu,Medium,
Ebonyi,Medium,
Anambra,Medium,
Imo,Medium,
Rivers,Medium,
Delta,Medium,
Edo,Medium,
Cross River,Medium,
Ondo,Medium,
Abia,Low,
Akwa Ibom,Low,
Bayelsa,Low,
Lagos,Low,
Ogun,Low,
Oyo,Low,
Osun,Low,
Ekiti,Low,
Kwara,Low,
FCT,Low,
```
food_insecurity_flag = states repeatedly flagged in Cadre Harmonisé (NE/NW/NC
crisis belt). Proxy/qualitative — treat as analyst flag, not an NBS statistic.
State-level unemployment is NOT published by NBS (NLFS reports nationally only),
so a per-state unemployment column is left out rather than guessed.

--------------------------------------------------------------------------------
## 4. GEOGRAPHIC ADJACENCY (real land borders) — undirected edge list
--------------------------------------------------------------------------------

Each line: STATE: neighbours (domestic land borders only; international borders
with Niger/Chad/Cameroon/Benin omitted). Use for building the spatial graph.

```
Abia: Imo, Anambra, Enugu, Ebonyi, Cross River, Akwa Ibom, Rivers
Adamawa: Borno, Gombe, Taraba
Akwa Ibom: Cross River, Abia, Rivers
Anambra: Delta, Imo, Rivers, Enugu, Kogi
Bauchi: Kano, Jigawa, Yobe, Gombe, Taraba, Plateau, Kaduna
Bayelsa: Rivers, Delta
Benue: Nasarawa, Taraba, Cross River, Ebonyi, Enugu, Kogi
Borno: Yobe, Gombe, Adamawa
Cross River: Benue, Ebonyi, Abia, Akwa Ibom
Delta: Edo, Ondo, Anambra, Rivers, Bayelsa
Ebonyi: Benue, Cross River, Abia, Enugu
Edo: Kogi, Anambra, Delta, Ondo
Ekiti: Kwara, Kogi, Ondo, Osun
Enugu: Kogi, Benue, Ebonyi, Abia, Imo, Anambra
FCT: Niger, Kaduna, Nasarawa, Kogi
Gombe: Borno, Yobe, Bauchi, Taraba, Adamawa
Imo: Anambra, Abia, Rivers
Jigawa: Kano, Katsina, Bauchi, Yobe
Kaduna: Katsina, Kano, Bauchi, Plateau, Nasarawa, FCT, Niger, Zamfara
Kano: Jigawa, Katsina, Kaduna, Bauchi
Katsina: Kano, Jigawa, Kaduna, Zamfara
Kebbi: Sokoto, Zamfara, Niger
Kogi: Kwara, Niger, FCT, Nasarawa, Benue, Enugu, Anambra, Edo, Ondo, Ekiti
Kwara: Niger, Kogi, Ekiti, Osun, Oyo
Lagos: Ogun
Nasarawa: Kaduna, FCT, Kogi, Benue, Taraba, Plateau
Niger: Kebbi, Zamfara, Kaduna, FCT, Kogi, Kwara
Ogun: Lagos, Oyo, Osun, Ondo
Ondo: Ekiti, Kogi, Edo, Delta, Ogun, Osun
Osun: Oyo, Kwara, Ekiti, Ogun, Ondo
Oyo: Kwara, Osun, Ogun
Plateau: Bauchi, Kaduna, Nasarawa, Taraba
Rivers: Bayelsa, Delta, Imo, Abia, Akwa Ibom, Anambra
Sokoto: Kebbi, Zamfara
Taraba: Adamawa, Gombe, Bauchi, Plateau, Nasarawa, Benue
Yobe: Borno, Gombe, Bauchi, Jigawa
Zamfara: Sokoto, Kebbi, Niger, Kaduna, Katsina
```

Note: treat as undirected — symmetrise before training (if A lists B, add B–A).
Lagos has only one domestic neighbour (Ogun); the rest of its border is the
Atlantic + Benin Republic. Bayelsa connects only to Rivers and Delta.

### Zone grouping (fallback / additional graph layer)
- North-Central: Benue, Kogi, Kwara, Nasarawa, Niger, Plateau, FCT
- North-East: Adamawa, Bauchi, Borno, Gombe, Taraba, Yobe
- North-West: Jigawa, Kaduna, Kano, Katsina, Kebbi, Sokoto, Zamfara
- South-East: Abia, Anambra, Ebonyi, Enugu, Imo
- South-South: Akwa Ibom, Bayelsa, Cross River, Delta, Edo, Rivers
- South-West: Ekiti, Lagos, Ogun, Ondo, Osun, Oyo

--------------------------------------------------------------------------------
## 5. OPTIONAL EXTRA POVERTY LINES (WB 2018/19, % of population)
--------------------------------------------------------------------------------

Higher poverty lines from the same World Bank source — useful as alternative
monetary-poverty node features. (Borno excluded by source.)

```csv
state,wb_215_pct,wb_365_pct,wb_685_pct
Taraba,80.4,95.8,99.3
Sokoto,79.9,95.7,99.2
Jigawa,78.8,95.7,99.5
Niger,72.8,92.9,99.4
Adamawa,63.7,92.7,99.1
Zamfara,62.0,93.2,99.3
Yobe,59.0,92.2,99.2
Katsina,55.3,86.9,98.7
Bauchi,49.7,88.5,99.0
Gombe,47.3,84.1,96.5
Nasarawa,44.2,83.5,98.4
Plateau,43.3,75.8,94.3
Benue,41.6,85.8,98.5
Kano,40.9,79.3,96.6
Kogi,39.9,85.8,98.6
Kebbi,38.9,76.7,96.5
Kaduna,37.3,68.6,91.6
Ekiti,26.1,63.0,92.8
Cross River,25.4,66.9,93.5
Ondo,21.5,59.2,92.0
Kwara,19.6,66.8,95.6
Ebonyi,19.3,58.5,94.2
Akwa Ibom,18.4,55.4,88.6
Ogun,17.7,54.4,89.8
Osun,16.2,64.9,95.0
Rivers,15.7,48.0,85.6
Bayelsa,13.3,52.7,89.2
FCT,11.7,56.0,93.4
Anambra,8.8,47.2,90.8
Edo,8.8,35.3,83.5
Enugu,6.7,41.9,89.2
Oyo,5.5,33.0,78.3
Abia,5.0,30.3,81.2
Lagos,3.8,36.3,86.0
Delta,2.9,25.5,72.1
Imo,1.3,15.5,66.7
```
National averages: 30.9% ($2.15), 63.5% ($3.65), 95.0% ($6.85).

--------------------------------------------------------------------------------
## 6. KEY GAPS / TODO
--------------------------------------------------------------------------------
- ACLED exact fatalities for 33 states (only 4 sourced precisely) → pull ACLED Data
  Export Tool (acleddata.com) for full 2024/2025 per-admin1 counts.
- State real GDP / IGGDP: left out entirely — only a handful of states (e.g. Lagos,
  Ekiti, Ondo) have ever published state GDP and no consistent 37-state series exists.
- State-level unemployment: not published by NBS (national NLFS only).
- Ondo population is a projection estimate (NBS table row was missing in source).
- 2023 IGR available as an alternative year if a non-2024 series is preferred.
```
