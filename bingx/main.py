

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

url = 'https://bingx.com/en-us/futures/forward/BTCUSDT/?margin=VST&grants=0'

def get_config(filename):
	with open(filename, 'r') as f:
		x = f.readlines()
		z = [y.strip() for y in x if y.strip()!='']
	version = z[1]
	path = z[3]
	profile = path.split("\\", -2)
	PROFILE = profile[-1]
	DATA_DIRECTORY = path[0:len(path)-len(profile) -1]
	default_stop_loss = z[5]
	return version, PROFILE, DATA_DIRECTORY, default_stop_loss


def add_trailing_stop(driver, TSTOP):
	edit_trail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[3]/table/tbody/tr/td[6]/div/div/i'))).click()
	if float(TSTOP) < 3.9:
		use = 3.9
	else:	
		use = TSTOP
	
	money_here = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div/div/div[2]/div[2]/input')))
	money_here.send_keys(use)

	confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]'))).click()


	
def get_percent(driver):
	percentage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[3]/table/tbody/tr/td[4]/div/div/div/p[1]')))
	return percentage


def main():
	version, PROFILE, DATA_DIRECTORY, default_stop_loss= get_config('config.txt')
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
	driver.get(url)
	trailing_stop
	# while 1:
	# 	percentage = get_percent(driver)

main()