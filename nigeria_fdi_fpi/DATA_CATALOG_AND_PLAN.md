# Data Catalog & Expansion Plan (A = fetched, B = derived)

This documents every variable family we set out to add, why it matters for an FDI/FPI
study, its source, and where it lands in the dataset. Status legend:
✅ done · 🔄 in progress (research agent running) · ⚠️ partial / unavailable.

---

## A. New data fetched

### A1. Investment-specific
| Item | Why it matters | Source | Status / file |
|---|---|---|---|
| FDI/FPI by sector & by country — full historical | Composition & origin of flows the headline misses | NBS Excel back-series 2013→ | ✅ `nbs_capital_importation_by_sector_annual.csv`, `..._by_country_annual.csv` (2013–2025) |
| Greenfield FDI projects & cross-border M&A | Captures investment *intent* the BoP omits | UNCTAD WIR 2025 annex (fDi Markets) | ✅ `nigeria_greenfield_manda.csv` (2003–2024) |
| FDI inward/outward stock & income (returns) | FDI profitability & repatriation | UNCTAD (stock) / IMF | ✅ stock in FDI file, outflows in external file; ⚠️ income not published per-country by UNCTAD — derive from IMF/CBN |
| Net errors & omissions (capital-flight proxy) | Unrecorded flows | World Bank BoP | ✅ `external_markets` file |

### A2. Markets & monetary (pull factors)
| Item | Source | Status / file |
|---|---|---|
| NGX All-Share Index, market cap | NGX / CBN | ✅ `nigeria_markets_monetary.csv` (2000–2025) |
| CBN MPR, T-bill yields | CBN Statistical Bulletin / DMO | ✅ same |
| External reserves | World Bank `FI.RES.TOTL.CD` + CBN | ✅ `external_markets` + markets file |
| Market cap (% GDP), stocks traded | World Bank `CM.MKT.*` | ✅ `external_markets` file |
| Eurobond yield + EMBI-proxy spread; S&P/Moody's/Fitch ratings | DMO / FRED / agencies | ✅ same (EMBI: proxy only — official paywalled) |

### A3. Global push factors
| Item | Source | Status / file |
|---|---|---|
| US Fed funds rate | FRED `FEDFUNDS` | ✅ `nigeria_global_push_factors.csv` |
| VIX (risk appetite) | FRED `VIXCLS` | ✅ same |
| Brent crude oil price | FRED `DCOILBRENTEU` | ✅ same |
| US 10-yr Treasury yield | FRED `DGS10` | ✅ same |
| Global FDI total | World Bank `BX.KLT.DINV.CD.WD` (WLD) | ✅ same |

### A4. Institutional / risk (alternatives to WGI)
| Item | Scale | Source | Status / file |
|---|---|---|---|
| Transparency Intl CPI | 0–10 (≤2011), 0–100 (≥2012) | transparency.org | ✅ `nigeria_institutions_indices.csv` (2000–2025) |
| World Bank Doing Business rank/score | rank; 0–100 DTF | archive.doingbusiness.org | ✅ same (DB2006–DB2020; DTF 2015–2020) |
| Heritage Economic Freedom | 0–100 | heritage.org | ✅ same (2000–2025) |
| Fraser EFW | 0–10 | fraserinstitute.org | ✅ same (2000–2023) |
| ICRG political risk | 0–100 | PRS Group | ⚠️ partial — only 2011–2015 in open sources |

### A5. Other macro / structural
| Item | Source | Status / file |
|---|---|---|
| External debt stock & service | World Bank `DT.DOD.DECT.CD`, `DT.TDS.DECT.EX.ZS` | ✅ `external_markets` |
| Current-account balance (US$ & %GDP) | World Bank `BN.CAB.XOKA.CD/.GD.ZS` | ✅ same |
| Electricity access | World Bank `EG.ELC.ACCS.ZS` | ✅ same |
| Oil rents (% GDP) | World Bank `NY.GDP.PETR.RT.ZS` | ✅ same |
| Exports/imports (% GDP), REER, GDP deflator | World Bank | ✅ same |
| Tax revenue (% GDP) | World Bank `GC.TAX.TOTL.GD.ZS` | ✅ same |
| Corporate total tax rate, lending rate, stocks traded | World Bank | ⚠️ not reported for NGA |
| Financial-openness (Chinn-Ito) index | Chinn-Ito (web.pdx.edu) | 🔄 if obtainable |

---

## B. Derived variables (computed from data already held) → `nigeria_fdi_fpi_derived.csv`

### B1. Scaling / normalization
- FDI & **FPI as % of GDP** (FPI%GDP newly computed; FDI%GDP for all source columns)
- **Per-capita** FDI & FPI (US$ per person)
- **Real / constant-USD** values (deflated by US CPI, base = latest year)

### B2. Standard transformations
- **log** levels; **first differences**; **growth rates (% YoY)**
- **IHS** (inverse hyperbolic sine) — sign-preserving, for series that go negative
- **Rolling volatility** (3-yr SD) of FDI and FPI — capital-flow risk proxy

### B3. Composition ratios
- **FPI : FDI ratio** ("hot money" share)
- **FDI share of total capital importation** (from NBS by-type)
- **Portfolio share of total capital importation**

### B4. Source-discrepancy & quality
- **Net-vs-gross gap** (NBS gross − BoP net) — round-tripping / measurement proxy
- **Source spread** (max − min across WB/UNCTAD/CBN per year) — reliability flag

### B5. Governance / institutions
- **Composite governance index** (simple mean of the six standardized WGI)
- **Exchange-rate depreciation %** (YoY change in LCU/US$)

### B6. Event-indicator variables (structural-break / regime markers) → `nigeria_event_indicators.csv`
- `d_gfc_2008_09`, `d_oil_crash_2014_16`, `d_recession_2016`, `d_covid_2020`,
  `d_fx_liberalization_2023ff`
- **Author-constructed (not observed data)** — binary 0/1 indicators coded from
  documented historical events. "Dummy variable" is the econometric term for these;
  it does **not** mean placeholder/irrelevant data. See README §6d for full definitions.

---

*This plan file is documentation only; the actual numbers live in the CSVs named above
and are described column-by-column in `README.md`.*
