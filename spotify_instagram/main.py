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
    sleep(1)

    path = x[0].strip()
    profile = path.split("\\", -2)
    PROFILE = profile[-1]
    DATA_DIRECTORY = path[0:len(path)-len(profile) -1]
    print("[+] " + PROFILE)
    print("[+] " + DATA_DIRECTORY)
    playlist = x[1].strip()
    print("[+] PLAYLIST: " + playlist)
    print("[!] 3")
    sleep(1)
    print("[!] 2")
    sleep(1)
    print('[!] 1')
    sleep(1)
    print("OPENING CHROME")
    return PROFILE, DATA_DIRECTORY, playlist


def instagram(driver, artist, track):
    try:
        driver.switch_to.window(driver.window_handles[-1])
        sleep(1)
        buttons = driver.find_elements(By.TAG_NAME, 'button')
        while len(buttons) == 0:
            buttons = driver.find_elements(By.TAG_NAME, 'button')
        for button in buttons:
            sleep(0.4)
            if button.text == 'Follow':
                button.click()
        sleep(1.5)
        buttons = driver.find_elements(By.TAG_NAME, 'button')
        for button in buttons:
            if button.text == 'Message':
                button.click()
                message_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
                with open('message.txt', 'r') as f:
                    x = f.readlines()
                for line in x:
                    new_line = line.strip()
                    new_line = new_line.replace('<SONGNAME>', track)
                    new_line = new_line.replace('<ARTISTNAME>', artist)
                    sender(new_line, message_box)
                    message_box.send_keys(Keys.RETURN)
                    sleep(0.3)
                break
    except:
        print("Incorrect instagram link")
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])


def song_action(driver, song):
    #driver.execute_script("arguments[0].scrollIntoView();", song)
    #song.click()
    a = ActionChains(driver)
    a.move_to_element(song).perform()
    track = ((song.text).split('\n'))[0]
    like = song.find_elements(By.TAG_NAME, 'button')
    for i in like:
        if str(i.get_attribute('aria-label')) == "Save to Your Library":
            i.click()
            links = song.find_elements(By.TAG_NAME, 'a')
            for link in links:
                href = link.get_attribute('href')
                if href[:31] == 'https://open.spotify.com/artist':
                    artist = link.text
                    driver.execute_script(f"window.open('{href}', '_blank')")
                    driver.switch_to.window(driver.window_handles[-1])
                    sleep(3)
                    button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[2]/div[4]/div/div/div/div/button[1]')))
                    if button.text == 'FOLLOW':
                        button.click()
                        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')
                        sleep(1.5)
                        about = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[2]/div[3]/div[2]/div[1]/div/button')))
                        about.click()

                        sleep(2)
                        socials = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[16]/div/div')))
                        all_socials= socials.find_elements(By.TAG_NAME, 'a')
                        insta_found = False
                        for social in all_socials:
                            if social.get_attribute('href').find('instagram') != -1:
                                insta_found = True
                                social.click()
                                instagram(driver, artist, track)
                                break
                        if insta_found == False:
                            driver.close()
                            driver.switch_to.window(driver.window_handles[-1])
                            print(f"{artist} DOESNT HAVE AN INSTAGRAM")
                    else:
                        print(f"ALREADY FOLLOWING {artist}")
                        driver.close()
                        driver.switch_to.window(driver.window_handles[-1])
                    



def main():
    PROFILE, DATA_DIRECTORY, playlist = get_config('config.txt')
    opt = uc.ChromeOptions()
    opt.add_argument(
        rf"--user-data-dir={DATA_DIRECTORY}"
    )
    opt.add_argument(rf"--profile-directory={PROFILE}")
    while 1:
        try:
            uc.TARGET_VERSION = 103
            uc.install(executable_path='chromedriver.exe')
            #opt.add_argument('--headless')
            opt.add_argument('--start-maximized')
            driver = uc.Chrome(options=opt)
            sleep(4)
            break
        except Exception as e:
            print("ERROR CAME, Trying again")
    driver.get(playlist)
    try:
        song_container = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]')))
    except:
        print("COULDNT FIND CONTAINER")
        exit()
    try:
        limit = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[1]/div[5]/div/span[2]')))
    except:
        limit = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[1]/div[5]/div/span')))
        
    temp1 = limit.text
    song_number = int(temp1.split(' ')[0])
    all_songs = []
    count = 0
    while len(all_songs) != song_number:
        sleep(2)
        songs = song_container.find_elements(By.XPATH, "./child::*")
        for i in songs:
            if i not in all_songs:
                all_songs.append(i)
                song_action(driver, i)
                count += 1
        sleep(0.5)
    input('[+] COMPLETED PLAYLIST')


main()