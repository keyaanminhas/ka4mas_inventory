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
import undetected_chromedriver as uc


url = """https://stake.com/casino/games/limbo"""


def sender(message, location):
    for i in range(0, len(message)):
        location.send_keys(message[i])
        sleep(0.1)
        # sleep(0.2)


opt = uc.ChromeOptions()
opt.add_argument("--incognito")


def run(url, USERNAME, PASSWORD):
    try:
        driver = uc.Chrome(options=opt)
        driver.get(url)

        login = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[3]/button[1]",
                )
            )
        )
        login.click()

        sleep(1)

        username = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div/form/label[1]/div/div[1]/input",
                )
            )
        )
        sender(USERNAME, username)
        sleep(0.2)

        password = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div/form/label[2]/div/div[1]/input",
                )
            )
        )
        sender(PASSWORD, password)

        signin = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div/form/button",
                )
            )
        )
        signin.click()
        sleep(2)

        input()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    username = "ka4ma777"
    password = "@Keyaan786"
    run(url, username, password)
