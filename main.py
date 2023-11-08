import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from core.handlers.basic import cmd_start
from core.settings import settings
logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bots.bot_token,
          parse_mode='HTML')

dp = Dispatcher()

# Включение и выключение бота


@dp.message.register(cmd_start)
# f
@dp.startup()
async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, f'<b>Бот был включён!</b>')


@dp.shutdown()
async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, f'<b>Бот был остановлен!</b>')

# Логика


async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
