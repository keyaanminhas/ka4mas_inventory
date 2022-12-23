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
		#sleep(0.07)
		# sleep(0.2)



def get_config(filename):
	with open(filename, 'r') as f:
		x = f.readlines()
		z = [y.strip() for y in x if y.strip()!='']

	version = z[1]
	account_number = z[3]
	username = z[5]
	password = z[7]
	number_to_send = z[9]
	accpeted_shippers = z[11]
	accepted_origincity = z[13]

	return version, account_number, username, password, number_to_send, accpeted_shippers, accepted_origincity



def login(driver, account_number, username, password):
	account_number_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'f_accountNumber')))
	sender(account_number, account_number_box)
	sleep(0.4)

	username_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'f_username')))
	sender(username, username_box)
	sleep(0.3)

	password_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'f_password')))
	sender(password, password_box)
	sleep(0.4)

	SUBMIT = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'f_btn2'))).click()

def execution(driver):
	driver.get('https://kewilltransport.net/tms/servlet/Execution')

def tenders(driver):
	tenders_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/table/tbody/tr/td[3]'))).click()

def ordering(driver, number_to_send, accepted_shippers, accepted_origincity):
	accepted_shippers = accepted_shippers.replace(' ', '')
	all_shippers = accepted_shippers.split(',')
	accepted_origincity = accepted_origincity.replace(' ', '')
	all_cities = accepted_origincity.split(',')
	print(all_shippers, all_cities)

	go_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'f_btn3'))).click()

	container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/table[1]/tbody/tr[3]/td/table/tbody/tr[3]/td[1]/table/tbody/tr[1]/td/div/table/tbody')))
	orders = container.find_elements(By.XPATH, "./child::*")
	amount = len(orders)
	
	while amount <2:
		# print(amount)
		go_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'f_btn3'))).click()

		container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/table[1]/tbody/tr[3]/td/table/tbody/tr[3]/td[1]/table/tbody/tr[1]/td/div/table/tbody')))
		orders = container.find_elements(By.XPATH, "./child::*")
		amount = len(orders)
		sleep(2)
	for i in range(1, amount):
		tds = orders[i].find_elements(By.TAG_NAME, 'td')
		city = tds[12].text
		shipper = tds[25].text
		if (city in all_cities) and (shipper in all_shippers):
			orders[i].click()
			print('yes')
			sleep(0.5)
			accept = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/table[1]/tbody/tr[3]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[1]/td/input'))).click()
			driver.switch_to.frame("pF1")
			
			ref_num = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'f_referenceNumber')))
			sender(number_to_send, ref_num)
			sleep(1)
			accepting = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr/td/form/table[3]/tbody/tr/td/input[2]'))).click()
			sleep(2)
			return

	



def instance(driver, account_number, username, password, number_to_send, accepted_shippers, accepted_origincity):
	url = 'https://kewilltransport.net'
	driver.get(url)
	driver.switch_to.frame("_sliverFrame")
	sleep(0.5)
	driver.switch_to.frame("MAIN")
	login(driver, account_number, username, password)
	while 1:
		execution(driver)
		sleep(0.5)
		driver.switch_to.frame("_sliverFrame")
		sleep(0.5)
		driver.switch_to.frame("_work")
		tenders(driver)
		sleep(1)
		ordering(driver, number_to_send, accepted_shippers, accepted_origincity)
def main():
	version, account_number, username, password, number_to_send, accepted_shippers, accepted_origincity = get_config('config.txt')
	print("[+] " + version)
	print("[+] " + account_number)
	print("[+] " + username)
	print("[+] " + password)
	print("[+] " + number_to_send)


	print('\n\n[+] PRESS ENTER TO START')
	input('')
	print('\n[!] STARTED...')
	sleep(1)
	opt = uc.ChromeOptions()
	# opt.add_argument(
	# 	rf"--user-data-dir={DATA_DIRECTORY}"
	# )
	# opt.add_argument(rf"--profile-directory={PROFILE}")
	while 1:
		try:
			uc.TARGET_VERSION = 105
			uc.install(executable_path='chromedriver.exe')
			#opt.add_argument('--headless')
			opt.add_argument('--start-maximized')
			driver = uc.Chrome(options=opt)
			sleep(4)
			break
		except Exception as e:
			print("ERROR CAME, Trying again")

	instance(driver, account_number, username, password, number_to_send, accepted_shippers, accepted_origincity)
main()