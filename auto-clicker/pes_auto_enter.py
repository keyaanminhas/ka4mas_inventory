import pyautogui as pg
from time import sleep
import threading

from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
mouse = Controller()


pg.FailSafeException = True


def clicker(key):
	mouse = Controller()
	run = False
	if key == Key.tab:
		run = True
		pg.click()
		sleep(3)
	while run:
		pg.click()
		sleep(0.4)


def show(key):
	
	if key == Key.tab:
		print("good")
		  
	if key != Key.tab:
		print("try again")
		  
	# by pressing 'delete' button 
	# you can terminate the loop 
	if key == Key.delete: 
		return False
# Collect all event until released
with Listener(on_press = clicker) as listener:
	listener.join()