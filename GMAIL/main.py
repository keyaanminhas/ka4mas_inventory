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
import threading








def sender(message, location):
	for i in range(0, len(message)):
		location.send_keys(message[i])
		sleep(0.1)
		# sleep(0.2)






def run(proxy=None, num =None):
	firstname = "karema"
	lastname = "access"
	username = f"{firstname + lastname + str(num)}"
	password = f"@{firstname + str(num)+ str(num)+ str(num)}" 
	url = "https://accounts.google.com/SignUp"
	print(username, password)
	global proxy_switch
	opt = uc.ChromeOptions()
	opt.add_argument("--incognito")
	if proxy_switch == 1:
		print(proxy)
		opt.add_argument("--proxy-server=%s" % proxy)
	driver = uc.Chrome(options=opt)
	driver.get(url)




	FIRST_NAME = WebDriverWait(driver, 30).until(
	EC.presence_of_element_located(
		(
			By.ID,
			'firstName',
		)
	)
)
	sender(firstname, FIRST_NAME)

	LAST_NAME = WebDriverWait(driver, 30).until(
	EC.presence_of_element_located(
		(
			By.ID,
			'lastName',
		)
	)
)
	sender(lastname, LAST_NAME)



	USERNAME = WebDriverWait(driver, 30).until(
	EC.presence_of_element_located(
		(
			By.ID,
			'username',
		)
	)
)
	sender(username, USERNAME)



	PASSWORD = WebDriverWait(driver, 30).until(
	EC.presence_of_element_located(
		(
			By.XPATH,
			'//*[@id="passwd"]/div[1]/div/div[1]/input',
		)
	)
)
	sender(password, PASSWORD)


	REPASSWORD = WebDriverWait(driver, 30).until(
	EC.presence_of_element_located(
		(
			By.XPATH,
			'//*[@id="confirm-passwd"]/div[1]/div/div[1]/input',
		)
	)
)
	sender(password, REPASSWORD)


	



	BUTTON = WebDriverWait(driver, 30).until(
	EC.presence_of_element_located(
		(
			By.XPATH,
			'//*[@id="accountDetailsNext"]/div/button',
		)
	)
).click()











	sleep(3)
	input()
	driver.close()














if __name__ == "__main__":
	instances = int(
		input("PLEASE ENTER THE NUMBER OF INSTANCES YOU WISH TO CREATE:   ")
	)
	with open("config/proxies.txt", "r") as handle:
		proxies = handle.readlines()
	global proxy_switch
	proxy_switch = int(input("PROXY TURNED ON '1', PROXY TURNED OFF '0':   "))
	i = 0
	while 1:
		for num in range(0, instances):
			x = threading.Thread(target=run, args=[proxies[i+num],i])
			x.start()
		run(proxies[i], i)
		i += 1
