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



def sender(message, location):
    for i in range(0,len(message)):
        location.send_keys(message[i])
        sleep(0.05)
        # sleep(0.2)



def instance(driver, title):
    url = "https://first-night.com/russia" 
    driver.get(url)
    sleep(10.5)
    create_new = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/button[3]'))).click()
    sleep(1)
    doc_title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/input')))
    #sender(title, doc_title)
    doc_title.send_keys(title)
    create_new = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/button[2]'))).click()



    #GENERATING LONG FORM
    sleep(0.3)
    long_form = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[4]/button'))).click()
    sleep(0.5)
    
    description = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/textarea')))
    description.send_keys(f"Get the latest Roblox {title} scripts")

    structure = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/textarea')))
    formatt = f"""## Get the latest Roblox {title} scripts
***
## Roblox {title} Script Features
***
## How to use Roblox {title} Script"""
    structure.send_keys(formatt)




    sleep(0.3)
    generate = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/button[2]'))).click()

    save = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/button[6]')))
    while 1:
        try: 
            save.click()
            break
        except Exception as e: 
            print("LOADING DID NOT END")
            sleep(3)

    sleep(2)


    ai_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="richtext-editor-0"]/div[1]')))

    with open(f'ALL_TITLES/{title}.txt', 'w') as f:
        f.write(ai_text.text)





def gen():
    
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
        #opt.add_argument('--headless')
        opt.add_argument('--start-maximized')
        driver = uc.Chrome(options=opt)
        sleep(3)
        with open('titles.txt', 'r') as f:
            titles = f.readlines()
        for i in range(4):
            title = titles[i].strip()
            instance(driver, title)





    except Exception as e:
        print("ERROR CAME ", e)



gen()