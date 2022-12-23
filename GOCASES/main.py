from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service


def instance():
	s=Service('chromedriver.exe')
	opt = webdriver.ChromeOptions()
	opt.add_experimental_option(
    'excludeSwitches',
    ['allow-pre-commit-input',
     'disable-background-networking',
     'disable-backgrounding-occluded-windows',
     'disable-client-side-phishing-detection',
     'disable-default-apps',
     'disable-hang-monitor',
     'disable-popup-blocking',
     'disable-prompt-on-repost',
     'disable-sync',
     'enable-automation', 
     'enable-blink-features=ShadowDOMV0', 
     'enable-logging',
     'log-level=0',
     'no-first-run', 
     'no-service-autorun', 
     'password-store=basic', 
     'remote-debugging-port=0', 
     'use-mock-keychain',
     'flag-switches-begin', 
     'flag-switches-end'])
	opt.add_argument(r"""user-data-dir=C:\Users\ka4ma\AppData\Local\Google\Chrome\User Data\Profile 1""")
	opt.add_argument("--no-sandbox")
	driver = webdriver.Chrome(service =s, options=opt)
	url = 'https://gcskins.gg/wheel'
	driver.get(url)
	sleep(2)
	wheel = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div'))).click()

	input("hello")

instance()
