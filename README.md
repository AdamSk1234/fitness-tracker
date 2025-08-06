# Fitness Tracker

[![CI](https://github.com/AdamSk1234/fitness-tracker/actions/workflows/ci.yml/badge.svg)](https://github.com/AdamSk1234/fitness-tracker/actions/workflows/ci.yml)

> **Why?** I hit the gym four times a week and was tired of juggling a worn‑out notebook and messy spreadsheets. This app keeps workouts, progress charts and goals in one tidy place — and lets me have some fun with a modern Python + React stack along the way.

---

## What you’ll find here

- Flask 3 backend (Python 3.12) with JWT auth, SQLAlchemy + Alembic
- React 19 + TypeScript 5 frontend powered by Vite & MUI dark theme
- Docker‑first workflow (docker compose up) — backend, frontend, database
- GitHub Actions CI: lint, tests, container build & push

---

## Quick start with Docker

```bash
# clone repo
git clone https://github.com/<ORG>/<REPO>.git
cd fitness-tracker

# copy env variables
touch .env  # or cp .env.example .env

# build & run everything
docker compose up --build
```

- API → [http://localhost:5000](http://localhost:5000) 
- UI  → [http://localhost:8080](http://localhost:8080)

---

## Local hacking (no Docker)

### Backend

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
flask --app backend.app run
```

### Frontend

```bash
cd frontend
pnpm install
pnpm dev
```

---

## Tests & linting

```bash
pytest -q
ruff .
npm run lint --workspace frontend
```

GitHub Actions runs the same checks on every push.

---

## Deployment (Render)

1. Create a **Docker Web Service**, point it at your repo, add env vars (`SECRET_KEY`, `DATABASE_URL`, …).
2. Build & start command:

   ```
   docker compose up --build
   ```

Render pulls the pre‑built image from the GitHub Container Registry, so deploys stay snappy.

---

## License

This project is licensed under the [MIT License](LICENSE).
