import requests

def unshort(update, context):
    if len(context.args)==1:
        session = requests.Session()
        unshortened = session.head(context.args[0], allow_redirects=True)
        update.message.reply_text(unshortened.url)
    else:
        update.message.reply_text('Please provide some URL.')
