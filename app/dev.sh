#!/usr/bin/env bash
# Run the macro-lab dashboard locally — backend + frontend together. Ctrl-C stops both.
set -euo pipefail
cd "$(dirname "$0")"

echo "▸ backend  → http://localhost:8000  (docs: /docs)"
echo "▸ frontend → http://localhost:3000"
echo

trap 'kill 0' EXIT INT TERM

( cd backend  && exec uv run uvicorn main:app --reload --port 8000 ) &
( cd frontend && exec npm run dev ) &
wait
