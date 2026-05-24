from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🆕 Создать карточку")],
            [KeyboardButton(text="📦 Мои проекты"), KeyboardButton(text="✍️ SEO для карточки")],
            [KeyboardButton(text="🖼 Промты для инфографики"), KeyboardButton(text="❓ Помощь")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие",
    )
