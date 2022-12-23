import socket
import sys

ip = input("ENTER THE IP: ")
port = int(input("ENTER THE PORT: "))
command = input("ENTER THE COMMAND: ")
open_this = str(input("FILE PATH: "))


with open(open_this, 'r') as f:
	offset = f.read()

print(offset)
print('\n'*7)

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.send((command + offset).encode('utf-8'))
	s.close()
except:
	print("ERROR")