from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from Number_systems_calculator_bot.keyboards.inline.menu import menu
router = Router()

@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer("Привет, я калькулятор для систем счисления!")

    await message.answer("Выберите действие:", reply_markup=menu())



