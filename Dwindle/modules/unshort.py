import requests

unshortmessage = "<b>Your URL : </b> {} \n\n<b>Expanded URL :</b> \n\n<b> - </b> {}"
'''       '''

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text
  
def unshort(update, context):
      
    if bool(update.message):
       message = update.message
       text = remove_prefix(update.message.text , "/unshort ")
    if bool(update.callback_query):
       message = update.callback_query.message
       text = update.callback_query.message.reply_to_message.text
      
    context.args = text.split(" ")

    if len(context.args)==1:
        session = requests.Session()
        unshortened = session.head(context.args[0], allow_redirects=True)
        message.reply_text(unshortmessage.format(context.args[0],unshortened.url),parse_mode='html')
    else:
        message.reply_text('Please provide me some URL.')
