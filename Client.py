from array import array
from os import stat
import socket


HEADER = 64
PORT = 13850
 #hier ngrok port einfügen
FORMAT = 'utf-8'
SERVER = "0.tcp.ngrok.io"
ADDR = (SERVER, PORT)

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(ADDR)

input()
with open('test.ogg', 'rb') as f:
  for l in f: conn.sendall(l)
print('File send')
conn.close()