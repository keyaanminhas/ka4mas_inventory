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
from msedge.selenium_tools import EdgeOptions
import random
from selenium.common.exceptions import TimeoutException
import threading
from selenium.webdriver.common.action_chains import ActionChains
import zipfile


manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""



#GETTING USER INPUT WITH AN APPROPRIATE PROMPT
instances = int(input('PLEASE ENTER THE NUMBER OF INSTANCES YOU WISH TO CREATE:   '))


#READING PROXIES FROM PROXY FILE STRONG THEM IN A VARIABLE NAMED PROXIES
with open('config/proxies.txt','r') as handle:
        proxies = handle.readlines()

global proxy_switch
proxy_switch = int(input("PROXY TURNED ON '1', PROXY TURNED OFF '0':   "))



#SETTINGS FOR BROWSER


#PRINTING THE PROXY_SWITCH
print(proxy_switch)

#THE FUNCTION THATS GOING TO BE OPENING THE WEBSITE AND AUTOMATING IT
def get_chromedriver(use_proxy=False, user_agent=None):
    path = os.path.dirname(os.path.abspath(__file__))
    edge_options = webdriver.EdgeOptions()
    edge_options.use_chromium = True   
    #edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-gpu")
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        edge_options.add_extension(pluginfile)
    if user_agent:
        edge_options.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Chrome(executable_path = r'driver\msedgedriver.exe',chrome_options=edge_options)
    return driver

def instance(PROXY_HOST = ' ',PROXY_PORT = ' ',PROXY_USER = ' ',PROXY_PASS = ' ',manifest_json = ' '): #BY DEFEAULT PROXY IS SET TO NONE
	global proxy_switch
	if proxy_switch == 1:
		#ADDING PROXIES IF THE SWITCH IS ON
		try:
			background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)
			get_chromedriver(True)

			driver.get('https://website-von-sperrplatzbeda.yolasite.com/')
		except:
			print("Errror in proxy loading")

	else:
		driver = webdriver.Chrome(executable_path = r'driver\msedgedriver.exe', options = edge_options)
		driver.get('https://website-von-sperrplatzbeda.yolasite.com/')


	sleep(3)


	
	#FINDING THE MAIN FRAME WHERE THE VIDEO IS LOCATED
	iframe2 = driver.find_element_by_xpath("/html/body/div[1]/ws-block[2]/section/div/div/ws-block/div/ws-media-container/ws-iframe/iframe")
	print(iframe2.get_attribute('innerHTML'))
	driver.switch_to.frame(iframe2)



	#CLICKING THE BUTTON TO CONFIRM MATURE CONTENT
	button = driver.find_element_by_tag_name('button')
	try:
		button.click()
	except:
		print('no button')

	sleep(5)

	#EXITING THE FRAME WHICH THE PROGRAM SWITCHED TO BEFORE

	driver.switch_to.parent_frame()


	#UNMUTING THE VIDEO
	sleep(1)
	try:
		iframe2.send_keys('m')
	except:
		print('cant send m')



#A LOOP USED TO ITERATE THROUGHT THE PROXIES
for number in range(0, instances):
	PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS = proxies[number].split( )
	if proxy_switch == 1:
		#CREATING THREADS WHICH WILL ENABLE US TO OPEN MULTIPLE BROSWER WINDOWS
		x = threading.Thread(target=instance, args=(PROXY_HOST,PROXY_PORT,PROXY_USER,PROXY_PASS,manifest_json))
		x.start()
	else:
		x = threading.Thread(target=instance)
		x.start()

#WAITING SO THE PROGRAM DOESNT CLOSE THE BROSWER WINDOWS AFTER EXECUTION
while True:
	sleep(1)