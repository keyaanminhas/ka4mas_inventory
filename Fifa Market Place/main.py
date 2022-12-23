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
	path = z[3]
	profile = path.split("\\", -2)
	PROFILE = profile[-1]
	DATA_DIRECTORY = path[0:len(path)-len(profile) -1]
	list_price = z[5]
	delay = z[7]

	return version, PROFILE, DATA_DIRECTORY, list_price, delay



def instance(driver, list_price, delay):
	url = 'https://www.ea.com/fifa/ultimate-team/web-app/'
	driver.get(url)
	Transfer_window_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
	done = False
	while 1:
		sleep(1)
		Transfer_window_button = driver.find_elements(By.TAG_NAME, 'button')

		for i in Transfer_window_button:
			if i.text == "TRANSFERS":
				sleep(0.5)
				i.click()
				done = True
				break
		if done == True:
			break
	while 1:
		try:
			sleep(1)
			search_transfer_market = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[2]'))).click()
			break
		except:
			print('UNABLE TO FIND THE SEARCH IN THE TRANSFER MARKET BUTTON')


	input('ENTER PLAYER AND STUFF AND THEN PRESS ENTER TO CONTINUE')
	count = 0
	player_found = False
	while player_found == False:
		
		while 1:
			sleep(int(delay))
			try:
				search = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]'))).click()
				buy_now = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]'))).click()
				confirm = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/section/div/div/button[1]'))).click()
				list_it = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]/button'))).click()
				path_to_price = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input')))
				path_to_price.send_keys('a')
				sleep(1)
				sender(list_price, path_to_price)
				listed = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/button'))).click()

			except:
				try:
					no_players = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section/div/div[2]/div/h2')))
					back = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[1]/button[1]'))).click()
				except:
					try:
						back = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[1]/button[1]'))).click()
					except:
						count +=1
						if count == 10:
							return 'error'
	# while 1:
	# 	try:
	# 		sleep(2)
	# 		player_name_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input')))
	# 		sleep(1)
	# 		player_name_input.send_keys('a')
	# 		sleep(1)
	# 		sender(search_name, player_name_input)
	# 		break
	# 	except:
	# 		print('UNABLE TO FIND: PLAYER_NAME FIELD')

	# container = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]')))
	# container.find_elements(By.TAG_NAME, 'button')

	# done = False
	# while 1:
	# 	sleep(4)
	# 	all_players = driver.find_elements(By.TAG_NAME, 'button')
	# 	if len(all_players) == 0:
	# 		print('NO PLAYERS FOUND WITH THAT NAME')
	# 		return
	# 	else:
	# 		for i in all_players:
	# 			print(i.text.lower(), player_name.lower())
	# 			if i.text.lower() == player_name.lower():
	# 				sleep(0.5)
	# 				i.click()
	# 				done = True
	# 				break
	# 		if done == True:
	# 			break



def main():
	version, PROFILE, DATA_DIRECTORY, list_price, delay = get_config('config.txt')
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
	code = instance(driver, list_price, delay)
	if code == 'error':
		print("THERE WAS AN ERROR DUE TO SPEED")
	input()

main()