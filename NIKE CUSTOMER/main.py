
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
from msedge.selenium_tools import EdgeOptions
import random
from selenium.common.exceptions import TimeoutException
import threading
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from random_user_agent.user_agent import UserAgent

user_agent_rotator = UserAgent()


def instance(gmail, password):
	chromedriver_autoinstaller.install()
	opt = webdriver.ChromeOptions()
	opt.add_argument("--start-maximized")
	opt.add_argument('--disable-blink-features=AutomationControlled')
	opt.add_argument('--disable-blink-features=AutomationControlled')
	opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
	opt.add_argument("window-size=1920,1000")
	opt.add_argument("--no-sandbox")
	opt.add_argument("--ignore-certificate-errors")
	opt.add_argument("--homepage=about:blank")
	opt.add_argument("--no-first-run")
	opt.add_argument('--single-process')
	opt.add_argument('--disable-dev-shm-usage')
	#opt.add_argument("--incognito")
	opt.add_experimental_option('useAutomationExtension', False)
	opt.add_experimental_option("excludeSwitches", ["enable-automation"])
	opt.add_argument("disable-infobars")
	driver = webdriver.Chrome(options=opt)
	url = 'https://www.nike.com/launch'
	driver.implicitly_wait(5)
	try:
		driver.get(url)
		driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/header/div[1]/section/div/ul/li[1]/button').click()
		sleep(2)
		driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[2]/input').send_keys(gmail)
		sleep(2)
		driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[3]/input').send_keys(password)
		sleep(2)
		driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[4]/label').click()
		sleep(2)
		driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[6]/input').click()
		sleep(2)
		input('Lol done')
	except NoSuchElementException as e:
		print(e)

instance('Brittany88@gmail.com', 'Brittany88@79')

