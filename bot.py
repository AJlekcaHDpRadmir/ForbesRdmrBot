from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TG_TOKEN

def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')
    bot.message.reply_text('Здравствуйте, {}! \n'
                           'Поговорите со мной!'.format(bot.message.chat.first_name))

def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)

def main():
    my_bot = Updater(TG_TOKEN)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))
    my_bot.start_polling()
    my_bot.idle()

main()