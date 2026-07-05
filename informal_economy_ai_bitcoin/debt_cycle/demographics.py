#!/usr/bin/env python3
"""
DEMOGRAPHICS — births vs deaths, and who is "dying off"   (macro-lab)
====================================================================
Makes the demographic pivot explicit — the deepest current under the whole debt-cycle picture.
Fertility below replacement (2.1) means a population will shrink once age-momentum fades; a
BIRTH-TO-DEATH RATIO below 1.0 means it is ALREADY shrinking (more deaths than births).

  1. WHO IS ALREADY IN NATURAL DECLINE (deaths > births) — ranked by how fast.
  2. THE EXTREME — South Korea's fertility 0.72, the lowest ever recorded (~⅓ of replacement).
  3. THE 2100 TRAJECTORY — the East-Asian / Southern-European halving vs Nigeria's near-doubling.
  4. THE PIVOT — the weight of humanity shifting from the aging North/East to the young South.

Feeds the demographic-vitality pillar of macro_index.py. Data: demographics.csv (UN WPP 2024,
World Bank; staging 35).  Run (from debt_cycle/):  uv run python demographics.py
"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPLACEMENT = 2.1


def main():
    d = pd.read_csv(os.path.join(HERE, "demographics.csv"))
    d["pop_change_2100_pct"] = (d["pop_millions_2100"] / d["pop_millions_2024"] - 1) * 100
    print("="*94)
    print("DEMOGRAPHICS — births vs deaths: who is growing, who is 'dying off'")
    print("="*94)

    print("\n[1] NATURAL CHANGE — birth-to-death ratio < 1.0 = ALREADY shrinking (deaths > births):")
    print(f"    {'country':<16}{'fertility':>10}{'birth/1k':>10}{'death/1k':>10}{'natural Δ':>11}{'B:D':>7}   status")
    for _, r in d.sort_values("natural_increase_per_1000").iterrows():
        status = "SHRINKING" if r.birth_to_death_ratio < 1 else "growing"
        mark = "🔻" if r.birth_to_death_ratio < 1 else "  "
        print(f"    {mark}{r.country:<14}{r.total_fertility_rate:>10.2f}{r.crude_birth_rate:>10.1f}"
              f"{r.crude_death_rate:>10.1f}{r.natural_increase_per_1000:>+11.1f}{r.birth_to_death_ratio:>7.2f}   {status}")
    decline = d[d.birth_to_death_ratio < 1].sort_values("natural_increase_per_1000")
    print(f"\n    {len(decline)} of {len(d)} already in natural decline: "
          + ", ".join(decline.country) + ".")
    print(f"    Fastest natural shrinkage: {decline.iloc[0].country} ({decline.iloc[0].natural_increase_per_1000:+.1f}/1000, "
          f"deaths {1/decline.iloc[0].birth_to_death_ratio:.1f}× births).")

    kor = d[d.country == "South Korea"].iloc[0]
    nig = d[d.country == "Nigeria"].iloc[0]
    print(f"\n[2] THE EXTREME: South Korea's fertility {kor.total_fertility_rate:.2f} — the world's lowest, ~"
          f"{kor.total_fertility_rate/REPLACEMENT*100:.0f}% of replacement (vs Nigeria's {nig.total_fertility_rate:.2f}).")
    print("    Its natural decrease looks mild TODAY only because it isn't yet as old as Italy/Japan —")
    print("    but low fertility is the leading indicator, so its future collapse is the deepest of all.")

    print("\n[3] POPULATION 2024 → 2100 (UN WPP 2024 medium) — the halving vs the doubling:")
    print(f"    {'country':<16}{'2024':>9}{'2050':>9}{'2100':>9}{'Δ 2024→2100':>13}")
    for _, r in d.sort_values("pop_change_2100_pct").iterrows():
        print(f"    {r.country:<16}{r.pop_millions_2024:>9.0f}{r.pop_millions_2050:>9.0f}{r.pop_millions_2100:>9.0f}{r.pop_change_2100_pct:>+12.0f}%")

    print("\n[4] THE PIVOT: the aging North/East (Korea −58%, China −55%, Japan −40%, Italy −29% by 2100)")
    print("    shrinks while the young South expands (Nigeria +105%, still growing past 2100). The weight")
    print("    of humanity is shifting from Asia/Europe toward Africa. India is the hinge — below")
    print("    replacement (1.98) but still growing on momentum to a ~2061 peak near 1.7bn.")

    d.round(2).to_csv(os.path.join(HERE, "demographics_scored.csv"), index=False)
    print("\nWrote demographics_scored.csv · feeds the vitality pillar of macro_index.py")


if __name__ == "__main__":
    main()
