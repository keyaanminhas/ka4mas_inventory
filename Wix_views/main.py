#IMPORTING LIBRARIES THAT ARE GOING TO BE USED

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import random
from selenium.common.exceptions import TimeoutException
import threading
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options



instances = int(input('PLEASE ENTER THE NUMBER OF INSTANCES YOU WISH TO CREATE:   '))


with open('config.txt') as f:
	x = f.readlines()
	z = [y.strip() for y in x if y.strip()!='']





url = (z[1])

chromedriver_autoinstaller.install()


def instance(url):
	chrome_options = Options() 
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--incognito")
	driver = webdriver.Chrome(options = chrome_options)
	driver.get(url)
	found = False

	sleep(3)
	while found != True:
		try:

			like_button = driver.find_element(By.XPATH, '/html/body/div/div/div[4]/div/main/div/div/div/div[2]/div/div/div/section/div[2]/div/div/div/div/div/div/div[4]/div[2]/div/div[2]/div/div[1]/div[1]/article/div/div[3]/div/div[4]/button/span[2]/div')
			actions = ActionChains(driver)
			actions.move_to_element(like_button).perform()
			sleep(0.5)
			like_button.click()
			found = True
		except Exception as e:
			print(e)
	sleep(1)
	driver.close()
	instance(url)

for number in range(0, instances):
	x = threading.Thread(target=instance, args=(url,))
	x.start()
