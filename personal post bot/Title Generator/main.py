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
import pyperclip as pc





def instance(driver, url, title):
    sleep(1)
    driver.get(url)
    sleep(0.5)
    topic = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/main/section[1]/div[3]/div[1]/div[1]/div[2]/div/input')))
    topic.send_keys(title)
    gen_num= WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/main/section[1]/div[3]/div[2]/div[1]/input')))
    gen_num.send_keys(Keys.BACKSPACE)
    gen_num.send_keys('5')

    sleep(0.2)
    generate = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/main/section[1]/div[3]/div[2]/div[2]/button')))
    generate.click()

    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/main/section[1]/div[3]/div[2]/div[2]/button")))
    sleep(1)
    print('[!] generated, Copying.....')
    
    copying1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/main/section[2]/div/div/div[2]/div/div[1]/div[1]/div/button[3]'))).click()
    sleep(1)
    first = pc.paste()
    sleep(1)
    
    copying2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/main/section[2]/div/div/div[2]/div/div[2]/div[1]/div/button[3]'))).click()
    sleep(1)
    second = pc.paste()
    sleep(1)


    copying3 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/main/section[2]/div/div/div[2]/div/div[3]/div[1]/div/button[3]'))).click()
    sleep(1)
    third = pc.paste()
    sleep(1)

    copying4 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/main/section[2]/div/div/div[2]/div/div[4]/div[1]/div/button[3]'))).click()
    sleep(1)
    fourth = pc.paste()
    sleep(1)

    copying5 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/main/section[2]/div/div/div[2]/div/div[5]/div[1]/div/button[3]'))).click()
    sleep(1)
    fifth = pc.paste()
    sleep(1)

    with open('generated.txt', 'a' ) as f:
        f.write(first+ '\n') 
        f.write(second+ '\n')
        f.write(third+ '\n')
        f.write(fourth+ '\n')
        f.write(fifth+ '\n')


def gen():
    url = "https://app.writesonic.com/template/c4c2d567-4ea2-431c-99d8-23fbd4f2dd3b/blog-ideas/b1fa92f4-a48a-434c-b84f-c7c4b1d65c5e?generateCopy=true" 
    sleep(1)
    opt = uc.ChromeOptions()
    with open('config.txt', 'r') as f:
        x = f.readlines()
    path = x[0].strip()
    profile = path.split("\\", -2)
    PROFILE = profile[-1]
    DATA_DIRECTORY = path[0:len(path)-len(profile) -1]
    print(PROFILE)
    print(DATA_DIRECTORY)

    opt.add_argument(
        rf"--user-data-dir={DATA_DIRECTORY}"
    )
    opt.add_argument(rf"--profile-directory={PROFILE}")
    while 1:
        try:
            print("RUNNING")
            uc.TARGET_VERSION = 103
            uc.install(executable_path='chromedriver.exe')
            #opt.add_argument('--headless')
            opt.add_argument('--start-maximized')
            driver = uc.Chrome(options=opt)
            sleep(3)
            driver.get(url)
            sleep(1)
            login = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/main/div/div/div[2]/div/div[2]/div[4]/button'))).click()
            sleep(8)
            break
        except Exception as e:
            print("ERROR CAME, Trying again", e)
    
    with open('titles.txt', 'r') as f:
        titles = f.readlines()
    for i in titles:
        sleep(2)
        instance(driver, url, i)

gen()