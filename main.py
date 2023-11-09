import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from core.handlers.basic import basic_class
from core.handlers.stars_adder import star_class
from core.handlers.stars_sender import star_accept
from core.settings import settings
from core.utils.statesform import StepsForm
logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.bots.bot_token,
          parse_mode='HTML')

dp = Dispatcher()

# Включение и выключение бота


async def main():
    bot = Bot(token=settings.bots.bot_token,
              parse_mode='HTML')

    dp = Dispatcher()

    dp.startup.register(basic_class.start_bot)
    dp.shutdown.register(basic_class.stop_bot)
    dp.message.register(basic_class.cmd_start, Command("start"))
    dp.message.register(star_class.cmd_star, Command("add"))
    dp.message.register(star_class.get_func, StepsForm.GET_FUNCTION)
    dp.message.register(star_class.add_star, StepsForm.ADD_STAR)
    dp.message.register(star_accept)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
if __name__ == "__main__":
    asyncio.run(main())
