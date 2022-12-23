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





url = 'file:///C:/Users/ka4ma/Downloads/wetransfer_pls-work_files_2022-06-04_2146/Pls%20work.html'






def sender(message, location):
    for i in range(0, len(message)):
        location.send_keys(message[i])
        sleep(0.1)
        # sleep(0.2)



def run(url):
    driver = uc.Chrome()
    input()
    one = Select(driver.find_element_by_xpath('//*[@id="EP_APPR_ITEM_REVIEW_RATING$4"]'))
    one.select_by_value('1')
    print('done')






if __name__ == '__main__':
    run(url)