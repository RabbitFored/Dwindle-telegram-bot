from Dwindle import bitlyApi
import requests
from Dwindle import dispatcher
from telegram.ext import CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import pyshorteners
import re

platforms = ['bitly', 'chilpit', 'nullpointer']

shortmessage = "<b>Your URL : </b> {} \n\n<b>Shortened URL :</b> \n\n<b> - </b> {}"
'''       '''
def short(update, context):
    link = context.args[0]

    validurl = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    if len(context.args) > 1:
        if context.args[0] == 'bitly':
            update.message.reply_text(shortmessage.format(context.args[1], bitly(bitlyApi, context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)
        elif context.args[0] == 'nullpointer':
            update.message.reply_text(shortmessage.format(context.args[1], nullpointer(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)
        elif context.args[0] == 'chilpit':
            update.message.reply_text(shortmessage.format(context.args[1], chilpit(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

    elif len(context.args) == 1:
        if re.match(
                r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
                , context.args[0]):
            keyboard = [
                [
                    InlineKeyboardButton("bitly", callback_data=f'bitly||{link}'),
                    InlineKeyboardButton("nullpointer", callback_data=f'nullpointer||{link}'),
                ],
                [InlineKeyboardButton("chilpit", callback_data=f'chilpit||{link}')],
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)

            update.message.reply_text('Please choose:', reply_markup=reply_markup)
        else:
            update.message.reply_text('Provide a valid URL', reply_markup=reply_markup)
    else:
        update.message.reply_text("Provide some url to short")


def bitly(api, url):
    return pyshorteners.Shortener(api_key=api).bitly.short(url)

def nullpointer(url):
    return pyshorteners.Shortener(domain='https://0x0.st').nullpointer.short(url)

def chilpit(url):
    return pyshorteners.Shortener().chilpit.short(url)

def short_buttons(update,context):
    query = update.callback_query
    query.answer()
    platform = (query.data).split("||")[0]
    link = (query.data).split("||")[1]
    if platform == 'bitly':
        shorten = bitly(bitlyApi,link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')

    elif platform == 'nullpointer':
        shorten = nullpointer(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')

    elif platform == 'chilpit':
        shorten = nullpointer(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')
