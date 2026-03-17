from fastapi import APIRouter

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("")
async def list_orders() -> dict[str, str]:
    return {"message": "orders module placeholder"}
