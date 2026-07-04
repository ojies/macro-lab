# Catch-Up Economies: Macro & Debt Trajectory After Reaching Nigeria's Current Income

**Purpose.** "Development-age" comparison. Nigeria today sits at ~$5,000-6,500 GDP/capita
in Maddison 2011$ PPP (~$9,000-9,500 in current-PPP int'l$) — call it **early-middle-income**.
For each great catch-up economy we (a) date the decade it was at Nigeria's-current level
(the *anchor*), then (b) track ~40 years of growth, public debt, inflation, savings/investment,
and export orientation, and (c) ask whether it SUCCEEDED or STALLED.

Deliverable table: `../countries_catchup_macro.csv`.
Flags: **[SOURCED]** = pulled from a named source below; **[ESTIMATED]** = well-established
decade averages reconstructed from standard economic-history series (Maddison / IMF HPDD /
World Bank WDI) and rounded — directionally firm, not a single citable cell; blank = unsourceable.

---

## 1. Income anchors — when each reached ~Nigeria's-current level (Maddison 2020, 2011$ PPP)

| Country | Anchor decade | GDP/cap at anchor | Basis |
|---|---|---|---|
| United States | ~1890 | ~$5,700 (1890) -> $6,700 (1900) | [ESTIMATED] Maddison; 1913 ~$8,600 |
| United Kingdom | ~1870 | ~$5,000 (1870) -> $6,400 (1890) | [ESTIMATED] Maddison; UK crossed earliest (frontier) |
| Germany | ~1890 | **$5,346 (1890) -> $6,328 (1900)** | **[SOURCED]** Maddison via OWID |
| Japan | ~1960 | ~$5,900 (1960) -> $6,900 (1962) | [ESTIMATED] Maddison; grew ~10%/yr so crossed band 1958-61 |
| South Korea | ~1980 | **$5,322 (1977) -> $6,457 (1980)** | **[SOURCED]** Maddison via OWID |
| China | ~2005 | **$6,627 (2005); $4,730 (2000); $8,190 (2008)** | **[SOURCED]** Maddison via OWID |
| Brazil (contrast) | ~1975 | ~$5,900 (1975) -> $7,200 (1980) | [ESTIMATED] Maddison; miracle peak |

Source: Maddison Project Database 2020, GDP per capita (2011 int'l $), served via Our World in Data
grapher CSV (`gdp-per-capita-maddison`). Korea, Germany, China values are exact reads from that CSV;
US/UK/Japan/Brazil are standard Maddison values reconstructed (the OWID CSV read intermittently
truncated for those entities). Maddison releases: https://www.rug.nl/ggdc/historicaldevelopment/maddison/releases/maddison-project-database-2020

---

## 2. Public debt / GDP path — sourcing

- **[SOURCED] China** govt debt/GDP: 2005 = 26.3%, 2010 = 33.9%, 2015 = 41.5%, 2020 = 70.2%
  (IMF/FRED general-government gross debt series). Broad total incl. LGFV/SOE/household ~250-280% GDP
  (BIS/IMF). https://fred.stlouisfed.org/series/GGGDTACNA188N ; IMF DataMapper DEBT dataset.
- **[SOURCED] Korea** general-govt debt/GDP: 1990 = 12.7%, 2000 = 16.1%, record low 15.3% (2003);
  ~40% by late-2010s. Kept low right through the catch-up. IMF HPDD / FRED GGGDTAKRA188N.
- **[SOURCED] UK** national debt/GDP: ~30% by 1900, low of ~25-29% in 1913-14 (a 200-year low) —
  the Victorian/Edwardian era drew debt down from post-Napoleonic ~180%. Then WWI spikes it >130%.
  Sources: OBR "300 years of UK public finance data"; ukpublicspending.co.uk; economicshelp.org.
- **[SOURCED] United States** gross federal debt/GDP: ~16.5% in 1930; 1920s "national debt reduced
  by ~one third" (Coolidge); WWI peak ~33% (1919). Late-19thC very low (post-Civil-War paydown,
  ~5-10%). Wikipedia "History of the United States public debt"; Reinhart-Rogoff/Historical Statistics.
- **[SOURCED] Japan** debt trajectory (direction): tiny in the 1960s (<10%), rising after the
  1970s oil-shock stimulus, ~50% by 1980, ~65% by 1990, then EXPLODES to ~100%+ across the 1990s
  "Lost Decade" and to >230% today. Key point: Japan's debt problem is POST-catch-up (stagnation-
  driven), not the growth engine. IMF HPDD; macrotrends; FRED GGGDTAJPA188N.
- **[ESTIMATED] Germany** ~40-50% pre-WWI (1890-1913); WWI debt-financed (~160%+); **1923
  hyperinflation liquidated nominal debt** (post-1924 ~20%). Reinhart-Rogoff historical series.
- **[ESTIMATED] Brazil** rising through the 1980s debt crisis (~30%->50%->60-70%); the 1982
  moratorium is the pivot into the lost decade.
- Reinhart & Rogoff public debt/GDP historical database (carmenreinhart.com/debt-to-gdp-ratios)
  and IMF Historical Public Debt Database (https://www.imf.org/external/datamapper/datasets/DEBT)
  underpin the pre-1950 figures. Decade values are rounded era-typical levels — treat as [ESTIMATED].

## 3. Savings / investment rate — sourcing

- **[SOURCED] Japan** gross saving averaged ~36% of national income 1960-71 (private saving rose
  16.5% -> 31.9% of GNP 1952-71; peak ~42% in 1970). Econlib "Japan"; World Bank NY.GNS.ICTR.ZS.
- **[SOURCED] Korea** domestic saving/GNP rose 3.3% (1962) -> 35.8% (1989); peak ~41.4% (1988);
  savings overtook investment late-1980s (current account into surplus 1986). Country Studies / KDI.
- **[SOURCED] China** gross saving climbed from ~30-35% (1982) to 40-45% (1990s) and >50% (late-2000s),
  ~42-45% recently — the highest of any large economy. BIS WP312; World Bank; Philadelphia Fed.
- **[ESTIMATED] US** gross domestic investment ~20-22% through 1890-1930 (Historical Statistics).
- **[ESTIMATED] UK** ~10-12% domestic investment 1870-1913 — LOW; Britain exported capital abroad
  (12.6% of national wealth invested 1870-74, incl. large overseas share). NBER "British Investment
  Overseas 1870-1913"; the LOW home-investment / high-capital-export pattern is the key contrast.
- **[ESTIMATED] Germany** ~22-24% pre-WWI (heavy industry + universal banks). Brazil ~17-20% (the
  trap signature — far below Asia's 35-45%).

## 4. Export orientation / trade openness — sourcing

- **[SOURCED] Korea** exports averaged ~28% of GDP (min 2.6% in 1960, max 52% in 2012) — the
  archetypal export-led model; trade deficit flipped to surplus in 1986. theglobaleconomy.com; WDI.
- **[SOURCED] China** trade ~61% of GDP in 2005; exports rose from ~20% (2000) to ~35% (2007) of GDP,
  then FELL as it rebalanced toward domestic demand (~20% by 2020s). WITS/World Bank; CRS.
- **[SOURCED] Japan** export-led but LOWER export share than Korea/China (~10-13% of GDP through the
  miracle) — large domestic market; perennial trade surplus from late-1960s. Britannica; MoF Japan.
- **[SOURCED] UK** high export share (~20-24% of GDP) — free-trade "workshop of the world," 9.1% of
  world GDP in 1870. Wikipedia econ history of UK.
- **[ESTIMATED] US** LOW trade share (~5-8% of GDP) — grew on a continental internal market, NOT
  export-led. Germany ~15-19%. Brazil ~8-12% (weak manufactured-export upgrade).

## 5. Real GDP growth — sourcing

- **[SOURCED] Japan** ~10-11%/yr in the 1960s, falling to ~4-5% in the 1970s-80s, ~1%+ in the 1990s.
  Multiple (Statista GDP-growth-by-decade; Britannica; BoJ).
- **[SOURCED] China** ~10%/yr 2005-2010, slowing to ~6-7% 2010-2020 (2.2% in the 2020 COVID year);
  1979-2010 average 9.9%. World Bank NY.GDP.MKTP.KD.ZG; CRS.
- **[SOURCED] Korea** ~8-9%/yr in the 1980s, ~7% 1990s (pre-1997), ~4-5% 2000s, ~3% 2010s. WDI.
- **[ESTIMATED] US/UK/Germany** pre-1950 decade averages from Maddison real GDP: US ~3.5-4%
  (per-capita ~2%), UK ~1.5-2.2% (the slow "climacteric"), Germany ~3-3.5% pre-1914 then war collapse.

## 6. Years to double GDP/cap from Nigeria's level, and middle-income-trap outcome

| Country | Yrs to 2x from anchor | Trap outcome |
|---|---|---|
| Japan | ~8 (1960 $5.9k -> 1968 $12k) | **ESCAPED** ~1970; high-income. Debt trouble came later. |
| South Korea | ~10 (1980 $6.5k -> 1990 $13.7k) | **ESCAPED** ~1995-2000; OECD 1996. Low-debt model. |
| China | ~8 (2005 $6.6k -> 2013 $13k) | **ESCAPING** — at high-income threshold ~2023-24; debt-heavy, verdict open. |
| United States | ~40 (per-capita; 1890 $5.7k -> ~1929 $11.4k) | **ESCAPED** decisively — became the frontier. |
| United Kingdom | ~60-65 (1870 $5.0k -> ~1935 $10k) | Escaped but SLOWEST — was already the mature leader. |
| Germany | nominal ~1958 (1890 $5.3k; reset by wars, 1950=$3.9k) | Fundamentals strong but **DERAILED ~60yr by WWI/hyperinflation/WWII**; secured post-1950. |
| Brazil (contrast) | ~40+ to barely 2x (1975 $5.9k -> 2019 ~$14k) | **STUCK** — classic middle-income trap. |

---

## Narrative per case

- **Japan (SUCCESS).** Anchor ~1960. State-guided heavy-industry + export manufacturing on a
  ~35% savings/investment base; grew ~10%/yr and doubled income in ~8 years. Public debt was
  trivial during the miracle — the debt explosion (100%+ then 230%+) is a POST-catch-up,
  stagnation-era phenomenon after the 1990 bubble burst. Escaped the trap by ~1970.

- **South Korea (SUCCESS).** Anchor ~1980. Chaebol-led export manufacturing, exports ~30-50% of GDP,
  savings ~34-41%, and — critically — **public debt kept low (12-22%) all through the catch-up**.
  Weathered the 1997 crisis, joined the OECD (1996), doubled income in ~10 years, and is now a
  high-income innovator. The cleanest "high savings + export orientation + fiscal discipline" template.

- **China (SUCCESS SO FAR).** Anchor ~2005. WTO-era export boom plus the highest investment/savings
  rate of any large economy (~45-50%). Doubled income in ~8 years and reached the high-income
  threshold ~2023-24. The distinguishing risk vs Japan/Korea: it leaned on **debt-financed
  investment** — broad economy-wide debt ~280% of GDP (property + LGFVs) — so trap-escape is real
  but its durability is the open question.

- **United States (SUCCESS, different model).** Anchor ~1890. NOT export-led (trade ~5-8% of GDP);
  grew on a vast continental internal market, immigration, mass production and strong institutions,
  with very low federal debt. Per-capita doubling took ~40 years (headline GDP also grew via
  population). Became the global frontier — the model where **scale + institutions**, not exports,
  drove catch-up.

- **United Kingdom (SUCCESS but SLOW / the caught leader).** Anchor ~1870. Already the richest
  economy, so "catch-up" is really the onset of relative decline (the "climacteric"). High export
  share but LOW domestic investment (~11-12%) because capital was exported to the empire and the US.
  Doubling took ~60-65 years; overtaken in per-capita income by the US and Germany by ~1900-1913.
  Lesson: a high trade share without high domestic investment is not the Asian growth engine.

- **Germany (SUCCESS but DERAILED).** Anchor ~1890. Textbook fundamentals — Second Industrial
  Revolution (steel, chemicals, electricals), technical education, universal banks, ~23% investment —
  and it caught the income frontier by 1913. Then **WWI, the 1923 hyperinflation, and WWII reset the
  clock ~60 years** (1950 income below the 1890 level). The cautionary tale within the success set:
  strong catch-up economics can be undone by war and institutional collapse; high-income was only
  locked in by the post-1950 Wirtschaftswunder.

- **Brazil (STALLED — the contrast).** Anchor ~1975. Reached Nigeria's-current level at the tail of
  the "miracle," but on **low savings (~18-20%), external debt and chronic inflation**. The 1982 debt
  crisis triggered a lost decade of hyperinflation and stagnation; manufactured exports never upgraded.
  ~40+ years later it has barely doubled — the definitive middle-income trap, and the mirror image of
  Korea/China.

## Key contrast (succeeders vs stalled)
The Asian succeeders (Japan/Korea/China) combined **35-45% savings/investment, export-manufacturing
upgrading, and — except China — low public debt**, doubling income in ~8-10 years and escaping the
trap. The stalled case (Brazil) had **~18-20% savings, weak export upgrading, and inflation/debt
crises**, taking ~40 years to barely double. Germany shows that even strong fundamentals can be
derailed by war/institutional collapse; the UK/US show that scale and institutions can substitute for
export-led growth but produce a much slower doubling. For Nigeria the operative levers are the ones
that separate Korea/China from Brazil: **raise the savings/investment rate far above today's ~15-20%,
build tradable-manufacturing exports, and avoid a debt/inflation crisis.**

## Caveats
- Pre-1950 decade averages (US, UK, Germany) are era-typical reconstructions from Maddison/Reinhart-
  Rogoff, not single citable cells — flagged [ESTIMATED]. PPP splices across a century carry wide bands.
- Germany 1910s-20s inflation left blank in the CSV: 1923 hyperinflation has no meaningful annual CPI.
- China's 30-40yr window is only ~20 years elapsed; second row spans 2015-2024 with recent data.
- "Debt/GDP" mixes general-government (Asia, modern) and gross-federal/national (US/UK, historical);
  definitions are not perfectly comparable across eras — read the levels as orders of magnitude.
