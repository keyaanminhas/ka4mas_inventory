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




def splitstring(Total_Name):
    Total_Name = "".join([n for n in Total_Name if n in 'abcdefghijklmnopqrstuvwxyz'])
    first = ''
    last = ''
    for i in range(0,len(Total_Name)):
        if i <= len(Total_Name)//2-1:
            first = first + Total_Name[i]
        else:
            last = last + Total_Name[i]
    return first, last

def main(driver, NEW_EMAIL):
    sleep(1)
    signup = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/header/div[1]/div[2]/a[1]/span'))).click()
    new_email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[1]/onereg-alias/fieldset/onereg-progress-meter/div[2]/div[2]/div/pos-input[1]/input'))).send_keys(NEW_EMAIL)
    sleep(1)
    MR = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/div[1]/div/onereg-radio-wrapper[2]/pos-input-radio/label/i/span'))).click()
    sleep(0.5)
    FIRST_NAME, LAST_NAME = splitstring(NEW_EMAIL)
    First_Name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[1]/div/div[2]/pos-input/input'))).send_keys(FIRST_NAME)
    sleep(0.5)
    Last_Name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[2]/div/div[2]/pos-input/input'))).send_keys(LAST_NAME)
    sleep(0.5)
    Drop_Down1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/fieldset/onereg-form-row[2]/div/div/pos-input/select')))
    sleep(0.5)
    Drop_Down2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/fieldset/onereg-form-row[1]/div/div/pos-input/select')))

    dropdown1 = Select(Drop_Down2)
    sleep(0.5)
    dropdown2 = Select(Drop_Down1)

    Month = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[1]/input'))).send_keys(f'0{str(random.randint(0, 9))}')
    sleep(0.5)
    Year = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[3]/input'))).send_keys(f'199{str(random.randint(0, 9))}')
    sleep(0.5)
    Day = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[2]/input'))).send_keys(f'{random.randint(0, 2)}{str(random.randint(0, 9))}')
    sleep(0.5)
    dropdown1.select_by_visible_text("United States of America")
    dropdown2.select_by_visible_text('California')

    sleep(0.5)
    Password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[4]/onereg-password/fieldset/onereg-progress-meter/onereg-form-row[1]/div/div/pos-input/input'))).send_keys(NEW_EMAIL)
    sleep(0.5)
    rePassword = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[4]/onereg-password/fieldset/onereg-progress-meter/onereg-form-row[2]/div/div/pos-input/input'))).send_keys(NEW_EMAIL)

    sleep(0.5)
    sms = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[5]/onereg-password-recovery/fieldset/onereg-progress-meter/div[3]/onereg-checkbox-wrapper/pos-input-checkbox/label/span'))).click()
    sleep(0.5)
    email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[5]/onereg-password-recovery/fieldset/onereg-progress-meter/div[4]/onereg-checkbox-wrapper/pos-input-checkbox/label/span'))).click()

    sleep(0.5)
    contact = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[5]/onereg-password-recovery/fieldset/onereg-progress-meter/onereg-form-row[2]/div/div[2]/pos-input/input'))).send_keys('ka4ma777@gmail.com')


    iframe = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/onereg-app/div/onereg-form/div/div/form/section/section[6]/onereg-terms-and-conditions/onereg-progress-meter/fieldset/onereg-captcha/div/onereg-recaptcha/fieldset/div/div/div/iframe')))
    driver.switch_to.frame(iframe)

    sleep(0.5)
    captcha = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]'))).click()

    driver.switch_to.default_content()

    try:
        iframe2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[4]/iframe')))
        driver.switch_to.frame(iframe2)

        sleep(0.5)
        solver = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'solver-button'))).click()

        sleep(5)
        driver.switch_to.default_content()
    except:
        pass
    input("DONE")

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
    driver.get('https://www.mail.com/')
    NEW_EMAIL = 'karmaaccount123'
    main(driver, NEW_EMAIL)