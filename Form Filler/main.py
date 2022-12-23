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
import undetected_chromedriver as uc






#CHROME DRIVER SERVICE



url = 'https://boutique.hublot.com/int_en/nftclaim/form/luckydraw'





def splitstring(Total_Name):
    first = ''
    last = ''
    for i in range(0,len(Total_Name)):
        if i <= len(Total_Name)//2-1:
            first = first + Total_Name[i]
        else:
            last = last + Total_Name[i]
    return first, last







def sender(message, location):
	for i in range(0,len(message)):
		location.send_keys(message[i])
		sleep(0.05)
		# sleep(0.2)




#START


def form(url, email, number, first_name, last_name):
	driver = uc.Chrome()
	sleep(2.5)
	driver.get(url)
	cookies_accept = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
	Email_Box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/form/div[1]/div[2]/input')))
	sender(email, Email_Box)
	sleep(2)
	Email_Button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/form/div[1]/div[3]/div/button'))).click()


	#MAIN FORM STARTS HERE


	First_Name = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/form/div[2]/div[3]/input')))
	sleep(2)
	sender(first_name, First_Name)

	Last_Name = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/form/div[2]/div[4]/input')))
	sender(last_name, Last_Name)

	sleep(0.1)

	country_code_selector = Select(driver.find_element_by_xpath('/html/body/div[2]/main/div[2]/div/div[2]/form/div[2]/div[5]/select'))
	country_code_selector.select_by_value('PK')


	sleep(0.1)
	Number_Input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/form/div[2]/div[5]/input[1]')))
	sleep(0.1)
	sender(number, Number_Input)


	Check_Box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/form/div[2]/div[8]/input'))).click()

	driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
	sleep(1.5)
	Terms_And_Conditions = driver.find_element_by_partial_link_text("Rules")
	driver.execute_script("arguments[0].scrollIntoView();", Terms_And_Conditions)
	action = ActionChains(driver)


	spanner = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/form/div[2]/div[8]/label')))
	location = spanner.location
	x_cd = location['x']
	y_cd = location['y']

	#action.move_to_element_with_offset(spanner, 154, 28).click().perform() #154, 28
	action.move_to_element_with_offset(spanner, (x_cd * 126.7676767/100)-x_cd, (y_cd*102.424844/100)-y_cd).click().perform()
	sleep(2.5)
	p = driver.current_window_handle
	parent = driver.window_handles[0]
	driver.switch_to.window(parent)

	participate = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/form/div[2]/div[12]/div/input')))
	sleep(0.8)
	participate.click()
	sleep(1.7)
	driver.quit()

	print("THERE WAS AN ERROR")
	try:
		driver.exit()
	except:
		print("Error in launching driver")





with open('emails.txt', 'r') as f:
	emails = f.readlines()
with open('numbers.txt', 'r') as f:
	numbers = f.readlines()
with open('names.txt', 'r') as f:
	names = f.readlines()


if __name__ == '__main__':
	for i in range(0,len(emails)):
		email = emails[i].strip()
		number = numbers[i].strip()
		name = names[i].strip()
		try:
			first_name, last_name = name.split(' ')
		except:
			print('Maybe you forgot to add the last names in the same line with a space')
		form(url, email, number, first_name, last_name)



