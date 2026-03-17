from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


def main_menu_keyboard(miniapp_url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎟 Open Mini App", web_app=WebAppInfo(url=miniapp_url))],
            [
                InlineKeyboardButton(text="🛒 Purchase flow", callback_data="purchase_flow"),
                InlineKeyboardButton(text="🛠 Admin", callback_data="admin_flow"),
            ],
        ]
    )
