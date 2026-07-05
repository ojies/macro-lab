# macro-lab · Japan module (the precedent)

The economy every other pole is measured against: a 1980s bubble, its 1990 burst, a Richard-Koo
**balance-sheet recession**, ~25 years of mild deflation, and the world's highest public debt that
**never triggered a crisis**. Japan ran the modern playbook first (ZIRP → QE → QQE → NIRP/YCC →
the 2024 exit) — the toolkit the Fed and ECB later copied.

Run (from `debt_cycle/`): `uv run python japan/japan_model.py`

## Files
| File | Contents |
|---|---|
| `japan_macro.csv` | Annual 1980–2025 (IMF WEO, BoJ, MOF, World Bank): growth, CPI, unemployment, gross & net govt debt, policy rate, BoJ balance sheet %GDP, 10y JGB, working-age share, fertility |
| `japan_model.py` | Bubble→balance-sheet-recession→lost-decades diagnosis + the lesson for the other poles |
| *(staging 34)* | Sourced data notes (IMF vintage reconciliation, BoJ timeline, splice notes) |

## What the model finds
- **The arc:** Nikkei ~38,900 (1989) → burst (BoJ hiked to 6% by Aug-1990) → deflation (CPI **averaged +0.2% across 1995–2020**) → the debt ramp as public borrowing offset private deleveraging (gross debt **55% (1990) → 214% (2024)**).
- **The debt paradox — the module's core lesson:** ~206% gross debt (net ~137%) and a BoJ balance sheet **~118% of GDP**, yet JGB yields stayed the *world's lowest*. Why no crisis: debt is **domestically owned (~90%+, BoJ holds ~half), yen-denominated, own central bank, high domestic savings, world's largest net external creditor.** *Who owns the debt and in what currency matters more than the ratio.*
- **The 2022–24 regime change:** inflation returned (2.7% 2024, 3.2% 2025) and the **BoJ exited** — ending NIRP/YCC in March 2024, its first hike since 2007 (policy rate 0.25% → 0.75%). The lost-decades regime may finally be turning.
- **Data note:** the current IMF WEO revised Japan's gross debt **down ~25–30pp** from the older ~250% basis; the "highest in the developed world" headline still holds.

## What Japan teaches the other poles
- **Europe** = the vulnerable case: shared currency, *no* shared treasury — the periphery lacks Japan's own-central-bank backstop.
- **China** = the most Japan-like: high-but-domestic debt, closed capital account, property bust, aging — but at **middle income** (Japan was already rich).
- **US** = has the reserve-currency + own-CB backstop, so "Japanification" is a chronic-drag risk, not a default risk.
- **Nigeria** = the opposite pole: none of Japan's cushions.

Japan is the **control experiment** for the whole lab — proof the debt *ratio* is not destiny; currency sovereignty, domestic ownership, and net-creditor status are.
