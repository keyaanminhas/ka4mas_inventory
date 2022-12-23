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
from ctypes import*
from ctypes.wintypes import *
import win32, win32com
import threading
import win32api
import win32con


file = open('data.txt', 'r')
data = file.read()
file.close()

#DATA

data = data.split('\n')
Ax, Ay = float(data[0]), float(data[1])
Bx, BBy = float(data[2]), float(data[3])
Cx, Cy = float(data[4]), float(data[5])
cycle_time = float(data[6])/1000
increase = float(data[7])
decrease = float(data[8])
extra_amount = float(data[9])
extra_percentage = float(data[10])
holding_time = float(data[11])/1000


flag = False


#CODE


def leftClick(x,y):
    global flag
    flag1 = flag
    while flag1 != False:
        sleep(0.1)

    flag = True

    x,y = int(abs(x)), int(abs(y))
    windll.user32.SetCursorPos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    sleep(holding_time)
    flag = False


def run(url):
    global flag
    opt = uc.ChromeOptions()
    opt.add_argument("--headless")
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    flag = False
    uc.TARGET_VERSION = 102
    uc.install(executable_path="chromedriver.exe",)
    driver = uc.Chrome(options=opt)
    driver.get(url)
    sleep(2)
    auto = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="spotOrderbook"]/div[3]/div[2]/div[2]',
                )
            )
    )
    btcprice = auto.text
    price1 = btcprice.replace('$', '')
    price = price1.replace(',', '')
    price = float(price)
    old_price = price
    lowest_extra_price = ((price + increase) - extra_amount) + ((extra_percentage/100) * extra_amount)
    extra_price = lowest_extra_price
    while 1:
        sleep(cycle_time)
        auto = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="spotOrderbook"]/div[3]/div[2]/div[2]',
                )
            )
        )
        btcprice = auto.text
        price1 = btcprice.replace('$', '')
        price = price1.replace(',', '')
        price = float(price)
        if ((float(price)) - (float(old_price))) > increase :
            print('A CLICKED', price - old_price)
            x = threading.Thread(target=leftClick(Ax, Ay))
            x.start()
            x = threading.Thread(target=leftClick(Cx, Cy))
            x.start()
        elif ((float(price)) - (float(old_price))) < (-decrease):
            print('B CLICKED', price - old_price)
            x = threading.Thread(target=leftClick(Bx, BBy))
            x.start()
            x = threading.Thread(target=leftClick(Cx, Cy))
            x.start()
        if price >= extra_price:
            x = threading.Thread(target=leftClick(Cx, Cy))
            x.start()
            extra_price = ((price - lowest_extra_price) * extra_percentage/100) + lowest_extra_price



        if price <= extra_price:
            x = threading.Thread(target=leftClick(Cx, Cy))
            x.start()
                extra_price = price - ((price - extra_price) * extra_percentage/100)
        old_price = price



if __name__ == "__main__":
    url = 'https://www.binance.com/en/trade/BTC_BUSD?theme=dark&type=spot'
    run(url)