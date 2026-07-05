// macro-lab dashboard — shared colours (the validated pole palette) and helpers.

export const POLE_COLORS: Record<string, string> = {
  Nigeria: "#eb6834",
  China: "#e34948",
  "Euro area": "#1baf7a",
  Europe: "#1baf7a",
  "United States": "#2a78d6",
  US: "#2a78d6",
  Japan: "#8b909b",
};

export const C = {
  us: "#2a78d6",
  ng: "#eb6834",
  eu: "#1baf7a",
  cn: "#e34948",
  jp: "#8b909b",
  gdp: "#2a78d6",
  unemp: "#e34948",
  infl: "#eda100",
  gold: "#b8892b",
  grow: "#c2571f",
  shrink: "#3f5d80",
};

export const fmtPct = (v: number | null | undefined, d = 0) =>
  v === null || v === undefined ? "—" : `${v.toFixed(d)}%`;

export const fmt = (v: number | null | undefined, d = 0) =>
  v === null || v === undefined ? "—" : v.toFixed(d);
