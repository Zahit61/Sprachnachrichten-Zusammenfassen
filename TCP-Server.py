import socket 
import threading
#from oggwav import convert_ogg_to_wav

HEADER = 64
PORT = 8080
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while (True):
        conn, addr = server.accept()
        #conn, addr = server.accept()
        #thread = threading.Thread(target=handle_client, args=(conn, addr))
        #thread.start()
        #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        #print("Hey Test")
        #filename = input(str("Please enter a filename for the incoming file : "))
        
        """file = open("test.ogg", 'ab')
        #print("Teil1")

        file_data = conn.recv(24000).decode(hex)
        #print(file_data)
        conn.send("Msg received".encode(FORMAT))

        file.write(file_data)
        #print("Teil3")

        file.close()
        #print("File has been received successfully.")"""

        with open('test.ogg','wb') as f:
            while True:
                l = conn.recv(1024)
                if not l: break
                f.write(l)
        conn.close()


        
#print("[STARTING] server is starting...")
start()

#convert_ogg_to_wav()