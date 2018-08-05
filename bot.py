# -*- coding: utf-8 -*-
from telegram.ext import Updater         # пакет называется python-telegram-bot, но Python-
from telegram.ext import CommandHandler  # модуль почему-то просто telegram ¯\_(ツ)_/¯

def handle_text(bot, update):
    # ...
def handle_command(bot, update):
    # ...
def start(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    text="Здравствуйте. "
    text+=str(telegram.getChatMembersCount(chat_id=update.message.chat_id))
    bot.sendMessage(chat_id=update.message.chat_id, text=text)
                    
updater = Updater(token='646056076:AAHTUqGeOBavOu_FGnR8LmAK_zZ69D2vyq0')  # тут токен, который выдал вам Ботский Отец!

start_handler = CommandHandler('start', start)  # этот обработчик реагирует
                                                # только на команду /start

updater.dispatcher.add_handler(start_handler)   # регистрируем в госреестре обработчиков
text_handler = MessageHandler(Filters.text, self.handle_text)
command_handler = MessageHandler(Filters.command, self.handle_command)
# регистрируем свеженькие обработчики в диспетчере
updater.dispatcher.add_handler(text_handler)     # без регистрации будет работать, 
updater.dispatcher.add_handler(command_handler)
updater.start_polling()  # поехали!
