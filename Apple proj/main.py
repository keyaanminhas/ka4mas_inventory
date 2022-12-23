
with open('info.txt','r') as handle:
        info = handle.readlines()
url = info[0]
edgepath = info[1]
zipcode= info[2]
enable_proxy = info[2]



with open('zips.txt','r') as zipper:
        zipcodeshere = zipper.readlines()


#if enable_proxy == 'proxy=True':


#url = 'https://www.apple.com/shop/buy-iphone/iphone-12/6.1-inch-display-256gb-black-unlocked'
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

edge_options = EdgeOptions()
print(enable_proxy)
if enable_proxy.find('proxy=false'):
	PROXY = info[3]
	edge_options.add_argument('--proxy-server=%s' % PROXY)

edge_options.use_chromium = True   

#edge_options.add_argument(rf"user-data-dir={edgepath}")

#edge_options.add_argument("--headless")
edge_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(executable_path = r'driver\msedgedriver.exe', options = edge_options)

driver.get(url)
sleep(5)

try:
	tradein = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'tradeupinline')))
	tradein = driver.find_elements_by_name('tradeupinline')
	notrade = tradein[0]
	yestrade = tradein[1]
	notrade.click()
except TimeoutException:
	print ("Loading took too much time!")

	

notrade.click()
sleep(1)
single = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@id="b080bce1-e8be-11ec-a433-ff1157c4ba42"]')))

single.send_keys(Keys.PAGE_DOWN)
print ("Loading took too much time!")
single.click()
sleep(2)

try:
	wait = WebDriverWait(driver, 3)
	applecareno = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[4]/div[2]/div[3]/div[2]/div[5]/div/div[1]/fieldset/ul/li/label/div/div')))
except:
	wait = WebDriverWait(driver, 2)
	applecareno = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[5]/div[4]/div[2]/div[3]/div[2]/div[5]/div/div[2]/fieldset/ul/li/label/div')))

applecareno.click()

try:
	searchstores = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[5]/div[4]/div[2]/div[3]/div[2]/div[6]/div[1]/div/div[2]/div/div/div[2]/div/div/button')))
except TimeoutException:
	searchstores = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[5]/div[4]/div[2]/div[3]/div[2]/div[6]/div[1]/div/div[2]/div/div/div[2]/div/div/span[2]/button')))
searchstores.click()

try:
	location = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'rc-overlay-popup-content')))
	location.click()
except TimeoutException:
	print("Took too long to find the element")

sleep(3)
zip_code = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div[1]/div[1]/form/div[1]/div/div/input')
for i in range(0,10):
	zip_code.send_keys(Keys.BACK_SPACE)
zip_code.send_keys(random.choice(zipcodeshere))
zip_code.send_keys(Keys.ENTER)
found = False


while found == False:
	try:
		stor = EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/fieldset/div/li[1]/label'))
		WebDriverWait(driver, random.randint(5,6)).until(stor)
		store_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/fieldset/div/li[1]/label/span/span[1]/span[1]')))
		if store_name.text == 'Apple Pioneer Place' or 'Apple Bridgeport Village' or 'Apple Washington Square':
			found = True
			break
	except:
		print('Not found')
	for i in range(0,5):
		zip_code.send_keys(Keys.BACK_SPACE)
	sleep(0.5)
	zip_code.send_keys(random.choice(zipcodeshere))
	zip_code.send_keys(Keys.ENTER)


try:
	store = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/fieldset/div/li[1]/label')))
except TimeoutException:
	print("Took too long to load")
store.click()
try:
	contin = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div/div[2]/div[2]/div[2]/button')))
except TimeoutException:
	print("Took too long to load")
contin.click()
try:
	addtobag = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[5]/div[4]/div[2]/div[3]/div[2]/div[6]/div[1]/div/div[3]/div[2]/form/div/span/button')))
except TimeoutException:
	print("Took too long to load")
addtobag.click()
sleep(5)

driver.get('https://www.apple.com/shop/bag')

try:
	guestexit = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[4]/div[2]/div[1]/div[3]/div/div/div[1]/button')))
	guestexit.click()
except TimeoutException:
	print("It took too long to load")

try:
	guest = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div[2]/div/div[3]/div/div/button')))
	guest.click()
except TimeoutException:
	print("It took too long to load")
check = 0
while check == 0:
	try:
		sleep(2)
		ordertime = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div[2]/div/div/div/fieldset/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div/fieldset/div/div[3]/select')))
		ordertime.send_keys(Keys.PAGE_DOWN)
		sleep(1)
		options = [x for x in ordertime.find_elements_by_tag_name("option")]
		sleep(0.2)
		select = Select(driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div[2]/div/div/div/fieldset/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div/fieldset/div/div[3]/select'))
		sleep(0.2)
		select_time = options[random.randint(0,len(options)-1)]
		sleep(0.2)
		select.select_by_value(select_time.get_attribute('value'))
		check = 1
	except TimeoutException:
		print("It took too long to load")


try:
	sleep(1)
	almost = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div[3]/div/div/div/div/button')))
	almost.click()
except TimeoutException:
	print("It took too long to load")



#check out details
with open('details.txt','r') as han:
        detailmain = han.readlines()

card_details = detailmain[0]
exp = detailmain[1]
cvv = detailmain[2]
address = detailmain[3]

name_choice = detailmain[4]
last_name_choice = detailmain[5]
email_choice = detailmain[6]
number_choice = detailmain[7]


try:
	sleep(1)
	First_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div[1]/div/div/fieldset/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div/input')))
	sleep(0.3)
	First_name.send_keys(name_choice)
except TimeoutException:
	print("It took too long to load")

try:
	sleep(1)
	Last_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div[1]/div/div/fieldset/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/input')))
	sleep(0.3)
	Last_name.send_keys(last_name_choice)
except TimeoutException:
	print("It took too long to load")
try:
	sleep(1)
	email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div[1]/div/div/fieldset/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div/div/input')))
	sleep(0.3)
	email.send_keys(email_choice)
	email.send_keys(Keys.PAGE_DOWN)
except TimeoutException:
	print("It took too long to load")

try:
	sleep(1)
	number = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div[1]/div/div/fieldset/div[2]/div/div/div/div/div/div/div/div[4]/div[1]/div/div/div/div/input')))
	sleep(0.3)
	number.send_keys(number_choice)
except TimeoutException:
	print("It took too long to load")


try:
	sleep(0.5)
	payment = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/button')))
	sleep(0.2)
	payment.click()
except TimeoutException:
	print('It took too long to load')
check = 0
while check == 0:
	try:
		sleep(0.5)
		credit = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[6]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/fieldset/div/div/div[1]/div[1]/div[1]/div[1]/div/label/span/span[1]')))
		sleep(0.2)
		credit.click()
		check =1
	except TimeoutException:
		print('It took too long to load')







try:
	sleep(0.5)
	card_det = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/fieldset/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div/input')))
	sleep(0.2)
	card_det.send_keys(card_details)
except TimeoutException:
	print('It took too long to load')

try:
	sleep(0.5)
	expi = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/fieldset/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div/input')))
	sleep(0.2)
	expi.send_keys(exp)
except TimeoutException:
	print('It took too long to load')

try:
	sleep(0.5)
	cvv_info = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/fieldset/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/input')))
	sleep(0.2)
	cvv_info.send_keys(cvv)
	cvv_info.send_keys(Keys.PAGE_DOWN)
except TimeoutException:
	print('It took too long to load')


try:
	sleep(0.5)
	name_again = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/fieldset/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/input')))
	sleep(0.2)
	name_again.send_keys(name_choice)
except TimeoutException:
	print('It took too long to load')

try:
	sleep(0.5)
	Last_name_again = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/fieldset/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/input')))
	sleep(0.2)
	Last_name_again.send_keys(name_choice)
except TimeoutException:
	print('It took too long to load')

try:
	sleep(0.5)
	street_address = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/fieldset/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div/div/div/div/div/div[4]/div/div/div/div/input')))
	sleep(0.2)
	street_address.send_keys(address)
except TimeoutException:
	print('It took too long to load')


try:
	sleep(0.5)
	zip_code_again = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/fieldset/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[2]/div/div/div/div/div/div/div[6]/div/fieldset/div/div/div[1]/div/div/div/input')))
	sleep(0.2)
	zip_code_again.send_keys(zipcode)
	zip_code_again.send_keys(Keys.PAGE_DOWN)
except TimeoutException:
	print('It took too long to load')


try:
	sleep(0.5)
	review = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[7]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/div/button')))
	sleep(0.2)
	review.click()
except TimeoutException:
	print('It took too long to load')
	print('found error')


sleep(2)
check = 0
while check == 0:
	try:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		check=1
	except TimeoutException:
		print("It took too long to load")

try:
	sleep(0.5)
	CHECKOUT = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[5]/div[1]/div[1]/div/div/div[2]/div[5]/div/div/div/div[1]/button')))
	sleep(0.2)
	CHECKOUT.click()
except TimeoutException:
	print('It took too long to load')