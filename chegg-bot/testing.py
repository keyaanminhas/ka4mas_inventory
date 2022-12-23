import pyautogui as pg
from time import sleep
import os
path = 'C:\\Users\\ka4ma\\Downloads\\screenshots\\'
url = 'http://ka4ma.unaux.com'

pg.hotkey('win', 'r')
sleep(0.1)
pg.typewrite('msedge')
pg.press('ENTER')
sleep(0.2)
pg.typewrite(url)
sleep(0.1)
pg.press('ENTER')
sleep(2)
pg.hotkey('alt', 'shift', 'p')
sleep(2)
files = os.listdir(path)
