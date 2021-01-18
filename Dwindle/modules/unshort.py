import requests

def unshort(update, context):
    session = requests.Session()
    unshortened = session.head(context.args[0], allow_redirects=True)
    update.message.reply_text(unshortened.url)