# AI Credit Underwriting for Africa's Informal Economy

*A technical and strategic deep dive — June 2026*

## 1. The Problem: Lending to the Invisible

Africa runs on the informal economy. The informal sector contributes roughly **38% of GDP in Sub-Saharan Africa (SSA)** and employs the large majority of the workforce. Yet the businesses that drive it — the kiosk owner, the *mama put* food vendor, the okada rider, the market trader restocking from a wholesaler — are functionally invisible to a credit system built around audited accounts, payslips, collateral, and bureau history.

The numbers frame the opportunity. The IFC estimates a **formal MSME finance gap of ~$331bn for Sub-Saharan Africa**, and **51% of SSA's ~44 million formal MSMEs** are credit-constrained. Once **informal enterprises** are included, the gap widens dramatically — globally the MSME gap rises from **$5.7tn to roughly $8tn** when informal firms are counted, and SSA carries a disproportionate share. Headline figures of **$700bn+** for the continent's true (formal + informal) credit shortfall are consistent with this once informal demand is added to the formal estimate.

Traditional scoring fails these borrowers structurally, not incidentally:

- **No bureau file.** A FICO/bureau-style model needs a repayment history that thin-file borrowers, by definition, do not have. The model has nothing to ingest, so it returns "decline" or "no score."
- **No audited financials.** Underwriting SMEs normally leans on financial statements. Informal firms keep cash records in their heads or a notebook.
- **No collateral.** Land titles are often informal/unregistered; movable-asset registries are weak.
- **Unit economics.** A ₦50,000 (~$30) loan cannot absorb a manual underwriter's time. Carbon's average ticket is around **₦50,000 — precisely the amount banks deemed "uneconomical."** Without automation, the cost-to-serve exceeds the revenue.

The result is a self-reinforcing exclusion: no history → no loan → no history.

## 2. Alternative Data: What Each Signal Carries

The core insight of AI underwriting is that informal businesses generate enormous **digital exhaust** even without formal accounts. The job is to convert that exhaust into a risk signal.

| Data source | Signal it carries | Limitations |
|---|---|---|
| **Mobile-money / POS flows** (M-Pesa, agent banking, card terminals) | The gold standard. Reveals real revenue, cash-flow seasonality, balance volatility, customer concentration, day-of-week patterns. A direct proxy for ability-to-repay. | Captures only digitized turnover; cash sales are invisible. Easily gamed by wash transactions if the lender doesn't own the rail. |
| **Airtime / data top-ups** | Top-up frequency, regularity and recharge size proxy disposable income and financial discipline. Strong for cold-start. | Weak signal alone; noisy; correlates with income but not with *intent* to repay. |
| **Utility & rent payments** | On-time electricity/water/rent = the closest analog to a repayment track record for the unbanked. | Coverage is thin and fragmented in informal settlements; data rarely digitized or shareable. |
| **B2B order / restocking history** | For micro-retailers buying from FMCG distributors (e.g. embedded lending on a B2B commerce app), order cadence and basket growth proxy real demand and business health. | Only available to platforms that own the supply chain; single-supplier view misses total business. |
| **Psychometric assessments** (LenddoEFL) | Personality/behavioral traits predict willingness to repay. World Bank/IADB studies show value as a **secondary screen** that can extend credit to rejected thin-file applicants *without raising portfolio risk*. | Weaker as a sole signal; vulnerable to coaching; survey fatigue; cultural-fairness questions. |
| **Smartphone / device & GPS behaviour** (Tala, Branch) | Handset model, app inventory, SMS metadata (e.g. transaction alerts), call-log regularity, GPS stability (a fixed home/work location signals stability). | Highly privacy-intrusive; the NDPA now restricts contact/photo/message harvesting; behaviour-vs-creditworthiness link is correlational and drifts. |
| **Social / telco data** | Network tenure, recharge consistency, mobility. Telcos hold deep, hard-to-fake longitudinal records. | Access requires telco partnership; weak as standalone signal. |
| **Agritech / satellite data** (for farmers) | Plot-level NDVI/yield estimates, weather, soil and crop type let lenders size a farmer's harvest income and time repayment to the season. | Needs accurate geolocation of plots; weather-correlated default risk is systemic, not diversifiable. |

The strategic ranking is clear: **owned transaction flow (mobile-money/POS/B2B orders) is the highest-fidelity signal**, behavioural/device data is a strong *cold-start* supplement, and psychometric/telco data is best as a secondary screen.

## 3. How the Models Actually Work

**Feature engineering from transaction data.** Raw transaction logs are transformed into hundreds of features: rolling inflow/outflow over 7/30/90 days, net cash-flow trend, balance volatility (coefficient of variation), minimum balance, overdraft frequency, revenue concentration, recurrence of specific counterparties, ratio of "salary-like" credits, and velocity. Indicina's *Decide* and Pngme's feature store exist specifically to industrialize this — Indicina has processed bank statements at scale and powered **~$700m in disbursements** by turning messy statements into model-ready features.

**ML approaches.** The workhorse is **gradient-boosted decision trees (XGBoost / LightGBM / CatBoost)** — they handle heterogeneous, missing, non-linear tabular features well and are relatively interpretable via SHAP, which matters for regulatory explainability. Logistic regression survives as a transparent baseline/champion. Deep learning appears for sequence modelling of raw transaction streams and for graph-based fraud rings, but tree ensembles dominate production credit decisions. Models output a probability of default that feeds a policy layer setting limit, price and tenor.

**The cold-start problem.** A first-time borrower with no history is the hardest case. Solutions: (1) start with **nano-loans** (tiny first limits) and let repayment behaviour bootstrap a real score — the "test-and-learn" ladder Tala, Branch and JUMO all use; (2) lean on **alternative cold-start signals** (airtime, device, psychometrics); (3) **transfer learning** — Kifiya and EFL begin with a pooled multi-country model, then re-weight toward the partner institution's own data once enough observations accrue.

**Behavioural vs financial signals.** Financial signals (cash flow) measure **ability** to repay; behavioural signals (top-up discipline, GPS stability, app usage, psychometrics) measure **willingness** and stability. The best models blend both — cash flow sizes the loan, behaviour adjusts the risk grade, especially when financial history is thin.

**Fraud detection.** Runs in parallel: device fingerprinting, velocity checks, synthetic-identity and SIM-swap detection, and **graph analytics** to catch coordinated default rings and first-party fraud. In high-volume nano-lending, fraud and credit risk blur together, so fraud scoring is part of the underwriting stack, not a separate gate.

## 4. Real-World Cases (with Numbers)

| Company | Market | Scale / numbers | Approach & outcome |
|---|---|---|---|
| **JUMO** | SSA + Asia (B2B rails for banks/telcos) | **222m+ loans disbursed in 2024 alone**; cumulatively **~120m loans / ~$3.5bn** to **18m+** people; raised **$120m at ~$400m valuation** (2021). | AI scoring on mobile-wallet behavioural data; 33% of 2024 loans to women; **>50% of high-risk users improved eligibility over time**; launched Africa's first e-money asset-backed securitisation with Standard Bank. |
| **Kifiya** | Ethiopia | With 6 banks: **717,000 loans / ~$44m**; cumulatively **~$150m uncollateralised credit to 382,000 MSMEs**, ~12% MoM growth; **75,000 smallholder farmers / ~$92m** in inputs. | Alternative-data AI scoring + bank partnership model; uncollateralised "missing middle" lending; won Global SME Finance Awards 2024. |
| **M-KOPA** | Kenya, Uganda, Nigeria, Ghana, SA | **$1.5bn+ credit unlocked to 5m+ customers**; ~2m added in ~15 months; 1m+ smartphones sold in 12 months. | **Asset financing as a data flywheel** — daily micro-repayments on a financed phone build a repayment record that unlocks further credit; the device itself is collateral and telemetry. |
| **Tala** | Kenya, Nigeria, Mexico, Philippines, India | 10m+ app installs; claims **~92% repayment rate** (earlier disclosures: 15–20% go past due, ~half of those recovered). | Smartphone behavioural + transaction data; ML scoring in seconds; nano-loan ladder. |
| **Branch** | Kenya, Tanzania, Nigeria, India, Mexico | Multi-million user base. | Handset data, SMS logs, GPS, contacts, repayment history → behavioural default prediction. |
| **Carbon** (Nigeria) | Nigeria | **$200m+ disbursed since 2016**, avg ticket **~₦50,000**. | CBN microfinance licence; alternative-data scoring on tickets banks ignored. |
| **FairMoney / Renmoney** | Nigeria | High-volume digital lenders under CBN MFB licences. | AI scoring on mobile metadata, utility and behavioural data to cut NPLs vs manual underwriting. |
| **Indicina** | Nigeria, Kenya (infra) | **~$700m loans powered**, **~$3bn** processed, ~120 institutional customers (incl. Polaris Bank, VFD). | *Decide* API: real-time bank-statement analysis, ML credit analytics sold to lenders. |
| **Pngme** | Nigeria, Kenya, Ghana | Financial-data infrastructure / feature store. | Aggregates accounts + builds ML features as a service for lenders. |
| **LenddoEFL** | Pan-African pilots | World Bank/IADB-validated. | Psychometric secondary screen; extends credit to rejected thin-file applicants without raising portfolio risk. |

**What worked:** the winners pair **automation** (sub-minute decisions on tiny tickets) with a **proprietary data source** (M-KOPA's device telemetry, JUMO's wallet rails, Lula's business bank account). **What's fragile:** standalone behavioural lenders relying on harvested phone data face rising NPLs and regulatory clampdowns. Nigerian deposit banks ran ~8.3% average NPLs in recent study periods, and research finds rapid, low-oversight digital disbursement can *elevate* NPL ratios when models lean on volatile alternative data.

## 5. Beyond Credit: Other AI Use Cases

- **Local-language voice/LLM assistants.** Real deployments exist. **Lelapa AI (South Africa)** ships *Vulavula* (transcription/translation across English, Afrikaans, isiZulu, Sesotho) and **InkubaLM**, a small multilingual LLM for isiZulu, Yoruba, Hausa, Swahili and isiXhosa. **Awarri (Nigeria)** built **N-ATLaS**, a multilingual model for Hausa, Igbo, Yoruba and West African Pidgin, anchoring the government's Nigerian Languages AI initiative (drawing on 7,000+ tech fellows). These power voice-first banking, customer support and government services for non-English, low-literacy users — directly relevant to onboarding informal merchants.
- **Agritech advisory.** **PlantVillage Nuru** (Penn State/CGIAR/IITA) runs an on-device CNN that diagnoses cassava (CMD/CBSD), maize and other crop diseases from a phone photo, **offline**, in Swahili and English; peer-reviewed studies validate its field accuracy, and it had reached tens of thousands of Kenyan farmers via ~200 extension workers by 2024.
- **Demand forecasting / inventory** for micro-retailers — B2B commerce platforms use ML on order history to recommend restock quantities and offer embedded working-capital credit; the same transaction data feeds both.
- **KYC automation** — OCR + facial-match + liveness + document fraud detection (and government ID/BVN/NIN matching in Nigeria) collapses onboarding cost, which is the binding constraint for micro-tickets.

## 6. Risks and Limitations

- **Data bias & fairness.** Models trained on the digitally-active can systematically score down rural, female or cash-heavy traders (proxy discrimination via device or location features). Cold-start signals can entrench existing exclusion.
- **Privacy & the NDPA.** Nigeria's **Data Protection Act 2023** requires **informed, specific, freely-given consent**, mandates **Data Protection Impact Assessments** for credit-scoring and automated decisions, and the NDPC has actively penalised lenders — fining **Fidelity Bank ₦555.8m** and targeting loan apps that **harvested contacts/photos to shame defaulters** (now prohibited). The 2026 DEON regulations tighten digital-lending rules further.
- **Over-indebtedness.** Frictionless nano-loans across multiple apps enable borrower stacking; weak data-sharing between lenders masks total exposure.
- **Model drift.** Behavioural relationships decay fast under inflation, FX shocks (naira devaluation) and macro stress; models trained on a benign period misprice risk in a downturn. Continuous monitoring/retraining is mandatory.
- **Thin-file ceiling.** For the truly cash-only, fully analog vendor, *no* alternative data exists — AI cannot conjure a signal where there is zero digital footprint.

## 7. Strategic Takeaway: Where AI Genuinely Wins, and the Data Moat

The genuine, durable differentiator is **not the model — it's the proprietary, high-frequency transaction data the model is fed.** Gradient-boosting libraries are commoditized and open-source; anyone can run XGBoost. What cannot be copied is **owning the rail** that generates the cash-flow signal. This is the data-moat dynamic, and it explains every winner above:

- **M-KOPA** finances the phone, so it sees daily repayment telemetry and holds the asset — credit *creates* the data that underwrites the next loan.
- **JUMO** embeds in telco/bank wallets, so it scores on transaction flows it processes directly.
- **Lula (formerly Lulalend)** is deliberately shifting from intermittent loan applications to a **business bank account / lending-as-a-service** model precisely because *controlling the account yields far richer cash-flow signal* — it can detect distress or growth in real time. (Industry evidence: alternative-data ML scoring delivers **~20–30% higher approval rates at constant risk** versus bureau-only models — the kind of uplift Lula targets; ~90% of its clients are first-time borrowers, backed by an IFC partnership.)
- **Kifiya / Indicina / Pngme** monetize this by selling the *infrastructure* to data owners (banks), capturing value without owning the borrower.

So the moat compounds: the lender with the most transaction data builds the best model, approves more good borrowers at lower loss, generates more transactions, and widens the data lead. Late entrants relying on *purchasable* alternative data (airtime, generic device data) get a thinner, more easily-gamed signal and worse unit economics.

**Where it's hype:** standalone "AI loan apps" that scrape phone data without owning a transaction relationship — high NPLs, regulatory exposure, no moat. **Where it's real:** AI that turns a **proprietary flow** (mobile-money, POS, B2B restocking, asset-financed device) into instant, automated, sub-$50-ticket underwriting. The strategic conclusion is blunt: **whoever owns the informal merchant's transaction data owns the credit relationship — and increasingly the bundled services (payments, inventory, advisory) on top of it.**

---

## Sources

- [IFC / SME Finance Forum — Africa's $331bn SME finance gap](https://www.smefinanceforum.org/post/ifc-sme-finance-forum-target-solutions-to-africa%E2%80%99s-331-billion-sme-finance-gap)
- [IFC MSME Finance Gap Report (March 2025)](https://www.smefinanceforum.org/sites/default/files/Data%20Sites%20downloads/IFC%20Report_MAIN%20Final%203%2025.pdf)
- [WEF — Africa's SMMEs and economic growth (2026)](https://www.weforum.org/stories/2026/01/africa-smmes-economies-growth/)
- [JUMO — Our 2024 impact: numbers and beyond](https://jumo.world/our-2024-impact-numbers-and-beyond/)
- [JUMO — Wikipedia (cumulative loans/value)](https://en.wikipedia.org/wiki/JUMO)
- [JUMO raises $120m at $400m valuation](https://jumo.world/press-release/jumo-raises-usd120m-in-latest-funding-round-led-by-fidelity-management-research-company-llc-visa-and-kingsway/)
- [Kifiya — AI-powered credit scoring](https://kifiya.com/2025/03/07/ai-powered-credit-scoring-unlocking-opportunities-for-small-businesses-in-africa-and-other-emerging-markets/)
- [Kifiya facilitates $150m for 382,000 MSMEs (TechMoran)](https://techmoran.com/2025/03/04/kifiya-facilitates-150m-in-uncollateralised-digital-credit-for-382000-msmes-via-ai-powered-credit-scoring/)
- [M-KOPA reaches 5m customers / $1.5bn credit](https://african.business/2024/09/apo-newsfeed/leading-fintech-m-kopa-reaches-5-million-customers-unlocking-1-5bn-in-credit-across-5-markets)
- [M-Kopa — Wikipedia](https://en.wikipedia.org/wiki/M-Kopa)
- [Tala / Branch behavioural credit scoring (Penser)](https://www.penser.co.uk/article/credit-scoring-the-unbanked-alternative-solutions-used-in-global-markets/)
- [Start-up uses mobile data as a credit score (CNBC)](https://www.cnbc.com/2020/01/03/start-up-uses-mobile-data-as-a-credit-score-for-the-global-unbanked.html)
- [Carbon $200m+ disbursed; AI in African financial inclusion](https://numeris-media.com/meekam-mgbewelu-in-nigeria-digital-lenders-such-as-carbon-formerly-paylater-fairmoney-and-renmoney-underwrite-loans-based-on-data-traditional-banks-ignored-carbon-alone-has-disbursed-over-20/)
- [AI credit risk & NPLs in Nigeria's digital lending (British JIR)](https://britishjir.org/index.php/bjir/article/download/115/97/158)
- [Indicina — credit decisioning & statement analysis (TechCrunch)](https://techcrunch.com/2022/06/06/nigerias-indicina-raises-3m-to-help-businesses-offer-credit-to-their-customers-at-scale/)
- [Indicina Decide API docs](https://developers.indicina.co/Decide/api-statement-analysis/)
- [Pngme — financial data infrastructure for Africa](https://www.pngme.com/)
- [Lula lands $21M for AI-driven SME credit (TechBuild)](https://techbuild.africa/lula-21m-ai-driven-credit-south-african-smes/)
- [South Africa's Lula bags $21M — banking/data moat (Launch Base Africa)](https://launchbaseafrica.com/2026/02/04/south-africas-lula-bags-21m-to-double-down-on-sme-lending/)
- [IFC partners with Lula](https://www.ifc.org/en/pressroom/2025/ifc-partners-with-lula-to-create-jobs-and-boost-small-business-growth-in-south-afr)
- [Zest AI / alternative-data 20–30% approval uplift (Lucid)](https://www.lucid.now/blog/machine-learning-small-business-credit-risk/)
- [LenddoEFL psychometric scoring (Caribou / Finance in Digital Africa)](https://www.financedigitalafrica.org/2018/10/10/delving-into-human-consciousness-using-psychometric-assessments-in-financial-services/)
- [World Bank — Psychometrics as a tool to improve credit information](https://documents1.worldbank.org/curated/en/999861565615232538/pdf/Psychometrics-as-a-Tool-to-Improve-Credit-Information.pdf)
- [Lelapa AI launches InkubaLM / Vulavula](https://africaworld.princeton.edu/news/2024/lelapa-ai-launches-africa%E2%80%99s-first-ai-large-language-model)
- [Awarri N-ATLaS multilingual LLM (Hugging Face)](https://huggingface.co/NCAIR1/N-ATLaS)
- [African techies build AI language tools (Context/TRF)](https://www.context.news/ai/african-techies-develop-ai-language-tools-from-swahili-to-zulu)
- [PlantVillage Nuru — AI crop disease detection (CGIAR)](https://bigdata.cgiar.org/inspire/inspire-challenge-2017/pest-and-disease-monitoring-by-using-artificial-intelligence/)
- [PlantVillage Nuru cassava accuracy study (Frontiers in Plant Science)](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2020.590889/full)
- [Nigeria Data Protection Act 2023 (full text)](https://cert.gov.ng/ngcert/resources/Nigeria_Data_Protection_Act_2023.pdf)
- [NDPA obligations for fintech / digital lending (Mondaq)](https://www.mondaq.com/nigeria/privacy-protection/1430338/understanding-the-nigeria-data-protection-act-2023-obligations-of-digital-platforms-and-businesses)
- [DEON Regulations 2026 — digital lending (Nigeria Data Protection)](https://nigeriadataprotection.com/understanding-the-deon-regulations-in-2026/)
- [Fintech compliance under NDPA, GAID & CBN (Babalakin & Co)](https://blog.babalakinandco.com/beyond-licensing-the-new-face-of-fintech-compliance-under-the-ndpa-gaid-and-cbn-guidelines/)
