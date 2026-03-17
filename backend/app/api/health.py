from fastapi import APIRouter

from app.db.redis import redis_client

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
async def health_check() -> dict[str, str]:
    await redis_client.ping()
    return {"status": "ok"}
