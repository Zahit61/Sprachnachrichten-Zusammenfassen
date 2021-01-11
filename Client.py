from array import array
from os import stat
import socket


HEADER = 64
PORT = 18341 #hier ngrok port einfügen
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "2.tcp.ngrok.io"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(message)
    print(client.recv(1024).decode(FORMAT))

input()
with open('test.ogg', 'rb') as f:
  for l in f: client.sendall(l)
client.close()