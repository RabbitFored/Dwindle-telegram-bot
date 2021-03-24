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
    URL = os.environ.get('PUBLIC_URL', "")
    PORT = int(os.environ.get('PORT', 5000))
    bitlyApi = os.environ.get('BitLy_Api')

else:
    import Dwindle.config

    TOKEN = config.TOKEN
    WEBHOOK = config.Webhook
    URL = config.URL
    PORT = config.PORT
    try:
        bitlyApi = config.bitlyapi
    except:
        bitlyApi = null

updater = telegram.ext.Updater(TOKEN)
dispatcher = updater.dispatcher
