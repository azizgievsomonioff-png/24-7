from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def categories_keyboard() -> InlineKeyboardMarkup:
    rows = [
        ["Одежда", "Обувь"],
        ["Автотовары", "Товары для дома"],
        ["Электроника", "Косметика"],
        ["Детские товары", "Продукты"],
        ["Инструменты", "Другое"],
    ]
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=item, callback_data=f"category:{item}") for item in row]
            for row in rows
        ]
    )
