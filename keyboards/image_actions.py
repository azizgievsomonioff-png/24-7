from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def image_generation_confirm_keyboard(project_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✅ Да, генерировать", callback_data=f"image_confirm:{project_id}")],
            [InlineKeyboardButton(text="❌ Нет", callback_data=f"project:{project_id}")],
        ]
    )


def image_generation_done_keyboard(project_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📦 Скачать картинки ZIP", callback_data=f"zip_images:{project_id}")],
            [InlineKeyboardButton(text="🆕 Новая карточка", callback_data="new_card")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
        ]
    )
