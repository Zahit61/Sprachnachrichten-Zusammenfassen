import socket 
import threading
from Speechtext import speechtext as st

HEADER = 64
PORT = 8080
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    conn, addr = server.accept()
    with open('test.ogg','wb') as f:
        print(addr)
        while True:
            l = conn.recv(1024)
            if not l: break
            f.write(l)
    conn.close()

print("[STARTING] server is starting...")
start()

print("Läuft...")

text = str(st())
print(text)