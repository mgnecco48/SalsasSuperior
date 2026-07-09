# Salsas Superior

Small webshop for handmade salsas, built as a side project and learning space for full-stack web development.

## Stack

- Frontend: React, TypeScript, Vite, Tailwind CSS
- Backend: FastAPI, managed with uv
- Database: PostgreSQL planned

## Current Features

- Product grid for available salsas
- Cart quantity controls and order overview
- FastAPI endpoint for salsa product data
- Static product images served from the backend

## Project Structure

```text
backend/   FastAPI app, API routes, product media
frontend/  React Vite app and UI assets
```

## Run Locally

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Backend:

```bash
cd backend
uv sync
uv run fastapi dev main.py
```

The frontend expects the backend at `http://127.0.0.1:8000`.

For development, point your editor at `backend/.venv` or open it after activating the environment so FastAPI imports and completions work correctly.

## Notes

Product data is currently stored in memory in the FastAPI app. PostgreSQL will be added later as the project grows.
