from aiogram import Bot, types, Dispatcher
from core.settings import settings
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm


class star_class():

    async def cmd_star(message: types.Message, state: FSMContext):
        if message.from_user.id == settings.bots.admin_id:
            await message.answer("Приветствую, О ВЕЛИКИЙ МОДЕРАТОР, Что хотите добавить?")
            await state.set_state(StepsForm.GET_FUNCTION)

    async def get_func(message: types.Message, state: FSMContext):
        if message.text.lower() == "добавить звёздочку":
            await state.set_state(StepsForm.ADD_IMAGE)
            await message.answer("ты выбрал звёздочки")

        elif message.text.lower() == "добавить картинку":
            await state.set_state(StepsForm.ADD_STAR)
            await message.answer('Ты выбрал картинки')
