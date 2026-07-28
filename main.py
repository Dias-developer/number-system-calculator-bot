from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from os import getenv
import logging
import asyncio

from Number_systems_calculator_bot.handlers.commands import router
from Number_systems_calculator_bot.handlers.callbacks import inline_router
load_dotenv()
token = getenv("TOKEN")
bot = Bot(token=token)
dp = Dispatcher()

async def main():
    # routers
    dp.include_router(router)
    dp.include_router(inline_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("Start...")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stop...")