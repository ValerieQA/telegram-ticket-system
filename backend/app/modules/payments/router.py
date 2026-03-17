from fastapi import APIRouter

router = APIRouter(prefix="/payments", tags=["payments"])


@router.get("")
async def list_payments() -> dict[str, str]:
    return {"message": "payments module placeholder"}
