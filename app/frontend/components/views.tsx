"use client";
import React, { useEffect, useState } from "react";
import { getJSON, Pole, IndexPole } from "@/lib/api";
import { C, POLE_COLORS } from "@/lib/theme";
import { LineChart, AreaFan, Scatter, HBars, Lollipop, Spark, DivBars, Pt } from "./charts";

/* ---------- tiny UI helpers ---------- */
function useData<T = any>(path: string) {
  const [data, setData] = useState<T | null>(null);
  const [err, setErr] = useState<string | null>(null);
  useEffect(() => {
    let ok = true;
    getJSON<T>(path).then((d) => ok && setData(d)).catch((e) => ok && setErr(String(e)));
    return () => { ok = false; };
  }, [path]);
  return { data, err, loading: !data && !err };
}
const Head = ({ n, title, sub }: { n: string; title: string; sub?: string }) => (
  <div style={{ marginBottom: 18 }}>
    <div className="eyebrow" style={{ color: "var(--accent)" }}>{n}</div>
    <h2 style={{ fontFamily: "var(--serif)", fontSize: "clamp(22px,3.2vw,30px)", margin: "6px 0 4px", letterSpacing: "-.01em" }}>{title}</h2>
    {sub && <p style={{ color: "var(--secondary)", fontSize: 15, maxWidth: "64ch", margin: 0 }}>{sub}</p>}
  </div>
);
const Cap = ({ children }: { children: React.ReactNode }) => (
  <p style={{ fontSize: 12.5, color: "var(--muted)", marginTop: 12, maxWidth: "74ch" }}>{children}</p>
);
const Legend = ({ items }: { items: { c: string; label: string; dot?: boolean }[] }) => (
  <div style={{ display: "flex", flexWrap: "wrap", gap: "10px 18px", marginBottom: 12, fontSize: 13.5, color: "var(--secondary)" }}>
    {items.map((it) => (
      <span key={it.label} style={{ display: "inline-flex", alignItems: "center", gap: 7 }}>
        <i style={{ width: it.dot ? 11 : 20, height: it.dot ? 11 : 3, borderRadius: it.dot ? "50%" : 2, background: it.c, display: "inline-block" }} />{it.label}
      </span>
    ))}
  </div>
);
const Loading = () => <div style={{ padding: 40, textAlign: "center", color: "var(--muted)", fontFamily: "var(--mono)", fontSize: 13 }}>loading model data…</div>;

/* ---------- embedded derived series (transforms of model output) ---------- */
const DEMO = [
  { c: "Nigeria", f: 4.48, a: 17.8, p: 223 }, { c: "Indonesia", f: 2.13, a: 29.8, p: 281 }, { c: "India", f: 1.98, a: 28.1, p: 1441 },
  { c: "Vietnam", f: 1.91, a: 32.4, p: 99 }, { c: "Brazil", f: 1.62, a: 33.9, p: 217 }, { c: "United States", f: 1.62, a: 38.0, p: 340 },
  { c: "United Kingdom", f: 1.56, a: 39.8, p: 69 }, { c: "Germany", f: 1.39, a: 45.1, p: 84 }, { c: "Japan", f: 1.20, a: 49.0, p: 124 },
  { c: "China", f: 1.00, a: 39.1, p: 1410 }, { c: "South Korea", f: 0.72, a: 44.5, p: 52 },
];
const CATCHUP = [
  { name: "South Korea", color: C.us, points: [[0, 100], [10, 229], [20, 520], [30, 781], [40, 1172], [50, 1420], [52, 1461]] as [number, number][], width: 2.4 },
  { name: "China", color: C.eu, points: [[0, 100], [7, 135], [17, 214], [27, 438], [37, 780], [39, 872]] as [number, number][], width: 2.4 },
  { name: "Brazil", color: C.cn, points: [[0, 101], [10, 152], [20, 207], [30, 369], [40, 351], [50, 440], [60, 636], [70, 612], [72, 655]] as [number, number][], width: 2.4 },
  { name: "Nigeria", color: C.ng, points: [[0, 100], [10, 92], [12, 97]] as [number, number][], width: 3.6 },
];
const MCFAN = [
  { year: 2025, p5: 1239, p25: 1239, p50: 1239, p75: 1239, p95: 1239 }, { year: 2026, p5: 1234, p25: 1325, p50: 1391, p75: 1460, p95: 1566 },
  { year: 2027, p5: 1271, p25: 1407, p50: 1513, p75: 1625, p95: 1804 }, { year: 2028, p5: 1340, p25: 1506, p50: 1640, p75: 1789, p95: 2060 },
  { year: 2029, p5: 1470, p25: 1642, p50: 1779, p75: 1958, p95: 2313 }, { year: 2030, p5: 1627, p25: 1803, p50: 1947, p75: 2152, p95: 2574 },
];
const VECTORS = [
  { i: "①", h: "Neutral & real assets", d: "Gold, Bitcoin, commodities, land — what no state can print or freeze, as the reserve issuer's resolution becomes inflation, not default." },
  { i: "②", h: "Sovereignty as the premium", d: "Who controls their money, energy, food, chips. The dividing line — not rich/poor. The euro periphery and most EMs lack it." },
  { i: "③", h: "The young South as the frontier", d: "The labour and consumers the aging North lost — if it converts the dividend. The lab warns Nigeria's is 'structurally unearned.'" },
  { i: "④", h: "Digital dollar rails", d: "For the dollar-scarce: stablecoins are dollar access without a US bank; AI-underwritten credit is institutions without a strong state." },
];
const USNG = [
  ["Position in the cycle", "LATE (reserve power)", "MID inflationary deleveraging"], ["Debt currency", "own reserve currency", "~47% external + local"],
  ["Reserve status", "yes — 57% of reserves (eroding)", "none"], ["Deleveraging type", "printing / debasement (latent)", "inflation + devaluation (underway)"],
  ["Debt-service / revenue", "~21% (interest only)", "~44% gross / >100% retained"], ["Central-bank lever", "the Fed — vast", "almost none"],
  ["External-default risk", "≈ nil (own currency)", "real (FX / rollover)"], ["The trap", "exorbitant privilege eroding", "no privilege to begin with"],
];

/* ==================== OVERVIEW (world order) ==================== */
export function Overview() {
  const res = useData("/api/reserves");
  const poles = useData<{ poles: Pole[] }>("/api/poles");
  const demoPts: Pt[] = DEMO.map((d) => ({
    x: d.f, y: d.a, color: d.f >= 2.1 ? C.grow : C.shrink, r: 4 + Math.sqrt(d.p) / 2.6,
    label: d.c === "United States" ? "US" : d.c === "South Korea" ? "S. Korea" : d.c,
    show: ["South Korea", "Nigeria", "Japan", "China", "United States", "India", "Germany"].includes(d.c),
    tip: `<b>${d.c}</b><br>fertility ${d.f} · median age ${d.a}<br>pop ~${d.p}m · ${d.f >= 2.1 ? "growing" : "below replacement"}`,
  }));
  const resSeries = res.data?.series || [];
  const usd = resSeries.filter((r: any) => r.usd_share_global_reserves_pct != null).map((r: any) => [r.year, r.usd_share_global_reserves_pct] as [number, number]);
  const fgn = resSeries.filter((r: any) => r.foreign_held_treasury_pct != null && r.year >= 2007).map((r: any) => [r.year, r.foreign_held_treasury_pct] as [number, number]);
  return (
    <div className="view-enter">
      <div style={{ maxWidth: "64ch", marginBottom: 40 }}>
        <p style={{ fontSize: "clamp(18px,2.5vw,22px)", color: "var(--secondary)", margin: 0, lineHeight: 1.4 }}>
          The incumbents are <b style={{ color: "var(--ink)" }}>all late in the same debt cycle at once</b>. The money is fragmenting. The people are moving south.
        </p>
      </div>

      <section style={{ marginBottom: 60 }}>
        <Head n="01 · the deepest current" title="The people are moving south"
          sub="Every economy below its replacement line (2.1 births/woman) is set to shrink. Almost the entire developed and risen world is there — Korea 0.72, China 1.00, Japan 1.20 — while the century's labour sits in the young South. Bubble = population." />
        <div className="panel">
          <Legend items={[{ c: C.grow, label: "at/above replacement (growing)", dot: true }, { c: C.shrink, label: "below replacement (set to shrink)", dot: true }, { c: "var(--muted)", label: "bubble = population", dot: true }]} />
          <Scatter points={demoPts} xDomain={[0.4, 4.8]} yDomain={[15, 52]} xTicks={[1, 2, 3, 4]} yTicks={[20, 30, 40, 50]}
            xLabel="births per woman  →" yLabel="median age  →" refX={2.1} refLabel="replacement 2.1" shade="left" />
        </div>
        <Cap>Total fertility rate (2023, World Bank) vs median age. Left of the line, births no longer replace deaths — South Korea's 0.72 is the lowest ever recorded.</Cap>
      </section>

      <section style={{ marginBottom: 60 }}>
        <Head n="02 · the money" title="The reserve order is fragmenting — slowly"
          sub="Not dollar collapse (nothing can yet replace it) but steady erosion: the dollar's share of global reserves has slid from 72% to 57% since 2000, and foreign ownership of US Treasuries is thinning." />
        <div className="panel">
          {res.loading ? <Loading /> : (
            <>
              <Legend items={[{ c: C.us, label: "USD share of reserves" }, { c: C.ng, label: "foreign-held US Treasuries" }]} />
              <LineChart series={[{ name: "USD reserves", color: C.us, points: usd }, { name: "Foreign Treasuries", color: C.ng, points: fgn }]}
                xDomain={[2000, 2025]} yDomain={[20, 75]} yTicks={[20, 35, 50, 65]} xTicks={[2000, 2010, 2020]} fmtY={(v) => v + "%"} rightPad={140} />
            </>
          )}
        </div>
        <Cap>USD share of allocated global FX reserves (IMF COFER) and foreign-held share of US Treasuries — live from <code>usa_debt_cycle.py</code>.</Cap>
      </section>

      <section style={{ marginBottom: 60 }}>
        <Head n="03 · the alignment" title="What the world is aligning with" />
        <div className="stagger" style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(220px,1fr))", gap: 14 }}>
          {VECTORS.map((v) => (
            <div key={v.h} className="panel" style={{ borderRadius: 12 }}>
              <div style={{ fontFamily: "var(--serif)", fontSize: 26, color: "var(--accent)" }}>{v.i}</div>
              <div style={{ fontWeight: 750, fontSize: 16, margin: "8px 0 5px" }}>{v.h}</div>
              <div style={{ fontSize: 13.5, color: "var(--secondary)" }}>{v.d}</div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

/* ==================== DEVELOPMENT AGE ==================== */
export function DevelopmentAge() {
  const { data, loading } = useData("/api/development-age");
  const dims = (data?.dimensions || []).map((d: any) => ({
    label: d.dim, value: d.korea_year,
    note: d.dim.startsWith("Urban") ? "ahead" : d.dim.startsWith("Health") ? "behind" : undefined,
    color: d.dim.startsWith("Urban") ? C.ng : d.dim.startsWith("Income") || d.dim.startsWith("Demog") ? "var(--muted)" : C.us,
  }));
  const div = data?.divergence || [];
  return (
    <div className="view-enter">
      <section style={{ marginBottom: 60 }}>
        <Head n="01 · the analogy" title="Nigeria is at South Korea's 1970 income"
          sub="Line each economy up at the moment it reached Nigeria's current income (year 0) and index it to 100. From the same start, Korea and China multiply; Brazil crawls; Nigeria is flat and slipping." />
        <div className="panel">
          <Legend items={CATCHUP.map((s) => ({ c: s.color, label: s.name }))} />
          <LineChart series={CATCHUP} xDomain={[0, 72]} yDomain={[80, 1600]} yLog yTicks={[100, 200, 400, 800, 1600]}
            xTicks={[0, 10, 20, 30, 40, 50, 60, 70]} xLabel="years after reaching Nigeria's current income" yLabel="income, indexed to 100"
            fmtY={(v) => (v === 100 ? "100" : "×" + v / 100)} height={420} />
        </div>
        <Cap>GDP per capita indexed to 100 at the year each country reached ~$2,207 (log scale). Maddison Project Database.</Cap>
      </section>

      <section style={{ marginBottom: 60 }}>
        <Head n="02 · the catch" title="Development is uneven — a 22-year spread"
          sub="Map Nigeria onto Korea's timeline dimension by dimension. Urbanization has run ~22 years ahead of health and industry: cities before jobs, health, or factories caught up." />
        <div className="panel">
          {loading ? <Loading /> : <Lollipop rows={dims} xDomain={[1958, 1986]} xTicks={[1960, 1965, 1970, 1975, 1980, 1985]} />}
        </div>
      </section>

      <section style={{ marginBottom: 60 }}>
        <Head n="03 · the odds" title="The Monte-Carlo 2030 fan"
          sub="A 40,000-draw simulation over the base/bull/bear scenarios. The median dollar income rises but does not regain its 2023 level ($2,139) — that happens in only ~26% of draws." />
        <div className="panel">
          <Legend items={[{ c: "#9ec5f4", label: "5–95th pct" }, { c: "#2a78d6", label: "median" }, { c: C.ng, label: "2023 income" }]} />
          <AreaFan data={MCFAN} yDomain={[1150, 2650]} yTicks={[1200, 1600, 2000, 2400]} refLine={2139}
            refLabel="2023 level $2,139 · regained in ~26% of draws" colors={{ band1: "#cde2fb", band2: "#9ec5f4", line: "#256abf", ref: C.ng }} />
        </div>
      </section>

      <section style={{ marginBottom: 40 }}>
        <Head n="04 · the conditioning" title="Why the parallel is unearned" sub="The income match is arithmetic; the outcome depends on initial conditions. All 7 catch-up factors are currently adverse." />
        {loading ? <Loading /> : (
          <div className="stagger" style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(240px,1fr))", gap: 12 }}>
            {div.map((f: any) => (
              <div key={f.factor} className="panel" style={{ borderRadius: 10, borderLeft: "3px solid #c8432f" }}>
                <div style={{ fontWeight: 700, fontSize: 15, textTransform: "capitalize" }}>{f.factor?.replace(/_/g, " ")}</div>
                <div style={{ color: "var(--secondary)", fontSize: 13, marginTop: 3 }}>{f.note}</div>
                <span style={{ display: "inline-block", fontFamily: "var(--mono)", fontSize: 10.5, letterSpacing: ".08em", textTransform: "uppercase", color: "#c8432f", background: "#fbe9e4", borderRadius: 100, padding: "2px 8px", marginTop: 8 }}>{f.tilt || "adverse"}</span>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}

/* ==================== TWO POLES (US) ==================== */
export function TwoPoles() {
  const { data, loading } = useData("/api/us");
  if (loading) return <div className="view-enter"><Loading /></div>;
  const g = data.gauges as any[];
  const pick = (col: string, years: number[]) => years.map((y) => [y, g.find((r) => r.year === y)?.[col]] as [number, number]).filter((p) => p[1] != null);
  const gaugeYears = [1980, 2000, 2007, 2010, 2020, 2025];
  const cards = [
    { k: "Debt held by public", col: "federal_debt_held_by_public_pct_gdp", end: "98%", color: C.us },
    { k: "Net interest / revenue", col: "net_interest_pct_revenue", end: "21%", color: C.us },
    { k: "USD share of reserves", col: "usd_share_global_reserves_pct", end: "57%", color: C.ng },
  ];
  const irf = data.irf as any[];
  const irfSeries = [
    { name: "GDP growth", color: C.gdp, points: irf.map((r) => [r.horizon, r.real_gdp_growth] as [number, number]) },
    { name: "Unemployment", color: C.unemp, points: irf.map((r) => [r.horizon, r.unemployment_rate] as [number, number]) },
    { name: "Inflation", color: C.infl, points: irf.map((r) => [r.horizon, r.cpi_inflation] as [number, number]) },
  ];
  return (
    <div className="view-enter">
      <section style={{ marginBottom: 60 }}>
        <Head n="01 · the reserve pole" title="The US, late-cycle"
          sub="Debt near a post-WWII record, a structural peacetime deficit, an interest bill compounding faster than growth, and the reserve privilege eroding. Because the US borrows in its own reserve currency, the resolution is inflation — not default." />
        <div className="stagger" style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(240px,1fr))", gap: 16 }}>
          {cards.map((c) => (
            <div key={c.k} className="panel" style={{ borderRadius: 14 }}>
              <div className="eyebrow">{c.k}</div>
              <div style={{ fontSize: 15, color: "var(--secondary)", margin: "2px 0 8px" }}>
                <b style={{ color: c.color, fontSize: 22, fontWeight: 800 }}>{c.end}</b> <span style={{ fontSize: 12 }}>2025</span>
              </div>
              <Spark points={pick(c.col, gaugeYears)} color={c.color} />
            </div>
          ))}
        </div>
      </section>

      <section style={{ marginBottom: 60 }}>
        <Head n="02 · the lever" title="How a rate hike transmits"
          sub="A monetary VAR (1960–2025, recursive identification) traces a +100bp fed-funds shock: output falls fast, unemployment rises with a lag, inflation eases last — after a brief 'price-puzzle' tick." />
        <div className="panel">
          <Legend items={irfSeries.map((s) => ({ c: s.color, label: s.name }))} />
          <LineChart series={irfSeries} xDomain={[0, 6]} yDomain={[-0.7, 0.5]} yTicks={[-0.5, -0.25, 0, 0.25, 0.5]}
            xTicks={[0, 1, 2, 3, 4, 5, 6]} xLabel="years after a +100bp fed funds shock" fmtY={(v) => v.toFixed(2)} />
        </div>
        <Cap>Impulse responses to a +100bp fed funds shock, percentage-point deviation — live from <code>usa_monetary_var.py</code>.</Cap>
      </section>

      <section style={{ marginBottom: 40 }}>
        <Head n="03 · the two poles" title="United States ↔ Nigeria" sub="Same big-debt-cycle template, opposite ends." />
        <div className="panel" style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 14, minWidth: 560 }}>
            <thead><tr>
              <th style={{ textAlign: "left", padding: "10px 12px", color: "var(--muted)", fontSize: 12, textTransform: "uppercase", letterSpacing: ".05em" }}>Dimension</th>
              <th style={{ textAlign: "left", padding: "10px 12px", color: C.us }}>United States</th>
              <th style={{ textAlign: "left", padding: "10px 12px", color: C.ng }}>Nigeria</th>
            </tr></thead>
            <tbody>{USNG.map((r) => (
              <tr key={r[0]}><td style={{ padding: "10px 12px", color: "var(--secondary)", borderTop: "1px solid var(--hair)" }}>{r[0]}</td>
                <td style={{ padding: "10px 12px", borderTop: "1px solid var(--hair)", borderLeft: "3px solid " + C.us }}>{r[1]}</td>
                <td style={{ padding: "10px 12px", borderTop: "1px solid var(--hair)", borderLeft: "3px solid " + C.ng }}>{r[2]}</td></tr>
            ))}</tbody>
          </table>
        </div>
      </section>
    </div>
  );
}

/* ==================== FIVE POLES ==================== */
export function FivePoles() {
  const { data, loading } = useData<{ poles: Pole[] }>("/api/poles");
  if (loading || !data) return <div className="view-enter"><Loading /></div>;
  const poles = data.poles;
  const scatterPts: Pt[] = poles.map((p) => ({
    x: p.debt_gdp || 0, y: p.space, color: p.color, r: 13, label: p.name, show: true,
    tip: `<b>${p.name}</b> · ${p.cycle}<br>debt ${p.debt_gdp}% · space ${p.space}/100<br>${p.own}`,
  }));
  const bars = poles.map((p) => ({ label: p.name, value: Math.round(p.debt_gdp || 0), color: p.color }));
  return (
    <div className="view-enter">
      <section style={{ marginBottom: 60 }}>
        <Head n="01 · the map" title="Debt level vs room to manage it"
          sub="Government debt (horizontal) against policy space (vertical). The diagonal is the story: low-debt Nigeria sits in the danger corner because it has no space; high-debt US and Japan sit higher because they do." />
        <div className="panel">
          <Legend items={poles.map((p) => ({ c: p.color, label: p.name, dot: true }))} />
          <Scatter points={scatterPts} xDomain={[0, 240]} yDomain={[0, 100]} xTicks={[0, 50, 100, 150, 200]} yTicks={[0, 25, 50, 75, 100]}
            xLabel="government debt, % of GDP  →" yLabel="policy space to manage it  →" height={480} />
        </div>
        <Cap>Debt = general-government gross debt % of GDP (live). Policy-space is a qualitative composite (0–100).</Cap>
      </section>

      <section style={{ marginBottom: 60 }}>
        <Head n="02 · like-for-like" title="Government debt, compared" sub="Same measure across poles. Nigeria's is the lowest by far; the strain there is FX and revenue, not the debt ratio." />
        <div className="panel"><HBars data={bars} max={230} unit="%" /></div>
      </section>

      <section style={{ marginBottom: 40 }}>
        <Head n="03 · the matrix" title="Five regimes, one template" />
        <div className="panel" style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13.5, minWidth: 680 }}>
            <thead><tr>
              <th style={{ textAlign: "left", padding: "10px 12px", color: "var(--muted)", fontSize: 12, textTransform: "uppercase" }}>Dimension</th>
              {poles.map((p) => <th key={p.name} style={{ textAlign: "left", padding: "10px 12px", color: p.color, fontSize: 12, textTransform: "uppercase" }}>{p.name}</th>)}
            </tr></thead>
            <tbody>
              {[["Cycle", "cycle"], ["Lever", "lever"], ["Main risk", "risk"], ["The trap", "trap"]].map(([label, k]) => (
                <tr key={label}><td style={{ padding: "10px 12px", color: "var(--muted)", borderTop: "1px solid var(--hair)", fontSize: 12.5 }}>{label}</td>
                  {poles.map((p) => <td key={p.name} style={{ padding: "10px 12px", borderTop: "1px solid var(--hair)" }}>{(p as any)[k]}</td>)}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}

/* ==================== INDEX ==================== */
export function IndexView() {
  const { data, loading } = useData<{ poles: IndexPole[] }>("/api/index");
  if (loading || !data) return <div className="view-enter"><Loading /></div>;
  const poles = [...data.poles].sort((a, b) => b.resilience - a.resilience);
  const bars = poles.map((p) => ({ label: p.name, value: Math.round(p.resilience), color: POLE_COLORS[p.name] || "var(--accent)", tip: `<b>${p.name}</b><br>resilience ${p.resilience} · fragility ${p.fragility}<br>buffer ${p.buffer} · sustain ${p.sustain} · vitality ${Math.round(p.vitality)}` }));
  return (
    <div className="view-enter">
      <section style={{ marginBottom: 40 }}>
        <Head n="composite index" title="Resilience, computed from three pillars"
          sub="Resilience = 0.40·buffer + 0.30·debt-sustainability + 0.30·demographic-vitality (each 0–100). Not the debt ratio — the room behind it." />
        <div className="panel"><HBars data={bars} max={80} unit="" labelW={130} /></div>
        <Cap>Higher = more resilient. US 64 (most resilient) → Europe 38 (most fragile). Live from <code>macro_index.py</code>.</Cap>
      </section>

      <section style={{ marginBottom: 40 }}>
        <Head n="the decomposition" title="Why Nigeria's youth is its balance sheet" />
        <div className="panel" style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 14, minWidth: 620 }}>
            <thead><tr>{["Pole", "Buffer", "Debt-sustain", "Vitality", "Resilience", "Fragility"].map((h) => (
              <th key={h} style={{ textAlign: h === "Pole" ? "left" : "right", padding: "10px 12px", color: "var(--muted)", fontSize: 12, textTransform: "uppercase" }}>{h}</th>
            ))}</tr></thead>
            <tbody>{poles.map((p) => (
              <tr key={p.name}>
                <td style={{ padding: "10px 12px", borderTop: "1px solid var(--hair)", fontWeight: 700, color: POLE_COLORS[p.name] }}>{p.name}</td>
                {[p.buffer, p.sustain, Math.round(p.vitality), Math.round(p.resilience), Math.round(p.fragility)].map((v, i) => (
                  <td key={i} style={{ padding: "10px 12px", borderTop: "1px solid var(--hair)", textAlign: "right", fontWeight: i >= 3 ? 700 : 400 }}>{v}</td>
                ))}
              </tr>
            ))}</tbody>
          </table>
        </div>
        <Cap>Strip out demographics and Nigeria collapses to ~15 (worst) — its vitality (99/100, the youngest) offsets the weakest buffer. The mirror image: Japan &amp; China score well on buffer but their vitality (7, 20) is collapsing. Resilient-but-dying vs fragile-but-young.</Cap>
      </section>
    </div>
  );
}

/* ==================== DEMOGRAPHICS ==================== */
export function Demographics() {
  const { data, loading } = useData("/api/demographics");
  return (
    <div className="view-enter">
      <Head n="demographics" title="Births, deaths, and who's shrinking"
        sub="Fertility below replacement means a shrinking population once age-momentum fades; a birth-to-death ratio below 1 means it's already happening." />
      {loading ? <Loading /> : data?.available ? (
        <>
        <div className="panel" style={{ marginBottom: 20 }}>
          <div className="chart-title" style={{ marginBottom: 10 }}>Natural change — births minus deaths, per 1,000</div>
          <DivBars domain={[-8, 30]} unit="/1k"
            data={[...(data.countries as any[])].sort((a, b) => a.natural_increase_per_1000 - b.natural_increase_per_1000).map((c) => ({
              label: c.country, value: c.natural_increase_per_1000,
              color: c.natural_increase_per_1000 < 0 ? "#c8432f" : "#1f8a5b",
              tip: `<b>${c.country}</b><br>births ${c.crude_birth_rate}/1k · deaths ${c.crude_death_rate}/1k<br>natural ${c.natural_increase_per_1000 > 0 ? "+" : ""}${c.natural_increase_per_1000}/1k · B:D ${c.birth_to_death_ratio}`,
            }))} />
          <Cap>Below zero = deaths outnumber births (already shrinking): Italy, Japan, Germany, China, South Korea. Nigeria (+28) is the outlier. Source: <code>demographics.py</code> (UN WPP 2024).</Cap>
        </div>
        <div className="panel" style={{ overflowX: "auto" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13.5, minWidth: 720 }}>
            <thead><tr>{["Country", "Fertility", "Birth/1k", "Death/1k", "Natural Δ", "B:D ratio", "Median age", "Pop 2024m", "Pop 2100m"].map((h) => (
              <th key={h} style={{ textAlign: h === "Country" ? "left" : "right", padding: "9px 11px", color: "var(--muted)", fontSize: 11.5, textTransform: "uppercase" }}>{h}</th>
            ))}</tr></thead>
            <tbody>{(data.countries as any[]).map((c) => (
              <tr key={c.country}>
                <td style={{ padding: "9px 11px", borderTop: "1px solid var(--hair)", fontWeight: 700, color: POLE_COLORS[c.country] || "var(--ink)" }}>{c.country}</td>
                {["total_fertility_rate", "crude_birth_rate", "crude_death_rate", "natural_increase_per_1000", "birth_to_death_ratio", "median_age_years", "pop_millions_2024", "pop_millions_2100"].map((k) => (
                  <td key={k} style={{ padding: "9px 11px", borderTop: "1px solid var(--hair)", textAlign: "right", color: k === "natural_increase_per_1000" && c[k] < 0 ? "#c8432f" : "inherit" }}>{c[k] ?? "—"}</td>
                ))}
              </tr>
            ))}</tbody>
          </table>
        </div>
        </>
      ) : (
        <div className="panel" style={{ textAlign: "center", padding: 48, color: "var(--muted)" }}>
          <div style={{ fontSize: 15, marginBottom: 6 }}>The birth-vs-death / population-to-2100 model is being built.</div>
          <div style={{ fontSize: 13, fontFamily: "var(--mono)" }}>demographics.csv → this view will populate automatically.</div>
        </div>
      )}
    </div>
  );
}
