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
import undetected_chromedriver._compat as uc

from fake_useragent import UserAgent




instances = int(input('PLEASE ENTER THE NUMBER OF INSTANCES YOU WISH TO CREATE:   '))

chromedriver_autoinstaller.install()




def instance(url):

	#url = 'https://takipstar.com/giris'
	#url= 'https://www.takipciking.com/member' #works
	#url = 'https://takipcimx.net/login' #works
	#url = 'https://takipcizen.com/login' #works
	#url = 'https://bayitakipci.com/memberlogin' #doesnt work
	#url = 'https://fastfollow.in/member' #never ending
	#url = 'https://hepsitakipci.com/member' #works
	#url = 'https://birtakipci.com/member' #works
	#url = 'https://takip48.com/login' #works


	username = 'lifelife2023'
	password = '@lifelife2023'
	follow_me = 'automate4you'
	count = '150000'

	chrome_options = uc.ChromeOptions()
	while 1:
		try:
			uc.TARGET_VERSION = 103
			uc.install(executable_path='chromedriver.exe')
			#chrome_options.add_argument('--headless')
			chrome_options.add_argument("--incognito")
			ua = UserAgent()
			a = ua.random
			user_agent = ua.random
			chrome_options.add_argument(f'user-agent={user_agent}')
			driver = uc.Chrome(options=chrome_options)
			sleep(4)
			break
		except Exception as e:
			print("ERROR CAME, Trying again")

	#chrome_options.add_argument("--headless")
	driver.get(url)

	username_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
	password_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))


	username_box.send_keys(username)
	password_box.send_keys(password)

	login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login_insta'))).click()
	print(driver.current_url, '\n' , url)

	while driver.current_url == url:
		sleep(1)
	sleep(1)

	links = driver.find_elements(By.TAG_NAME, 'a')
	for i in links:
		try:
			if i.get_attribute('href').find('follower') != -1:
				sleep(2)
				i.click()
		except:
			pass
	sleep(2)

	follow_who = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.NAME, 'username')))
	follow_who.send_keys(follow_me)



	sleep(2)
	follow_who.send_keys(Keys.ENTER)
	sleep(3)
	increase_count = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.NAME, 'adet'))).send_keys(count)
	submit2 = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.ID, 'formTakipSubmitButton'))).click()


	sleep(1)
	sleep(150)
	driver.close()
	instance()

# for number in range(0, instances):
# 	x = threading.Thread(target=instance)
# 	x.start()
with open('links.txt', 'r') as f:
	links = f.readlines()
for i in links:
	print(i)
	instance(i)