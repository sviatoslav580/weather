from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
import asyncio
import logging
from api.api_function import get_wether
from keyboard.keyboard import get_yes_no_kb
router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        text="Здравствуй! Это бот который показывает погоду🌍🌡. На втором ряду снизу расположены Москва и Санкт-Петербург и другие города",
        reply_markup=get_yes_no_kb()
     )
# # @router.message(F.location)
# # async def handle_location(message: Message):
# #     loc = message.location
# #     lat = loc.latitude
# #     long = loc.longitude
# #     await message
#
# @router.message(F.location)
# async def handle_location(message: Message):
#     lat = message.location.latitude
#     lon = message.location.longitude
#     print(lat, lon)
#     await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
#     try:
#
#         weather = get_wether(lat, lon)
#         answer = (
#             f"🌍 Погода в городе {weather['city']}:\n"
#             f"🌡 Температура: {weather['temperature']}°C (ощущается как {weather['feels_like']}°C)\n"
#             f"☁️ {weather['description'].capitalize()}\n"
#             f"💧 Влажность: {weather['humidity']}%\n"
#             f"💨 Ветер: {weather['wind_speed']} м/с"
#         )
#
#         await message.answer(answer)
#     except Exception as e:
#         logging.error(f"Ошибка получения погоды: {e}")
#         await message.answer("Не удалось получить погоду. Попробуйте позже или проверьте API‑ключ.")

CITIES = {
    "Москва": (55.7558, 37.6173),
    "Санкт-Петербург": (59.9343, 30.3351),
    "Новосибирск": (55.0084, 82.9357),
    "Екатеринбург": (56.8389, 60.6057),
    "Казань": (55.7887, 49.1221),
    "Нижний Новгород": (56.2965, 43.9361),
    "Челябинск": (55.1644, 61.4368),
    "Омск": (54.9885, 73.3242),
    "Самара": (53.1959, 50.1002)
}

@router.message(F.location)
async def handle_location(message: Message):
    lat = message.location.latitude
    lon = message.location.longitude
    print(lat, lon)
    await send_weather(message, lat, lon, city_name=None)

@router.message(F.text.in_(CITIES.keys()))
async def handle_city(message: Message):
    city = message.text
    lat, lon = CITIES[city]
    await send_weather(message, lat, lon, city_name=city)

async def send_weather(message: Message, lat: float, lon: float, city_name: str = None):
    """Общая функция отправки погоды с индикатором 'печатает'"""
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    try:
        weather = get_wether(lat, lon)
        display_city = city_name if city_name else weather['city']
        text = (
            f"🌍 Погода в городе {display_city}:\n"
            f"🌡 Температура: {weather['temperature']}°C (ощущается {weather['feels_like']}°C)\n"
            f"☁️ {weather['description'].capitalize()}\n"
            f"💧 Влажность: {weather['humidity']}%\n"
            f"💨 Ветер: {weather['wind_speed']} м/с"
        )
        await message.answer(text)
    except Exception as e:
        await message.answer("Не удалось получить погоду. Попробуйте позже.")
        raise e