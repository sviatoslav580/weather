from handlers import handler

import requests
key = 'ВАШ КЛЮЧ open weather'

# def get_wether(lat, lon):
#     url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
#     response = requests.get(url)
#     response.raise_for_status()
#     data = response.json()
#
#     weather_info = {
#         "temperature": round(data['main']['temp'], 1),
#         "feels_like": round(data['main']['feels_like'], 1),
#         "description": data["weather"][0]["description"],
#         "humidity": data["main"]["humidity"],
#         "wind_speed": data["wind"]["speed"],
#         "city": data.get("name", "неизвестный город")
#     }
#     return weather_info


def get_wether(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric&lang=ru'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    weather_info = {
        'temperature': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'city': data.get('name', 'неизвестный город')
    }
    return weather_info





