from Dwindle import bitlyApi
import requests
from Dwindle import dispatcher
from telegram.ext import CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import pyshorteners
import re
import json

platforms = ['adfly','bitly',  'chilpit', 'clckru', 'cuttly', 'dagd', 'gitio', 'isgd',
                 'nullpointer', 'osdb', 'owly', 'post', 'qpsru', 'shortcm', 'tinycc', 'tinyurl']

shortmessage = "<b>Your URL : </b> {} \n\n<b>Shortened URL :</b> \n\n<b> - </b> {}"
'''       '''
def short(update, context):
    validurl = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    if len(context.args)==2:
        if context.args[0] == 'adfly':
            update.message.reply_text(shortmessage.format(context.args[1], adfly(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

        elif context.args[0] == 'bitly':
            update.message.reply_text(shortmessage.format(context.args[1], bitly(bitlyApi, context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

        elif context.args[0] == 'chilpit':
            update.message.reply_text(shortmessage.format(context.args[1], chilpit(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

        elif context.args[0] == 'clckru':
            update.message.reply_text(shortmessage.format(context.args[1], clckru(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

        elif context.args[0] == 'dagd':
            update.message.reply_text(shortmessage.format(context.args[1], dagd(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)
        elif context.args[0] == 'gitio':
            update.message.reply_text(shortmessage.format(context.args[1], gitio(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

        elif context.args[0] == 'isgd':
            update.message.reply_text(shortmessage.format(context.args[1], isgd(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

        elif context.args[0] == 'nullpointer':
            update.message.reply_text(shortmessage.format(context.args[1], nullpointer(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)
        elif context.args[0] == 'osdb':
            update.message.reply_text(shortmessage.format(context.args[1], osdb(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

        elif context.args[0] == 'owly':
            update.message.reply_text(shortmessage.format(context.args[1], owly(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

        elif context.args[0] == 'qpsru':
            update.message.reply_text(shortmessage.format(context.args[1], qpsru(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

        elif context.args[0] == 'tinyurl':
            update.message.reply_text(shortmessage.format(context.args[1], tinyurl(context.args[1])),
                                      parse_mode='html',
                                      reply_to_message_id=update.message.message_id)

    elif len(context.args) == 1:
            keyboard  = [
                [
                    InlineKeyboardButton("adfly", callback_data=f'adfly||{context.args[0]}'),
                    InlineKeyboardButton("bitly", callback_data=f'bitly||{context.args[0]}'),
                    InlineKeyboardButton("chilpit", callback_data=f'chilpit||{context.args[0]}'),
                ],
                [
                    InlineKeyboardButton("clckru", callback_data=f'clckru||{context.args[0]}'),
                    InlineKeyboardButton("dagd", callback_data=f'dagd||{context.args[0]}'),
                    InlineKeyboardButton("gitio", callback_data=f'gitio||{context.args[0]}'),

                ],
                [
                    InlineKeyboardButton("isgd", callback_data=f'isgd||{context.args[0]}'),
                    InlineKeyboardButton("nullpointer", callback_data=f'nullpointer||{context.args[0]}'),

                ],
                [
                    InlineKeyboardButton("osdb", callback_data=f'osdb||{context.args[0]}'),
                    InlineKeyboardButton("qpsru", callback_data=f'qpsru||{context.args[0]}'),
                    InlineKeyboardButton("tinyurl", callback_data=f'tinyurl||{context.args[0]}'),
                ],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text("Please choose some platform:", reply_markup=reply_markup)

    else:
        update.message.reply_text("Provide some valid URL")

def short_buttons(update,context):

    query = update.callback_query
    query.answer()
    platform = query.data.split("||")[0]
    link = query.data.split("||")[1]

    if platform =='adfly':
        shorten = adfly(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')

    elif platform == 'bitly':
        shorten = bitly(bitlyApi,link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')


    elif platform == 'chilpit':
        shorten = chilpit(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')

    elif platform == 'clckru':
        shorten = clckru(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')
    elif platform == 'dagd':
        shorten = dagd(link)

        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')
    elif platform == 'gitio':
        shorten = gitio(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')

    elif platform == 'gplinks':
        shorten = gplinks(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')

    elif platform == 'isgd':
        shorten = isgd(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')

    elif platform == 'nullpointer':
        shorten = nullpointer(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')

    elif platform == 'osdb':
        shorten = osdb(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')


    elif platform == 'qpsru':
        shorten = qpsru(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')

    elif platform == 'tinyurl':
        shorten = tinyurl(link)
        query.edit_message_text(text=shortmessage.format(link, shorten), parse_mode='html')

def adfly(url):
    return pyshorteners.Shortener(api_key='', user_id='', domain='test.us',
                               group_id=12, type='int').adfly.short(url)

def bitly(api, url):
    return pyshorteners.Shortener(api_key=api).bitly.short(url)

def chilpit(url):
    return pyshorteners.Shortener().chilpit.short(url)

def clckru(url):
    return pyshorteners.Shortener().clckru.short(url)

def dagd(url):
    return pyshorteners.Shortener().dagd.short(url)

def gitio(url):
    return pyshorteners.Shortener().gitio.short(url)

def isgd(url):
    return pyshorteners.Shortener().isgd.short(url)
def nullpointer(url):
    return pyshorteners.Shortener(domain='https://0x0.st').nullpointer.short(url)

def osdb(url):
    return pyshorteners.Shortener().osdb.short(url)

def qpsru(url):
    return pyshorteners.Shortener().qpsru.short(url)

def tinyurl(url):
    return pyshorteners.Shortener().tinyurl.short(url)
