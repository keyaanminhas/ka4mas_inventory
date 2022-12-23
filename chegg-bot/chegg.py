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

import requests, os, discord
from discord.ext import commands
from bs4 import BeautifulSoup
import util


ssl._create_default_https_context = ssl._create_unverified_context


client = commands.Bot(command_prefix="!")

TOKEN = 'OTAwMzYwNTI1MTQwMDcwNDAw.YXAMFQ.YFWeeyP8o7e11rjP-Yy1B-883Cg'

@client.event
async def on_ready():
    global driver
    print(f'{client.user} is connected to the following guild :\n')
    opt = uc.ChromeOptions()
    DATA_DIRECTORY = r'C:\Users\ka4ma\AppData\Local\Google\Chrome\User Data'
    PROFILE = 'Profile 1'
    opt.add_argument(
        rf"--user-data-dir={DATA_DIRECTORY}"
    )
    opt.add_argument(rf"--profile-directory={PROFILE}")
    try:
        print("RUNNING")
        uc.TARGET_VERSION = 104
        uc.install(executable_path='chromedriver.exe',)
        #opt.add_argument('--headless')
        opt.add_argument('--start-maximized')
        driver = uc.Chrome(options=opt)
        url = 'https://chegg.com/'
        driver.get(url)
    except Exception as e:
        print("COULDNT START THE CHROME", e)

@client.command()

async def chegg(ctx, arg):
    try:

        if "https://www.chegg.com/homework-help/" not in arg: 
            await ctx.channel.send(ctx.author.mention + "This is not a chegg link!")
            return
        else:
            global driver
            driver.get(arg)
            sleep(0.5)
            
            util.fullpage_screenshot(driver, 'answer.png')
            #images=driver.find_elements_by_tag_name("a")
            await ctx.author.send(file=discord.File('answer.png'))
    except Exception as e:
        print("UNKNOWN ERROR",e)





client.run(TOKEN)