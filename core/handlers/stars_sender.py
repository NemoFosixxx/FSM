from aiogram import Bot, types, Dispatcher
from core.settings import settings
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, InputMediaPhoto

star_list = []


async def star_accept(message: types.Message, bot: Bot):

    if message.text.lower() == '⭐️ получить звёздочку ⭐️':
        with open('stars.txt', 'r', encoding='utf8') as file:
            star_list = file.readlines()

        if len(star_list) != 0:
            # response_message = star_list[0]

            # ОТПРАВЛЯЕМ ЗВЁЗДОЧКУ
            await message.answer(str(star_list[0]))
            await bot.send_message(settings.bots.admin_id, "⚡️Лисёнку была отправлена следующая звёздочка: \n" + str(star_list[0]))

        # прочитаем файл построчно
            with open('stars.txt', 'r', encoding='utf8') as file:
                lines = file.readlines()

            index = 0
            lines.pop(index)

            with open("stars.txt", "w", encoding='utf-8') as f:
                f.writelines(lines)
        else:
            responce_message = '😢Звёздочки закончились, но не волнуйся, Лисёнок, котёнок их скоро добавит'
            await message.answer(responce_message)
            await message.answer_sticker("CAACAgIAAxkBAAEB4WxlTL5tW5YoRhwHR4djp3820PjVvAACHxcAAiOjqUraw0RfUkBNhzME")
            await bot.send_message(settings.bots.admin_id, "⚡️Лисёнку была отправлена следующая звёздочка:", responce_message)


async def image_sender(message: types.Message, bot: Bot):
    photo = InputMediaPhoto(
        type='photo', media=FSInputFile(f'core\images\image.png'))
    await bot.send_photo(1048810471, photo)  # 5286076490
