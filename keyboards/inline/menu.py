from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 Перевести число", callback_data="convert")],
            [InlineKeyboardButton(text="➕ Сложить", callback_data="add")],
            [InlineKeyboardButton(text="➖ Вычесть", callback_data="subtract")],
            [InlineKeyboardButton(text="✖️ Умножить", callback_data="multiply")],
            [InlineKeyboardButton(text="➗ Разделить", callback_data="divide")],
        ],
    )
    return keyboard
