from fastapi import APIRouter

router = APIRouter(prefix="/events", tags=["events"])


@router.get("")
async def list_events() -> dict[str, str]:
    return {"message": "events module placeholder"}
