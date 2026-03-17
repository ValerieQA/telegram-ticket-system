from fastapi import APIRouter

router = APIRouter(prefix="/seats", tags=["seats"])


@router.get("")
async def list_seats() -> dict[str, str]:
    return {"message": "seats module placeholder"}
