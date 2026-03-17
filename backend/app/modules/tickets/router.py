from fastapi import APIRouter

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.get("")
async def list_tickets() -> dict[str, str]:
    return {"message": "tickets module placeholder"}
