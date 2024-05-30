import time
import struct, os
import socketserver
from socket import *

SENDING_COOLDOWN = 0.3
BUFFER_SIZE = 4096
FORMAT = 'utf-8'
ok_str = 'OK'
receive = ""

client = socket(AF_INET, SOCK_STREAM)    
print("========================= Initialize Socket ========================")
SERVER_ADDR = input("input IP address: ")
SERVER_PORT = int(input("input port number: "))
ADDR = (SERVER_ADDR, SERVER_PORT)
error = client.connect(ADDR)

while error == None:
    print("============================ Input command ============================")
    command = input("Input Command: ")
    client.send(command.encode(FORMAT))
    if command == "GET":
        print("---------Recieved Messages---------")
        rcv_msg = client.recv(BUFFER_SIZE)
        while(rcv_msg.decode(FORMAT) != "server: &"):
            print(rcv_msg.decode(FORMAT))
            rcv_msg = client.recv(BUFFER_SIZE)
        print(rcv_msg.decode(FORMAT))
        print(f"( IP address: {SERVER_ADDR}, port number {SERVER_PORT} )")
        print("Connect status: OK")
        print("Server status: OK")
    elif command == "POST_STRING":
        print("=============== Content (Type a lone '&' to end message) ===============")
        msg = input("Client: ")
        n=1
        while msg!="&":
            client.send(msg.encode(FORMAT))
            msg = input("Client: ")
            n+=1
        client.send(msg.encode(FORMAT))
        rcv_msg = client.recv(len('server: OK'))
        print(rcv_msg.decode(FORMAT))
        print("---------")
        print(f"Sent {n} messages to ( IP address: {SERVER_ADDR}, port number {SERVER_PORT} )")
        print("Connect status: OK")
        print("Server status: OK")
        print("---------")
    elif command == "POST_FILE":
        rcv_msg = client.recv(len('server: please send your file and its path name'))
        print(rcv_msg.decode(FORMAT))
        file_path = input("Client: ")
        file_size = os.path.getsize(file_path)
        file_name = file_path.split('/')[-1]
        print(file_name)
        client.send(struct.pack('128sl', file_name.encode(FORMAT), file_size))
        file = open(file_path, 'rb')
        while True:
            msg = file.read(10)
            if not msg:
                break
            client.send(msg)
        receive = client.recv(BUFFER_SIZE).decode(FORMAT)
        print(receive.strip())

    elif command == "EXIT":
        rcv_msg = client.recv(BUFFER_SIZE)
        print(rcv_msg.decode(FORMAT))
        client.close()
        break
    else:
        rcv_msg = client.recv(len("server: ERROR - Command not understood"))
        print(rcv_msg.decode(FORMAT))
