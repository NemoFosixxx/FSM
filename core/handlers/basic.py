from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command
from core.settings import settings


async def cmd_start(message: types.Message):
    await message.answer('Приф!!!! Твой id:' + str(message.from_user.id))


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, f'<b>Бот был включён!</b>')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, f'<b>Бот был остановлен!</b>')
