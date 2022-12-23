import undetected_chromedriver as uc
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
import ssl

ssl._create_default_https_context = ssl._create_unverified_context




def instance(driver, url):
    sleep(6)
    count = 0 
    while True:
        try:
            driver.get(url)
            break
        except:
            continue
    sleep(5)
    latest_item_name = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]/div[2]/div/div[2]/a')))
    current = latest_item_name.text
    print(current)
    with open('already.txt', 'r') as f:
        x = f.readlines()
    flag = False
    for i in x:
        done = i.strip()
        if current == done:
            flag = True
            break
    if flag == False:
        sleep(4)
        latest_item_name.click()
        sleep(4)
        done = False
        more_info = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
        buttons = driver.find_elements(By.TAG_NAME,'button')
        done = False
        for button in buttons:
            if button.text == 'Inserent kontaktieren':
                button.click()
                done = True
                break
        if done == False:
            more_info = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
            buttons = driver.find_elements(By.TAG_NAME, 'button')
            done = False
            for button in buttons:
                if button.text == 'Inserent kontaktieren':
                    button.click()
                    done = True
                    break
        
        if done == False:
            print("No direct contact")
        else:
            send_here = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="quickReplyWrapper"]/div[1]/textarea')))
            with open('message.txt', 'r') as f:
                x = f.read()
            send_here.send_keys(x)
            sleep(0.3)
            send_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[1]/div/div[2]/div[2]/form/div[5]/div[2]/button')))
            sleep(1)
            send_button.click()
            count = count + 1
            with open('already.txt', 'w') as b:
                b.write(current + '\n')
        if count > 9:
            os.system('sudo pkill -a -i "Google Chrome"')
            return 1



if __name__ == '__main__':
    sleep(1)
    opt = uc.ChromeOptions()
    with open('config.txt', 'r') as f:
        x = f.readlines()
    path = x[0].strip()
    profile = path.split("/", -2)
    PROFILE = profile[-1]
    DATA_DIRECTORY = path[0:len(path)-len(profile) -2]
    print(PROFILE)
    print(DATA_DIRECTORY)

    opt.add_argument(
        rf"--user-data-dir={DATA_DIRECTORY}"
    )
    opt.add_argument(rf"--profile-directory={PROFILE}")
    while 1:
        try:
            print("RUNNING")
            #opt.add_argument('--headless')
            opt.add_argument('--start-maximized')
            driver = uc.Chrome(options=opt)
            sleep(3)
            break
        except Exception as e:
            print("ERROR CAME, Trying again", e)
    url = "https://www.tutti.ch/de/li/ganze-schweiz/gratis?organic=true"
    while 1: 
        instance(driver, url)