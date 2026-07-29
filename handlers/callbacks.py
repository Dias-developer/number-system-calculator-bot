from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from Number_systems_calculator_bot.services.math_functions import to_decimal_convert
from Number_systems_calculator_bot.states.calculator import Calculator

inline_router = Router()

@inline_router.callback_query(lambda call: call.data == "convert")
async def func1(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Calculator.waiting_for_to_decimal_conversion)
    await callback.message.answer(
        "Введите число, исходную и целевую систему счисления.\n"
        "Например: 1010 2 10"
    )
    await callback.answer()

@inline_router.message(Calculator.waiting_for_to_decimal_conversion)
async def process_conversion(message: Message, state: FSMContext):
    try:
        num, from_base, to_base = message.text.split()

        result = to_decimal_convert(
            num,
            int(from_base),
            int(to_base)
        )

        await message.answer(
            f"Результат: {result}"
        )

        await state.clear()

    except ValueError:
        await message.answer(
            "Ошибка! Введите данные в формате:\n"
            "1010 2 10"
        )

@inline_router.callback_query(lambda call: call.data == "add")
async def func2(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для сложения:"
    )
    await callback.answer()
@inline_router.callback_query(lambda call: call.data == "subtract")
async def func3(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для вычитания:"
    )
    await callback.answer()
@inline_router.callback_query(lambda call: call.data == "multiply")
async def func4(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для умножения:"
    )
    await callback.answer()
@inline_router.callback_query(lambda call: call.data == "divide")
async def func5(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для деления:"
    )
    await callback.answer()