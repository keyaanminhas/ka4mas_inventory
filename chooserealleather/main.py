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





def main():
    while 1:
        try:
            sleep(3)
            uc.install(executable_path='chromedriver.exe')
            opt = uc.ChromeOptions()
            opt.add_argument("--incognito")
            driver = uc.Chrome(options = opt)
            sleep(1)
            

            driver.get('https://chooserealleather.com/international-competition/#/project/data-migration')
            popup = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.ID, "close-welcome")
            )
        )
            sleep(1)
            count = 0
            while 1:
                count = count + 1
                try:
                    if count == 10:
                        break
                    popup.click()
                    break
                except:
                    sleep(1)
            sleep(1)
            buttons = driver.find_elements(By.TAG_NAME, 'button')
            clicked = False
            for i in buttons:
                if i.text == "Vote for this project":
                    actions = ActionChains(driver)
                    actions.move_to_element(i).perform()
                    i.click()
                    clicked = True
                    print("VOTED")
            buttons = driver.find_elements(By.TAG_NAME, 'button')
            for i in buttons:
                if i.text == "Vote for this project":
                    i.click()
                    clicked = True
                    print("VOTED")
            if clicked == False:
                print("ALREADY VOTED")
            sleep(1)
            driver.close()
            sleep(1)
        except:
            driver.close()
            sleep(3)
if __name__ == '__main__':
    sleep(1)
    main()