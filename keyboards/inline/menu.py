from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔄 Перевести число", callback_data="func1")],
            [InlineKeyboardButton(text="➕ Сложить", callback_data="func2")],
            [InlineKeyboardButton(text="➖ Вычесть", callback_data="func3")],
            [InlineKeyboardButton(text="✖️ Умножить", callback_data="func4")],
            [InlineKeyboardButton(text="➗ Разделить", callback_data="func5")],
        ],
    )
    return keyboard
