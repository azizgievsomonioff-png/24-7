from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def skip_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Пропустить", callback_data="skip")]])
