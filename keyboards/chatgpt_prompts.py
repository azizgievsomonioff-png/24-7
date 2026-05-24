from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def slide_prompt_keyboard(project_id: int, slide_number: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔁 Переделать этот слайд", callback_data=f"chatgpt_regen_slide:{project_id}:{slide_number}")],
            [InlineKeyboardButton(text="✏️ Добавить правку", callback_data=f"chatgpt_edit_slide:{project_id}:{slide_number}")],
            [InlineKeyboardButton(text="📋 Скопировать промт", callback_data=f"chatgpt_copy_prompt:{project_id}:{slide_number}")],
            [InlineKeyboardButton(text="➡️ Следующий", callback_data=f"chatgpt_next_slide:{project_id}:{slide_number}")],
        ]
    )
