# AGENTS.md

## Project

Salsas Superior is a small salsa webshop and learning project.

## Stack

- Frontend: React, TypeScript, Vite, Tailwind CSS
- Backend: FastAPI, managed with uv
- Database: PostgreSQL planned, not implemented yet

## Structure

```text
backend/   FastAPI API, in-memory product data, static media
frontend/  React Vite app and UI assets
```

## Local Commands

Frontend:

```bash
cd frontend
npm install
npm run dev
npm run build
npm run lint
```

Backend:

```bash
cd backend
uv sync
uv run fastapi dev main.py
```

For editor completions during development, use the Python interpreter from `backend/.venv` or open the editor after activating that environment.

## Notes For Agents

- Keep changes small and beginner-friendly.
- Use `uv` for backend dependency and command management.
- Do not introduce a database layer until PostgreSQL work is explicitly requested.
- The frontend currently expects the backend at `http://127.0.0.1:8000`.
- Product data currently lives in `backend/main.py`.
- Static product images are served by FastAPI from `backend/media/`.
