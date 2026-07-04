# The Off-Ramp & Liquidity Layer: Stablecoin Picks-and-Shovels in Nigeria & Africa

*A deep dive on the infrastructure business of turning USDT/USDC into spendable naira — and back — analyzed as a standalone opportunity, not an app feature.*

---

## 1. The Core Problem: The Last-Mile of Money

A stablecoin is only as useful as your ability to spend it. USDT sitting in a Tron wallet pays no rent in Lagos. The entire value proposition of dollar stablecoins for Africans — beating ~9% remittance fees, escaping a naira that lost roughly **70% of its value against the USD between June 2023 and early 2025** ([Orbitt Capital](https://orbitt.capital/managing-currency-risk-in-africa-a-playbook-for-decision-making/)) — collapses at the conversion boundary. That boundary is the off-ramp.

**On-ramp vs. off-ramp mechanics.** An *on-ramp* takes local fiat (naira in a bank account) and outputs crypto (USDT/USDC) in a wallet. An *off-ramp* does the reverse: stablecoin in, naira in a bank account out. Crucially, the two are not symmetric. On-ramps are comparatively easy because demand for dollars is structural; off-ramps are hard. As Lisk's infrastructure analysis puts it, *"exiting crypto tends to trigger higher fees, slower settlement, and increased scrutiny, particularly as transaction size or frequency increases"* ([Lisk](https://lisk.com/blog/posts/on-off-ramps-crypto/)). The off-ramp requires someone, somewhere, to be holding naira and *willing to part with it* in exchange for stablecoin — at a fair price, instantly, without their bank account being frozen. That "someone holding naira" is the liquidity layer, and it is the single hardest, most valuable bottleneck in African crypto.

Why valuable? Because the volume is enormous. Nigeria received roughly **$92.1 billion in on-chain value between July 2024 and June 2025** — nearly triple South Africa and the largest stablecoin economy outside the US — with **over 65% of inflows stablecoin-denominated** ([Chainalysis 2025](https://www.chainalysis.com/blog/subsaharan-africa-crypto-adoption-2025/); [TechCabal](https://techcabal.com/2026/06/15/how-stablecoins-became-part-of-nigerias-central-banks-plan-for-payments/)). Every dollar of that flow eventually wants to touch the real economy, and someone provides the liquidity to make that happen.

---

## 2. How Off-Ramping Actually Works Today

The Nigerian off-ramp has evolved through three overlapping eras, each a response to the previous one breaking.

**Era 1 — P2P marketplaces (now degraded).** The dominant model until 2024 was peer-to-peer escrow. On Binance P2P, a seller posts USDT; a buyer pays naira by bank transfer; the platform holds the crypto in **escrow until the seller confirms naira receipt**, then releases it. This worked until it became a geopolitical target. Binance **suspended naira P2P on Feb 20, 2024, delisted the naira around March 1, and auto-converted residual NGN balances to USDT at ₦1,515/USDT on March 8, 2024** ([Binance](https://www.binance.com/en/support/announcement/binance-to-discontinue-all-nigerian-naira-ngn-services-f9857dc2fea4448ba1fb8815d87d8144); [DL News](https://www.dlnews.com/articles/regulation/binance-delists-nigerian-naira-from-its-exchange/)). Users scattered to Bybit, KuCoin, OKX, and informal Telegram/WhatsApp desks *"where scams, fake receipts, and identity fraud are rampant"* ([Azasend](https://azasend.com/news/binance-p2p-ban-in-nigeria-reasons-timeline-and-a-safer-alternative-for-crypto-traders/)).

**Era 2 — OTC desks and liquidity providers.** Most Nigerian crypto startups now run **OTC desks alongside retail**, serving whales, businesses, and *other startups* needing bulk liquidity ([TechCabal](https://techcabal.com/2026/04/25/why-nigerian-startups-expand-beyond-crypto-retail-trading/)). The "liquidity providers" are frequently the same P2P traders, just KYC'd more rigorously and aggregated. This is the wholesale layer that consumer apps quietly plug into.

**Era 3 — Hybrid finance apps (virtual accounts).** The current frontier removes escrow and counterparty matching entirely. Apps like Prestmit (**700,000+ users**), Taja, Palremit, Breet (~250,000 users), and at least **20 such startups** give each user a **virtual bank account** via a payment processor, let them sell USDT directly to the app, and pay out naira over the NIBSS Instant Payment (NIP) rail — Monica markets settlement *"in under 60 seconds"* ([TechCabal](https://techcabal.com/2025/03/13/hybrid-finance-apps/); [Monica](https://monica.cash/)). The user never meets a counterparty; the app *is* the counterparty, sourcing liquidity from OTC desks behind the scenes.

**Where it breaks.** The flow has three structural failure points:

| Break point | Mechanism | Evidence |
|---|---|---|
| **Rails risk** | Platforms get killed by regulators | Binance naira P2P shutdown (Feb–Mar 2024) |
| **Banking risk** | A seller's naira is frozen *after* releasing crypto | EFCC froze **₦548.6m across 22 accounts** (Sept 2024); court order on **1,146 accounts** (April 2024); Moniepoint/PalmPay/Paga/OPay threatened to close crypto-linked accounts (May 2024) |
| **Price/liquidity risk** | Thin order books → slippage, delay, manipulated street rate | OTC net margins as thin as **0.1%**; P2P spreads of 1.5–3%; "fake ad" rate manipulation alleged |

Sources: [Nairametrics](https://nairametrics.com/2024/09/11/court-freezes-n548-6-million-belonging-to-bybit-kucoin-nigerian-crypto-users-over-naira-fluctuation-allegations/), [TechCabal](https://techcabal.com/2024/05/03/p2p-crypto-ban-imminent/), [Techpoint](https://techpoint.africa/2024/05/02/moniepoint-paga-to-block-accounts-crypto-trading/). This "P2P de-banking" is the defining operational hazard: the off-ramp business is, at root, a bet on keeping naira liquidity *unfrozen and replenishable*.

---

## 3. The FX Dimension: The Spread Is the Business

Stablecoins redeem 1:1 — there is *"no spread on properly priced rails"* on the redemption itself ([Eco](https://eco.com/support/en/articles/15039727-how-to-off-ramp-crypto-2026-guide-for-usdc-usdt-eth)). So **the liquidity provider's entire margin is the FX spread**: the gap between the rate at which it acquires naira/USDT and the rate it offers customers.

For most of crypto's Nigerian boom this spread was fat because the *currency itself* was dislocated. After the **June 14, 2023 float** (naira fell ~23% in a day, ₦464→₦600) and the **February 2024 devaluation** (₦898→₦1,400 in days), the parallel-market premium over the official rate hit **62% in May 2023** ([BusinessDay](https://businessday.ng/business-economy/article/naira-parallel-market-nears-official-on-reforms/)). During the Feb 2024 crisis, USDT traded ~₦1,650 while banks quoted ~₦1,400 — an **~18% premium** that off-ramp desks operated inside ([CCN](https://www.ccn.com/news/binance-nigeria-naira-10billion/)).

That window is now closing. CBN reforms drove the official–parallel premium down to **~2.1% by December 2025**, with daily volatility falling from >4% (2024) to ~0.5% (May 2026) ([Nairametrics](https://nairametrics.com/2026/05/06/how-a-stable-naira-is-quietly-fixing-nigeria/)). **A stable naira compresses the off-ramp's structural margin.** This is the single most important macro fact for the business model: the easy money (arbitraging a broken currency) is largely gone; the durable money is in *operational* spread on volume.

**Liquidity sourcing & treasury.** A provider needs two inventories: naira (sourced from bank partners, IMTO settlement flows, and traders' deposits) and dollars/USDT (from global markets, OTC, or partners like Circle Mint). Yellow Card explicitly sells *"treasury management, and access to hard currency liquidity"* with *"deep liquidity across key corridors"* ([Yellow Card](https://yellowcard.io/about-us)).

**FX risk.** Whoever holds naira inventory eats devaluation risk — the 70% drawdown above is the nightmare scenario. A sophisticated insight from a 1,835-trading-day study: a widening *parallel-vs-official* gap usually resolves through devaluation (hedge it), while a widening *crypto-vs-parallel* gap signals transient channel friction that self-corrects — *"hedging the two identically overpays on one and underpays on the other"* ([BusinessDay](https://businessday.ng/opinion/article/why-nigerias-crypto-ban-added-friction-without-stabilising-the-naira/)). Hedging tools now exist (naira-settled OTC NDF futures referencing the I&E window), but the cleanest defense is *velocity*: hold inventory for minutes, not days.

---

## 4. Who Provides the Infrastructure Today

The market is splitting into two layers: **global stablecoin orchestration/issuance** (Bridge, Conduit, BVNK, Noah) and **Africa-native last-mile rails with licensing** (Yellow Card, Onafriq, Bitnob, Fonbnk, Juicyway). The global players increasingly *partner with* the African ones for distribution.

| Provider | Layer | Model | Scale | Funding | Gap |
|---|---|---|---|---|---|
| **Yellow Card** | Africa B2B/liquidity | Spread + API, treasury, 20–34 countries | >$3B (2024), 30k businesses, 99% stablecoin | $33M Series C (Oct 2024, Blockchain Capital); ~$85M total | Exited retail Nov 2025; thin-margin B2B |
| **Onafriq** (ex-MFS Africa) | Pan-African rails | Interop hub adding crypto via partners | 500M+ wallets, 35+ countries, 300k agents | $100M Series C (2021) | Not crypto-native; depends on Ripple/Circle/Conduit |
| **Juicyway** | Cross-border B2B+consumer | Liquidity pools + API, FX | $1.3B / 25k txns / 4k users (stealth) | $3M pre-seed (Dec 2024) | Very early; no consumer brand |
| **Fonbnk** | On/off-ramp + agents | Airtime/mobile-money ↔ USDC | Multi-chain; opaque volume | ~$3.6M (Mastercard/Circle backed) | Small; telco-dependent margins |
| **Bitnob** | Consumer + B2B infra | BTC+stablecoin, cards, payouts, OTC | $4.5B cumulative, 110+ payout countries | YC-backed; amounts opaque | Funding transparency |
| **Busha / Quidax** | Consumer exchange (+API) | Buy/sell/store; OTC; embed API | Busha 800k users; Quidax 70+ countries | Busha $4.2M seed; Quidax undisclosed | Exchange model, not ramp infra; *first SEC provisional licenses* |
| **Conduit** | Global B2B orchestration | Fee + FX spread, SWIFT alternative | $10B annualized; 16x in 2024 | $36M Series A (May 2025) | Not Africa-native (serves via Onafriq) |
| **Bridge (Stripe)** | Global orchestration + issuance | One API across chains/fiat; issues USDB | 7 chains; OCC trust charter (2026) | **$1.1B Stripe acquisition** | *Excludes Nigeria/SA/Ghana* — local players build on it |
| **Lazerpay** | Payment gateway | Merchant stablecoin acceptance | **Defunct April 2023** | $1.1M pre-seed | Couldn't raise — cautionary tale |
| **Aggregators** (Onramper, Transak, Noah, Cybrid, BVNK) | Global LaaS | Routing/orchestration APIs | BVNK ~$30–36B annualized | Noah $22M seed; BVNK well-funded | Africa only via underlying local rails |

Sources: [TechCrunch/Yellow Card](https://techcrunch.com/2024/10/16/african-crypto-startup-yellow-card-raises-33m-led-by-blockchain-capital-to-scale-its-b2b-pivot/), [TechCrunch/Juicyway](https://techcrunch.com/2024/12/16/this-stealthy-african-stablecoin-startup-already-processed-over-1b-in-cross-border-payments/), [CoinDesk/Conduit](https://www.coindesk.com/business/2025/05/28/conduit-raises-36m-to-expand-stablecoin-based-cross-border-payments-beyond-swift), [CNBC/Bridge](https://www.cnbc.com/2025/02/04/stripe-closes-1point1-billion-bridge-deal-prepares-for-stablecoin-push-.html), [Ledger Insights](https://www.ledgerinsights.com/stripe-rolls-out-stablecoin-accounts-in-101-countries-as-bridge-launches-usdb/), [Onafriq/Ripple](https://www.businesswire.com/news/home/20231107602363/en/), [Mariblock/Yellow Card retail](https://www.mariblock.com/stories/why-yellow-card-shuttered-its-retail-business-2).

**The telling signal:** Yellow Card, the category leader, *killed its retail app in November 2025 to go all-in on B2B liquidity infrastructure*. The smart money has concluded the value is in the picks-and-shovels, not the storefront.

---

## 5. Business Models & Unit Economics

| Model | How it earns | Realistic economics | Capital intensity |
|---|---|---|---|
| **(a) Spread / FX margin** | Buy-sell rate gap | Retail P2P 1.5–3%; B2B configurable 0–10%; Yellow Card "well into eight figures" on spread | Medium |
| **(b) Liquidity-as-a-Service API** | Per-txn take rate | Bridge **~10 bps + network fee**; Stripe flat 1.5%; Transak 0.5–5.5%; Juicyway **0.2–10%** | Low (thin infra) to high (if holding float) |
| **(c) Agent cash-out network** | Margin on physical cash-in/out | Market maker buys stablecoin for local fiat, resells into global demand | High (cash logistics) |
| **(d) Treasury / float yield** | Yield on stablecoin balances | BVNK/Juicyway plan "interest on customer balances" | Low (yield *on* float you'd hold anyway) |
| **(e) Settlement / clearing** | Replace correspondent banking | Bypasses nostro-vostro; frees **$15–25M trapped transit funds** per deployment | Very high |

The unit-economics punchline: **blockchain cross-border lands at 0.1–0.5% all-in vs. 6–9% for traditional Sub-Saharan remittances** (World Bank SSA average **8.78%**, Q1 2025) ([World Bank RPW](https://remittanceprices.worldbank.org/sites/default/files/2026-04/RPW_main_report_and_annex_Q325.pdf); [a16z](https://a16zcrypto.com/posts/article/stablecoin-data-charts/)). That ~6-point cost wedge is the prize — but as the naira stabilizes, you capture it through *volume and velocity*, not fat per-transaction spreads.

**Float is the crux.** Operating an off-ramp means *"having the funds to cover a payout before incoming payments settle"* ([FXC Intelligence](https://www.fxcintel.com/research/analysis/stablecoin-infrastructure-liquidity-explainer/)). You pre-fund naira so the customer gets paid in 60 seconds while your stablecoin leg settles later. This working-capital tax scales with every market you serve — which is precisely why LaaS providers (Arf, Visa Direct) sell *revolving stablecoin liquidity with 1–5 day repayment* as a product. **Whoever finances the float captures a structural toll.**

---

## 6. Defensibility vs. Risk

**The moat is liquidity depth, and it compounds.** Thin liquidity means slippage, delay, and unreliable pricing; deep liquidity means tight quotes and instant settlement — which attracts more flow, which deepens liquidity ([a16z](https://a16zcrypto.com/posts/article/global-finance-stablecoins-new-stack)). Layered on top: **per-jurisdiction licenses, local banking relationships, and treasury scale** that take years and capital to assemble ([Lisk](https://lisk.com/blog/posts/on-off-ramps-crypto/)). Yellow Card's 20–34-country licensed footprint is not copy-pasteable.

| Moat | Risk |
|---|---|
| Liquidity depth → tighter spreads → more flow (network effect) | **Capital intensity** — float and treasury are a working-capital tax |
| Per-country licensing (SEC/CBN, FSCA, CBK) as a barrier | **Regulatory whiplash & de-banking** — frozen accounts, P2P bans, the Binance saga ($10B demand, 8-month detention) |
| Banking relationships hard to replicate | **Margin compression** — a stabilizing naira (2.1% premium) thins the easy spread |
| First-mover data/corridor depth | **Incumbent encroachment** — Stripe/Bridge, Visa, banks adding stablecoin rails |

The regulatory ground is actually *firming up*, which favors licensed infrastructure over informal P2P: Nigeria's **ISA 2025 classifies digital assets as securities** under SEC jurisdiction, CBN lifted its bank ban (Dec 2023) and issued VASP account guidelines, and **Quidax and Busha hold provisional SEC licenses** ([Nairametrics](https://nairametrics.com/2025/04/04/isa-2025-nigeria-formally-recognizes-cryptocurrency-as-securities-in-new-sec-act-2025/); [Techpoint](https://techpoint.africa/insight/nigerias-sec-grants-crypto-licence-to-busha-and-quidax/)). South Africa's FSCA has approved ~300 CASP licenses; Kenya's VASP Act commenced Nov 2025. Regulation kills the informal off-ramp and *raises the moat* for the compliant one.

---

## 7. Strategic Takeaway

**Yes — the liquidity/off-ramp layer is a stronger wedge than a consumer app.** The evidence is unambiguous: consumer crypto in Nigeria is a commoditized race (20+ near-identical hybrid apps, OTC net margins of 0.1%, "the market is saturated"), while the category leader Yellow Card *exited retail entirely* to become infrastructure. Consumer apps live or die on the liquidity layer beneath them — so own the layer, and you tax all of them. The Stripe/Bridge thesis confirms it at the global level: the $1.1B value was in the orchestration API, and Bridge *excludes Nigeria*, leaving the African last-mile to local players who can become the indispensable plug.

**Who should build it:** an operator with (1) banking and licensing relationships in-country, (2) access to float/treasury capital, and (3) a B2B sales motion — not a consumer-growth team. The natural builders are existing OTC desks formalizing into LaaS, or a well-capitalized new entrant partnering with a global orchestrator (Bridge/Conduit) for the rails while owning the Nigerian liquidity and licenses.

**What the MVP looks like:**
- **B2B API-first, not consumer.** Sell "USDT-in, naira-in-bank-out in 60 seconds" as an API to the 20+ apps, payroll/remittance startups, and businesses that currently each rebuild this badly.
- **Aggregate liquidity before holding your own float.** Start as a smart router across existing OTC desks and P2P-pro liquidity (capital-light, fast to launch), then graduate to holding proprietary float only on proven, high-velocity corridors where you can finance and hedge it.
- **Velocity over spread.** Win on reliability and settlement speed (uptime through de-banking events via diversified bank partners), price near the market rate, and monetize on volume + float yield + a thin, transparent take rate — the Juicyway/Yellow Card playbook.
- **Compliance as product.** A licensed, KYC'd, audit-friendly off-ramp is what lets institutional flow off the informal P2P rails — that *is* the differentiated wedge as the naira stabilizes and regulators tighten.

The off-ramp is not a feature. It is the toll booth on $90B+ of annual flow, and the toll booth is a better business than any of the cars passing through it.

---

## Sources

- [Chainalysis — Sub-Saharan Africa Crypto Adoption 2025](https://www.chainalysis.com/blog/subsaharan-africa-crypto-adoption-2025/)
- [Chainalysis — Sub-Saharan Africa Crypto Adoption 2024](https://www.chainalysis.com/blog/subsaharan-africa-crypto-adoption-2024/)
- [TechCabal — How stablecoins became part of CBN's payments plan](https://techcabal.com/2026/06/15/how-stablecoins-became-part-of-nigerias-central-banks-plan-for-payments/)
- [TechCabal — After P2P, hybrid finance apps take off](https://techcabal.com/2025/03/13/hybrid-finance-apps/)
- [TechCabal — Why Nigerian startups expand beyond retail trading](https://techcabal.com/2026/04/25/why-nigerian-startups-expand-beyond-crypto-retail-trading/)
- [TechCabal — P2P crypto ban imminent](https://techcabal.com/2024/05/03/p2p-crypto-ban-imminent/)
- [TechCabal — Yellow Card closes retail app, turns to enterprises](https://techcabal.com/2025/11/03/yellow-card-closes-retail-app-turns-to-enterprises/)
- [Binance — Discontinue all naira services](https://www.binance.com/en/support/announcement/binance-to-discontinue-all-nigerian-naira-ngn-services-f9857dc2fea4448ba1fb8815d87d8144)
- [DL News — Binance delists naira](https://www.dlnews.com/articles/regulation/binance-delists-nigerian-naira-from-its-exchange/)
- [Nairametrics — Court freezes ₦548.6m of Bybit/KuCoin users](https://nairametrics.com/2024/09/11/court-freezes-n548-6-million-belonging-to-bybit-kucoin-nigerian-crypto-users-over-naira-fluctuation-allegations/)
- [Techpoint — Moniepoint, Paga to block crypto accounts](https://techpoint.africa/2024/05/02/moniepoint-paga-to-block-accounts-crypto-trading/)
- [Fortune — Binance exec released after 8-month detention](https://fortune.com/crypto/2024/10/23/binance-exec-released-from-nigerian-prison-after-8-month-detention/)
- [CoinDesk — Binance moved $26B untraceable funds (Cardoso)](https://www.coindesk.com/policy/2024/02/28/binance-nigeria-moved-26b-worth-of-untraceable-funds-in-2023-central-bank-chief-says-reports)
- [Nairametrics — ISA 2025 recognizes crypto as securities](https://nairametrics.com/2025/04/04/isa-2025-nigeria-formally-recognizes-cryptocurrency-as-securities-in-new-sec-act-2025/)
- [Nairametrics — CBN releases VASP guidelines](https://nairametrics.com/2023/12/22/cbn-releases-guidelines-for-regulating-virtual-assets-in-nigeria/)
- [Techpoint — SEC grants crypto licences to Busha and Quidax](https://techpoint.africa/insight/nigerias-sec-grants-crypto-licence-to-busha-and-quidax/)
- [BusinessDay — Naira parallel market nears official on reforms](https://businessday.ng/business-economy/article/naira-parallel-market-nears-official-on-reforms/)
- [Nairametrics — How a stable naira is quietly fixing Nigeria](https://nairametrics.com/2026/05/06/how-a-stable-naira-is-quietly-fixing-nigeria/)
- [BusinessDay — Why Nigeria's crypto ban added friction (1,835-day study)](https://businessday.ng/opinion/article/why-nigerias-crypto-ban-added-friction-without-stabilising-the-naira/)
- [Orbitt Capital — Managing currency risk in Africa](https://orbitt.capital/managing-currency-risk-in-africa-a-playbook-for-decision-making/)
- [TechCrunch — Yellow Card raises $33M Series C](https://techcrunch.com/2024/10/16/african-crypto-startup-yellow-card-raises-33m-led-by-blockchain-capital-to-scale-its-b2b-pivot/)
- [TechCrunch — Juicyway processes $1B+ in stealth](https://techcrunch.com/2024/12/16/this-stealthy-african-stablecoin-startup-already-processed-over-1b-in-cross-border-payments/)
- [CoinDesk — Conduit raises $36M Series A](https://www.coindesk.com/business/2025/05/28/conduit-raises-36m-to-expand-stablecoin-based-cross-border-payments-beyond-swift)
- [CNBC — Stripe closes $1.1B Bridge deal](https://www.cnbc.com/2025/02/04/stripe-closes-1point1-billion-bridge-deal-prepares-for-stablecoin-push-.html)
- [Ledger Insights — Stripe stablecoin accounts in 101 countries (excl. Nigeria)](https://www.ledgerinsights.com/stripe-rolls-out-stablecoin-accounts-in-101-countries-as-bridge-launches-usdb/)
- [Businesswire — Ripple partners with Onafriq](https://www.businesswire.com/news/home/20231107602363/en/Ripple-partners-with-Onafriq-to-power-digital-asset-enabled-cross-border-payments-between-Africa-and-the-rest-of-the-world)
- [Mariblock — Why Yellow Card shuttered retail](https://www.mariblock.com/stories/why-yellow-card-shuttered-its-retail-business-2)
- [TechCabal — Lazerpay shuts down](https://techcabal.com/2023/04/13/crypto-and-web3-startup-lazerpay-shuts-down/)
- [TechCrunch — Cedar Money $9.9M seed](https://techcrunch.com/2025/01/30/qed-seeds-9-9m-in-cedar-money-a-stablecoin-payment-platform/)
- [FXC Intelligence — Stablecoin infrastructure & liquidity explainer](https://www.fxcintel.com/research/analysis/stablecoin-infrastructure-liquidity-explainer/)
- [Lisk — On and off ramps: the underestimated infrastructure](https://lisk.com/blog/posts/on-off-ramps-crypto/)
- [a16z — The new stack for global finance (stablecoins)](https://a16zcrypto.com/posts/article/global-finance-stablecoins-new-stack)
- [a16z — Stablecoin data & charts (State of Crypto 2025)](https://a16zcrypto.com/posts/article/stablecoin-data-charts/)
- [World Bank — Remittance Prices Worldwide Q3 2025](https://remittanceprices.worldbank.org/sites/default/files/2026-04/RPW_main_report_and_annex_Q325.pdf)
- [Jas Shah — BVNK: Banking on Stablecoin](https://jasshah.substack.com/p/bvnk-stablecoin-infrastructure)
- [DLA Piper Africa — FSCA CASP licensing update](https://www.dlapiperafrica.com/en/south-africa/insights/2026/FSCA_Update_on_Licensing_and_Supervision_of_Crypto_Asset_Service_Providers)
- [Dentons — Kenya VASP Act 2025](https://www.dentonshhm.com/en/insights/articles/2025/november/19/kenyas-crypto-leap-the-virtual-asset-service-providers-act-2025-ushers-in-a-new-regulatory-dawn)
- [Yellow Card — About / liquidity & treasury](https://yellowcard.io/about-us)
- [Breet — Off-ramp platforms & business API](https://breet.io/business/api)
- [WEF — GENIUS Act stablecoin regulation](https://www.weforum.org/stories/2025/07/stablecoin-regulation-genius-act/)
