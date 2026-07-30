from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def decimal_inline():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='В десятичную', callback_data='to_decimal')],
            [InlineKeyboardButton(text='Из десятичной', callback_data='from_decimal')],
        ]
    )
    return keyboard
