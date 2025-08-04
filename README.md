# Fitness Tracker

> **Why?** I hit the gym four times a week and was tired of juggling a worn‑out notebook and messy spreadsheets.  This app is my attempt to keep workouts, progress charts and goals in one tidy place — and to have some fun with a modern Python + React stack on the way.

---

## What you’ll find here

* **Flask 3** backend (Python 3.12) with JWT auth and SQLAlchemy
* **React 19 + TypeScript 5** frontend powered by Vite & MUI dark theme
* Docker‑first workflow (`docker compose up` and you’re rolling)
* GitHub Actions CI (lint, tests, container build)

---

## Quick start with Docker

```bash
# clone repo
 git clone https://github.com/<ORG>/<REPO>.git
 cd fitness-tracker

# add your secrets
 cp .env.example .env

# build & run everything
 docker compose up --build
```

* API → [http://localhost:5000](http://localhost:5000)
* UI  → [http://localhost:8080](http://localhost:8080)

---

## Local hacking (no Docker)

**Backend**

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
flask --app backend.app run
```

**Frontend**

```bash
cd frontend
pnpm install   # or npm install
dev
```

---

## Tests & linting

```bash
pytest -q                # ≥ 85 % coverage
ruff .                   # Python lint / format
npm run lint --workspace frontend   # ESLint
```

GitHub Actions runs the same checks on every push.

---

## Deployment (Render)

Create a **Docker Web Service**, point it at your repo, add env vars (`SECRET_KEY`, `DATABASE_URL`), and use:

```
docker compose up --build
```

Render pulls the pre‑built image from the GitHub Container Registry, so deploys stay snappy.

---

## License

This project is licensed under the [MIT License](LICENSE).

