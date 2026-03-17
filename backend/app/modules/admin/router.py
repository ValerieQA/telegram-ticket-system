from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("")
async def list_admin() -> dict[str, str]:
    return {"message": "admin module placeholder"}
