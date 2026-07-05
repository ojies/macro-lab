"use client";
import React, { createContext, useContext, useEffect, useRef, useState } from "react";

/* ---------------- tooltip ---------------- */
const TooltipCtx = createContext<{ show: (e: React.MouseEvent, html: string) => void; hide: () => void }>({
  show: () => {},
  hide: () => {},
});
export const useTooltip = () => useContext(TooltipCtx);

export function TooltipProvider({ children }: { children: React.ReactNode }) {
  const ref = useRef<HTMLDivElement>(null);
  const show = (e: React.MouseEvent, html: string) => {
    const el = ref.current;
    if (!el) return;
    el.innerHTML = html;
    el.style.opacity = "1";
    el.style.left = Math.min(e.clientX + 14, window.innerWidth - 270) + "px";
    el.style.top = e.clientY - 10 + "px";
  };
  const hide = () => {
    if (ref.current) ref.current.style.opacity = "0";
  };
  return (
    <TooltipCtx.Provider value={{ show, hide }}>
      {children}
      <div ref={ref} className="tt" />
    </TooltipCtx.Provider>
  );
}

export function useMounted() {
  const [m, setM] = useState(false);
  useEffect(() => {
    const t = requestAnimationFrame(() => setM(true));
    return () => cancelAnimationFrame(t);
  }, []);
  return m;
}

const AX = 940; // logical chart width

/* ---------------- line chart (optional log-y) ---------------- */
export type Series = { name: string; color: string; points: [number, number][]; width?: number };
export function LineChart({
  series, xDomain, yDomain, yTicks, xTicks, yLog = false, xLabel, yLabel, height = 340, rightPad = 108, fmtY,
}: {
  series: Series[]; xDomain: [number, number]; yDomain: [number, number]; yTicks: number[]; xTicks: number[];
  yLog?: boolean; xLabel?: string; yLabel?: string; height?: number; rightPad?: number; fmtY?: (v: number) => string;
}) {
  const mounted = useMounted();
  const tt = useTooltip();
  const W = AX, H = height, m = { t: 16, r: rightPad, b: 42, l: 52 };
  const iw = W - m.l - m.r, ih = H - m.t - m.b;
  const [x0, x1] = xDomain;
  const ly = (v: number) => (yLog ? Math.log(v) : v);
  const [yy0, yy1] = [ly(yDomain[0]), ly(yDomain[1])];
  const sx = (v: number) => m.l + ((v - x0) / (x1 - x0)) * iw;
  const sy = (v: number) => m.t + ih - ((ly(v) - yy0) / (yy1 - yy0)) * ih;
  return (
    <svg viewBox={`0 0 ${W} ${H}`} style={{ width: "100%", height: "auto", overflow: "visible" }}>
      <g className="grid">{yTicks.map((v) => <line key={v} x1={m.l} x2={m.l + iw} y1={sy(v)} y2={sy(v)} />)}</g>
      <g className="axis">
        {yTicks.map((v) => <text key={v} x={m.l - 9} y={sy(v) + 4} textAnchor="end">{fmtY ? fmtY(v) : v}</text>)}
        {xTicks.map((v) => <text key={v} x={sx(v)} y={m.t + ih + 20} textAnchor="middle">{v}</text>)}
        {xLabel && <text x={m.l + iw / 2} y={H - 4} textAnchor="middle" style={{ fill: "var(--secondary)", fontSize: 12 }}>{xLabel}</text>}
        {yLabel && <text transform={`rotate(-90 ${m.l - 40} ${m.t + ih / 2})`} x={m.l - 40} y={m.t + ih / 2} textAnchor="middle" style={{ fill: "var(--secondary)", fontSize: 12 }}>{yLabel}</text>}
      </g>
      {series.map((s) => {
        const d = s.points.map((p, i) => (i ? "L" : "M") + sx(p[0]).toFixed(1) + " " + sy(p[1]).toFixed(1)).join(" ");
        const last = s.points[s.points.length - 1];
        return (
          <g key={s.name}>
            <path d={d} fill="none" stroke={s.color} strokeWidth={s.width || 2.4} strokeLinejoin="round" strokeLinecap="round"
              pathLength={1} style={{ strokeDasharray: 1, strokeDashoffset: mounted ? 0 : 1, transition: "stroke-dashoffset 1.1s ease" }} />
            <circle cx={sx(last[0])} cy={sy(last[1])} r={3.5} fill={s.color} style={{ opacity: mounted ? 1 : 0, transition: "opacity .4s ease 1s" }} />
            <text x={sx(last[0]) + 8} y={sy(last[1]) + 4} style={{ fill: s.color, fontSize: 12.5, fontWeight: 700, opacity: mounted ? 1 : 0, transition: "opacity .4s ease 1s" }}>{s.name}</text>
            {s.points.map((p, i) => (
              <circle key={i} cx={sx(p[0])} cy={sy(p[1])} r={9} fill="transparent" style={{ cursor: "pointer" }}
                onMouseMove={(e) => tt.show(e, `<b>${s.name}</b> · ${p[0]}<br>${(fmtY ? fmtY(p[1]) : p[1].toFixed(2))}`)} onMouseLeave={tt.hide} />
            ))}
          </g>
        );
      })}
    </svg>
  );
}

/* ---------------- area fan (Monte Carlo) ---------------- */
export function AreaFan({ data, yDomain, yTicks, refLine, refLabel, colors }: {
  data: { year: number; p5: number; p25: number; p50: number; p75: number; p95: number }[];
  yDomain: [number, number]; yTicks: number[]; refLine?: number; refLabel?: string; colors: { band1: string; band2: string; line: string; ref: string };
}) {
  const mounted = useMounted();
  const tt = useTooltip();
  const W = AX, H = 360, m = { t: 16, r: 60, b: 40, l: 56 };
  const iw = W - m.l - m.r, ih = H - m.t - m.b;
  const xs = data.map((d) => d.year);
  const [x0, x1] = [Math.min(...xs), Math.max(...xs)];
  const sx = (v: number) => m.l + ((v - x0) / (x1 - x0)) * iw;
  const sy = (v: number) => m.t + ih - ((v - yDomain[0]) / (yDomain[1] - yDomain[0])) * ih;
  const band = (lo: keyof (typeof data)[0], hi: keyof (typeof data)[0]) => {
    let d = "M";
    data.forEach((r, i) => (d += (i ? "L" : "") + sx(r.year).toFixed(1) + " " + sy(r[hi] as number).toFixed(1) + " "));
    for (let i = data.length - 1; i >= 0; i--) d += "L" + sx(data[i].year).toFixed(1) + " " + sy(data[i][lo] as number).toFixed(1) + " ";
    return d + "Z";
  };
  const median = data.map((r, i) => (i ? "L" : "M") + sx(r.year).toFixed(1) + " " + sy(r.p50).toFixed(1)).join(" ");
  return (
    <svg viewBox={`0 0 ${W} ${H}`} style={{ width: "100%", height: "auto", overflow: "visible" }}>
      <g className="grid">{yTicks.map((v) => <line key={v} x1={m.l} x2={m.l + iw} y1={sy(v)} y2={sy(v)} />)}</g>
      <g style={{ opacity: mounted ? 1 : 0, transition: "opacity .8s ease" }}>
        <path d={band("p5", "p95")} fill={colors.band1} />
        <path d={band("p25", "p75")} fill={colors.band2} />
      </g>
      <path d={median} fill="none" stroke={colors.line} strokeWidth={2.6} strokeLinecap="round"
        pathLength={1} style={{ strokeDasharray: 1, strokeDashoffset: mounted ? 0 : 1, transition: "stroke-dashoffset 1.1s ease" }} />
      {refLine !== undefined && (
        <>
          <line x1={m.l} x2={m.l + iw} y1={sy(refLine)} y2={sy(refLine)} stroke={colors.ref} strokeWidth={1.5} strokeDasharray="5 4" />
          {refLabel && <text x={m.l + iw} y={sy(refLine) - 7} textAnchor="end" style={{ fill: colors.ref, fontSize: 12.5, fontWeight: 700 }}>{refLabel}</text>}
        </>
      )}
      <g className="axis">
        {yTicks.map((v) => <text key={v} x={m.l - 9} y={sy(v) + 4} textAnchor="end">${v}</text>)}
        {data.map((r) => <text key={r.year} x={sx(r.year)} y={m.t + ih + 20} textAnchor="middle">{r.year}</text>)}
      </g>
      {data.map((r) => (
        <rect key={r.year} x={sx(r.year) - 14} y={m.t} width={28} height={ih} fill="transparent" style={{ cursor: "pointer" }}
          onMouseMove={(e) => tt.show(e, `<b>${r.year}</b><br>median $${r.p50}<br>P5–P95 $${r.p5}–$${r.p95}`)} onMouseLeave={tt.hide} />
      ))}
    </svg>
  );
}

/* ---------------- scatter (bubbles) ---------------- */
export type Pt = { x: number; y: number; label?: string; color: string; r: number; tip: string; show?: boolean };
export function Scatter({ points, xDomain, yDomain, xTicks, yTicks, xLabel, yLabel, refX, refLabel, height = 500, fmtX, shade }: {
  points: Pt[]; xDomain: [number, number]; yDomain: [number, number]; xTicks: number[]; yTicks: number[];
  xLabel?: string; yLabel?: string; refX?: number; refLabel?: string; height?: number; fmtX?: (v: number) => string; shade?: "left" | "bottom";
}) {
  const mounted = useMounted();
  const tt = useTooltip();
  const W = AX, H = height, m = { t: 20, r: 30, b: 50, l: 56 };
  const iw = W - m.l - m.r, ih = H - m.t - m.b;
  const sx = (v: number) => m.l + ((v - xDomain[0]) / (xDomain[1] - xDomain[0])) * iw;
  const sy = (v: number) => m.t + ih - ((v - yDomain[0]) / (yDomain[1] - yDomain[0])) * ih;
  return (
    <svg viewBox={`0 0 ${W} ${H}`} style={{ width: "100%", height: "auto", overflow: "visible" }}>
      <g className="grid">
        {xTicks.map((v) => <line key={"x" + v} x1={sx(v)} x2={sx(v)} y1={m.t} y2={m.t + ih} />)}
        {yTicks.map((v) => <line key={"y" + v} x1={m.l} x2={m.l + iw} y1={sy(v)} y2={sy(v)} />)}
      </g>
      {shade === "left" && refX !== undefined && <rect x={m.l} y={m.t} width={sx(refX) - m.l} height={ih} fill="var(--shrink)" opacity={0.05} />}
      {refX !== undefined && (
        <>
          <line x1={sx(refX)} x2={sx(refX)} y1={m.t - 4} y2={m.t + ih} stroke="var(--accent)" strokeWidth={1.5} strokeDasharray="5 4" />
          {refLabel && <text x={sx(refX) - 8} y={m.t + 10} textAnchor="end" style={{ fill: "var(--accent)", fontSize: 11, fontWeight: 700 }}>{refLabel}</text>}
        </>
      )}
      <g className="axis">
        {xTicks.map((v) => <text key={v} x={sx(v)} y={m.t + ih + 20} textAnchor="middle">{fmtX ? fmtX(v) : v}</text>)}
        {yTicks.map((v) => <text key={v} x={m.l - 10} y={sy(v) + 4} textAnchor="end">{v}</text>)}
        {xLabel && <text x={m.l + iw / 2} y={H - 6} textAnchor="middle" style={{ fill: "var(--secondary)", fontSize: 12 }}>{xLabel}</text>}
        {yLabel && <text transform="rotate(-90)" x={-(m.t + ih / 2)} y={16} textAnchor="middle" style={{ fill: "var(--secondary)", fontSize: 12 }}>{yLabel}</text>}
      </g>
      {points.map((p, i) => (
        <g key={i} style={{ transformOrigin: `${sx(p.x)}px ${sy(p.y)}px`, animation: mounted ? `popIn .5s cubic-bezier(.2,.7,.2,1) both ${0.05 + i * 0.05}s` : "none" }}>
          <circle cx={sx(p.x)} cy={sy(p.y)} r={p.r} fill={p.color} opacity={0.85} stroke="var(--surface)" strokeWidth={2} />
          {p.label && p.show && <text x={sx(p.x)} y={sy(p.y) - p.r - 4} textAnchor="middle" style={{ fill: p.color, fontSize: 12, fontWeight: 700 }}>{p.label}</text>}
          <circle cx={sx(p.x)} cy={sy(p.y)} r={Math.max(p.r, 11)} fill="transparent" style={{ cursor: "pointer" }}
            onMouseMove={(e) => tt.show(e, p.tip)} onMouseLeave={tt.hide} />
        </g>
      ))}
    </svg>
  );
}

/* ---------------- horizontal bars (animated grow) ---------------- */
export function HBars({ data, max, unit = "%", height, labelW = 130 }: {
  data: { label: string; value: number; color: string; tip?: string }[]; max: number; unit?: string; height?: number; labelW?: number;
}) {
  const mounted = useMounted();
  const tt = useTooltip();
  const rowH = 40, W = AX, m = { t: 6, r: 64, b: 24, l: labelW };
  const iw = W - m.l - m.r, H = height || m.t + data.length * rowH + m.b;
  const sx = (v: number) => (v / max) * iw;
  return (
    <svg viewBox={`0 0 ${W} ${H}`} style={{ width: "100%", height: "auto", overflow: "visible" }}>
      {data.map((d, i) => {
        const y = m.t + i * rowH + 7, bh = rowH - 16, w = Math.max(2, sx(d.value));
        return (
          <g key={d.label}>
            <text x={m.l - 12} y={y + bh / 2 + 4} textAnchor="end" style={{ fill: "var(--secondary)", fontSize: 13, fontWeight: 600 }}>{d.label}</text>
            <rect x={m.l} y={y} width={mounted ? w : 0} height={bh} rx={4} fill={d.color}
              style={{ transition: `width .9s cubic-bezier(.2,.7,.2,1) ${i * 0.06}s`, cursor: "pointer" }}
              onMouseMove={(e) => tt.show(e, d.tip || `<b>${d.label}</b><br>${d.value}${unit}`)} onMouseLeave={tt.hide} />
            <text x={m.l + w + 8} y={y + bh / 2 + 4} style={{ fill: "var(--ink)", fontSize: 12.5, fontWeight: 700, opacity: mounted ? 1 : 0, transition: `opacity .4s ease ${0.5 + i * 0.06}s` }}>{d.value}{unit}</text>
          </g>
        );
      })}
    </svg>
  );
}

/* ---------------- lollipop (dimension spread) ---------------- */
export function Lollipop({ rows, xDomain, xTicks }: {
  rows: { label: string; value: number; note?: string; color: string }[]; xDomain: [number, number]; xTicks: number[];
}) {
  const mounted = useMounted();
  const tt = useTooltip();
  const W = AX, rowH = 46, m = { t: 30, r: 60, b: 34, l: 220 };
  const iw = W - m.l - m.r, H = m.t + rows.length * rowH + m.b;
  const sx = (v: number) => m.l + ((v - xDomain[0]) / (xDomain[1] - xDomain[0])) * iw;
  const lo = Math.min(...rows.map((r) => r.value)), hi = Math.max(...rows.map((r) => r.value));
  return (
    <svg viewBox={`0 0 ${W} ${H}`} style={{ width: "100%", height: "auto", overflow: "visible" }}>
      <rect x={sx(lo)} y={m.t - 12} width={sx(hi) - sx(lo)} height={4} rx={2} fill="var(--surface-2)" />
      <text x={(sx(lo) + sx(hi)) / 2} y={m.t - 18} textAnchor="middle" style={{ fill: "var(--muted)", fontSize: 12 }}>{hi - lo}-year spread</text>
      <g className="axis">{xTicks.map((v) => <text key={v} x={sx(v)} y={m.t + rows.length * rowH + 12} textAnchor="middle">{v}</text>)}</g>
      {rows.map((r, i) => {
        const cy = m.t + i * rowH + rowH / 2;
        return (
          <g key={r.label} style={{ animation: mounted ? `fadeUp .5s ease both ${0.08 * i}s` : "none" }}>
            <line x1={m.l} x2={sx(r.value)} y1={cy} y2={cy} stroke="var(--hair)" />
            <text x={m.l - 14} y={cy + 4} textAnchor="end" style={{ fill: "var(--secondary)", fontSize: 13, fontWeight: 600 }}>{r.label}</text>
            <circle cx={sx(r.value)} cy={cy} r={7} fill={r.color} stroke="var(--surface)" strokeWidth={2} style={{ cursor: "pointer" }}
              onMouseMove={(e) => tt.show(e, `<b>${r.label}</b><br>≈ Korea ${r.value}`)} onMouseLeave={tt.hide} />
            <text x={sx(r.value)} y={cy - 13} textAnchor="middle" style={{ fill: r.color, fontSize: 11, fontWeight: 700, fontFamily: "var(--mono)" }}>{"'" + String(r.value).slice(2)}</text>
            {r.note && <text x={sx(r.value) + (r.note === "ahead" ? 14 : -14)} y={cy + 4} textAnchor={r.note === "ahead" ? "start" : "end"} style={{ fill: r.color, fontSize: 11 }}>{r.note}</text>}
          </g>
        );
      })}
    </svg>
  );
}

/* ---------------- diverging bars (around zero) ---------------- */
export function DivBars({ data, domain, unit = "", labelW = 130 }: {
  data: { label: string; value: number; color: string; tip?: string }[]; domain: [number, number]; unit?: string; labelW?: number;
}) {
  const mounted = useMounted();
  const tt = useTooltip();
  const rowH = 34, W = AX, m = { t: 6, r: 40, b: 26, l: labelW };
  const iw = W - m.l - m.r, H = m.t + data.length * rowH + m.b;
  const sx = (v: number) => m.l + ((v - domain[0]) / (domain[1] - domain[0])) * iw;
  const zero = sx(0);
  return (
    <svg viewBox={`0 0 ${W} ${H}`} style={{ width: "100%", height: "auto", overflow: "visible" }}>
      <line x1={zero} x2={zero} y1={m.t} y2={m.t + data.length * rowH} stroke="var(--muted)" strokeWidth={1.2} />
      <text x={zero} y={m.t + data.length * rowH + 18} textAnchor="middle" className="axis" style={{ fill: "var(--muted)" }}>0 (replacement of deaths)</text>
      {data.map((d, i) => {
        const y = m.t + i * rowH + 6, bh = rowH - 13;
        const x = d.value >= 0 ? zero : sx(d.value);
        const w = Math.abs(sx(d.value) - zero);
        return (
          <g key={d.label}>
            <text x={m.l - 12} y={y + bh / 2 + 4} textAnchor="end" style={{ fill: "var(--secondary)", fontSize: 12.5, fontWeight: 600 }}>{d.label}</text>
            <rect x={d.value >= 0 ? zero : sx(d.value)} y={y} width={mounted ? w : 0} height={bh} rx={3} fill={d.color}
              style={{ transition: `width .8s cubic-bezier(.2,.7,.2,1) ${i * 0.04}s`, transformOrigin: `${zero}px center`, cursor: "pointer" }}
              onMouseMove={(e) => tt.show(e, d.tip || `<b>${d.label}</b><br>${d.value > 0 ? "+" : ""}${d.value}${unit}`)} onMouseLeave={tt.hide} />
            <text x={d.value >= 0 ? sx(d.value) + 6 : sx(d.value) - 6} y={y + bh / 2 + 4} textAnchor={d.value >= 0 ? "start" : "end"}
              style={{ fill: d.color, fontSize: 11.5, fontWeight: 700, opacity: mounted ? 1 : 0, transition: `opacity .4s ease ${0.4 + i * 0.04}s` }}>{d.value > 0 ? "+" : ""}{d.value}</text>
          </g>
        );
      })}
    </svg>
  );
}

/* ---------------- sparkline (small multiple) ---------------- */
export function Spark({ points, color, height = 90 }: { points: [number, number][]; color: string; height?: number }) {
  const mounted = useMounted();
  const W = 300, H = height, m = { t: 10, r: 12, b: 8, l: 8 };
  const iw = W - m.l - m.r, ih = H - m.t - m.b;
  const xs = points.map((p) => p[0]), ys = points.map((p) => p[1]);
  const [x0, x1] = [Math.min(...xs), Math.max(...xs)];
  const [y0, y1] = [Math.min(...ys) * 0.92, Math.max(...ys) * 1.05];
  const sx = (v: number) => m.l + ((v - x0) / (x1 - x0)) * iw;
  const sy = (v: number) => m.t + ih - ((v - y0) / (y1 - y0)) * ih;
  const d = points.map((p, i) => (i ? "L" : "M") + sx(p[0]).toFixed(1) + " " + sy(p[1]).toFixed(1)).join(" ");
  const area = d + `L${sx(x1)} ${m.t + ih} L${sx(x0)} ${m.t + ih} Z`;
  const last = points[points.length - 1];
  return (
    <svg viewBox={`0 0 ${W} ${H}`} style={{ width: "100%", height: "auto" }}>
      <path d={area} fill={color} opacity={0.08} />
      <path d={d} fill="none" stroke={color} strokeWidth={2.4} strokeLinejoin="round" strokeLinecap="round"
        pathLength={1} style={{ strokeDasharray: 1, strokeDashoffset: mounted ? 0 : 1, transition: "stroke-dashoffset 1s ease" }} />
      <circle cx={sx(last[0])} cy={sy(last[1])} r={3.4} fill={color} style={{ opacity: mounted ? 1 : 0, transition: "opacity .4s ease .9s" }} />
    </svg>
  );
}
