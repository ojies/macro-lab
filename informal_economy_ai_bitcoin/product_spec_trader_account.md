# Product Specification — "Dollar Operating Account" for the Informal Cross-Border Trader & Freelancer (Nigeria)

*Spec v1 · 2026-06-29 · companion to [README.md](./README.md)*

**Working product name:** **TradeDollar** (placeholder) — *"Your dollar account that pays your supplier, banks your client, and lends you the difference — in your language, from WhatsApp."*

---

## 0. The one-paragraph thesis

Nigeria's informal importer already lives in dollars: she buys from China/UAE in USD-equivalent, sources FX on the parallel market or through informal agents who net naira against RMB via WeChat/Alipay, and prices her market stall against the street rate she heard this morning. She has *already adopted* stablecoins to do this — Nigeria moved ~$22–26bn in stablecoins in a single year, much of it import-linked. What she does **not** have is a single, licensed, low-literacy product that (1) settles her supplier in USDT in minutes, (2) gives her a reliable naira off-ramp at a transparent rate, (3) underwrites working capital from her own trade and POS history, and (4) talks to her in Pidgin/Hausa/Yoruba over WhatsApp, voice and USSD. Every incumbent does *one* slice of this for *formal, English-literate, app-comfortable* users. The wedge is the **other 89%** — the unregistered trader running on cash, trust and a smartphone she barely reads.

---

## 1. Target personas

### Persona A — "Mama Chinedu," the Onitsha/Alaba importer (PRIMARY)
- 38, runs a phone-accessories/auto-parts/textile stall; buys 1–4 containers a quarter from Guangzhou/Yiwu/Dubai via a sourcing agent.
- **FX today:** hands naira to an informal "China payment" agent in Lagos who nets it against RMB held in Alipay by Nigerians in China; or buys USDT P2P and her agent settles the supplier. Rate is opaque, she eats 3–6% spread + agent margin and has *zero recourse* if funds vanish.
- **Pain:** unpredictable rate, settlement risk, capital gap between paying upfront and selling out, no credit (banks won't touch her — no audited accounts, "informal").
- **Reads English haltingly; transacts in Igbo/Pidgin; lives on WhatsApp.** Has a Moniepoint/OPay POS terminal.

### Persona B — "Tunde," the freelancer/digital exporter (SECONDARY, beachhead)
- 27, designer/dev/VA billing US/EU clients $800–4,000/month, paid via USDT (TRC-20) or platforms like Deel.
- **Pain:** stranded dollars, wants to *hold* USD as inflation hedge but also spend naira; pays 1–2%+ to off-ramp via Grey/Geegpay; no credit against predictable invoices.
- App-comfortable, English-literate — **the easy on-ramp customer who funds the harder importer business and supplies dollar liquidity into the network.**

### Persona C — "Hajiya Amina," the cross-border regional trader (EXPANSION)
- Trades into Niger/Cameroon/Chad; needs CFA/cross-border settlement and naira off-ramp; even lower literacy, USSD/voice-first, intermittent connectivity.

> **Opinionated call:** Build for Persona A; acquire via Persona B. Tunde's predictable inbound dollars are the cheapest source of the USD liquidity Mama Chinedu needs to pay suppliers — the two personas are two sides of the *same internal FX book*. That is the structural advantage no single-sided player has.

---

## 2. Core Jobs-To-Be-Done

| # | JTBD (in user's words) | Who |
|---|---|---|
| J1 | "Pay my supplier in China/Dubai today, at a rate I can trust, and *prove* it arrived." | A, C |
| J2 | "Hold my money in dollars so the naira doesn't eat it before I restock." | A, B, C |
| J3 | "Turn dollars into naira fast, anywhere, at a fair rate — to a bank or my POS float." | All |
| J4 | "Lend me the gap between paying my supplier and selling the goods." | A, C |
| J5 | "Let my US client pay me, and let me decide later: keep dollars or take naira." | B |
| J6 | "Talk to me in my language, by voice or WhatsApp — I don't read long English." | A, C |
| J7 | "Don't get me arrested or my money frozen." (compliance/trust) | All |

J1 + J4 are the *unserved* jobs and the whole moat. J2/J3/J5 are table-stakes the incumbents already do.

---

## 3. Competitive landscape — and exactly where they fall short

| Player | What they do well | Gap for OUR user |
|---|---|---|
| **Juicyway** | $1B+ processed; multi-currency hold/send/receive, payment links, transparent P2P-priced rates; money-transmitter licensed (US/UK/CA/NG) | Built for **registered businesses**; English app-first; **no working-capital credit**; no local-language/USSD; treats user as a CFO, not a market trader |
| **Bitnob** | Lightning rails, virtual USD cards, savings, enterprise payouts across 23 countries | **Consumer/remittance + infra**, not a trader operating account; no trade-history underwriting; supplier-settlement to China not the focus |
| **Yellow Card** | Compliance-forward (Swiss SRO), treasury & stablecoin settlement for businesses across Africa | **Enterprise/treasury** tier; not a low-literacy retail trader product; no embedded credit on trade data |
| **Grey / Geegpay (Raenest)** | Cheap freelancer USD accounts (0.5–1% receive, low NGN withdrawal); virtual USD account numbers | **Inbound-only freelancer** focus; **no supplier payout to China/UAE**; no credit; no informal-trader UX |
| **Informal "China agents" / P2P** | Fast, negotiable, naira-in RMB-out, deeply trusted | **Unregulated, uninsured, no recourse**; opaque spread; the risk our product replaces |

**The white space, stated plainly:** *No licensed player bundles supplier-settlement + naira off-ramp + AI working-capital credit + local-language voice/USSD UX for the unregistered informal trader.* Juicyway is closest but aims up-market at registered businesses and omits credit. That is the entire opportunity.

---

## 4. Feature breakdown — MVP vs. later

### MVP (months 0–9) — *win J1, J2, J3, J5 for one corridor*
1. **Dollar (USDC/USDT) wallet** — balance shown as "$"; chain/gas/seed-phrase fully abstracted. Default TRC-20 (cheap, deep P2P liquidity); Solana as fallback.
2. **Supplier payout** — pay a China/UAE supplier from naira or dollar balance: user enters supplier WeChat/Alipay/bank or USDT address; we settle in USDT and (via on-the-ground partner) deliver RMB/AED or USDT, with a **delivery receipt + tracking**. This is the killer feature.
3. **Naira off-ramp** — sell dollars to bank account or **POS-agent float** at a *single transparent all-in rate* (mid-market + disclosed spread), settling in minutes.
4. **Freelancer inbound (Tunde)** — virtual USD account number + USDT deposit address; auto-convert or hold.
5. **WhatsApp + USSD + voice-note interface** in English, Pidgin, Hausa, Yoruba, Igbo; app is optional, not required.
6. **Tiered KYC** — phone + BVN/NIN for low tier; ID + selfie + address for higher limits; built ARIP-compliant from day one (no anonymous transactions).
7. **Rate alerts & receipts** — daily rate in local language; shareable proof-of-payment (trust artifact for the trader↔supplier relationship).

### V2 (months 9–18) — *win J4, the margin layer*
8. **AI working-capital credit** — underwrite a revolving "restock line" from the user's own data: supplier-payment cadence, POS/transaction inflows (open-banking/Mono + Moniepoint/OPay terminal data, with consent), wallet history, repayment behavior. **Disburse and repay in stablecoin** to keep naira-devaluation risk off the loan book; size loans to a single restock cycle (30–60 days).
9. **Trade invoicing & proforma capture** — photograph/forward a supplier proforma; AI extracts amount, supplier, goods → one-tap pay + auto-loan offer against it.
10. **POS-agent cash-out network** — partner with existing Moniepoint/OPay agents for physical naira cash-out (don't rebuild cash distribution).
11. **Multi-currency** — AED, RMB, USD; CFA for Persona C.

### V3 (months 18–36) — *platform & defensibility*
12. **Embedded insurance** (goods-in-transit, shipment) and **savings-in-dollars** (J2 deepened).
13. **Supplier-side network** — verified China/UAE supplier directory + escrow-style milestone payouts (releases on shipment proof) — turns single-sided payouts into a two-sided trade network.
14. **Credit-as-a-service API** — license the AI underwriting + stablecoin disbursement to B2B platforms (Sabi/TradeDepot-style) as infrastructure.
15. **Stablecoin debit card** (à la MiniPay/Bitnob) for spend.

---

## 5. Money-flow / settlement architecture

### 5.1 The internal FX book (the core insight)
Run an **internal liquidity pool** that nets two opposite flows:
- **Dollars IN:** freelancers (Persona B) receiving USDT/ACH; diaspora; treasury.
- **Dollars OUT / naira IN:** importers (Persona A) buying dollars to pay suppliers; naira off-rampers.

When inbound USD (Tunde) and outbound USD demand (Mama Chinedu) are matched internally, **we never touch a public P2P spread on that slice** — we capture the full bid-ask ourselves and pass a better rate to both sides. The unmatched residual is balanced via licensed exchange partners (Busha/Quidax) and OTC desks.

### 5.2 Supplier-payment rail (J1) — naira → supplier
```
Mama Chinedu (naira) ──► TradeDollar wallet
   │ (off internal book; residual via licensed OTC)
   ▼
USDC/USDT (TRC-20)  ──► China/UAE settlement partner
   │
   ├─► RMB to supplier Alipay/WeChat/bank   (Yogupay-style local agent network)
   ├─► AED to UAE supplier
   └─► USDT direct to supplier wallet
   ▼
Delivery receipt + tracking ──► back to user via WhatsApp
```

### 5.3 Off-ramp rail (J3) — dollar → naira
```
Dollar balance ──► sell at disclosed all-in rate ──►
   ├─► instant transfer to Nigerian bank (NIP)
   └─► POS-agent float / cash-out (Moniepoint/OPay agent network)
```

### 5.4 Credit rail (J4)
```
Consented data (POS terminal + bank inflows + supplier-payment cadence + wallet history)
   ▼
AI underwriting model (region/activity-specific, à la JUMO/Lulalend)
   ▼
Stablecoin restock line  ──► disbursed as USDT to pay supplier directly
   ▼
Repay in stablecoin from sales inflows  ──► loan book stays dollar-denominated (no FX risk)
```

**Why disburse/repay in stablecoin:** a naira loan to an importer is a bet against the naira you'll lose; a dollar loan that finances a dollar-denominated import and is repaid from naira sales *converted at point of repayment* keeps the lender whole and matches the trader's real economics.

---

## 6. Revenue model & unit economics

| Stream | Mechanism | Indicative take |
|---|---|---|
| **FX spread (supplier payout)** | Spread on naira→USD→supplier; richer when netted internally | **1.5–3.0%** all-in (vs. informal agent 3–6%) — *cheaper for user, more margin for us* |
| **Off-ramp spread** | Disclosed spread on USD→NGN | **0.8–1.5%** |
| **Freelancer inbound** | Receive + convert fee | **0.5–1.0%** (competitive with Grey/Geegpay to win them) |
| **Working-capital credit** | Interest + origination on restock line | **3–6% per 30–60-day cycle** (≈ the real margin) |
| **FX float / treasury** | Yield on idle dollar balances | spread-dependent |
| **Card / interchange (V3)** | Stablecoin card spend | ~0.5–1% interchange |

### Illustrative unit economics — one active importer
- Avg quarterly import: **$8,000**, ~3.3 cycles/yr → **~$26k/yr** supplier volume.
- Off-ramp volume (sales proceeds cycling back): **~$30k/yr**.
- Supplier-payout spread @ 2% on $26k = **$520**
- Off-ramp spread @ 1% on $30k = **$300**
- Credit: finances ~40% of restocks ($10.4k/yr) @ 4%/cycle = **~$420**
- **≈ $1,240 gross/active importer/yr.** At 5,000 active importers → **~$6.2m gross revenue**, before the larger freelancer base and card/treasury. CAC target < $15 via WhatsApp/agent referral; payback < 1 cycle.

> The spread business alone is thin and contested. **Credit is where this becomes a real business** — and credit is precisely what the trade + POS data uniquely enables and incumbents lack.

---

## 7. Go-to-market wedge

1. **Beachhead = ONE corridor, ONE market cluster.** Pick the **China→Onitsha/Alaba/Computer-Village electronics & parts corridor**. Win it deeply (agents embedded in the market, vernacular onboarding) before widening to Dubai/textiles.
2. **Acquire freelancers first for liquidity, importers for margin.** Run a cheap, best-in-class freelancer USD account (Persona B) to undercut Grey/Geegpay and *fill the dollar side of the internal book* — then spend that liquidity advantage on better supplier-payout rates that pull in importers.
3. **Agent-led, trust-first distribution.** Crypto carries scam stigma; recruit respected market-association members and existing POS agents as onboarding/cash-out agents. Human in the loop beats a slick app for this user.
4. **Lead with the supplier-payment receipt.** The shareable proof-of-payment is a viral trust artifact inside tight market trade networks — one successful container settlement sells the next ten.
5. **Compliance as marketing.** Post-Binance, "licensed by SEC under ARIP, your money is traceable and protected" is a *differentiator* vs. informal agents, not just a cost.

---

## 8. Regulatory & compliance plan

- **Enter SEC ARIP** (Accelerated Regulatory Incubation Program) → Approval-in-Principle → supervised operations under **ISA 2025**, which now puts virtual assets under SEC oversight. Mandatory: full KYC/AML/CFT (no anonymous transactions), governance, tech-risk, capital adequacy, investor protection, reporting.
- **Capital:** budget for the **₦500m minimum share capital** (proposed rising to **₦1bn**) plus the **~₦30m registration fee** — material; bakes regulation into the cap-table from seed.
- **Partner, don't rebuild, the regulated edges:** route exchange/OTC through licensed locals (**Busha/Quidax**); use a licensed bank/PSP for NIP naira rails; consider EMTL/IMTO posture for the cross-border leg.
- **FX-scapegoat risk mitigation:** transparent, traceable, KYC'd flows; cooperative regulator posture; avoid anonymous P2P that triggered the 2024 Binance crackdown.
- **Lending license:** the credit product likely needs a separate lending/finance-company structure (state money-lender or partner MFB) — keep loan book dollar-denominated but disbursement/repayment naira-compliant.

---

## 9. Key risks

| Risk | Severity | Mitigation |
|---|---|---|
| **Regulatory whipsaw** (2021 ban → 2024 crackdown precedent) | High | License early; full KYC; cooperative posture; diversify corridors/jurisdictions |
| **Off-ramp liquidity / spread blowout** during naira volatility | High | Internal FX book + multiple OTC partners; dynamic, *disclosed* spreads; never promise a rate we can't fill |
| **Credit defaults** on a low-doc base | High | Start tiny (single-cycle, secured against future inflows), dollar-denominated loan book, region/activity-specific AI models, graduated limits |
| **Stablecoin peg/issuer risk** | Med | Diversify USDC/USDT; short holding windows; transparent disclosure |
| **Incumbent encroachment** (Moniepoint/OPay add stablecoins; Juicyway moves down-market) | Med | Move fast on the *specific* low-literacy + credit combo they're slow to serve; lock distribution via market-association agents |
| **Trust / scam stigma / low literacy** | Med | Agent-assisted onboarding, vernacular voice UX, proof-of-payment receipts, guarantees |
| **Supplier-side fraud** (paying wrong/fake supplier) | Med | V3 verified-supplier directory + milestone escrow |

---

## 10. Phased roadmap

| Phase | Timeline | Goal | Ship |
|---|---|---|---|
| **0 — Foundation** | M0–4 | License + rails | ARIP application; bank/PSP + Busha/Quidax + China settlement partner integrations; dollar wallet + off-ramp |
| **1 — Freelancer beachhead** | M4–9 | Dollar liquidity + revenue | Best-in-class freelancer USD account (Persona B); WhatsApp/USSD vernacular UX; supplier-payout v1 for early importers |
| **2 — Importer core** | M9–18 | Own J1 + J4 in one corridor | China→Onitsha corridor; proforma-capture; **AI working-capital restock line**; POS-agent cash-out network |
| **3 — Expand corridors** | M18–30 | Dubai/textiles + regional (CFA) | Multi-currency; Persona C; verified-supplier directory + milestone escrow |
| **4 — Platform** | M30–48 | Defensibility | Credit-as-a-service API; stablecoin card; insurance & dollar-savings |

**North-star metric:** *active importers settling ≥1 supplier payment/quarter AND drawing a restock line.* Everything else (freelancer accounts, off-ramp volume) is in service of feeding that number.

---

## Sources

- [How Nigerian Businesses Can Pay Chinese Suppliers Despite FX Constraints — YoguPay](https://yogupay.com/blog/how-nigerian-businesses-can-pay-chinese-suppliers-despite-fx-constraints)
- [How to pay Chinese Suppliers from Nigeria using Stablecoin — YoguPay](https://yogupay.com/pay-chinese-suppliers-in-nigeria-with-stablecoins/)
- [Forex traders say Chinese traders now collecting naira instead of dollars — Nairametrics](https://nairametrics.com/2025/09/02/exchange-rate-forex-traders-say-chinese-traders-now-collecting-naira-instead-of-dollars/)
- [Chinese Businesses Now Accepting Naira Over Dollars — Nigerian Eye](https://www.nigerianeye.com/2025/09/chinese-businesses-now-accepting-naira.html)
- [How to Pay Your Chinese Supplier from Nigeria in 2026 (Without SWIFT) — Xchange4me](https://xchange4me.org/blog/how-to-pay-chinese-supplier-from-nigeria)
- [The USD/Naira Informal Exchange Market: How It Works — Romano Law](https://www.romanolaw.com/the-usd-naira-informal-exchange-market-how-it-works-why-it-thrives-and-the-legal-risks-you-need-to-know/)
- [China's exports to Nigeria surge 37% to $13bn in 2025 — Finance in Africa](https://financeinafrica.com/insights/chinas-exports-to-nigeria-surge/)
- [Nigeria Stablecoin Remittance Boom — CryptoDaily](https://cryptodaily.co.uk/2026/06/nigeria-stablecoin-remittance-fees)
- [USDT Network Fees Nigeria: TRC20 vs ERC20 vs Solana — MEXC](https://blog.mexc.com/crypto-knowledge/usdt-network-fees-nigeria-trc20-vs-erc20-vs-solana-explained/)
- [Top Crypto On-Ramp & Off-Ramp Solutions in Nigeria — YoguPay](https://yogupay.com/on-ramp-off-ramp-solutions-in-nigeria/)
- [Best Stablecoins Off-Ramp Solutions for African Enterprises in 2025 — FinchTrade](https://finchtrade.com/blog/best-stablecoins-off-ramp-solutions-for-african-enterprises-in-2025)
- [How Nigeria's Juicyway is helping African businesses send, receive and hold foreign currency — Disrupt Africa](https://disruptafrica.com/2025/11/11/how-nigerias-juicyway-is-helping-african-businesses-send-receive-and-hold-foreign-currency/)
- [This stealthy African stablecoin startup already processed over $1B — TechCrunch](https://techcrunch.com/2024/12/16/this-stealthy-african-stablecoin-startup-already-processed-over-1b-in-cross-border-payments/)
- [How does Juicyway Handle Cross Border Payments — Juicyway](https://www.juicyway.com/blog/how-does-juicyway-handle-cross-border-payments)
- [Why MiniPay launched stablecoin-linked cards — TechCabal](https://techcabal.com/2026/06/25/minipay-visa-cards-for-stablecoins/)
- [How to get SEC license for Digital Asset Companies in Nigeria (2025) — T Corporate Legal Advisory](https://tcorporatelegaladvisory.com/how-to-get-sec-license/)
- [ARIP Checklist for VASP Onboarding — SEC Nigeria](https://sec.gov.ng/about/resources/checklists/accelerated-regulatory-incubation-program-arip-checklist-for-vasp-onboarding/)
- [Nigeria Crypto Regulation: ISA 2025 Explained — Cryptoverse Lawyers](https://www.cryptoverselawyers.io/nigeria-crypto-regulation-isa-2025)
- [VASP License Nigeria: How to Get Your Crypto Business Registered — Glavx](https://glavx.org/vasp-license-nigeria-how-to-get-your-crypto-business-registered)
- [Grey fees vs Geegpay vs Payoneer and Wise in Nigeria — Grey](https://grey.co/blog/grey-fees-vs-geegpay-vs-payoneer-and-wise-in-nigeria)
- [Grey vs GeegPay (Raenest): Which Platform is Best for African Freelancers? — Paycape](https://paycape.com/blog/grey-vs-geegpay-raenest-payment/)
- [Receive USD in Nigeria (2025): Best Options for Freelancers — Cenoa](https://www.cenoa.com/blog/how-to-receive-usd-payments-in-nigeria-2025-guide)
- [Noah and Payd Partner to Provide Dollar-Native Salaries to 30,000+ African Digital Workers — Financial IT](https://financialit.net/news/personal-finance/noah-and-payd-partner-provide-dollar-native-salaries-30000-african-digital)
- [Getting Paid In USDT In Nigeria: A Freelancer's Guide — MEXC](https://blog.mexc.com/crypto-knowledge/getting-paid-in-usdt-in-nigeria-a-freelancers-guide-to-cashing-out-on-mexc/)
