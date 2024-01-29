import random
import threading
from time import sleep

import telebot
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_2fa.settings')
django.setup()
from app.models import User

bot = telebot.TeleBot('6544933471:AAGSYBK7nmuxWL8f42tpxHXV8z-lfhF2p5g')


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    try:
        user = User.objects.get(tg_id=chat_id)
    except Exception:
        try:
            unique_id = message.text.split()[1]
        except IndexError:
            pass
        else:
            code = random.randint(10000, 100000)
            user = User.objects.create(
                tg_id=chat_id,
                unique_id=unique_id,
                code=code)
            text = f'Ваш код: `{user.code}`'
            bot.send_message(chat_id, text, parse_mode='MarkdownV2')
    else:
        text = f'Ваш код: `{user.code}`'
        bot.send_message(chat_id, text, parse_mode='MarkdownV2')


def polling_process():
    bot.polling(none_stop=True)


def update_code():
    while True:
        users = User.objects.all()
        for user in users:
            new_code = random.randint(10000, 100000)
            user.code = new_code
            user.save()
        sleep(60)

def start_server():
    os.system('python manage.py runserver 0.0.0.0:8000')

if __name__ == '__main__':
    polling_thread = threading.Thread(target=polling_process)
    polling_thread.start()
    update_code = threading.Thread(target=update_code)
    update_code.start()
    start_server = threading.Thread(target=start_server)
    start_server.start()

