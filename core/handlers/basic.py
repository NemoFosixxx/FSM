from aiogram import Bot, types, Dispatcher
from core.settings import settings


class basic_class():

    async def start_bot(bot: Bot):
        await bot.send_message(settings.bots.admin_id, f'<b>Бот был включён!</b>')

    async def stop_bot(bot: Bot):
        await bot.send_message(settings.bots.admin_id, f'<b>Бот был остановлен!</b>')

    async def cmd_start(message: types.Message):
        await message.answer("Отправляю звёздочки лисёнку. Умею работать асинхронно. Ver 2.0")
