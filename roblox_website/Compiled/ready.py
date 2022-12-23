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
categories:
  - scripts
  
tags:
  - Roblox
---

'''
    data = data.replace('\n', '\n\n[![script button](https://github.com/robloxpaste/robloxpaste.github.io/blob/main/script_button.png?raw=true)](https://rbxpaste.com/latest-script)\n\n', 1)
    data = data.replace(f'## How To Use Roblox {title} Script', '[![script button](https://github.com/robloxpaste/robloxpaste.github.io/blob/main/script_button.png?raw=true)](https://rbxpaste.com/latest-script)\n\n## How To Use Roblox Weapon Fighting Simulator Script', 1)
    data = defaults + data + '\n\n[![script button](https://github.com/robloxpaste/robloxpaste.github.io/blob/main/script_button.png?raw=true)](https://rbxpaste.com/latest-script)'
    return data


def instance(title):
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    print(d1)
    data = get_data(title)
    title = title.replace(' ', '-')
    with open(f'UPLOADABLE/{d1}-{title}.md', 'w') as f:
        f.write(data)
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
        with open('titles.txt', 'r') as f:
            titles = f.readlines()
        for i in range(0,len(titles)):
            title = titles[i].strip()
            instance(title)




uploader()