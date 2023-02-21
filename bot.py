import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
import ephem
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):    
    print("Вызван /start")
    update.message.reply_text('Привет, пользователь!')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planets(update, context):
    user_planet = input('Название планеты  ').capitalize()
    print(user_planet)
    list_of_planets = str(ephem._libastro.builtin_planets())
    if user_planet in list_of_planets:
        planet = getattr(ephem, user_planet)
        date = planet(ephem.Date(datetime.date.today()))
        constellation = ephem.constellation(date)
        update.message.reply_text(constellation)
    
    else:
        update.message.reply_text("Такая планета мне не известна")
    

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()        