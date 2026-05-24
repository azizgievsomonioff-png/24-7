from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def audience_keyboard() -> InlineKeyboardMarkup:
    rows = [
        ["Для мужчин", "Для женщин"],
        ["Для детей", "Универсальный"],
        ["Для авто", "Для дома"],
        ["Другое", "Пропустить"],
    ]
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=item, callback_data=f"audience:{item}") for item in row]
            for row in rows
        ]
    )
