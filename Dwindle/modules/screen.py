from selenium import webdriver
import telegram
from Dwindle import TOKEN
from time import sleep
import requests
import emoji
import os
from Dwindle.drawable import *


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text
  
def screen(update, context):
      
    if bool(update.message):
       message = update.message
       text = remove_prefix(update.message.text , "/screen ")
    if bool(update.callback_query):
       message = update.callback_query.message
       text = update.callback_query.message.reply_to_message.text
      
    context.args = text.split(" ")

    url = context.args[0]

    try:
        response = requests.get(url)
        status_code = 200
    except requests.ConnectionError as exception:
        status_code = 404
    if status_code == 200:

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        driver.get(context.args[0])
        sleep(1)
        driver.get_screenshot_as_file("screen.png")
        driver.quit()
        message.reply_photo(photo=open('screen.png', 'rb'))
    else:
        message.reply_photo(photo="https://cdn.dribbble.com/users/935591/screenshots/15664793/media/90c2e1253482c777325f6172940087e3.jpeg",caption="OOPS! Web page not Found")

