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
import urllib




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
        uc.TARGET_VERSION = 102
        uc.install(executable_path='chromedriver.exe',)
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
            sleep(1)
            
            question = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="chegg-main-content"]/div/div/div/div/div[1]',
                )
            )
        )
            embed = discord.Embed(colour = random.randint(0, 255))
            embed.add_field(name = "Question" , value= question.text)

            await ctx.author.send(embed = embed)
            images=question.find_elements(by=By.TAG_NAME, value="img")
            if len(images)!= 0:
                for img in images:
                    src = img.get_attribute('src')
                    urllib.request.urlretrieve(src, 'question.png')

                    await ctx.author.send(file=discord.File('question.png'))








            
            answer = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="chegg-main-content"]/div/div/div/div/div[2]/section/div[2]/div/div/div/div/div[2]',
                )
            )
        )
            embed = discord.Embed(colour = random.randint(0, 255))
            embed.add_field(name = "CHEGG" , value= answer.text)
            await ctx.author.send(embed = embed)
            images=answer.find_elements(by=By.TAG_NAME, value="img")
            if len(images)!= 0:
                for img in images:
                    src = img.get_attribute('src')
                    urllib.request.urlretrieve(src, 'answer.png')

                    await ctx.author.send(file=discord.File('answer.png'))


            #await ctx.author.send(file=discord.File('answer.png'))
    except Exception as e:
        print("UNKNOWN ERROR",e)





client.run(TOKEN)