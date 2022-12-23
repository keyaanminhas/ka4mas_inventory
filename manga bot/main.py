import chromedriver_autoinstaller
from selenium import webdriver

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import random
from selenium.common.exceptions import TimeoutException

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)





#START 


url = 'https://tiki.vn/chu-tiem-banh-chien-binh-va-co-phuc-vu-nguoi-may-tap-5-p145898412.html'

driver.get(url)


source = driver.page_source

print(source)

word_to_find = str(input('PLEASE ENTER THE WORD TO FIND:  '))


if source.find(word_to_find) != -1:
	print(f'The Word {word_to_find} is found!')

