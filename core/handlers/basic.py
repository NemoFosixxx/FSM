from aiogram import Bot, types, Dispatcher
from core.settings import settings
from core.keyboards.reply import star_keyboard


class basic_class():

    async def start_bot(bot: Bot):
        await bot.send_message(settings.bots.admin_id, f'✅<b>Бот был включён!</b>✅')

    async def stop_bot(bot: Bot):
        await bot.send_message(settings.bots.admin_id, f'❌<b>Бот был остановлен!</b>❌')

    async def cmd_start(message: types.Message):
        await message.answer("❤️Создан специально для лисёночка, чтобы присылать ему звёздочки❤️",
                             reply_markup=star_keyboard)
        await message.answer_sticker("CAACAgIAAxkBAAEB7ZxlUJqPFn09AAGkvTAPKgicGrprA60AAuEiAAJaxrBKjeyQoKBHevkzBA")
