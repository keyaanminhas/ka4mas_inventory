import os
import cv2
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM




height = 500
width = 500
dim = (width, height)
path = os.getcwd()
path = path + r'\images'
images = os.listdir(path)

print(images)



for image in images:
	clear = False
	if image[-3:].find('svg') != -1:
		svgpic = svg2rlg('images/'+ image)
		renderPM.drawToFile(svgpic, 'images/'+ image[:-3]+'png', fmt='PNG')
		image = image[:-3]+'png'
		clear = True

	pic = cv2.imread('images/'+image)
	try:
		print('cropping....')
		resized = cv2.resize(pic, dim, interpolation = cv2.INTER_AREA)
		cv2.imwrite('design/'+ image, resized, [cv2.IMWRITE_JPEG_QUALITY, 100])
		print('saved......')
	except:
		print("unknown error")
	if clear == True:
		os.remove('images/' + image)
