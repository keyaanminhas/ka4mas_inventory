import socket
import threading
import time

port = 5500
ip = socket.gethostbyname(socket.gethostname())
ADDR = (ip,port)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "disconnect"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
	try:
		print(f"NEW CONNECTION {addr} connected.")
		connected = True
		while connected:
			msg_len = conn.recv(HEADER).decode(FORMAT)
			if msg_len:
				msg_len = int(msg_len)
				msg = conn.recv(msg_len).decode(FORMAT)
				print(f'{addr} SAID {msg}')
				if msg == DISCONNECT_MESSAGE:
					connected = False
					print(f'[{addr}] DISCONNECTED')
	except:	
		conn.close()



def start():
	server.listen()
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"ACTIVE CONNECTIONS {threading.active_count() -1}")

print("Server is starting.....")
start()

