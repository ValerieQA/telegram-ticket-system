from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "purchase_flow")
async def purchase_flow(callback: CallbackQuery) -> None:
    await callback.message.answer("Purchase flow placeholder: event list -> seats -> checkout.")
    await callback.answer()


@router.callback_query(F.data == "admin_flow")
async def admin_flow(callback: CallbackQuery) -> None:
    await callback.message.answer("Admin flow placeholder: manage venues, events, and inventory.")
    await callback.answer()
