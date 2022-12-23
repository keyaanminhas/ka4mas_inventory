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





def get_config(filename):
	with open(filename, 'r') as f:
		x = f.readlines()
		z = [y.strip() for y in x if y.strip()!='']
	version = z[1]
	path = z[3]
	profile = path.split("\\", -2)
	PROFILE = profile[-1]
	DATA_DIRECTORY = path[0:len(path)-len(profile) -1]
	fine_date = z[5]
	fine_time = z[7]
	day_or_night = z[9]
	fine_amount = z[11]

	return version, PROFILE, DATA_DIRECTORY, fine_date, fine_time, day_or_night, fine_amount







def instance(driver, url, fine_date, fine_time, day_or_night, fine_amount):
	driver.get(url)
	add_trip_fine = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
	done = False
	while 1:
		sleep(1)
		add_trip_fine = driver.find_elements(By.TAG_NAME, 'button')

		for i in add_trip_fine:
			if i.text == "Add Trip Fine":
				sleep(0.5)
				i.click()
				done = True
				break
		if done == True:
			break





	REASON =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/div/div[1]/div/div/div')))
	REASON.click()


	PARKING_VOILATION = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[3]/ul/li[1]')))
	PARKING_VOILATION.click()

	DATE = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/div/div[3]/div/div/input')))
	DATE.click()


	selector = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'MuiPickersCalendar-week')))
	selector.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[1]/div/div[1]/div[2]/button/span[1]/h4').click()
	all_dates = driver.find_elements(By.CLASS_NAME, 'MuiPickersDay-day')
	for i in all_dates:
		if i.text == str(fine_date):
			i.click()
			break

	hr, mins = fine_time.split(':')

	all_hours = driver.find_elements(By.CLASS_NAME, 'MuiPickersClockNumber-clockNumber')
	for i in all_hours:
		if i.text == str(hr):
			action = ActionChains(driver)
			action.move_to_element(i).click().perform()
			break

	all_mins = driver.find_elements(By.CLASS_NAME, 'MuiPickersClockNumber-clockNumber')
	for i in all_mins:
		if i.text == str(mins):
			action = ActionChains(driver)
			action.move_to_element(i).click().perform()
			break

	if day_or_night == 'am':
		am_button = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[1]/div/div[3]/button[1]')
		action = ActionChains(driver)
		action.move_to_element(am_button).click().perform()
	elif day_or_night == 'pm':
		pm_button = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[1]/div/div[3]/button[2]')
		action = ActionChains(driver)
		action.move_to_element(pm_button).click().perform()


		
	ok_button = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[2]/button[2]').click()
	# for i in all_dates:
	# 	if i.text == '1':
	# 		DATE_BUTTON = i.find_element(By.TAG_NAME, 'button')
	# 		loc = DATE_BUTTON.location
	# 		sleep(1)
	# 	i.click()


	
	violation_amount = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/div/div[4]/div/div/input')))
	violation_amount.send_keys(fine_amount)

	violation_amount = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/div/div[5]/div/div/input')))
	violation_amount.send_keys('100')


	FINE_TRIP = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')))
	FINE_TRIP.click()
	
	add_trip_fine = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))

def main():
	version, PROFILE, DATA_DIRECTORY, fine_date, fine_time, day_or_night, fine_amount = get_config('config.txt')
	print("[+] VERSION NUMEBR:", version )
	print('[+] CHORME PROFILE', PROFILE)
	print('[+] CHROME DIRECTORY', DATA_DIRECTORY)
	# print('[+] PLAYER TO BUY:', player_name)
	# print('[+] MAX BUY NOW PRICE', max_buy_now)

	print('\n\n[+] PRESS ENTER TO START')
	input('')
	print('\n[!] STARTED...')
	sleep(1)
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

	with open('links.txt', 'r') as f:
		links = f.readlines()
	for link in links:
		code = instance(driver, link, fine_date, fine_time, day_or_night, fine_amount)
		sleep(1)
		if code == 'error':
			print("THERE WAS AN ERROR.")
	input("DONE WITH ALL")





main()