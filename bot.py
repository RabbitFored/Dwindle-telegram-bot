import logging
import requests
import telegram
from telegram.ext import Updater, CommandHandler, dispatcher, MessageHandler, Filters
import emoji
import os

TOKEN = os.environ.get('Bot_Token')
GpApi = os.environ.get('GpLinksApi')
GpBase = "https://gplinks.in/api?api={}&url=".format(GpApi)
bitlyApi = os.environ.get('BitLy_Api')
bitlybase = "https://api-ssl.bitly.com/v3/shorten?access_token={}&uri=".format(bitlyApi)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)


def start (update, context):
    wave = (emoji.emojize(":wave:", use_aliases=True))
    firstname = update.message.chat.first_name
    update.message.reply_text("<b>Hi {} {} ! \n\nI'm <a href=\"tg://user?id=1451118099\">Dwindle</a> - A Simple URL shortener bot."
                               "\n\nSend me any link , I can short it for You."
                              "\n\nHit /help to find out more about how to use me.</b>".format(firstname,wave) , parse_mode='html')

def help(update, context):
    update.message.reply_text("*Hey! My name is Dwindle.* "
                              "\n\nI am a link shortener bot, here to help you to shorten your links!"
                              "\nI have lots of handy features to help You"
                              "\n\n*Helpful commands:*"
                              "\n\t\t- /start: Starts me! You've probably already used this."
                              "\n\t\t- /help: Sends this message; I'll tell you more about myself!"
                              "\n\t\t- /short <url> : Shortens the given URL"
                              "\n\t\t- /donate: Gives you info on how to support me and my creator.",
                              parse_mode=telegram.ParseMode.MARKDOWN)


def short(update , context):
    gpintext = requests.get((GpBase + context.args[0])).json()
    bitlyintext = requests.get(bitlybase+context.args[0]).json()
    bi = bitlyintext['data']

    update.message.reply_text("*Your URL :* "+ context.args[0] +
                              "\n\n*Shortened URL : *"+
                              "\n\n\t\t* - *" + gpintext['shortenedUrl'] +
                              "\n\n\t\t* - *" + bi['url']+
                              "\n\n*You can Choose any of the above shortened links*", parse_mode=telegram.ParseMode.MARKDOWN)

def unshort(update , context):
    session = requests.Session()
    unshortened = session.head(context.args[0], allow_redirects=True)
    update.message.reply_text(unshortened.url)
    
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("short", short))
    dispatcher.add_handler(CommandHandler("unshort", unshort))
    dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
