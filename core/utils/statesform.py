from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_FUNCTION = State()
    ADD_STAR = State()
    ADD_IMAGE = State()
