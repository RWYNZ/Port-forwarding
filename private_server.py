import socket

#again a socket
PSsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#now the private server binds and listens for connections
PSsocket.bind(('0.0.0.0',5070))
PSsocket.listen(1)
print("private server is online on port 5070 waiting for call...!")

#now server accepts the client B
client_B, addr_B = PSsocket.accept()
print(f"Client B connected from {addr_B}")

#now we get messsages
while True:
        message = client_B.recv(1024).decode()
        if message:
            print(f"Message from client B (middle server and client A): '{message}'")
        else:
            print("Client B disconnected")
            break



PSsocket.close()

