# Nigeria Debt-Cycle Dataset — Consolidated Source Documentation

**Compiled:** 2026-06-30

This is the **provenance index** for the dataset. It (1) explains the source-of-record model, (2) maps each CSV to its sourced staging file(s), and (3) lists the primary-source institutions with URLs. For audit-grade, per-cell attribution (every figure tagged with its publication, period, and a confidence flag), open the relevant `_staging/NN_*.md` file — that is the authoritative provenance layer.

---

## 1. Provenance model

- **Every CSV value derives from a staging file** in `_staging/`. The CSVs are the clean, machine-readable extract; the staging files are the **source-of-record** and carry the full citation for each cell.
- **Every staging cell is flagged:** `[SOURCED]` (primary/official or credible secondary citing official), `[ESTIMATED]` (analyst-derived, method stated), `[PROVISIONAL]` (latest/incomplete/forecast). **Blank = not reliably sourceable, left empty — never guessed.**
- **Primary sources were prioritised** (DMO, CBN, NBS, IMF, World Bank, OPEC, ACLED, UNDP, etc.). Where an official portal blocked automated access (CBN/DMO Cloudflare; IMF PDFs HTTP 403; NBS image-PDFs), the figure was taken from a reputable secondary outlet *explicitly quoting* the official release and flagged `[SOURCED-2nd]`. These gaps are documented in each staging file.
- **~200+ distinct sources** underpin the dataset across the 17 staging files.

---

## 2. CSV → staging file → key sources

| CSV | Staging file(s) | Primary sources |
|---|---|---|
| `nigeria_debt_cycle_gauges.csv` | 01, 02, 03, 04, 06 | DMO, CBN, NBS, IMF WEO/Article IV, World Bank WDI, OPEC ASB |
| `nigeria_debt_cycle_quarterly.csv` | 01, 03, 04, 06 | DMO quarterly debt, CBN (FX/reserves/MPR), NBS CPI, OPEC |
| `nigeria_external_debt_profile.csv` | 01 | DMO (creditor composition, Q-by-Q 2025) |
| `nigeria_eurobond_maturity_wall.csv` | 01 | DMO Eurobond closing prices/yields (Bloomberg-sourced) |
| `imf_weo_nigeria_projections.csv` | (IMF direct) | IMF World Economic Outlook (Apr-2026 vintage) |
| `nigeria_monetary_credit_banking.csv` | 05 | CBN Money & Credit Statistics, IMF FSI, World Bank, DMO/FMDQ |
| `nigeria_markets_capital.csv` | 10, 15 | NGX, FMDQ, DMO, Damodaran/NYU (CDS), Trading Economics |
| `nigeria_sectoral_gdp_activity.csv` | 12 | NBS GDP, S&P Global/Stanbic PMI, NERC, NPA, Dangote, MAN |
| `nigeria_labour_demographics.csv` | 07 | NBS NLFS, World Bank, ILOSTAT |
| `nigeria_cost_of_living.csv` | 08 | NBS price watches, NERC, Cadre Harmonisé/FAO-WFP |
| `nigeria_consumer_spending_indicators.csv` | 16 | NBS NLSS, CEIC, NielsenIQ, SBM Intelligence, EFInA |
| `nigeria_financial_inclusion_remittances.csv` | 09 | EFInA A2F, World Bank Findex, NIBSS, SANEF, CBN/World Bank remittances |
| `nigeria_fiscal_detail.csv` | 11 | FIRS/NRS, Budget Office, NBS, PenCom, NEITI, NCS |
| `nigeria_social_security_humandev.csv` | 13 | ACLED, IEP GTI, IDMC/IOM/UNHCR, UNDP HDR, World Bank, UNICEF |
| `nigeria_migration_japa.csv` | 07 + child agents | Canada IRCC, UK NMC/GMC, US IIE/State Dept, UN DESA, Afrobarometer, World Bank |
| `nigeria_private_capital_vc.csv` | 14 | Partech Africa, AVCA, Briter Bridges, Disrupt Africa, NBS, UNCTAD |
| `nigeria_historical_precycle.csv` | 17 | World Bank WDI/IDS, DMO Paris Club doc, Paris Club, EIA, IMF |
| `state_panel.csv` (spatial GCN) | 21, 22 | NBS MPI 2022, NBS 2024 IGR, NBS population, **ACLED-2024/25 fatalities via HDX** |

---

## 3. Primary sources by institution

**Nigerian official**
- Debt Management Office (DMO) — total public debt, external composition, Eurobonds, Paris Club: https://www.dmo.gov.ng
- Central Bank of Nigeria (CBN) — money/credit, FX, reserves, MPR, BoP, Ways & Means: https://www.cbn.gov.ng
- National Bureau of Statistics (NBS) — GDP, CPI, NLFS, NLSS, price watches, MSME, IGR: https://www.nigerianstat.gov.ng · microdata: https://microdata.nigerianstat.gov.ng
- Budget Office of the Federation — appropriations, MTEF/FSP, BIR: https://budgetoffice.gov.ng
- FIRS / Nigeria Revenue Service — tax collections: (via official releases & NBS)
- PenCom — pension assets: https://www.pencom.gov.ng
- NERC — electricity tariffs/generation: https://nerc.gov.ng
- NUPRC — oil production; NNPCL — remittances/subsidy
- NPA — port throughput: https://nigerianports.gov.ng
- NEITI — FAAC/oil revenue: https://neiti.gov.ng
- NGX / FMDQ — equities, fixed income, FX fixings: https://ngxgroup.com · https://fmdqgroup.com
- EFInA — Access to Financial Services survey: https://efina.org.ng
- NIBSS — instant-payment volumes; SANEF — agent banking

**International / multilateral**
- IMF — WEO, Article IV, FSI: https://www.imf.org · DataMapper: https://www.imf.org/external/datamapper/profile/NGA
- World Bank — WDI, IDS, Findex, Poverty & Inequality Platform, NDU: https://data.worldbank.org
- OPEC — Annual Statistical Bulletin (Bonny Light, production): https://www.opec.org/annual-statistical-bulletin.html
- EIA — Brent/WTI historical prices: https://www.eia.gov
- UN DESA — World Population Prospects, migrant stock: https://www.un.org/development/desa/pd
- UNDP — Human Development Report: https://hdr.undp.org
- UNICEF / UNESCO UIS — out-of-school, literacy
- IDMC / IOM DTM / UNHCR — displacement & refugees
- ACLED — political-violence events & fatalities: https://acleddata.com
- IEP — Global Terrorism Index: https://www.visionofhumanity.org
- FAO / WFP / Cadre Harmonisé (IPC) — food security: https://www.ipcinfo.org/ch
- Paris Club — debt-treatment press releases: https://clubdeparis.org

**Destination-country migration data**
- Canada IRCC open data (study/work permits, PR): https://open.canada.ca
- UK NMC (nurses), GMC (doctors), GOV.UK visa statistics
- US IIE Open Doors (students), US State Dept Bureau of Consular Affairs (visas)
- Afrobarometer — emigration-intent surveys: https://www.afrobarometer.org

**Private-capital trackers**
- Partech Africa, AVCA, Briter Bridges, Disrupt Africa, UNCTAD WIR

**Reputable secondary (used only when quoting official data, flagged `[SOURCED-2nd]`)**
- Nairametrics, TechCabal, BusinessDay, Premium Times, TheCable, Vanguard, Punch, Guardian NG, ThisDay, Channels TV, Proshare, Intelpoint, Africa Check, Trading Economics, CEIC

---

## 4. Known provenance gaps (documented, not hidden)

Each staging file ends with a "Known gaps" section listing values left blank because the authoritative source was access-blocked this session. The recurring blocked sources are: **CBN Statistical Bulletin / DMO portal** (Cloudflare/HTTP 406), **IMF.org PDFs** (HTTP 403), **NBS image-based PDFs** (not machine-readable), and **subscription feeds** (Bloomberg NDF/CDS history, CEIC monthly). These are the priority targets for any future audit-grade gap-fill. No value was ever guessed to fill a gap.
