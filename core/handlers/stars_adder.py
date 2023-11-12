from aiogram import Bot, types, Dispatcher
from core.settings import settings
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm
from core.keyboards.inline import get_inline_keyboard

from aiogram.utils.keyboard import InlineKeyboardBuilder


class star_class():
    star_list = []

    async def cmd_star(message: types.Message, bot: Bot):
        if message.from_user.id == settings.bots.admin_id:
            await message.answer("Приветствую, О ВЕЛИКИЙ МОДЕРАТОР, Что хотите добавить?",
                                 reply_markup=get_inline_keyboard())

    async def get_func(callback_query: types.CallbackQuery, state: FSMContext):
        if callback_query.data == 'add_star':
            await callback_query.answer('Что добавить в звёздочку?')
            await state.set_state(StepsForm.ADD_STAR)
        elif callback_query.data == 'add_image':
            await callback_query.answer('Какую картинку добавить?')
            await state.set_state(StepsForm.ADD_IMAGE)

    async def add_image(message: types.Message, state: FSMContext):
        await message.answer("здесь должен быть функционал")
        await state.clear()

    async def add_star(message: types.Message, state: FSMContext):
        new_star = message.text

        # Сначала считываем существующие звёздочки из файла и разделяем их
        with open("stars.txt", 'r', encoding='utf8') as file:
            existing_stars = file.read().splitlines()

        # Добавляем новую звёздочку в список существующих
        existing_stars.append(new_star)

        # Теперь записываем все строки обратно в файл с разделителем
        with open("stars.txt", 'w', encoding='utf8') as file:
            file.write('\n'.join(existing_stars))

        await state.clear()

        await message.answer("Звёздочка успешно добавлена!")
