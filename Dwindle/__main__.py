import logging
from telegram.ext import Updater, CommandHandler, dispatcher, CallbackQueryHandler,MessageHandler, Filters
import emoji
import telegram
from Dwindle.modules.short import short_buttons
from Dwindle import TOKEN, LOGGER, PORT, WEBHOOK , URL
from Dwindle.modules import *
from Dwindle.modules.short import short_buttons
from Dwindle.modules.unshort import unshort
from Dwindle.modules.screen import screen
import html

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
    
def start(update, context):
  bot_first_name = context.bot.get_me().first_name
  user_first_name = update.effective_user.first_name
    
  update.message.reply_text( f"<b>Hi {html.escape(user_first_name)}👋! \n"
                             f"I'm {html.escape(bot_first_name)}- Send me a URL, and I can do interesting stuff for you.\n\n"
                             "Check </b>/help<b> to find out more about how to use me.</b>",
                             parse_mode='html',
                             reply_to_message_id=update.message.message_id)

def assist(update, context):
    update.message.reply_text("I have lots of handy features to help You."
                              "\n\n*Helpful commands:*"
                              "\n\t\t- /short <url>: _Shortens the given URL_"
                              "\n\t\t- /unshort <url>: _Expand the given URL_"
                              "\n\t\t- /screen <url>: _Generates screenshot of the webpage of URL_"
                                
                              "\n\n*Other bot commands:*"
                              "\n\t\t- /start: _Starts me!_"
                              "\n\t\t- /help: _Sends this message_"
                              "\n\t\t- /about: _Know more about me_"
                              "\n\t\t- /donate: _Provides info on how to support me and my creators_",
                              
                              reply_markup=telegram.InlineKeyboardMarkup([ 
                                           [ telegram.InlineKeyboardButton("GET HELP", url="https://telegram.me/ostrichdiscussion") ] 
                                                                        ]),
                              parse_mode=telegram.ParseMode.MARKDOWN,
                              reply_to_message_id=update.message.message_id)




def aboutTheBot(update, context):
  bot_first_name = context.bot.get_me().first_name
  update.message.reply_text(f"<b>Hey! I am {html.escape(bot_first_name)}.</b>"
                             "\nI can handle URLs in different ways."
                             "\n\n<b>About Me :</b>"
                            f"\n  - <b>Name</b>        : {html.escape(bot_first_name)}"
                             "\n  - <b>Creator</b>      : @quantumbackdoor"
                             "\n  - <b>Language</b>  : Python 3"
                             "\n  - <b>Library</b>       : <a href=\"https://github.com/python-telegram-bot/python-telegram-bot/\">python-telegram-bot</a>"
                             "\n  - <b>Source Code</b>  : <a href=\"https://github.com/RabbitFored/Dwindle/\">Dwindle-Source</a>"
                             "\n\nIf you enjoy using me and want to contribute, /donate to help us maintain this project. Doesn't have to be much - every little helps!\nThanks for reading :)",
                            parse_mode='html',
                            reply_markup=telegram.InlineKeyboardMarkup([
                                                   [ telegram.InlineKeyboardButton("➰ Updates", url="t.me/theostrich"),
                                                     telegram.InlineKeyboardButton("👥 Support Group",url="t.me/ostrichdiscussion") ] ]),
                            disable_web_page_preview=True)


def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    if query.data == 2:
        print(query.data)
    query.edit_message_text(text="Support Group arrives Soon")

def donate(update, context):
  update.message.reply_text("Thank you for your wish to contribute. I hope you enjoyed using our services. Make a small donation/contribution to let this project stay alive.",
                           reply_markup=telegram.InlineKeyboardMarkup([
                                          [ telegram.InlineKeyboardButton("Contribute", url="https://github.com/theostrich/Dwindle-telegram-bot"),
                                            telegram.InlineKeyboardButton("Paypal Us", url="https://paypal.me/donateostrich") ]]))
def button(update, context):
    query = update.callback_query
    query.answer()



def error(update, context):
  """Log Errors caused by Updates."""

  text = f"<b>Error ID: <code>007</code></b>\n"\
         f"<b>Instance:</b>\n<code>{html.escape(str(update))}</code>\n"\
         f"<b>Error:</b>\n<code>{html.escape(str(context.error))}</code>"
  context.bot.send_message(text=text, chat_id = logChannel, parse_mode='html')
  

def chooseFeature(update,context):
  update.message.reply_text('''<b>Select an option:</b>''',                             
                             reply_markup=telegram.InlineKeyboardMarkup([
                                    [ telegram.InlineKeyboardButton("Short", callback_data="1short")    ],
                                    [ telegram.InlineKeyboardButton("Unshort",callback_data="1unshort") ],
                                    [ telegram.InlineKeyboardButton("Screen",callback_data="1screen")   ]]), 
                             parse_mode='html',
                             reply_to_message_id=update.message.message_id)

def callback(update,context):
    query = update.callback_query
 
    if query.data =='1short':
        short.short(update,context)   
    if query.data =='1unshort':
        unshort.unshort(update,context)    
    if query.data =='1screen':
        screen.screen(update,context)   
        
    query.answer()
def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    
    dispatcher.add_handler(MessageHandler(Filters.text & Filters.entity("url"), chooseFeature))
    dispatcher.add_handler(CallbackQueryHandler(callback,pattern='^1'))
    dispatcher.add_handler(CallbackQueryHandler(short_buttons))
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(short_buttons))
    dispatcher.add_handler(CommandHandler("help", assist))
    dispatcher.add_handler(CommandHandler("short", short))
    dispatcher.add_handler(CommandHandler("unshort", unshort))
    dispatcher.add_handler(CommandHandler("screen", screen))
    dispatcher.add_handler(CommandHandler("about", aboutTheBot))
    dispatcher.add_handler(CommandHandler("donate", donate))
    dispatcher.add_error_handler(error)

    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)
        updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info("Using long polling.")
        updater.start_polling(timeout=15, read_latency=4)

    updater.idle()

if __name__ == '__main__':
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    main()
