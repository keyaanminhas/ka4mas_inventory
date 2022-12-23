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



#GETTING USER INPUT WITH AN APPROPRIATE PROMPT
instances = int(input('PLEASE ENTER THE NUMBER OF INSTANCES YOU WISH TO CREATE:   '))


#READING PROXIES FROM PROXY FILE STRONG THEM IN A VARIABLE NAMED PROXIES
with open('config/proxies.txt') as f:
    proxies = f.read().splitlines() 
global proxy_switch
proxy_switch = int(input("PROXY TURNED ON '1', PROXY TURNED OFF '0':   "))



#SETTINGS FOR BROWSER
edge_options = EdgeOptions()
edge_options.use_chromium = True   
#edge_options.add_argument("--headless")
edge_options.add_argument("--disable-gpu")

#PRINTING THE PROXY_SWITCH
print(proxy_switch)

#THE FUNCTION THATS GOING TO BE OPENING THE WEBSITE AND AUTOMATING IT

def instance(proxy = ' '): #BY DEFEAULT PROXY IS SET TO NONE
	global proxy_switch
	if proxy_switch == 1:
		#ADDING PROXIES IF THE SWITCH IS ON
#		try:
			edge_options.add_argument('--proxy-server=%s' % str(proxy))
			driver = webdriver.Chrome(executable_path = r'driver\msedgedriver.exe', options = edge_options)
			#SETTINGS FOR LOADING THE WEBPAGE
			driver.set_network_conditions(
				offline=False,
				latency=5,
				download_throughput=500 * 1024, 
				upload_throughput=500 * 1024)
			driver.get('https://website-von-sperrplatzbeda.yolasite.com/')
#		except:
			print("INVALID PROXY:", proxy)

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

	#EXITING THE FREAME WHICH THE PROGRAM SWITCHED TO BEFORE

	driver.switch_to.parent_frame()


	#UNMUTING THE VIDEO
	sleep(1)
	try:
		iframe2.send_keys('m')
	except:
		print('cant send m')



print(proxies)
for i in proxies:
	print(i)

#A LOOP USED TO ITERATE THROUGHT THE PROXIES
for number in range(0, instances):
	if proxy_switch == 1:
		#CREATING THREADS WHICH WILL ENABLE US TO OPEN MULTIPLE BROSWER WINDOWS
		x = threading.Thread(target=instance, args=(proxies[number],))
		x.start()
	else:
		x = threading.Thread(target=instance)
		x.start()

#WAITING SO THE PROGRAM DOESNT CLOSE THE BROSWER WINDOWS AFTER EXECUTION
while True:
	sleep(1)