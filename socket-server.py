import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT) #server and port need to be in a tuple like this 
DISCONNECT_MESSAGE= "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #This tells the network what type of addresses we are accepting
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR) #This has essentially binded our socket to our address 

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True 
    while connected :
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                not connected
            print(f"[{addr}] {msg}")
    conn.close()

        

def start():   #This allows our server to be available for possible connections
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() #This waits for the connection and gets its address and object
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTOIONS] {threading.activeCount()-1}")

print("[STARTING] server is starting")
start()