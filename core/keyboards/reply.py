from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

star_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='⭐️ Получить звёздочку ⭐️'
        )
    ]
], resize_keyboard=True)
