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
import re



def runner(driver):
    url = 'https://www.scottycameron.com/store/'
    driver.get(url)
    container = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div[3]/div/div/div/div/ul')))
    products = container.find_elements(By.XPATH, "./child::*")
    add_to_buttons = []
    for product in products:
        links = product.find_elements(By.TAG_NAME, 'a')
        for link in links:
            if link.text == 'ADD TO CART':
                add_to_buttons.append(link)
    button = random.choice(add_to_buttons)
    button.click()
    input()



if __name__ == '__main__':
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
    driver = uc.Chrome(options = opt)
    sleep(2)
    runner(driver)




