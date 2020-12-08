import socket

HEADER = 64
PORT = 18690 #hier ngrok port einfügen
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "4.tcp.ngrok.io"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

#send('Hello World')
input()
file = open('test.rtf', 'rb')
file_data = file.read(1024)
send(file_data)
file.close
print ("Send")
input()

#send(DISCONNECT_MESSAGE)
