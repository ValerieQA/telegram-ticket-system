from fastapi import APIRouter

from app.api.health import router as health_router
from app.modules.admin.router import router as admin_router
from app.modules.events.router import router as events_router
from app.modules.orders.router import router as orders_router
from app.modules.payments.router import router as payments_router
from app.modules.seats.router import router as seats_router
from app.modules.tickets.router import router as tickets_router
from app.modules.users.router import router as users_router
from app.modules.venues.router import router as venues_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(users_router)
api_router.include_router(venues_router)
api_router.include_router(events_router)
api_router.include_router(seats_router)
api_router.include_router(orders_router)
api_router.include_router(tickets_router)
api_router.include_router(payments_router)
api_router.include_router(admin_router)
