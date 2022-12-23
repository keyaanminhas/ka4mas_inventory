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
import requests
import threading
from datetime import date





def get_config(filename):
	with open(filename, 'r') as f:
		x = f.readlines()
		z = [y.strip() for y in x if y.strip()!='']

	file = z[1]
	API_KEY = z[3]
	COUNTRY_CODE = z[5]
	SERVICE_CODE = z[7]
	SCREEN = z[9]
	GAP = z[11]
	print(file, API_KEY, COUNTRY_CODE, SERVICE_CODE, SCREEN, GAP)
	return file, API_KEY, COUNTRY_CODE, SERVICE_CODE, SCREEN, GAP


def get_price(API_KEY, COUNTRY_CODE, SERVICE_CODE):
	method = 'get_service_price'
	resp = requests.get(f'https://smspva.com/priemnik.php?metod={method}&country={COUNTRY_CODE}&service={SERVICE_CODE}&apikey={API_KEY}')
	data = resp.json()
	return data['price']




def get_number(API_KEY, COUNTRY_CODE, SERVICE_CODE):
	method = 'get_number'
	resp = requests.get(f'https://smspva.com/priemnik.php?metod={method}&country={COUNTRY_CODE}&service={SERVICE_CODE}&apikey={API_KEY}', verify = False)
	data = resp.json()
	return data['response'], data['number'], data['id']


def get_messages(API_KEY, COUNTRY_CODE, SERVICE_CODE, idd):
	method = 'get_sms'
	resp = requests.get(f'https://smspva.com/priemnik.php?metod={method}&country={COUNTRY_CODE}&service={SERVICE_CODE}&id={idd}&apikey={API_KEY}', verify = False)
	data = resp.json()
	return data['response'], data['number'], data['sms']


def instance(API_KEY, COUNTRY_CODE, SERVICE_CODE, idd, number, HEADLESSS, GAP):	
	while 1:
		try:
			with open("names.txt",'r+') as file:
				lines = file.readlines()

				file.seek(0)
				file.truncate()

				file.writelines(lines[1:])
			NAME = lines[0]
			NAME = NAME.strip()
			FIRST_NAME, LAST_NAME = NAME.split(' ')
			EMAIL = FIRST_NAME + LAST_NAME + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + '@gmail.com'
			PASSWORD = '@' + FIRST_NAME + LAST_NAME + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

			print(FIRST_NAME, LAST_NAME,EMAIL, PASSWORD)
			break
		except:
			pass


	opt = uc.ChromeOptions()
	while 1:
		try:
			uc.TARGET_VERSION = 108
			uc.install(executable_path='chromedriver.exe')
			if HEADLESSS.lower() == 'yes':
				opt.add_argument('--headless')
			opt.add_experimental_option("excludeSwitches", ["enable-logging"])
			opt.add_argument('--start-maximized')
			driver = uc.Chrome(options=opt)
			sleep(3)
			break
		except Exception as e:
			print("ERROR CAME, LEAVING", e)
			exit()

	driver.get(r'https://deliveroo.fr/fr/login?redirect=%2Ffr%2F')

	try:
		sign_up = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'continue-with-email'))).click()

		email_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email-address')))
		email_box.send_keys(EMAIL)
		sleep(0.2)
		email_box.send_keys(Keys.ENTER)


		number_here = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'phone_number')))
		number_here.send_keys(number)
		number_here.send_keys(Keys.ENTER)





		success = 0
		count = 0
		while success != '1' and count!=25:
			sleep(int(GAP))
			success, number, sms = get_messages(API_KEY, COUNTRY_CODE, SERVICE_CODE, idd)
			count = count + 1

		if sms == None:
			return 'NO SMS CAME'

		print(sms)


		phone_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'phone_code')))
		phone_code.send_keys(sms)
		phone_code.send_keys(Keys.ENTER)







		first_name_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'firstName')))
		first_name_box.send_keys(FIRST_NAME)

		last_name_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'lastName')))
		last_name_box.send_keys(LAST_NAME)
		


		password_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
		password_box.send_keys(PASSWORD)

		sleep(1)

		mainframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]')))
		buttonsss = mainframe.find_elements(By.TAG_NAME, 'button')
		sleep(1)
		driver.execute_script("arguments[0].click();", buttonsss[0]) 

		today = date.today()
		d1 = today.strftime("%d/%m/%Y")

		with open('accounts.txt', 'a') as f:
			f.write(EMAIL +':' + PASSWORD + ' ' + str(d1) + '\n')


		page_load = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'location-search')))
		sleep(2)
		driver.close()
	except Exception as e:
		print(e)
		try:
			driver.close()
		except:
			pass


	


def create(file, API_KEY, COUNTRY_CODE, SERVICE_CODE, screen, num, acc_to_create, GAP):

	num = num + 1
	success = 0
	while success != '1':
		success, number, idd = get_number(API_KEY, COUNTRY_CODE, SERVICE_CODE)
		try:
			print(success, number, idd)
		except Exception as e:
			print(e)
		sleep(int(GAP))

	instance(API_KEY, COUNTRY_CODE, SERVICE_CODE, idd, number, screen, GAP)
	if str(num) == str(acc_to_create):
		print('INSTANCE COMPLETE')
		return 'done'
	else:
		create(file, API_KEY, COUNTRY_CODE, SERVICE_CODE, screen, num, acc_to_create, GAP)







def main():
	instances = input('NUMBER OF INSTANCES: ')
	acc_to_create = input('NUMBER OF ACCOUNTS PER INSTANCE: ')
	
	print('\n')
	file, API_KEY, COUNTRY_CODE, SERVICE_CODE, screen, GAP = get_config('config.txt')
	input('PRESS ENTER TO START')
	print('\n\n\n')


	for i in range(0, int(instances)):
		num = 0
		x = threading.Thread(target=create, args=(file, API_KEY, COUNTRY_CODE, SERVICE_CODE, screen, num, acc_to_create, GAP))
		x.start()
		sleep(4)
			
				

main()