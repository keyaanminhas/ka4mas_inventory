
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import smtplib
import time
import os
import random
from selenium.common.exceptions import TimeoutException
import schedule
from datetime import date
from datetime import datetime
import base64
from selenium.webdriver.chrome.service import Service



username = 'a2E0bWFsZWFybmVyQGdtYWlsLmNvbQ=='
passwd = 'QEtleWFhbjc4Ng=='

s=Service('chromedriver.exe')


opt = webdriver.ChromeOptions()
#opt.add_argument("--headless")





login_btn = '/html/body/div[1]/div/div/div/div[1]/div[2]/button'
email_inp = '/html/body/div[1]/div/div/div/div[4]/div[2]/div/input[1]'
pass_inp = '/html/body/div[1]/div/div/div/div[4]/div[2]/div/input[2]'
enter_creds = '/html/body/div[1]/div/div/div/div[4]/div[2]/div/button'
alive_btn = '/html/body/div[1]/div/div/div/div[3]/div/div[2]/button/div'
click_this = '/html/body/div[1]/div/div/div/div[3]/div/div[2]/button'
already_comp = '/html/body/div[1]/div/div/div/div[3]/div/div[2]/div'

email = 'abdallahk@gmail.com'
password = 'p4J@V9' 
email2 = 'amirakml@gmail.com'
password2 = 'Alive111'
global result
result = ''
global time1, time2, initime


def job(email, password):
	global result, time1, time2, waittime
	sleep(random.randint(0,int(waittime))*60)
	#chromedriver_autoinstaller.install()
	driver = webdriver.Chrome(service=s, options=opt)
	url = 'https://tontine.cash/'
	driver.implicitly_wait(5)
	count = 0
	alrdy= False
	logger = False
	error = False

	while logger == False and count != 2 and alrdy == False:
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		result = result + str(current_time) + " "
		try:
			driver.get(url)
			loginbtn = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, login_btn)))
			sleep(random.randint(1, 40)/10)
			loginbtn.click()
			emailbox = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, email_inp)))

			passbox = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, pass_inp)))
			sleep(random.randint(1, 40)/10)
			for i in email:
				sleep(random.randint(1, 50)/10)
				emailbox.send_keys(i)
			sleep(random.randint(1, 40)/10)
			for i in password:
				sleep(random.randint(1, 50)/10)
				passbox.send_keys(i)
			entercreds = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, enter_creds)))
			sleep(random.randint(1, 40)/10)
			entercreds.click()
			alivebtn = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, alive_btn)))
			alive = alivebtn.text
			print(f"NEXT RUN WILL BE AT {time1} and {time2}")
			if alive == 'STAY ALIVE':
				clickthis = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, click_this)))
				sleep(random.randint(1, 40)/10)
				clickthis.click()
				sleep(random.randint(1, 40)/10)
				try:
					move = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/canvas")))
					for i in range(5):
						move.send_keys(Keys.ARROW_DOWN)	
				except:
					print(' ')				
				logger = True
				driver.close()
				result = result + f'{email} successfully clicked alive button |||'
			else:
				error = True
				driver.close()
				result = result + ' change in source code of the website |||'

		except:
			try:
				already = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, already_comp)))
				alrdy = True
				driver.close()
				result = result + f'{email} already completed |||'
			except:
				error = True
				count += 1
				if count ==2:
					driver.close()
					result = result + ' Contact ka4ma as unknown issue is found |||'




def mail(username,password, to):
	sleep(5)
	sent = False
	tried = 0
	try:
		while sent!=True and tried != 6:
			
				with smtplib.SMTP('smtp.gmail.com',587) as smtp:
					smtp.ehlo() # Identifies us with mail server not imp
					smtp.starttls() #encrypting the connection
					smtp.ehlo() #Identify again
					username = base64.b64decode(username)
					password = base64.b64decode(password)
					username = str(username)[2:-1]
					password = str(password)[2:-1]
					smtp.login(username, password)
					global result
					msg = f'Subject: {"if there is a problem contact ka4ma. Also contact if there is no subject."}\n\n{result}'

					smtp.sendmail(username, to, msg)
					sent = True
					tried = tried + 1
					if sent == True:
						print('done')
						result = ''
	except:
		print('ERROR IN MAILING, please check manually if the button is clicked.')


with open('time.txt', 'r') as f:
	x = f.readlines()
	initime = x[0]
	global waittime
	waittime = x[1]

schedule.every().day.at(initime).do(job,email,password)
schedule.every().day.at(initime).do(job, email2, password2)
schedule.every().day.at(initime).do(mail, username, passwd, 'abdallahk@gmail.com')

while True:
	schedule.run_pending()