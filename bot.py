# -*- coding: utf-8 -*-
from telegram.ext import Updater         # пакет называется python-telegram-bot, но Python-
from telegram.ext import CommandHandler  # модуль почему-то просто telegram ¯\_(ツ)_/¯

def start(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    bot.sendMessage(chat_id=update.message.chat_id, text="Здравствуйте.")
def users(bot,update):
	bot.sendmessage(chat_id=update.message.chat_id, str(telegram.getChatMembersCount(chat_id=update.message.chat_id)))

updater = Updater(token='646056076:AAHTUqGeOBavOu_FGnR8LmAK_zZ69D2vyq0')  # тут токен, который выдал вам Ботский Отец!

start_handler = CommandHandler('start', start)  # этот обработчик реагирует
                                                # только на команду /start
users_counter = CommandHandler('users', users)

updater.dispatcher.add_handler(start_handler)   # регистрируем в госреестре обработчиков
updater.start_polling()  # поехали!
