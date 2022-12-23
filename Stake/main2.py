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
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


url = """https://stake.com/casino/games/limbo"""


def sender(message, location):
    for i in range(0, len(message)):
        location.send_keys(message[i])
        sleep(0.1)
        # sleep(0.2)




def run(url, BET_AMOUNT, ON_LOSS, STOP_ON_PROFIT, TARGET, FAIRNESS):
    opt = uc.ChromeOptions()
    # opt.add_argument("--incognito")
    opt.add_argument(
        r"--user-data-dir=C:\Users\ka4ma\AppData\Local\Google\Chrome\User Data"
    )
    opt.add_argument(r"--profile-directory=Profile 1")
    try:
        driver = uc.Chrome(options=opt)
        driver.get(url)
        sleep(2)
        auto = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/button[2]',
                )
            )
        )
        auto.click()


        settings = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div[1]/div/button',
                )
            )
        )
        settings.click()

        sleep(1)
        try:
            animations = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '/html/body/div[4]/div/div/div[2]/div/button[2]',
                    )
                )
            )
            animations.click()



            instant = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '/html/body/div[4]/div/div/div[2]/div/button[1]',
                    )
                )
            )
            instant.click()
        except:
            animations = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '/html/body/div[3]/div/div/div[2]/div/button[2]',
                    )
                )
            )
            animations.click()



            instant = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '/html/body/div[3]/div/div/div[2]/div/button[1]',
                    )
                )
            )
            instant.click()





        bet_amount = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/label[1]/div/div[1]/input',
                )
            )
        )
        sender(BET_AMOUNT, bet_amount)






        on_loss_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div[3]/div/div/button[2]',
                )
            )
        )
        print("CLICKING on loss")
        on_loss_button.click()



        on_loss = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div[3]/div/label/div/div/input',
                )
            )
        )
        sender(ON_LOSS, on_loss)






        stop_on_profit = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/div[4]/label/div[1]/div/input',
                )
            )
        )
        sender(STOP_ON_PROFIT, stop_on_profit)



        target = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/div/div[3]/label[1]/div/div/input',
                )
            )
        )
        sender(TARGET, target)




        start_bet = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/button',
                )
            )
        )
        print("STARTED BETTING")
        start_bet.click()


        MONEY = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/div/div[2]/span',
                )
            )
        )



        TOTAL = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div[3]/button',
                )
            )
        )
        TOTAL.click()





        Fairy = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/button',
                )
            )
        )
        Fairy.click()
        fairness = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/button',
            )
        )
    )
        fairness.click()
        print("CLICKED")








        counter = 1
        flag = 0
        while 1:
            try:
                MONEY = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/div/div[2]/span',
                    )
                )
            )

                rgba = MONEY.value_of_css_property('color')
                rgba = rgba[5:-4]
                red,green,blue = rgba.split(',')
                red, green, blue = int(red), int(green), int(blue)

                if red == 255 and green == 255 and blue == 255:
                    flag = 0
                elif green == 231 and flag == 0:
                    # print('green')
                    counter = 1
                    flag = 1
                    print('BROKE')
                    break


                    CHANGE_SEED = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[3]/div[2]/div[4]/form/label/div/div[2]/button',
                        )
                    )
                )
                    CHANGE_SEED.click()
                    close2 = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[3]/div[2]/div[1]/button',
                        )
                    )
                )
                    close2.click()


                    stop_win = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/button',
                        )
                    )
                )
                    stop_win.click()
                    sleep(1)

                    bet_amount = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/label[1]/div/div[1]/input',
                        )
                    )
                )
                    sender(BET_AMOUNT, bet_amount)



                    sleep(2)
 
                    start_again = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/button',
                        )
                    )
                )
                    start_again.click()
                    sleep(1)


                    fairness = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/button',
                        )
                    )
                )
                    fairness.click()
                    sleep(1)




                    

                elif red == 254 and flag == 0:
                    flag = 1
                    # print('red')
                    print(counter)
                    counter = counter + 1

                if counter >= int(FAIRNESS)+1:
                    counter = 1
                    CHANGE_SEED = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[3]/div[2]/div[4]/form/label/div/div[2]/button',
                        )
                    )
                )
                    CHANGE_SEED.click()
                try:
                    error = driver.find_element_by_xpath('//*[@id="svelte"]/div[1]/div[2]/div[2]/div/div/div/button')
                    if error != None:
                        close = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH,
                                '//*[@id="svelte"]/div[1]/div[2]/div[1]/button',
                            )
                        )
                    )
                        close.click()
                        sleep(2)
                        close2 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH,
                                '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[3]/div[2]/div[1]/button',
                            )
                        )
                    )
                        close2.click()


                    #     stop_win = WebDriverWait(driver, 5).until(
                    #     EC.presence_of_element_located(
                    #         (
                    #             By.XPATH,
                    #             '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/button',
                    #         )
                    #     )
                    # )
                    #     stop_win.click()
                    #     sleep(1)



                        sleep(2)
     
                        start_again = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH,
                                '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div[1]/button',
                            )
                        )
                    )
                        start_again.click()
                        sleep(1)


                        fairness = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (
                                By.XPATH,
                                '//*[@id="scrollable"]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/button',
                            )
                        )
                    )
                        fairness.click()
                        sleep(1)
                        
                        
                        print("There was an error which was solved")

                except:
                    pass

            except:
                pass

        driver.close()
        return 1
    except Exception as e:
        driver.close()
        print(e)




if __name__ == "__main__":
    with open('config.txt', 'r') as f:
        LINES = f.readlines()
        bet_amount = LINES[2].strip()
        on_loss = LINES[6].strip()
        stop_on_profit = LINES[10].strip()
        target = LINES[14].strip()
        fairness = LINES[18].strip()

    print(bet_amount, on_loss, stop_on_profit, target, fairness)
    while 1:
        print('restaring')
        run(url,bet_amount, on_loss, stop_on_profit, target, fairness)

