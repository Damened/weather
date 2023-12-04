import os
import requests
import datetime
from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from code_smile import code_to_smile

load_dotenv()

TOKEN_TG = os.getenv('TOKEN_TG_BOT')
TOKEN_WEATHER = os.getenv('TOKEN_WEATHER_API')
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="
BOT = Bot(token=TOKEN_TG)
dp = Dispatcher(BOT)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(
        "Привет! Напиши мне название города и я пришлю сводку погоды")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        response = requests.get(
            f"{WEATHER_BASE_URL}"
            f"{message.text}&appid={TOKEN_WEATHER}&lang=ru&units=metric")
        data = response.json()
        city = data['name']  # Название города
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            # Если эмодзи для погоды нет, выводим другое сообщение
            wd = "Посмотри в окно, я не понимаю, что там за погода..."
            
        cur_waether = data['main']['temp']  # Температура
        humidity = data['main']['humidity']  # Влажность
        pressure = data['main']['pressure']   # Давление
        wind = data['wind']['speed']  # Скорость ветра
        sunrise_timestamp = datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])  # Восход
        sunset_timestamp = datetime.datetime.fromtimestamp(
            data['sys']['sunset'])  # Закат
        length_of_the_day = datetime.datetime.fromtimestamp(
            data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])  # Вычесляем сколько врмени длиться световой день

        await message.reply(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                            f"Погода в городе: {city}\n"
                            f"Температура: {cur_waether}°C {wd}\n"
                            f"Влажность: {humidity}%\n"
                            f"Давление: {pressure} мм.рт.ст\n"
                            f"Ветер: {wind} м/с \n"
                            f"Восход солнца: {sunrise_timestamp}\n"
                            f"Закат солнца: {sunset_timestamp}\n"
                            f"Продолжительность дня: {length_of_the_day}\n"
                            f"Хорошего дня!")
    except:
        await message.reply("Проверьте название города!")

if __name__ == '__main__':
    executor.start_polling(dp)
