# Nigeria Debt-Cycle — Positioning (Phase 4)

**Engine:** `positioning_model.py` → `positioning_returns.csv` · **Weights:** base 55% / bull 20% / bear 25% (from `ANALOGUE_CALIBRATION.md`)

Phase 4 turns the macro call into **what to own**. Everything is in **USD total return** because for a Nigerian saver, an SME treasury, or a foreign allocator the binding question is the dollar outcome *after FX* — which is exactly what the debt cycle drives (the graph/VAR showed FX is downstream of oil→current-account→reserves).

---

## 1. The positioning matrix (USD total return, % p.a., ~2026–29)

| Asset | Base | Bull | Bear | **E[USD]** | Dispersion | Downside | Risk-adj |
|---|---:|---:|---:|---:|---:|---:|---:|
| **NGN T-bills (1yr)** | 11 | 15 | 2 | **9.6** | 4.6 | 0.0 | **0.97** |
| FGN bonds (10yr, NGN) | 14 | 24 | −12 | 9.5 | 13.0 | 6.0 | 0.34 |
| NGX banks (USD) | 12 | 28 | −16 | 8.2 | 15.3 | 8.0 | 0.21 |
| **Gold / BTC (tail hedge)** | 6 | 2 | 18 | **8.2** | 5.9 | 0.0 | **0.54** |
| FGN Eurobonds (USD) | 9 | 13 | −8 | 5.6 | 8.0 | 4.0 | 0.06 |
| **USD / stablecoin (yield)** | 5 | 4 | 6 | 5.0 | 0.7 | 0.0 | 0.00 |
| NGX equities (broad, USD) | 8 | 22 | −18 | 4.3 | 13.9 | 9.0 | −0.05 |
| Lagos real estate (USD) | 3 | 8 | −5 | 2.0 | 4.5 | 2.5 | −0.68 |

*Risk-adj = (E[USD] − safe leg) / dispersion, with USD/stablecoin as the ~5% safe leg.*

---

## 2. Per-asset rationale

- **NGN T-bills / short duration (best risk-adjusted).** High naira yields (~17–20%) outpace base-case depreciation (~5–6%/yr) for a positive USD carry, and the short tenor caps the bear-case loss (you re-price fast as the naira slides). The classic "stabilising-EM carry" trade — works in base, great in bull, only mildly negative in bear.
- **FGN bonds (10yr) — the duration bet.** Biggest base/bull upside (disinflation rallies the long end, 17%→12%) but a brutal bear (yields spike + FX crash) → high dispersion. A leveraged bet on the 20% bull; size accordingly.
- **NGX banks — cheap, high-beta.** Trading 4–8× earnings with ~50% ROE; explosive in bull (re-rating + stable naira), but the naira destroys USD returns in bear. Best *equity* expression of the bull.
- **Gold / BTC — the bear hedge (2nd-best risk-adjusted).** The only asset that *pays in the bear* (capital flight, naira collapse, dollarization). Negatively correlated to the domestic book — the portfolio's insurance.
- **FGN Eurobonds — USD carry, no FX risk.** ~6.7% yield (2032s), spread tightening in base/bull; the moderate middle. The clean way for a USD investor to own the *sovereign* improvement without naira exposure.
- **USD / stablecoin — the numeraire & safe leg.** ~0% real USD but +4–6% with on-chain/T-bill-backed yield, near-zero dispersion. *This is the base currency of the whole analysis* — and (see §4) the household's rational default.
- **Broad equities / real estate — poor risk-adjusted.** Naira-denominated, illiquid, FX-exposed; negative risk-adjusted scores. Avoid as a USD allocator except the specific cheap-bank sleeve.

---

## 3. The barbell verdict

In a **55/20/25 world with a fat bear tail**, the portfolio is a **barbell**, not a directional bet:

```
        CARRY LEG  (base-case income)        HEDGE LEG  (bear insurance)
        NGN T-bills / short FGN duration  +  USD-stablecoin (yield) + Gold/BTC
        FGN Eurobonds (USD carry)            ───────────────────────────────
        ── high-conviction satellite ──      sized to the 25% bear weight
        NGX banks (the bull expression)
```

- **Core:** NGN T-bill carry (best risk-adjusted) + USD-stablecoin safe leg + a gold/BTC tail hedge sized to the bear weight.
- **Satellite (bull expression):** long-duration FGN bonds and cheap NGX banks — high-beta upside to the 20% case, kept small because the calibration says the beautiful path is the minority.
- **Avoid:** broad naira equities and real estate as USD positions (FX overwhelms the naira gains outside bull).
- **The single most robust trade** is the one that pays in *both* base and bear: **hold dollars (stablecoins) with yield.** It loses only in the 20% bull (mild) and wins everywhere else.

---

## 4. The bridge — positioning *is* the informal-economy/Bitcoin thesis

Here the debt-cycle layer rejoins the application layer (the `MASTER_REPORT.md` AI + Bitcoin opportunity). The positioning conclusion and the household conclusion are **the same fact seen from two sides:**

- **For the saver/SME:** the analysis says *hold dollars (stablecoins), earn yield, keep a gold/BTC tail hedge, and clip naira carry only at short duration.* That is precisely what **~95% of surveyed Nigerians already do** by reaching for USDT/USDC — they are running the optimal barbell intuitively.
- **For the builder:** that household barbell **is the demand curve** for the informal-economy fintech opportunity. The "USD/stablecoin safe leg" line in the matrix is, at population scale, the **dollar-operating-account + stablecoin-treasury + off-ramp** businesses the master report identified. The debt cycle *manufactures* the demand; the AI+Bitcoin stack *serves* it.
- **Scenario sensitivity ties the two layers:** in **base**, persistent inflation keeps dollar demand structural while thin FX spreads push the fintech toward credit + velocity (not spread) — the master report's exact conclusion. In **bear**, dollar demand surges (more stablecoin volume) but regulatory/de-banking risk spikes — so the licensed, compliant operator wins. In **bull**, the hedge motive softens and the **AI-credit + trade-settlement** value props outlast the pure-hedge one. *The product strategy is robust across all three macro paths* — which is the whole point of building on flow and credit rather than on currency collapse.

> **One line:** the debt cycle says *own dollars and short-duration carry, hedge the tail*; the household runs that barbell via stablecoins; and serving that barbell at scale — dollar accounts, stablecoin treasury, AI-underwritten credit on a licensed off-ramp — is the business the whole project pointed to.

---

## 5. Triggers (tie to the quarterly tracker)

Re-weight the barbell as the `MODEL_AND_TRACKER.md` gauges move:
- **Toward the carry/duration leg** if: inflation keeps falling, naira holds, reserves rise, MPR cuts proceed (bull/base strengthening) → add FGN duration and banks.
- **Toward the hedge leg** if: ACLED/security deteriorates, oil falls (the VAR's lead variable), the parallel premium re-opens, or fiscal slippage appears (bear triggers) → raise USD-stablecoin + gold/BTC, cut duration.
- **The earliest mover is oil** (the graph hub / VAR lead): an oil shock hits reserves first, then the naira with a ~1-year lag — so an oil roll-over is the cue to shift toward the hedge leg *before* the FX and inflation prints confirm it.
