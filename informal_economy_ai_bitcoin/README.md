# The Informal Economy in Africa & Nigeria — and the AI + Bitcoin Opportunity

*Research report · compiled 2026-06-29*

A business/product opportunity assessment of the intersection of the informal economy, AI, and Bitcoin/stablecoins in Africa and Nigeria. Built from multi-source web research with figures attributed inline.

> **One-line thesis:** The informal economy is the *real* economy of Nigeria and most of Africa — ~80–90% of jobs. A first wave of "enabling" businesses (agent banking, B2B retail, POS) already digitised its **payments and supply chains**. The next two layers of value — **AI** (turning informal data into credit, advice, and forecasting) and **stablecoins/Bitcoin** (turning the naira trap into dollar access and cheap cross-border settlement) — are early, fast-growing, and where a focused new entrant can still win. The single sharpest niche is **the dollar-denominated, AI-underwritten, stablecoin-settled "operating account" for the informal cross-border trader and freelancer.**

---

## 1. What is the informal economy in Africa and Nigeria?

The informal economy = economic activity that is not registered, regulated, or taxed in the same way as formal businesses — street traders, market sellers, artisans, smallholder farmers, okada/keke transport, micro-retailers ("mama put", kiosks, provision stores), and the self-employed. It is not a fringe; it is the majority.

### Africa
- **~83% of all employment in Africa is informal** (UN/ILO, 2024) — and **~85% in Sub-Saharan Africa**. The share has barely moved in 20 years (84.3% in 2005 → ~83% in 2024). [ILO; North Africa Post]
- **Central and West Africa are the most informal regions on earth: ~92.5% and ~91.8%** informal employment respectively. [ILO regional profile, 2024]
- The informal economy is **~30–40% of Africa's GDP** (UNCTAD / World Bank). The gap between the employment share (~83%) and the GDP share (~35%) is the productivity gap — lots of people, low output per worker.
- **60–80% of African workers have no formal social protection** (no pension, no insurance, no safety net). [ILO]
- Women hold **>85% of informal jobs** in several African countries (retail trade, domestic services).

### Nigeria specifically
- **Informal sector ≈ 42.5% of GDP** after a recent national-accounts revision; older/other estimates run as high as **57–65%** (the IMF has cited ~65%). The wide range reflects how hard it is to measure activity that is deliberately unrecorded. [businessamlive/IMF; TechCabal; World Economics]
- **>80% of employment is informal**; among youth aged 15–24, **~98% work informally** (ILO). The informal sector is Nigeria's de facto unemployment insurance.
- **~89% of Nigeria's ~40 million MSMEs are informal** (Moniepoint 2025 Informal Economy Report).
- Key sectors: **agriculture** (smallholder farming), **trade** (open-air markets, provision shops, FMCG resellers), **transport** (okada motorcycles, keke tricycles, danfo buses), **artisans/services** (tailors, mechanics, hairdressers, electricians), and **light manufacturing/food**.

### Why it stays informal
- **Cost & friction of formalising:** complex registration, bureaucracy, and high compliance costs. Many rationally stay out of the tax/regulatory net. [Opinion Nigeria; Businessday]
- **The formal sector can't absorb the labour force.** Informality is a response to a shortage of formal jobs — **38% of informal owners (Moniepoint 2025) started their business because of unemployment**, not entrepreneurial ambition.
- **No access to formal finance.** Unbanked/underbanked traders can't get loans, so they have no incentive to build a formal paper trail; they run on cash and informal credit.
- **Skills/education gap** between formal and informal workers.
- **Risk:** Nigeria's 2025 tax reforms may, if compliance costs rise too fast, *push more activity informal*, not less. [Businessday]

**Takeaway for a builder:** informality is structural and sticky. Don't build a product that requires users to "become formal" first. Build products that **meet informal businesses where they are** (cash-adjacent, phone-first, low-literacy, trust-based) and give them a reason to leave a digital footprint.

---

## 2. Businesses & platforms that already enable the informal economy

A first wave has already digitised the informal economy's **rails**. Understanding their models is essential — they are both the competition and the distribution partners.

### a) Agent banking / POS networks (the cash on-ramp)
- **Moniepoint** — Nigeria's largest fintech by merchant terminal footprint; **~2.3 million businesses** on its POS machines (Jan 2025). Got a CBN **digital banking licence in 2024** and now lends to SMEs off its transaction data. This is the dominant "operating system" play for informal merchants. [Rest of World; Moniepoint]
- **OPay** — Chinese-backed; **$2bn valuation** (2021, $400m raise). Mass-market wallets + agent network for the unbanked.
- **Paga**, **PalmPay**, **Kuda** — adjacent agent-banking / neobank players.
- *Model that works:* put a cheap POS terminal + float in the hands of millions of micro-merchants, monetise transaction fees, then **layer credit on top of the transaction data**. The terminal is the trojan horse for financial services.

### b) Mobile money (the East African template)
- **M-Pesa** (Safaricom, Kenya) — the canonical success: phone-based money for the unbanked, now a full financial platform. Nigeria's bank-led model meant mobile money came *later* and via fintechs/agents rather than telcos.
- **Wave** (Francophone West Africa) — undercut incumbents on price; aggressive low-fee mobile money.

### c) B2B e-commerce / embedded finance for informal retailers
- **TradeDepot** — B2B platform connecting small retailers to manufacturers/wholesalers; uses **mobile transaction data to embed BNPL/working-capital credit** for shops.
- **Sabi** — B2B commerce "operating system" for African merchants; marketplace + logistics + **embedded BNPL**. Revenue grew **$1.52m (2021) → $46.5m (2024)**. On the FT Africa fastest-growing list.
- **OmniRetail** — B2B distribution + embedded finance; also on the FT fastest-growing list.
- **Twiga** (Kenya) — B2B produce/FMCG distribution to informal kiosks.
- *The B2B BNPL market in Nigeria is **$1.75bn+** and growing* (2026 report), driven by the scale of informal trade. Nigeria is the **largest B2B BNPL market in West Africa**.

### d) The pattern
The winning model across all of these is the same three-layer stack:

```
Layer 3:  CREDIT / INSURANCE / SAVINGS   ← the profit (underwritten by Layer 2 data)
Layer 2:  DATA (transactions, orders, location, inventory)
Layer 1:  A RAIL THE INFORMAL BIZ ALREADY NEEDS  (payments POS, or restocking/B2B)
```

You win Layer 1 by solving a painful daily need (accept payment, restock cheaply). That earns you Layer 2 data. Layer 3 is where the margin is. **AI supercharges Layer 2→3, and Bitcoin/stablecoins open an entirely new Layer 1 (cross-border) that the incumbents above barely touch.**

---

## 3. How can AI help the informal economy?

AI's role is to **convert the informal economy's invisibility into legibility** — without forcing formalisation. Concrete, proven-or-emerging use cases:

1. **Alternative-data credit scoring (the biggest one).** Informal businesses have no audited accounts, but they generate rich digital exhaust: mobile-money flows, POS transactions, airtime top-ups, utility payments, B2B order history, even smartphone/GPS behaviour. ML models turn this into a credit score.
   - There is a **~$700bn financing gap** in Africa's informal economy that alternative-data lending targets. [FurtherAfrica; AInvest]
   - **Lulalend (SA):** adding regional business payment cycles to its model **raised informal-retailer approval rates ~30% while cutting defaults**.
   - **JUMO** builds region- and activity-specific models ("a taxi driver in Accra shows consistency differently than a market seller in Nairobi").
   - **Kifiya (Ethiopia):** enabled **717,000 loans worth $44m** with banks using AI scoring.
   - **>350m adults in Sub-Saharan Africa are unbanked** — the addressable base.

2. **Voice & local-language assistants.** Many informal operators have low literacy or don't read English. LLM-based **voice agents in Pidgin, Hausa, Yoruba, Igbo, Swahili** can deliver bookkeeping, price info, government/tax guidance, and customer support. *Moniepoint shipped an AI chatbot ("M") in 2025* to surface informal-economy data — a sign the incumbents see this.

3. **Agritech advisory.** Image-recognition crop/pest diagnosis, weather + planting advice, and input recommendations delivered to smallholder farmers by SMS/WhatsApp/voice.

4. **Demand forecasting & inventory for micro-retailers.** AI tells a kiosk owner what to restock, how much, and when — reducing dead stock and stockouts. Naturally bundles with B2B restocking platforms (Sabi/TradeDepot model).

5. **Fraud detection & risk.** Pattern detection on agent-banking and P2P flows to catch fraud, a major friction in cash-adjacent networks.

6. **Onboarding / KYC automation.** OCR + face match to onboard low-documentation users cheaply and at scale.

**Where AI is genuinely differentiating vs. hype:** credit scoring and local-language voice interfaces. The data moat (Layer 2 above) is the real asset; AI is the engine that mines it.

---

## 4. How can Bitcoin / stablecoins / Lightning help the informal economy?

This is where the most acute, *currently-felt* pain meets a working solution. The headline: in high-inflation, capital-controlled economies, **the killer app is not "Bitcoin the investment" — it is the dollar (via stablecoins), delivered over crypto rails.**

1. **Store of value / inflation hedge (the #1 driver in Nigeria).** The naira hit record lows in Feb 2024; inflation has been punishing. **Stablecoins (USDT/USDC) let anyone hold synthetic dollars from a phone**, no US bank account needed. **Stablecoins are ~40% of Nigeria's crypto market**, dominated by USDT/USDC. A 2026 survey found **95% of Nigerian respondents preferred receiving payments in stablecoins**; **59% hold USDT, 48% hold USDC.** [Chainalysis; BVNK]

2. **Cheaper, faster remittances.** Traditional Lagos↔Nairobi: **3–5 days, 6–8% fee.** Stablecoin on the same corridor: **~60 seconds, 1.5–2.5% all-in**, or under $1 on Tron/Solana. Sub-Saharan Africa is the **most expensive remittance region on earth (avg ~8.4%)** — the cost-saving is enormous. [Web3 Enabler; World Bank]

3. **Cross-border trade settlement.** Informal importers (e.g. buying goods from China/UAE) struggle to get dollars through banks under FX controls. Nigeria processed an estimated **~$22–26bn in stablecoin volume (Jul 2023–Jun 2024), much of it USDT for import/export financing.** Nigeria is **~43% of all SSA crypto volume and ~60% of SSA stablecoin inflows.** [Chainalysis]

4. **Merchant payments via Lightning (Bitcoin proper).** The **Lightning Network** settles BTC in seconds for fractions of a cent (a $50 payment costs **$0.01–0.03** vs **$3.25** traditional). **Bitnob** was the first African company to integrate Lightning end-to-end; its Lightning salary/remittance volume grew **340% YoY** across 23 countries.

5. **Freelancer / gig income.** African freelancers billing US/EU clients increasingly get paid in **USDT on Tron** to dodge 10%+ wire fees and slow/blocked bank rails. New entrants **Hurupay (>$50m processed), Payd, Noah, Yogupay, TransFi** are racing here. ~**70% of African freelancers rely on gig income** for daily needs; ~**93% of global freelancers want part-pay in digital assets.**

**Bitcoin vs. stablecoins — be precise:** For *informal-economy utility*, **stablecoins are doing ~90% of the real work** (payments, savings, trade) because volatility makes raw BTC a poor medium of exchange. **Bitcoin's roles are:** (a) the **settlement/liquidity backbone** beneath services like Strike↔Bitnob "Send Globally", and (b) **Lightning as a cheap payment rail**. A serious product treats *stablecoins as the user-facing asset and Bitcoin/Lightning as plumbing.*

---

## 5. Can Bitcoin bridge the informal economy and developed economies? Is it already?

**Yes — and it already is, at material scale, primarily through stablecoins on crypto rails.** The "bridge" is real and measurable:

- **Remittance bridge (developed → informal):** **Strike + Bitnob "Send Globally"** lets someone in the US send dollars that travel over **Bitcoin/Lightning** and land as **naira/cedi/shilling in a bank account, mobile-money wallet, or Bitnob wallet within minutes** — launched first in Nigeria, Kenya, Ghana. Diaspora remittances to Nigeria were **$20.93bn in 2024 (~4–6% of GDP, ~37% of all SSA remittances)** — a huge pool that crypto rails are starting to undercut on price.
- **Earnings bridge (developed → informal worker):** stablecoin payroll/freelance platforms (Hurupay, Payd, Rise, TransFi) connect African workers to US/EU employers, converting ACH/SEPA into USDT/USDC settled instantly. Documented cases cut fees **from ~11% (wire) to ~$2 flat**, and one pilot **from 29% → 2%** for Kenyan micro-payments.
- **Trade bridge:** informal importers settle with foreign suppliers in USDT when bank dollars are unavailable — **~$22bn+ of Nigeria's stablecoin flow is trade/import-linked.**
- **Savings/dollarisation bridge:** ordinary Nigerians hold the world reserve currency synthetically, escaping naira depreciation, without touching the US banking system.

**How it does it mechanically:** crypto rails replace the slow, expensive correspondent-banking chain (SWIFT → multiple intermediaries → high FX spread → cash-out) with **one fast, cheap public network + local on/off-ramps (P2P, exchanges, agents)**. The "bridge" is really the **on/off-ramp + the dollar-stable asset**, not BTC's price.

**The honest counter-evidence (why it's not a clean win yet):**
- **Volatility & UX:** raw BTC is too volatile for the poor to hold; stablecoins solve store-of-value but add issuer/peg risk.
- **Regulation is the central risk (see §below).** Nigeria *banned banks from servicing crypto in Feb 2021*, which pushed everything to **P2P** (Nigerians kept trading via bank transfer/cash without centralized exchanges). The ban was **lifted in Dec 2023**, replaced by regulation.
- **The off-ramp is the weak link:** turning USDT back into spendable naira still often relies on P2P liquidity, informal agents, and price spreads — that's the friction a good product must own.

### Nigeria regulatory timeline (you must build around this)
- **Feb 2021:** CBN bars banks from facilitating crypto transactions → activity moves to **P2P**.
- **Oct 2021:** **eNaira** CBDC launched — largely failed to gain adoption.
- **Dec 2023:** CBN **reverses the ban**; pivots from prohibition to regulation ("crypto is here to stay").
- **Feb 2024:** Naira crisis; **Binance executives arrested/prosecuted**, govt blames P2P/Binance for FX manipulation. Chilling effect on offshore exchanges.
- **Mar 2024:** SEC launches **ARIP** (Accelerated Regulatory Incubation Programme) to license crypto businesses.
- **Late 2024:** SEC grants first provisional exchange licences (**Busha, Quidax**).
- **2025:** **Investment and Securities Act (ISA) 2025** formally recognises crypto/virtual assets and puts them under **SEC oversight** — a real legal foundation.

**Net:** Nigeria has moved from *ban → regulated tolerance* in ~2 years. The window for **licensed, compliant** operators is opening; the era of pure offshore/P2P grey-market is closing.

---

## 6. How can the bridge be improved / leveraged to work smoothly?

The bridge works but is rough. The improvements are precisely the product opportunities:

1. **Own the off-ramp & local liquidity.** The pain isn't sending USDT — it's reliably converting to naira at a fair rate, instantly, anywhere. Deep local liquidity + agent/POS cash-out integration is the moat. **Partner with or plug into Moniepoint/OPay agent networks** rather than rebuilding cash distribution.
2. **Abstract the crypto away.** Users should see "dollars" and "naira", not wallets, gas, chains, or seed phrases. Stablecoins + Lightning as invisible plumbing; a clean fiat-feeling UX on top. (This is the Bitnob/Strike insight.)
3. **Compliance as a feature, not an afterthought.** Get into **ARIP / SEC licensing**, build KYC/AML in, partner with licensed exchanges (Busha/Quidax). Post-Binance, *regulatory legitimacy is a competitive advantage*, not a cost.
4. **Vertical integration with the existing rails (§2).** Combine the **B2B-restocking / POS data** (Layer 1–2) with **stablecoin settlement** (cross-border Layer 1) and **AI credit** (Layer 3). No incumbent yet owns all three for the cross-border informal trader.
5. **Local-language, voice-first, offline-tolerant UX.** USSD/WhatsApp/voice for feature-phone and low-literacy users; works on patchy connectivity.
6. **Manage peg & FX risk transparently.** Show the true all-in rate; hedge; diversify stablecoin exposure; be honest about issuer risk.
7. **Trust & education.** Crypto carries scam stigma in Nigeria. Agent-assisted onboarding, community trust, and clear guarantees matter more than features.

---

## 7. Is this a viable entrepreneurial niche?

**Yes — but the niche is specific, and the generic versions are already crowded.** Assessment:

### Why it's attractive
- **Massive, underserved base:** 80–90% of jobs informal; 350m+ unbanked; $700bn credit gap; $20.9bn/yr Nigerian remittances; Nigeria #2 globally in crypto adoption.
- **Acute, daily pain:** naira depreciation + FX controls + expensive remittances = users who *already* adopted stablecoins on their own (95% prefer them). You're not creating demand; you're organising existing demand.
- **Regulatory door opening (2024–25):** licensed operators now have a path.
- **Three value layers compound:** rails → AI data/credit → cross-border dollar settlement. Owning the combination is defensible.

### Where it's already crowded (don't go here head-on)
- **Generic POS / agent banking:** Moniepoint, OPay, PalmPay — won, capital-heavy, don't fight them.
- **Generic stablecoin remittance / freelancer payout:** Bitnob, Yellow Card, Hurupay, Payd, Noah, Yogupay, TransFi, plus Strike — getting crowded fast.
- **Generic B2B retail BNPL:** Sabi, TradeDepot, OmniRetail.

### The sharp, still-open niches (pick one wedge)
1. **The "dollar operating account" for the informal cross-border trader** — the Nigerian importer/exporter who buys from China/UAE and sells in local markets. Bundle: USDT settlement to suppliers + AI credit underwritten by their trade/POS history + naira off-ramp + invoicing in local language. *No incumbent owns this full stack for this user.*
2. **AI credit-as-a-service on stablecoin rails** — underwrite working capital for micro-merchants using alternative data, *disbursed and repaid in stablecoins*, removing naira-devaluation risk from the loan book.
3. **Voice-first, local-language financial assistant** for low-literacy informal owners (bookkeeping + savings-in-dollars + payments), USSD/WhatsApp/voice.
4. **The reliable off-ramp / liquidity layer** others build on (B2B infra play).

### Risks (rate them honestly)
- **Regulatory (highest):** policy can whipsaw (Feb 2021 ban, Feb 2024 Binance crackdown). *Mitigate:* license up, stay compliant, avoid being the FX scapegoat.
- **FX / peg / volatility:** stablecoin de-peg or issuer risk; naira off-ramp spreads.
- **Adoption & trust:** scam stigma, low literacy, feature phones.
- **Incumbent encroachment:** Moniepoint/OPay can add stablecoins; move fast on the *specific* wedge they're slow to serve (cross-border).
- **Margins / liquidity costs:** thin spreads; capital-intensive to hold float.

### Bottom line
The broad theme (informal economy + fintech) is **proven and partly saturated at the rails layer**. The *specific* combination — **AI-underwritten, stablecoin-settled, dollar-denominated financial services for the informal cross-border trader and freelancer, delivered in local language with a reliable naira off-ramp and a real license** — is **early, large, and defensible.** That is the niche. The winner won't be "a Bitcoin company" or "an AI company"; it'll be a **financial-services company for the informal economy that uses AI to underwrite and stablecoins to settle**, with crypto invisible to the user.

---

## Key figures at a glance

| Metric | Value | Source |
|---|---|---|
| Informal employment, Africa | ~83% | ILO/UN 2024 |
| Informal employment, Sub-Saharan Africa | ~85% | ILO |
| Informal employment, Central / West Africa | ~92.5% / ~91.8% | ILO 2024 |
| Nigeria informal share of GDP | ~42.5% (revised); up to 57–65% older est. | NBS / IMF |
| Nigeria youth (15–24) informal | ~98% | ILO |
| Nigeria MSMEs that are informal | ~89% of ~40m | Moniepoint 2025 |
| Africans unbanked (SSA) | 350m+ adults | World Bank |
| Informal-economy credit gap (Africa) | ~$700bn | FurtherAfrica/AInvest |
| Nigeria global crypto adoption rank | #2 | Chainalysis 2024 |
| Nigeria crypto inflows (Jul'23–Jun'24) | ~$59bn | Chainalysis |
| Nigeria stablecoin volume (Jul'23–Jun'24) | ~$22–26bn (~43% of SSA crypto) | Chainalysis |
| Nigerians preferring stablecoin pay (2026 survey) | 95% | BVNK |
| Nigeria diaspora remittances 2024 | $20.93bn (~4–6% GDP; ~37% of SSA) | World Bank / Nairametrics |
| Traditional vs stablecoin remittance cost | ~6–8% / 3–5 days → ~1.5–2.5% / ~60s | Web3 Enabler |
| Lightning fee on $50 payment | $0.01–0.03 vs $3.25 traditional | Plaitr/industry |
| Bitnob Lightning volume growth | +340% YoY, 23 countries | Bitnob |
| Moniepoint POS merchants | ~2.3m businesses (Jan 2025) | Rest of World |
| Nigeria B2B BNPL market | $1.75bn+ | 2026 industry report |
| Informal owners w/o 1 month savings (Nigeria) | 42% | Moniepoint 2025 |
| Informal owners who started due to unemployment | 38% | Moniepoint 2025 |

---

## Sources

**Informal economy size & structure**
- [Nigeria's informal economy in five charts — TC Insights](https://insights.techcabal.com/nigerias-informal-economy-in-five-charts/)
- [Nigeria's informal economy accounts for 65% of GDP – IMF (Business AM)](https://businessamlive.com/nigerias-informal-economy-accounts-65-gdp-imf/)
- [Nigeria Shadow Economy 2000–2025 — World Economics](https://www.worldeconomics.com/National-Statistics/Informal-Economy/Nigeria.aspx)
- [ILO Nigeria policy brief (Nov 2024, PDF)](https://www.ilo.org/sites/default/files/2024-11/Nigeria%20policy%20brief%207%20Nov.pdf)
- [ILO Africa Informality Regional Statistical Profile (PDF)](https://www.ilo.org/sites/default/files/2025-02/Africa_Informality%20Regional%20statistical%20profile.pdf)
- [Africa's informal economy employs 83% of workforce in 2024 — North Africa Post](https://northafricapost.com/96624-africas-informal-economy-employs-83-of-workforce-in-2024-un-data.html)
- [World Bank — Urban Informality in Sub-Saharan Africa (PDF)](https://documents1.worldbank.org/curated/en/099417402142413528/pdf/IDU1e9d2d68a110ad14aaa1af9a110e90bd603f1.pdf)
- [WIEGO — Informal Economy Statistical Picture](https://www.wiego.org/informal-economy/statistical-picture/)

**Why informality persists**
- [Bridging the Divide: Nigeria's Formal & Informal Sectors — Opinion Nigeria](https://www.opinionnigeria.com/bridging-the-divide-uniting-nigerias-formal-and-informal-sectors-for-prosperity-by-dovish-okojie/)
- [The informal economy is both a safety net and a drain — Africa at LSE](https://blogs.lse.ac.uk/africaatlse/2025/07/02/the-informal-economy-is-both-a-safety-net-and-a-drain-on-resources/)
- [Nigeria's tax reforms may deepen informal economy shift — Businessday](https://businessday.ng/business-economy/article/nigerias-tax-reforms-may-deepen-informal-economy-shift/)

**Enabling businesses & platforms**
- [Moniepoint leads Nigerian fintech along with OPay — Rest of World](https://restofworld.org/2024/nigeria-fintech-moniepoint/)
- [Moniepoint 2025 Informal Economy Report](https://informalreport.moniepoint.com/)
- [Only 1 in 4 informal businesses earn 10% of revenue digitally — TechCabal](https://techcabal.com/2025/10/17/moniepoint-informal-economy-report-2025-nigeria-digital-payments/)
- [Nigeria B2B BNPL Report 2026: $1.75bn market (TradeDepot, Sabi, Moniepoint) — GlobeNewswire](https://www.globenewswire.com/news-release/2026/04/22/3279189/28124/en/Nigeria-B2B-Buy-Now-Pay-Later-Business-Report-2026-1-75-Billion-Market-Expands-as-TradeDepot-Sabi-and-Moniepoint-Scale-Embedded-SME-Credit-While-Major-Banks-Leverage-Data-and-Fundi.html)
- [OmniRetail, M-KOPA, Sabi on FT Africa fastest-growing list — TechCabal](https://techcabal.com/2026/05/12/30-startups-on-ft-africas-fastest-growing-companies-list/)

**AI for the informal economy**
- [AI Credit Scoring: Unlocking Africa's Invisible Economy — FurtherAfrica](https://furtherafrica.com/2025/09/24/ai-credit-scoring-unlocking-africas-invisible-economy/)
- [Alternative Credit Scoring in Africa — In-Depth Research](https://indepthresearch.org/blog/alternative-credit-scoring-in-africa/)
- [AI-Powered Credit Scoring for SMEs — Kifiya](https://kifiya.com/2025/03/07/ai-powered-credit-scoring-unlocking-opportunities-for-small-businesses-in-africa-and-other-emerging-markets/)
- [ML-Based Credit Scoring for Informal African Merchants — Springer](https://link.springer.com/article/10.1007/s44230-025-00105-6)

**Bitcoin, stablecoins & crypto adoption**
- [Sub-Saharan Africa: Nigeria Takes #2 — Chainalysis 2024](https://www.chainalysis.com/blog/subsaharan-africa-crypto-adoption-2024/)
- [Stablecoins, DeFi boost Nigeria to #2 — CryptoSlate/Chainalysis](https://cryptoslate.com/stablecoins-defi-boost-nigeria-to-second-in-global-crypto-adoption-rankings-chainalysis/)
- [Grassroots Cryptocurrency Adoption in Nigeria — Cornell](https://business.cornell.edu/article/2025/08/grassroots-cryptocurrency-adoption/)
- [Stablecoin Remittances to Africa & MENA — Web3 Enabler](https://web3enabler.com/blog/stablecoin-remittances-faster-cheaper-cross-border-payments-to-africa-and-mena/)
- [Stablecoins in Nigeria Gain Ground in Cross-Border Trade — Serrari Group](https://serrarigroup.com/stablecoins-in-nigeria-gain-ground-in-cross-border-trade/)
- [How Africans use stablecoins to survive inflation — Cointelegraph](https://cointelegraph.com/news/how-africans-are-using-stablecoins-to-survive-inflation)
- [Strike partners with Bitnob for Bitcoin-powered remittances — Mariblock](https://www.mariblock.com/stories/strike-partners-with-bitnob-to-facilitate-bitcoin-powered-remittances-to-africa)
- [Bitnob Is Building Global Crypto Infrastructure From Africa — The Condia](https://thecondia.com/bitnob-global-crypto-infrastructure-africa/)
- [Lightning Network for merchant payments: 2026 reality check — Plaitr](https://www.plaitr.com/blog/lightning-network-for-merchant-payments-a-2026-reality-check)
- [How Hurupay processed $50m for Africa's freelancers — TechCabal](https://techcabal.com/2026/03/18/hurupay-crosses-50m-processing-freelancer-payments/)
- [Payd, Noah launch stablecoin payments for African freelancers — TechCabal](https://techcabal.com/2026/02/12/payd-noah-launch-stablecoin-payments/)

**Regulation**
- [Nigeria's crypto comeback: SEC approves local exchanges post-Binance — The Africa Report](https://www.theafricareport.com/360383/nigerias-crypto-comeback-sec-approves-local-exchanges-post-binance-ban/)
- [CBN Crypto Policy Evolution: From Ban to Regulation — AINFP](https://ainfp.org/central-bank-of-nigeria-crypto-policy-evolution-from-ban-to-regulation)
- [Blockchain 2025 – Nigeria Trends & Developments — Chambers](https://practiceguides.chambers.com/practice-guides/blockchain-2025/nigeria/trends-and-developments)
- [Updated overview of Nigeria's cryptocurrency landscape — IBA](https://www.ibanet.org/Updated-overview-of-Nigerian-cryptocurrency-landscape)

**Remittances**
- [Diaspora remittances to Nigeria hit $20.93B in 2024 — Nairametrics](https://nairametrics.com/2025/07/26/diaspora-remittances-to-nigeria-hit-20-93b-in-2024/)
- [Personal remittances received (% of GDP), Nigeria — World Bank](https://data.worldbank.org/indicator/BX.TRF.PWKR.DT.GD.ZS?locations=NG)

*Note: figures dated 2026 reflect industry reports published after this research's nominal date; treat the most recent single-source statistics as indicative rather than audited. Where ranges appear (e.g. Nigeria informal share of GDP), they reflect genuine methodological disagreement between sources, not error.*
