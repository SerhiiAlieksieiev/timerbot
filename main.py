import ptbot
import os
from pytimeparse import parse

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  
TELEGRAM_CHAT_ID = '340356067'  

def reply(text):
    time = parse(text)
    message = "Таймер запущен на {} секунд".format(time)
    message_id = bot.send_message(TELEGRAM_CHAT_ID, message)
    bot.create_countdown(time, notify_progress, message_id=message_id, total_time=time)
    bot.create_timer(time, notify)
  

def notify_progress(secs_left, message_id, total_time):
    message = "Осталось {} секунд\n {}".format(secs_left, render_progressbar(total_time,secs_left))
    bot.update_message(TELEGRAM_CHAT_ID, message_id, message)

def notify():
    bot.send_message(TELEGRAM_CHAT_ID, "Время вышло!")

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

if __name__ == '__main__':  
    bot = ptbot.Bot(TELEGRAM_TOKEN)
    bot.send_message(TELEGRAM_CHAT_ID, "На сколько запустить таймер?")
    bot.reply_on_message(reply)
    bot.run_bot()

