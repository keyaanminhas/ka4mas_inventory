import undetected_chromedriver._compat as uc
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
import re
from datetime import date





def get_data(title):
    with open(f'ALL_TITLES/{title}.txt', 'r') as f:
        data = f.read()
        defaults = f'''---
title: "{title} Scripts"
---

'''
    paras = []
    with open('config.txt', 'r') as f:
        x = f.readlines()
        snippet = x[4].strip()
    rem =data.splitlines()
    for para in rem:
        fullstops = para.count('.')
        exclaimation_marks = para.count('!')
        question_marks = para.count('?')
        if fullstops + exclaimation_marks + question_marks < 2 and len(para) > 1:
            data = data.replace(para, '## ' + para)
            paras.append(para)
    data = data.replace('## ' + paras[-2], snippet + '\n\n' + '## ' + paras[-2])
    data = data.replace('\n', f'\n\n{snippet}\n\n', 1)
    data = defaults + data + f'\n\n{snippet}'
    return data


def instance(title):
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    data = get_data(title)
    title = title.replace(' ', '-')
    with open(f'UPLOADABLE/{d1}-{title}.md', 'w') as f:
        f.write(data)
        print(f'UPLOADABLE/{d1}-{title}.md')
    # url = 'https://github.com/robloxpaste/robloxpaste.github.io/tree/main/_posts'
    # driver.get(url)



def sender(message, location):
    for i in range(0,len(message)):
        location.send_keys(message[i])
        sleep(0.05)
        # sleep(0.2)


def uploader():

    # opt = uc.ChromeOptions()
    # DATA_DIRECTORY = r'C:\Users\ka4ma\AppData\Local\Google\Chrome\User Data'
    # PROFILE = 'Profile 1'
    # opt.add_argument(
    #     rf"--user-data-dir={DATA_DIRECTORY}"
    # )
    # opt.add_argument(rf"--profile-directory={PROFILE}")
    # try:
    #     print("RUNNING")
    #     uc.TARGET_VERSION = 103
    #     uc.install(executable_path='chromedriver.exe')
    #     #opt.add_argument('--headless')
    #     opt.add_argument('--start-maximized')
    #     driver = uc.Chrome(options=opt)
    #     sleep(3)
    titles = os.listdir('ALL_TITLES/')
    for title in titles:
        instance(title[:-4])
    input("DONE")



uploader()