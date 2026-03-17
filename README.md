# Telegram Event Ticketing Monorepo

Production-oriented skeleton for a Telegram-first event ticketing product:
- **Telegram Bot** as chat entry point
- **Telegram Mini App** as mobile promotional landing + purchase UI
- **FastAPI backend** for business logic and future integrations
- **PostgreSQL** for persistent data
- **Redis** for temporary seat locks and short-lived session/state

## Project structure

```text
.
├── backend/      # FastAPI + SQLAlchemy async + Alembic
├── bot/          # aiogram 3.x Telegram bot
├── miniapp/      # Next.js Mini App (mobile-first landing)
├── infra/        # Placeholder for production infra IaC
├── docker-compose.yml
├── .env.example
└── README.md
```

## Backend overview

`backend/app` is modular and ready for scaling with placeholder routers:
- `users`
- `venues`
- `events`
- `seats`
- `orders`
- `tickets`
- `payments`
- `admin`

Included foundations:
- `/api/v1/health` health-check endpoint (includes Redis ping)
- async PostgreSQL engine/session
- async Redis client
- environment-driven settings
- SQLAlchemy models: `User`, `Venue`, `Event`, `Seat`, `Order`, `Ticket`
- Alembic configured with initial migration

## Bot overview

- `/start` command
- welcome message
- inline keyboard with Telegram Mini App WebApp button
- placeholder callbacks for purchase and admin flows

## Mini App overview

- dark, mobile-first scrolling landing page
- hero section with poster placeholder + CTA
- “Who is this artist?” content block
- slider/carousel with left-right arrows
- embedded media placeholder cards
- “View tickets” CTA
- Telegram WebApp SDK init helper (`ready()`, `expand()`)

## Local development

### 1) Prepare env

```bash
cp .env.example .env
# Fill BOT_TOKEN
```

### 2) Start all services

```bash
docker compose up --build
```

Services:
- Backend API: `http://localhost:8000`
- Mini App: `http://localhost:3000`
- Postgres: `localhost:5432`
- Redis: `localhost:6379`

### 3) Run migrations

```bash
docker compose exec backend alembic upgrade head
```

## Environment variables

All services read from root `.env`:
- `ENVIRONMENT`, `DEBUG`
- `POSTGRES_*`
- `REDIS_*`
- `BOT_TOKEN`
- `MINIAPP_URL`

Backend and bot use settings classes to map env vars into typed configuration.

## Render deployment notes

For Render, split into separate services:
1. **backend** web service (FastAPI)
2. **miniapp** web service (Next.js)
3. **bot** worker service (long polling/webhook)
4. **postgres** managed database
5. **redis** managed Redis

Recommended production improvements:
- switch bot to webhook mode
- use CI/CD for migrations (`alembic upgrade head`)
- add observability (Sentry + metrics + structured logs)
- configure secrets in Render environment groups
- add CDN/storage for poster/media assets

## Phase 2 implementation roadmap

1. **Core business logic**
   - event catalog APIs
   - seat availability query APIs
   - Redis-based seat lock lifecycle (lock, refresh, release, expire)
2. **Checkout and payments**
   - order state machine
   - payment provider integration
   - webhook handlers and idempotency keys
3. **Ticket issuing**
   - ticket QR generation
   - anti-fraud validation endpoint
4. **Mini App UX expansion**
   - real event feed and media
   - seat map module
   - checkout flow screens
5. **Admin tools**
   - protected admin endpoints
   - venue/event CRUD dashboards
