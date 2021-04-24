# Timerbot
 
Бот запускает таймер на заданное количество времени. Использует Telegram.

### Локальный запуск
1. Создайте телеграм-бота - [Гайд по созданию телеграм-бота](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
2. Скачайте репозиторий командой
  
	`git clone https://github.com/SerhiiAlieksieiev/timerbot.git`
3. Сделайте виртуальное окружение командой
 
 	`python -m venv --copies /полный/путь/до/папки/виртуального/окружения `
4. Установите зависимости  командой 

	`py -m pip install -r requirements.txt`
5. Добавьте [переменные окружение](https://github.com/SerhiiAlieksieiev/timerbot#%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F)
   
6. Запустите скрипт командой 

	`python main.py`
 
### Переменные окружения
Часть настроек проекта берётся из переменных окружения. 

Доступны 2 переменные:
- `TELEGRAM_TOKEN` — токен вашего бота, можно узнать у [BotFarther](https://telegram.me/BotFather)
- `TELEGRAM_CHAT_ID` — персональный chat id, можно узнать у [userinfobot](https://telegram.me/userinfobot)

### Цели проекта
Код написан в учебных целях — это урок в [курсе](https://dvmn.org/referrals/khnIM90ONObdHawnJXjYOyKnwrucdRj9zsA5DEPm/) по Python на сайте [Devman](https://dvmn.org/referrals/eC72w2BASG9Zj3T7iMTSsxDbHXthCmJmeLKBNfwf/).

### Подсказки

[Ссылка на урок](https://dvmn.org/modules/meeting-python/lesson/timer-in-telegram/#3)

[Документация к библиотеке ptbot](https://devman.org/encyclopedia/modules/ptbot_docs/#top)
