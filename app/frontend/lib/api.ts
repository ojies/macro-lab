// Typed-ish fetch helpers against the FastAPI backend (proxied via /api/*).

export async function getJSON<T = any>(path: string): Promise<T> {
  const res = await fetch(path, { cache: "no-store" });
  if (!res.ok) throw new Error(`${path} → ${res.status}`);
  return res.json();
}

export type Pole = {
  name: string;
  color: string;
  debt_gdp: number | null;
  growth: number | null;
  inflation: number | null;
  year: number | null;
  space: number;
  cycle: string;
  lever: string;
  risk: string;
  trap: string;
  own: string;
};

export type IndexPole = {
  name: string;
  buffer: number;
  sustain: number;
  vitality: number;
  resilience: number;
  fragility: number;
  why: string;
  debt_gdp: number;
};
