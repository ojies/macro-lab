"use client";
import React, { useState } from "react";
import { TooltipProvider } from "@/components/charts";
import { Overview, DevelopmentAge, TwoPoles, FivePoles, IndexView, Demographics } from "@/components/views";

const TABS: { id: string; label: string; Comp: React.ComponentType }[] = [
  { id: "overview", label: "World Order", Comp: Overview },
  { id: "dev", label: "Development Age", Comp: DevelopmentAge },
  { id: "us", label: "Two Poles", Comp: TwoPoles },
  { id: "five", label: "Five Poles", Comp: FivePoles },
  { id: "index", label: "Index", Comp: IndexView },
  { id: "demo", label: "Demographics", Comp: Demographics },
];

export default function Page() {
  const [active, setActive] = useState("overview");
  const Active = TABS.find((t) => t.id === active)!.Comp;
  return (
    <TooltipProvider>
      <header style={{ position: "sticky", top: 0, zIndex: 20, background: "color-mix(in srgb, var(--bg) 88%, transparent)", backdropFilter: "blur(10px)", borderBottom: "1px solid var(--hair)" }}>
        <div style={{ maxWidth: 1040, margin: "0 auto", padding: "14px clamp(16px,4vw,40px) 0" }}>
          <div style={{ display: "flex", alignItems: "baseline", justifyContent: "space-between", flexWrap: "wrap", gap: 8 }}>
            <div style={{ display: "flex", alignItems: "baseline", gap: 12 }}>
              <span style={{ fontFamily: "var(--serif)", fontSize: 22, fontWeight: 700, letterSpacing: "-.01em" }}>macro-lab</span>
              <span style={{ fontFamily: "var(--mono)", fontSize: 11, letterSpacing: ".14em", textTransform: "uppercase", color: "var(--muted)" }}>five poles of the debt cycle</span>
            </div>
            <span style={{ fontFamily: "var(--mono)", fontSize: 11, color: "var(--muted)" }}>live · from the models</span>
          </div>
          <nav style={{ display: "flex", gap: 4, marginTop: 12, overflowX: "auto", paddingBottom: 2 }}>
            {TABS.map((t) => {
              const on = t.id === active;
              return (
                <button key={t.id} onClick={() => setActive(t.id)}
                  style={{
                    appearance: "none", border: "none", background: "transparent", cursor: "pointer",
                    padding: "9px 14px", fontSize: 14, fontWeight: on ? 700 : 500, whiteSpace: "nowrap",
                    color: on ? "var(--ink)" : "var(--muted)", borderBottom: `2px solid ${on ? "var(--accent)" : "transparent"}`,
                    transition: "color .2s, border-color .2s", fontFamily: "var(--sans)",
                  }}>
                  {t.label}
                </button>
              );
            })}
          </nav>
        </div>
      </header>

      <main style={{ maxWidth: 1040, margin: "0 auto", padding: "clamp(24px,4vw,48px) clamp(16px,4vw,40px) 80px" }}>
        <div key={active}>
          <Active />
        </div>
      </main>

      <footer style={{ maxWidth: 1040, margin: "0 auto", padding: "24px clamp(16px,4vw,40px) 48px", borderTop: "1px solid var(--hair)", color: "var(--muted)", fontSize: 12.5 }}>
        <strong>macro-lab</strong> · a Next.js + FastAPI dashboard over the quantitative models · data: IMF, World Bank/UN, FRED, IMF COFER, Eurostat, BIS, DMO/CBN/NBS. A scenario/analysis lens — not investment advice.
      </footer>
    </TooltipProvider>
  );
}
