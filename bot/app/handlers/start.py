from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.core.config import get_settings
from app.keyboards.main import main_menu_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    settings = get_settings()
    await message.answer(
        "Welcome to the Telegram Event Ticketing System!\n"
        "Tap the button below to open the Mini App landing page.",
        reply_markup=main_menu_keyboard(settings.miniapp_url),
    )
