from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

# keyboards
from Number_systems_calculator_bot.services.math_functions import to_decimal_convert, from_decimal_convert
from Number_systems_calculator_bot.keyboards.inline.decimal import decimal_inline

# functions
from Number_systems_calculator_bot.states.calculator import Calculator

inline_router = Router()

@inline_router.callback_query(F.data == "convert")
async def show_convert_menu(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Выберите направление перевода:",
        reply_markup=decimal_inline(),
    )
    await callback.answer()

# keyboards handlers
@inline_router.callback_query(F.data == "to_decimal")
async def to_decimal(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Calculator.waiting_for_to_decimal_conversion)
    await callback.message.edit_text(
        "Введите число и его систему счисления.\n"
        "Например:\n1010 2"
    )
    await callback.answer()

@inline_router.callback_query(F.data == "from_decimal")
async def from_decimal(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Calculator.waiting_for_from_decimal_conversion)
    await callback.message.edit_text(
        "Введите десятичное число и систему счисления,\n"
        "в которую нужно перевести.\n\n"
        "Например:\n"
        "10 2"
    )
    await callback.answer()

@inline_router.message(Calculator.waiting_for_to_decimal_conversion)
async def process_to_decimal(message: Message, state: FSMContext):
    try:
        num, from_base = message.text.split()

        result = to_decimal_convert(
            num,
            int(from_base),
        )

        await message.answer(
            f"Результат: {result}"
        )

        await state.clear()

    except ValueError:
        await message.answer(
            "Ошибка! Введите данные в формате:\n"
            "1010 2"
        )


@inline_router.message(Calculator.waiting_for_from_decimal_conversion)
async def process_from_decimal(message: Message, state: FSMContext):
    try:
        num, to_base = message.text.split()

        result = from_decimal_convert(
            num,
            int(to_base),
        )

        await message.answer(
            f"Результат: {result}"
        )

        await state.clear()

    except ValueError:
        await message.answer(
            "Ошибка! Введите данные в формате:\n"
            "1010 2"
        )


@inline_router.callback_query(F.data == "add")
async def add_handler(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для сложения:"
    )
    await callback.answer()
@inline_router.callback_query(F.data == "subtract")
async def subtract_handler(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для вычитания:"
    )
    await callback.answer()
@inline_router.callback_query(F.data == "multiply")
async def multiply_handler(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для умножения:"
    )
    await callback.answer()
@inline_router.callback_query(F.data == "divide")
async def divide_handler(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для деления:"
    )
    await callback.answer()