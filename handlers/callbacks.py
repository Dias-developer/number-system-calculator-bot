from aiogram import Router
from aiogram.types import CallbackQuery

inline_router = Router()

@inline_router.callback_query(lambda call: call.data == "convert")
async def func1(callback: CallbackQuery):
    await callback.message.answer(
        "Введите число и его систему счисления:"
    )
    await callback.answer()

@inline_router.callback_query(lambda call: call.data == "add")
async def func2(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для сложения:"
    )
    await callback.answer()
@inline_router.callback_query(lambda call: call.data == "subtract")
async def func2(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для вычитания:"
    )
    await callback.answer()
@inline_router.callback_query(lambda call: call.data == "multiply")
async def func2(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для умножения:"
    )
    await callback.answer()
@inline_router.callback_query(lambda call: call.data == "divide")
async def func2(callback: CallbackQuery):
    await callback.message.answer(
        "Введите два числа для деления:"
    )
    await callback.answer()