from ctypes import*
from ctypes.wintypes import *
from time import sleep
import win32ui

def getpos():
    global pt
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return pt.x, pt.y

while 1:
    input()
    print(getpos())