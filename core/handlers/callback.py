from aiogram import Bot
from aiogram.types import CallbackQuery


async def select_add(call: CallbackQuery, bot: Bot):
    star = call.data[1]
    image = call.data[2]
