from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Звёздочку', callback_data='add_star')
    keyboard_builder.button(text='Картинку', callback_data='add_image')

    return keyboard_builder.as_markup()
