from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command


async def cmd_start(message: types.Message):
    await message.answer('Приф!!!! Твой id:' + str(message.from_user.id))
