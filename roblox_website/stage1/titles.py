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


letters = 'abcdefghijklmnopqrstuvwxyz '
letters = letters + letters.upper()





def easy_titles(driver, window, scroll):
    all_titles = []

    MESSAGES = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,window)))
    titles1 = remove_emojis(MESSAGES.text)
    scroll1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, scroll)))

    try:
        while 'disabled' not in scroll1.get_attribute('class'):
            scroll1.click()
            MESSAGES = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,window)))
            titles1 = titles1 + (remove_emojis(MESSAGES.text))
            scroll1.get_attribute('class')
        [all_titles.append(item) for item in titles1 if item not in all_titles]
        return all_titles
    except Exception as e:
        print("ERROR", e)




def remove_emojis(text):
    # \(.*?\) ==> it is a regular expression for finding
    # the pattern for brackets containing some content
    text=re.sub("\[.*?\]","",text)
    #text = text.replace("K", "")
    text = ''.join(c for c in text if c in letters or c == '\n')
    titles = text.split('\n')
    for element in titles:
        if element == '' or len(element) == 1:
            titles.remove(element)
    return titles

def get_titles():
    all_titles = []
    url = "https://www.roblox.com/discover#/"
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
        uc.install(executable_path='chromedriver.exe')
        opt.add_argument('--headless')
        opt.add_argument('--start-maximized')
        driver = uc.Chrome(options=opt)
        sleep(5)
        driver.get(url)
        TITLES = []

        for i in range(2,18):
            TITLES = TITLES + easy_titles(driver, f'/html/body/div[5]/div[3]/div[2]/div/div[{i}]/div/div/div[1]/ul', f'/html/body/div[5]/div[3]/div[2]/div/div[{i}]/div/div/div[3]')

        ANSWER = []
        [ANSWER.append(item) for item in TITLES if item not in ANSWER]
        with open('titles.txt', 'w') as f:
            for title in ANSWER:
                if len(title) < 2:
                    pass
                while title.startswith(' ') == True:
                    title = title[1:]
                f.write(str(title) + '\n')
        driver.quit()
    except Exception as e:
        print("ERROR CAME ", e)


get_titles()
