# weather
## Telegram-бот служит  для получения данных о погоде в любом городе нашей планеты. Изучал новую асинхронную библиотеку aiogram
## стек технологий : 
 - Python 3.9
 - Aiogram
### Как запустить проект.
#### Клонировать репозиторий и перейти в него в командной строке:
 * git@github.com:Damened/weather.git
 * cd weather
#### Cоздать и активировать виртуальное окружение:
 * python3 -m venv venv
 * source venv/bin/activate
#### Установить зависимости из файла requirements.txt:
 * python3 -m pip install --upgrade pip
 * pip install -r requirements.txt
#### Создать файл .env в внести токен от телеграм бота и токен с openweathermap ( его можно получит после регистрации на данныом сайте)
 * TOKEN_TG_BOT = "token api "
 * TOKEN_WEATHER_API = "token openweathermap"
#### Запустить приложение.
