import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from core.handlers.basic import cmd_start, start_bot, stop_bot
from core.settings import settings
logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bots.bot_token,
          parse_mode='HTML')

dp = Dispatcher()
# Включение и выключение бота


@dp.message.register(cmd_start)
@dp.startup.register(start_bot)
@dp.shutdown(stop_bot)
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
