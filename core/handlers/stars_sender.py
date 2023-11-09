from aiogram import Bot, types, Dispatcher
from core.settings import settings
from aiogram.fsm.context import FSMContext

star_list = []


async def star_accept(message: types.Message, bot: Bot):

    if message.text.lower() == 'получить звёздочку':
        with open('stars.txt', 'r', encoding='utf8') as file:
            star_list = file.readlines()

        if len(star_list) != 0:
            # response_message = star_list[0]

            # ОТПРАВЛЯЕМ ЗВЁЗДОЧКУ
            responce_message = star_list[0]
            await message.answer(str(star_list[0]))
            await bot.send_message(settings.bots.admin_id, "Лисёнку была отправлена следующая звёздочка: " + str(star_list[0]))

        # прочитаем файл построчно
            with open('stars.txt', 'r', encoding='utf8') as file:
                lines = file.readlines()

            index = 0
            lines.pop(index)

            with open("stars.txt", "w", encoding='utf-8') as f:
                f.writelines(lines)
        else:
            await message.answer_sticker("CAACAgIAAxkBAAEB4WxlTL5tW5YoRhwHR4djp3820PjVvAACHxcAAiOjqUraw0RfUkBNhzME")
            await message.answer("Звёздочки закончились, но не волнуйся, Лисёнок, котёнок их скоро добавит")
