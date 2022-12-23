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





def sender(message, location):
    for i in range(0,len(message)):
        location.send_keys(message[i])
        sleep(0.07)
        # sleep(0.2)



def get_config(filename):
    with open(filename, 'r') as f:
        x = f.readlines()
        z = [y.strip() for y in x if y.strip()!='']
    path = z[1].strip()
    profile = path.split("\\", -2)
    PROFILE = profile[-1]
    DATA_DIRECTORY = path[0:len(path)-len(profile) -1]
    messages_file = z[3]
    people_file = z[5]
    version = z[7]
    timesleep = z[9]
    time1, time2 = timesleep.split('-')

    return PROFILE, DATA_DIRECTORY, messages_file, people_file, version, time1, time2



def instance(driver, username, message, time1, time2):
    sleeptimer = random.randint(int(time1),int(time2))
    print('SLEEPING FOR', sleeptimer)
    sleep(sleeptimer)
    print(f"""
{username}:
{message}

""")
    url = 'https://www.instagram.com/' + username
    driver.get(url)
    sleep(1.5)
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    done = False
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    comp = False
    while 1:
        for button in buttons:
            if button.text == 'Message':
                button.click()
                comp =True
                break
        if comp == True:
            break

    while done == False:
        try:
            message_box = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Message...']")))
            break
        
        except:
            try:
                message_box = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
                break
            except:
                pass
    message = message.replace('<USERNAME>', username)
    sender(message, message_box)
    message_box.send_keys(Keys.RETURN)
    sleep(0.3)



def main():
    PROFILE, DATA_DIRECTORY, messages_file, people_file, version, time1, time2 = get_config('config.txt')
    print("[+] " + PROFILE)
    print("[+] " + DATA_DIRECTORY)
    print("[+] " + messages_file)
    print("[+] " + people_file)
    print("[+] " + version)

    print('\n\n[+] PRESS ENTER TO START')
    input('')
    print('\n[!] STARTED...')
    sleep(1)
    with open(people_file, 'r') as f:
        x = f.readlines()
        peoples = [y.strip() for y in x if y.strip()!='']
    with open(messages_file, 'r') as f:
        x = f.readlines()
        messages = [y.strip() for y in x if y.strip()!='']

    opt = uc.ChromeOptions()
    opt.add_argument(
        rf"--user-data-dir={DATA_DIRECTORY}"
    )
    opt.add_argument(rf"--profile-directory={PROFILE}")
    while 1:
        try:
            uc.TARGET_VERSION = version
            uc.install(executable_path='chromedriver.exe')
            #opt.add_argument('--headless')
            opt.add_argument('--start-maximized')
            driver = uc.Chrome(options=opt)
            sleep(4)
            break
        except Exception as e:
            print("ERROR CAME, Trying again")

    for username in peoples:
        instance(driver, username, random.choice(messages), time1, time2)


main()
