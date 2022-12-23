from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os
import random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import undetected_chromedriver._compat as uc
import ssl
import util

updater = Updater("5356973124:AAGCEVm_CovBpAkF_J7i8B6reDh1qVcA5hE",
                  use_context=True)
  
disp = updater.dispatcher

def start(update, context):
    update.message.reply_text(
        "WELCOME TO CHEGG BOT.")


def help(update, context):
    update.message.reply_text("COMMAND: chegg <url to the question>")

def chegg(update, context):
    junk, arg = (update.message.text).split(" ", 1)
    print(arg)
    if "https://www.chegg.com/homework-help/" not in arg: 
            update.message.reply_text("This is not a chegg link!")
    else:
        global driver
        driver.get(arg)
        sleep(0.5)
        util.fullpage_screenshot(driver, 'answer.png')
        chat_id = update.effective_chat.id
        context.bot.send_photo(chat_id = chat_id,  photo=open('answer.png', 'rb'))



global driver
opt = uc.ChromeOptions()
DATA_DIRECTORY = r'C:\Users\ka4ma\AppData\Local\Google\Chrome\User Data'
PROFILE = 'Profile 1'
opt.add_argument(
    rf"--user-data-dir={DATA_DIRECTORY}"
)
opt.add_argument(rf"--profile-directory={PROFILE}")
try:
    print("RUNNING")
    uc.TARGET_VERSION = 103
    uc.install(executable_path='chromedriver.exe',)
    #opt.add_argument('--headless')
    opt.add_argument('--start-maximized')
    driver = uc.Chrome(options=opt)
    url = 'https://chegg.com/'
    driver.get(url)
except Exception as e:
    print("COULDNT START THE CHROME", e)


disp.add_handler(CommandHandler('start', start))
disp.add_handler(CommandHandler('help', help))
disp.add_handler(CommandHandler('chegg', chegg))
updater.start_polling()
updater.idle()