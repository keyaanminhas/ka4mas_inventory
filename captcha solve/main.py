from selenium import webdriver
from selenium.webdriver.common import keys
import time
import random
import pytesseract
from pytesseract import image_to_string 
from PIL import Image, ImageEnhance, ImageFilter 


def ParsePic():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    im = Image.open("captcha.png") 
    im = im.filter(ImageFilter.CONTOUR)
    im = im.filter(ImageFilter.DETAIL)
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(4)
    im = im.convert('L')
    im.save('temp10.png')   
    text = image_to_string(Image.open('temp10.png'))
    print(text)

ParsePic()