#!/usr/bin/python
import logging
import os
import sys
import telegram.ext

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 4:
    LOGGER.error("You MUST have a python version of at least 3.4! Multiple features depend on this. Bot quitting.")
    quit(1)

ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN = os.environ.get('BOT_TOKEN', None)
    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    URL = os.environ.get('PUBLIC_URL',"")
    PORT = int(os.environ.get('PORT', 5000))
    GpApi = os.environ.get('GpLinksApi')
    GpBase = "https://gplinks.in/api?api={}&url=".format(GpApi)
    bitlyApi = os.environ.get('BitLy_Api')
    bitlybase = "https://api-ssl.bitly.com/v3/shorten?access_token={}&uri=".format(bitlyApi)

else:
    from Dwindle import Config
    TOKEN = Config.TOKEN
    WEBHOOK = Config.Webhook
    URL = Config.URL
    PORT = Config.PORT
    GpBase= Config.GpBase
    bitlybase = Config.bitlybase

updater = telegram.ext.Updater(TOKEN)
dispatcher = updater.dispatcher

