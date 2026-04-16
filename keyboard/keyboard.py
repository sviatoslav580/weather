from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Данное местоположение", request_location=True)
    kb.button(text="Москва")
    kb.button(text="Санкт-Петербург")
    kb.button(text="Челябинск")
    kb.button(text="Новосибирск")
    kb.button(text="Екатеринбург")
    kb.button(text="Омск")
    kb.button(text="Самара")
    kb.button(text="Нижний Новгород")
    kb.button(text="Казань")
    kb.adjust(1, 2, 2, 2, 2, 1)
    return kb.as_markup(resize_keyboard=True)
