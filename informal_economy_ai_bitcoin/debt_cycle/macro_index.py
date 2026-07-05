#!/usr/bin/env python3
"""
MACRO-LAB COMPOSITE INDEX — a computed resilience/fragility score per pole
==========================================================================
Turns the whole lab's thesis into one number per economy. The dashboard's "policy-space" score was
hand-set; this DERIVES a composite from three transparent pillars, each 0-100 (higher = healthier):

  A. BUFFER / policy space  (weight 0.40) — currency sovereignty + reserve/creditor status + CB
     capacity. The cushion behind the debt. (The lab's core lesson: this, not the debt ratio.)
  B. DEBT SUSTAINABILITY    (weight 0.30) — inverse of the debt-SERVICE burden and external-currency
     reliance. NOT the debt level (Japan's 206% is sustainable; Nigeria's 39% is not).
  C. DEMOGRAPHIC VITALITY   (weight 0.30) — COMPUTED from fertility (vs 2.1 replacement) + youth
     (median age). The long-run engine — or its absence.

RESILIENCE = 0.40·A + 0.30·B + 0.30·C ;  FRAGILITY = 100 − RESILIENCE.

The punchline the index is built to expose: Nigeria and Europe screen as the MOST fragile — but for
OPPOSITE reasons. Strip out demographics and Nigeria is by far the worst (no buffer, weak service
cover); its YOUTH is the one thing holding it up. Japan/China look resilient on buffer but are
demographically dying. Same debt cycle, very different fragility once you score all three pillars.

Buffer & sustainability sub-scores are documented judgments (0-100) grounded in the module gauges;
debt/GDP, fertility and median age are pulled/derived from data. Run (from debt_cycle/):
  uv run python macro_index.py
"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
WA, WB, WC = 0.40, 0.30, 0.30
REPLACEMENT = 2.1

# Per-pole inputs. buffer/sustain are documented 0-100 judgments (rationale in `why`);
# debt_gdp / fertility / median_age are quantitative (fertility & age drive the COMPUTED vitality).
POLES = [
    dict(name="Nigeria", debt_gdp=39, buffer=8, sustain=25, fertility=4.48, median_age=17.8,
         why="no reserve status, FX-constrained, thin reserves; debt-service >100% of retained revenue"),
    dict(name="China", debt_gdp=99, buffer=62, sustain=40, fertility=1.00, median_age=39.1,
         why="huge reserves + capital controls + state banks (own-currency workout), but no reserve currency; credit-intensity ×3.1, property"),
    dict(name="Europe", debt_gdp=89, buffer=48, sustain=45, fertility=1.50, median_age=45.0,
         why="UK sovereign vs euro-periphery no currency control (blend); ECB backstop but union-without-fiscal-union"),
    dict(name="United States", debt_gdp=120, buffer=95, sustain=55, fertility=1.62, median_age=38.0,
         why="reserve currency + the Fed + deep markets; interest/revenue ~21% and rising is the one soft spot"),
    dict(name="Japan", debt_gdp=206, buffer=72, sustain=50, fertility=1.20, median_age=49.0,
         why="own CB + world's largest net creditor + domestic debt (206% at ~1% yields); demographics the drag"),
]


# map each pole to a representative entity in demographics.csv (Europe = Germany+Italy blend)
DEMO_MAP = {"Nigeria": ["Nigeria"], "China": ["China"], "Europe": ["Germany", "Italy"],
            "United States": ["United States"], "Japan": ["Japan"]}


def _demo():
    p = os.path.join(HERE, "demographics.csv")
    return pd.read_csv(p).set_index("country") if os.path.exists(p) else None


def vitality(pole_name, fert, age, demo):
    """COMPUTED demographic vitality 0-100. Now folds in the actual BIRTH-vs-DEATH dynamic:
    0.4 fertility (vs replacement) + 0.3 youth (median age) + 0.3 natural increase (births−deaths).
    Falls back to fertility+youth if demographics.csv is absent."""
    f = max(0, min(100, (fert - 0.7) / (4.5 - 0.7) * 100))
    y = max(0, min(100, (50 - age) / (50 - 17) * 100))
    if demo is None:
        return 0.5 * f + 0.5 * y
    ent = [e for e in DEMO_MAP.get(pole_name, []) if e in demo.index]
    ni = demo.loc[ent, "natural_increase_per_1000"].mean() if ent else 0.0   # births−deaths /1000
    n = max(0, min(100, (ni + 8) / (30 + 8) * 100))                          # −8→0, +30→100
    return 0.4 * f + 0.3 * y + 0.3 * n


def main():
    demo = _demo()
    rows = []
    for p in POLES:
        c = vitality(p["name"], p["fertility"], p["median_age"], demo)
        res = WA * p["buffer"] + WB * p["sustain"] + WC * c
        rows.append({**p, "vitality": c, "resilience": res, "fragility": 100 - res})
    df = pd.DataFrame(rows)

    print("="*96)
    print("MACRO-LAB COMPOSITE INDEX — resilience & fragility, computed from three pillars")
    print("="*96)
    print(f"\n    {'pole':<15}{'A:buffer':>10}{'B:sustain':>11}{'C:vitality':>12}   {'RESILIENCE':>11}{'FRAGILITY':>11}")
    print("    " + "-"*70)
    for _, r in df.sort_values("resilience", ascending=False).iterrows():
        print(f"    {r['name']:<15}{r['buffer']:>10.0f}{r['sustain']:>11.0f}{r['vitality']:>12.0f}   "
              f"{r['resilience']:>11.1f}{r['fragility']:>11.1f}")
    print(f"    weights: buffer {WA} · sustainability {WB} · demographic vitality {WC}  (each pillar 0-100, higher=healthier)")

    print("\n[MOST FRAGILE → MOST RESILIENT]:")
    for _, r in df.sort_values("fragility", ascending=False).iterrows():
        print(f"    {r['name']:<15} fragility {r['fragility']:>4.0f}   — {r['why']}")

    # the demographic counterfactual — Nigeria's youth as its buffer
    nig = df[df.name == "Nigeria"].iloc[0]
    res_no_demo = (WA * nig["buffer"] + WB * nig["sustain"]) / (WA + WB)
    print(f"\n[THE COUNTERFACTUAL] strip out demographics and Nigeria's score collapses from "
          f"{nig['resilience']:.0f} to {res_no_demo:.0f} —")
    print("    it screens middling only because its demographic vitality (96/100, the youngest, fertility")
    print("    4.5) offsets the worst buffer (8) and weak debt-service cover. Its youth IS its balance sheet.")
    print("    The mirror image: Japan & China score well on buffer but their vitality (7, 20) is collapsing —")
    print("    resilient-but-dying vs fragile-but-young. That contrast is the whole point of scoring 3 pillars.")

    df.round(1).to_csv(os.path.join(HERE, "macro_index_scores.csv"), index=False)
    print(f"\nWrote macro_index_scores.csv")
    print("Note: the demographic pillar will sharpen when the birth-vs-death / population-to-2100 model")
    print("(demographics.py) lands — vitality will fold in natural-increase and the projected trajectory.")


if __name__ == "__main__":
    main()
