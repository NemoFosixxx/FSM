from aiogram import Bot, types, Dispatcher
from core.settings import settings
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm


class star_class():
    star_list = []

    async def cmd_star(message: types.Message, state: FSMContext):
        if message.from_user.id == settings.bots.admin_id:
            await message.answer("Приветствую, О ВЕЛИКИЙ МОДЕРАТОР, Что хотите добавить?")
            await state.set_state(StepsForm.GET_FUNCTION)

    async def get_func(message: types.Message, state: FSMContext):
        if message.text.lower() == "звёздочку":
            await message.answer("Что добавить в звёздочку?")
            await state.set_state(StepsForm.ADD_STAR)

        # elif message.text.lower() == "картинку":
        #     await state.update_data(name=message.text)
        #     await message.answer('Ты выбрал картинки')
        #     await state.set_state(StepsForm.ADD_IMAGE)

    async def add_star(message: types.Message, state: FSMContext):
        await state.clear()
        new_star = message.text

        # Сначала считываем существующие звёздочки из файла и разделяем их
        with open("stars.txt", 'r', encoding='utf8') as file:
            existing_stars = file.read().splitlines()

        # Добавляем новую звёздочку в список существующих
        existing_stars.append(new_star)

        # Теперь записываем все строки обратно в файл с разделителем
        with open("stars.txt", 'w', encoding='utf8') as file:
            file.write('\n'.join(existing_stars))

        await message.answer("Звёздочка успешно добавлена!")
