# -*- coding: utf-8 -*-
from telegram.ext import Updater         # пакет называется python-telegram-bot, но Python-
from telegram.ext import CommandHandler  # модуль почему-то просто telegram ¯\_(ツ)_/¯


def start(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    bot.sendMessage(chat_id=update.message.chat_id, text="Привет! ")
   # bot.sendMessage(chat_id=update.message.chat_id, text="Сейчас я посчитаю сколько нас!")
   # count=telegram.getChatMembersCount(chat_id=update.message.chat_id)
   # bot.sendMessage(chat_id=update.message.chat_id, text="Получилось: "+count)
def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

updater = Updater(token='646056076:AAHTUqGeOBavOu_FGnR8LmAK_zZ69D2vyq0')  # тут токен, который выдал вам Ботский Отец!

start_handler = CommandHandler('start', start)  # этот обработчик реагирует
                                                # только на команду /start
text_message_handler = MessageHandler(Filters.text, textMessage)

updater.dispatcher.add_handler(start_handler)   # регистрируем в госреестре обработчиков
dispatcher.add_handler(text_message_handler)
updater.start_polling()  # поехали!
