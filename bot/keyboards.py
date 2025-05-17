from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config.settings import LANGUAGES


def get_language_keyboard():
    # Создаём список кнопок
    buttons = [
        InlineKeyboardButton(text=name, callback_data=code)
        for code, name in LANGUAGES.items()
    ]

    # Формируем строки по 2 кнопки в каждой
    keyboard_rows = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]

    # Передаём готовую разметку
    return InlineKeyboardMarkup(inline_keyboard=keyboard_rows)
