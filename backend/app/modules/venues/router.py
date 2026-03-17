from fastapi import APIRouter

router = APIRouter(prefix="/venues", tags=["venues"])


@router.get("")
async def list_venues() -> dict[str, str]:
    return {"message": "venues module placeholder"}
