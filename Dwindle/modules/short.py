from Dwindle import GpBase, bitlybase, TOKEN
import requests
from Dwindle import dispatcher
from telegram.ext import CommandHandler


def short(update, context):
    platforms = ['bitly', 'gplinks']
    gpintext = requests.get(GpBase + context.args[1]).json()
    bitlyintext = requests.get(bitlybase + context.args[1]).json()
    bi = bitlyintext['data']

    if context.args[0] in platforms:
        if context.args[0] == "bitly":
            update.message.reply_text("<b>Your URL : </b>" + context.args[1] + "\n\n<b>Shortened URL :</b>"+
                                       "\n\n<b> - </b>" + bi['url'] , parse_mode='html',reply_to_message_id=update.message.message_id)

        elif context.args[0] == "gplinks":
            update.message.reply_text("<b>Your URL : </b>" + context.args[1] +
                                      "\n\n<b>Shortened URL :</b> "+
                                      "\n\n<b> - </b>" + gpintext['shortenedUrl'] , parse_mode='html',reply_to_message_id=update.message.message_id)

    else:
        update.message.reply_text("Enter A valid Platform")

