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
import requests


def get_proxies():
    req = requests.get(
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
    )
    raw_proxies = req.text
    proxies = raw_proxies[:-1].split("\n")

    return proxies


def get_proxy_v2():
    req = requests.get(
        "https://proxylist.geonode.com/api/proxy-list?limit=100&page=1&sort_by=lastChecked&sort_type=desc&speed=fast"
    )
    response = req.json()
    response = response["data"]
    proxies = []
    for i in response:
        if len((i["protocols"])) == 1:
            protocol = (i["protocols"])[0]
            ip = i["ip"]
            port = i["port"]
            proxies.append(f"{protocol}://{ip}:{port}")
        else:
            pass
    return proxies


url = (
    """https://account.proton.me/signup?plan=free&billing=12&currency=EUR&language=en"""
)


def splitstring(name):
    first = ""
    last = ""
    for i in range(0, len(Total_Name)):
        if i <= len(Total_Name) // 2 - 1:
            first = first + Total_Name[i]
        else:
            last = last + Total_Name[i]
    return first, last


def sender(message, location):
    for i in range(0, len(message)):
        location.send_keys(message[i])
        sleep(0.1)
        # sleep(0.2)


def run(url, EMAIL, PASSWORD, FIRST_NAME, LAST_NAME, PROXY):
    try:
        opt = uc.ChromeOptions()
        opt.add_argument("--incognito")
        opt.add_argument(f"--proxy-server={PROXY}")
        driver = uc.Chrome(options=opt)

        driver.get(url)

        sleep(10)

        iframe = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/iframe",
                )
            )
        )
        driver.switch_to.frame(iframe)

        email = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        sender(EMAIL, email)

        driver.switch_to.parent_frame()

        password = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/label[1]/div[2]/div/div[1]/input",
                )
            )
        )
        sender(PASSWORD, password)

        sleep(2)

        re_password = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/label[2]/div[2]/div/div[1]/input",
                )
            )
        )
        sender(PASSWORD, re_password)

        sleep(2)

        next_button3 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[3]/div[1]/div/main/div[2]/form/button",
                )
            )
        )
        next_button3.click()

        sleep(2)
        iframe2 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[3]/div/div/main/div[2]/div/div[2]/iframe",
                )
            )
        )
        driver.switch_to.frame(iframe2)

        print("SWITCHED")
        sleep(1)

        iframe3 = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/iframe"))
        )
        driver.switch_to.frame(iframe3)

        print("SWITCHED")
        sleep(1)

        captcha = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "checkbox"))
        )
        captcha.click()

        sleep(2)

        FINAL = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[3]/div/div/main/div[2]/form/button")
            )
        )
        FINAL.click()
        with open("gen.txt", "a") as f:
            f.write(f"{EMAIL} {PASSWORD}")
        sleep(5)
        driver.close()
    except:
        driver.close()
        print("FAILED")


if __name__ == "__main__":
    proxies = get_proxy_v2()
    for i in range(0, len(proxies)):
        run(
            url,
            f"hallamadrid{i}",
            "@Halla123",
            "Halla",
            "Madrid",
            proxies[i],
        )
