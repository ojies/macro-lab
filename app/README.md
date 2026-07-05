# macro-lab — dashboard (full-stack)

A **FastAPI backend** that serves the quantitative models as JSON, and a **Next.js frontend** that
renders them as an animated, navigable dashboard. Both live in this `app/` folder.

```
app/
├── backend/   FastAPI — reads the debt_cycle model CSVs, serves /api/* JSON
└── frontend/  Next.js (App Router) — six animated views over the API
```

## Run it

**Option A — one command, containerized** (needs Docker/Podman):
```bash
cd app
docker compose up --build          # → frontend http://localhost:3000 · API http://localhost:8000
```
Compose mounts the model outputs read-only, so the API serves live CSVs.

**Option B — one command, local** (needs `uv` + Node ≥ 18):
```bash
cd app
make install                       # backend (uv) + frontend (npm) deps, once
make dev                           # runs BOTH dev servers together; Ctrl-C stops both
```
`make help` lists all targets (`backend`, `frontend`, `up`, `build`, `clean`). `make dev` just calls
`./dev.sh`.

**Option C — two terminals** (most explicit):
```bash
# terminal 1 — backend (reuses model data in ../informal_economy_ai_bitcoin/debt_cycle/)
cd app/backend && uv sync && uv run uvicorn main:app --reload --port 8000   # :8000/docs

# terminal 2 — frontend
cd app/frontend && npm install && npm run dev                              # :3000
```

The frontend proxies `/api/*` → the backend (set `API_URL` to point elsewhere), so the browser
fetches same-origin — no CORS setup needed.

## The views
| View | Source endpoint | Shows |
|---|---|---|
| **World Order** | `/api/reserves` + `/api/poles` | the demographic pivot, reserve fragmentation, the alignment vectors |
| **Development Age** | `/api/development-age` | the catch-up divergence, the 22-year spread, the Monte-Carlo 2030 fan, the conditioning scorecard |
| **Two Poles** | `/api/us` | US late-cycle gauges, the Fed rate-hike transmission, the US↔Nigeria table |
| **Five Poles** | `/api/poles` | debt-vs-policy-space map, debt bars, the five-regime matrix |
| **Index** | `/api/index` | the computed resilience/fragility score + pillar decomposition |
| **Demographics** | `/api/demographics` | births-vs-deaths (who's shrinking), fertility, the 2100 trajectory |

Every quantitative cell is pulled **live from the model outputs** — run a model in `debt_cycle/`,
its CSV changes, and the dashboard reflects it on next load.

## Backend endpoints
`/api/health` · `/api/index` · `/api/poles` · `/api/development-age` · `/api/us` · `/api/reserves` ·
`/api/demographics` · interactive docs at `/docs`.

## Notes
- Charts are hand-built animated SVG (line-draw, bar-grow, bubble pop-in) — no chart-lib dependency.
- Respects `prefers-reduced-motion` and `prefers-color-scheme` (dark mode).
- Data provenance and model definitions: see [`../MODELS.md`](../MODELS.md).
