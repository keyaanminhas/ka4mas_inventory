import appium
from appium import webdriver
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


global last_num
last_num = 0

global number
number = ''

desired_cap = {
  "deviceName": "Android Emulator",
  "platformName": "Android",
  "appPackage": "com.nike.snkrs",
  "appWaitActivity": "com.nike.snkrs.feed.activities.TheWallActivity",
  "app": "C:\\Users\\ka4ma\\Downloads\\nike.apk"
}

with open('pass.txt', 'r') as f:
	accounts = f.readlines()


def get_phone_number():
	global last_num
	global number
	if last_num == 10:
		last_num = 0
	last_num +=1
	opt = webdriver.ChromeOptions()
	opt.add_argument("--start-maximized")
	opt.add_argument("--user-data-dir=C:/Users/ka4ma/AppData/Local/Google/Chrome/User Data")
	opt.add_argument("--profile-directory=Profile2")
	opt.add_argument('--disable-blink-features=AutomationControlled')
	opt.add_argument('--disable-blink-features=AutomationControlled')
	opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
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
	driver = webdriver.Chrome('chromedriver.exe', options=opt)
	driver.implicitly_wait(20)
	driver.get('https://5sim.net/free')
	sleep(5)
	all_phone_numbers = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[6]/div/div[2]/div[1]/div/div[2]')
	phone_numbers = all_phone_numbers.find_elements_by_tag_name('a')
	number_to_use = phone_numbers[last_num-1]
	number = str(number_to_use.text)
	number = number[2:]
	if last_num != 1:
		number_to_use.click()
	nike_message = False
	sleep(1)
	reloa = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[6]/div/div[2]/div[2]/div/div[1]/div/a')
	while nike_message == False:
		message = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[6]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[1]/div/h5/span[1]')
		if message.text == 'NIKE':
			nike_message = True
		else:
			sleep(3)
			reloa.click()
			sleep(1)
	tex = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[6]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[1]/div/span')
	text = tex.text


def instance(email, password):
	driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
	driver.implicitly_wait(50)
	sleep(3)
	sign_in = driver.find_element(by = By.ID ,value ='com.nike.snkrs:id/loginButton')
	sign_in.click()
	sleep(5)
	email_box = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.EditText')
	password_box = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.widget.EditText')
	email_box.send_keys(email)
	sleep(2)
	password_box.send_keys(password)
	sleep(1)
	loginbtn = driver.find_element_by_xpath('//android.widget.Button[@content-desc="SIGN IN"]')
	loginbtn.click()
	global last_num
	global number
	if last_num == 10:
		last_num = 0
	last_num +=1
	opt = webdriver.ChromeOptions()
	opt.add_argument("--start-maximized")
	opt.add_argument("--user-data-dir=C:/Users/ka4ma/AppData/Local/Google/Chrome/User Data")
	opt.add_argument("--profile-directory=Profile2")
	opt.add_argument('--disable-blink-features=AutomationControlled')
	opt.add_argument('--disable-blink-features=AutomationControlled')
	opt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
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
	driv = webdriver.Chrome('chromedriver.exe', options=opt)
	driv.implicitly_wait(20)
	driv.get('https://5sim.net/free')
	sleep(5)
	all_phone_numbers = driv.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[6]/div/div[2]/div[1]/div/div[2]')
	phone_numbers = all_phone_numbers.find_elements_by_tag_name('a')
	number_to_use = phone_numbers[last_num-1]
	number = str(number_to_use.text)
	number = number[2:]
	number_field = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.EditText')
	number_field.send_keys(number)
	send_code = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Send Code"]')
	send_code.click()

	if last_num != 1:
		number_to_use.click()
	nike_message = False
	sleep(1)
	reloa = driv.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[6]/div/div[2]/div[2]/div/div[1]/div/a')
	while nike_message == False:
		message = driv.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[6]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[1]/div/h5/span[1]')
		if message.text == 'NIKE':
			nike_message = True
		else:
			sleep(3)
			reloa.click()
			sleep(1)
	tex = driv.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[6]/div/div[2]/div[2]/div/div[2]/div/div/ul/li[1]/div/span')
	text = tex.text
	print(text)
	input("helo")





email, password = (accounts[0]).split(':')
print(email, password)

instance(email, password)
