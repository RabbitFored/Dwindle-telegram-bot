from selenium import webdriver
import telegram
from Dwindle import TOKEN
from time import sleep
import requests
import emoji
import os
from Dwindle.drawable import *

bot = telegram.Bot(token=TOKEN)

def screen(update, context):
    chat_id = update.message.chat_id
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
        bot.send_photo(chat_id=chat_id, photo=open('screen.png', 'rb'))
    else:
        bot.send_photo(chat_id=chat_id, photo=open('Dwindle/drawable/404_error.png','rb'),caption="OOPS! Web page not Found"+(emoji.emojize(":confused:",use_aliases=True)))

