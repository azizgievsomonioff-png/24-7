from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def confirm_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✅ Сгенерировать карточку", callback_data="generate_card")],
            [InlineKeyboardButton(text="🤖 Сгенерировать промты через ChatGPT", callback_data="chatgpt_prompts_from_state")],
            [InlineKeyboardButton(text="✏️ Изменить данные", callback_data="restart_card")],
            [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel_flow")],
        ]
    )


def result_actions_keyboard(project_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🤖 Сгенерировать промты через ChatGPT", callback_data=f"chatgpt_prompts:{project_id}")],
            [InlineKeyboardButton(text="🎨 Сгенерировать картинки", callback_data=f"generate_images:{project_id}")],
            [InlineKeyboardButton(text="📦 Скачать картинки ZIP", callback_data=f"zip_images:{project_id}")],
            [InlineKeyboardButton(text="📄 Скачать TXT", callback_data=f"export:{project_id}")],
            [InlineKeyboardButton(text="🔁 Переделать", callback_data="restart_card")],
            [InlineKeyboardButton(text="🆕 Новая карточка", callback_data="new_card")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
        ]
    )


def project_actions_keyboard(project_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="👁 Открыть текстовый результат", callback_data=f"open_project:{project_id}")],
            [InlineKeyboardButton(text="🤖 Сгенерировать промты через ChatGPT", callback_data=f"chatgpt_prompts:{project_id}")],
            [InlineKeyboardButton(text="🎨 Сгенерировать картинки", callback_data=f"generate_images:{project_id}")],
            [InlineKeyboardButton(text="🖼 Показать картинки", callback_data=f"show_images:{project_id}")],
            [InlineKeyboardButton(text="📦 Скачать картинки ZIP", callback_data=f"zip_images:{project_id}")],
            [InlineKeyboardButton(text="📄 Скачать TXT", callback_data=f"export:{project_id}")],
            [InlineKeyboardButton(text="🗑 Удалить проект", callback_data=f"delete_project:{project_id}")],
            [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
        ]
    )


def delete_confirm_keyboard(project_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Да, удалить", callback_data=f"delete_confirm:{project_id}")],
            [InlineKeyboardButton(text="Нет, назад", callback_data=f"project:{project_id}")],
        ]
    )
