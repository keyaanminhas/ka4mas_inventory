
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


instances = 1

chromedriver_autoinstaller.install()


