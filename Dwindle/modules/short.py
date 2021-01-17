from Dwindle.Config import GpBase, RareBase, bitlybase, TOKEN
import requests
from bs4 import BeautifulSoup
from Dwindle import dispatcher
from telegram.ext import CommandHandler


def short(update, context):
    platforms = ['bitly', 'gplinks', 'rare']
    gpintext = requests.get((GpBase + context.args[1])).json()
    rarintext = requests.get(RareBase + context.args[1])
    bitlyintext = requests.get(bitlybase + context.args[1]).json()
    bi = bitlyintext['data']
    soup = BeautifulSoup(rarintext.text, 'lxml')

    if context.args[0] in platforms:
        if context.args[0] == "bitly":
            update.message.reply_text("<b>Your URL : </b>" + context.args[1] + "\n\n<b>Shortened URL :</b>"
                                                                               "\n\n<b> - </b>" + bi['url'] +
                                      "\n\n<b> - </b> " + soup.shorturl.string, parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

        elif context.args[0] == "gplinks":
            update.message.reply_text("<b>Your URL : </b>" + context.args[1] +
                                      "\n\n<b>Shortened URL :</b> "
                                      "\n\n<b> - </b>" + gpintext['shortenedUrl'] +
                                      "\n\n<b> - </b>" + soup.shorturl.string, parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

    else:
        update.message.reply_text("Enter A valid Platform")

