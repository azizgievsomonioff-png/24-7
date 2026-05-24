from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def marketplace_keyboard() -> InlineKeyboardMarkup:
    values = ["Ozon", "Wildberries", "Яндекс.Маркет", "Avito", "Универсальная карточка"]
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=value, callback_data=f"marketplace:{value}")] for value in values]
    )
