import asyncio

from aiogram import Bot, Dispatcher

from app.core.config import get_settings
from app.handlers.callbacks import router as callbacks_router
from app.handlers.start import router as start_router


async def main() -> None:
    settings = get_settings()
    if not settings.bot_token:
        raise ValueError("BOT_TOKEN is required")

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(callbacks_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
