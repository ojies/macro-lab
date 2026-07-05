# macro-lab dashboard — dev shortcuts.  `make help` lists targets.
.DEFAULT_GOAL := help
.PHONY: help install dev backend frontend up down build clean

help: ## show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN{FS=":.*?## "}{printf "  \033[1m%-10s\033[0m %s\n", $$1, $$2}'

install: ## install backend (uv) + frontend (npm) deps
	cd backend && uv sync
	cd frontend && npm install

dev: ## run BOTH dev servers together (Ctrl-C stops both)
	./dev.sh

backend: ## backend only → http://localhost:8000
	cd backend && uv run uvicorn main:app --reload --port 8000

frontend: ## frontend only → http://localhost:3000
	cd frontend && npm run dev

up: ## containerized: docker compose up (both services)
	docker compose up --build

down: ## stop the containers
	docker compose down

build: ## production build of the frontend
	cd frontend && npm run build

clean: ## remove build artifacts
	rm -rf frontend/.next backend/.venv
