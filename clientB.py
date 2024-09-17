import socket

# creating a socket and connecting to private server
PSsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PSsocket.connect(('127.0.0.1', 5070))

# Createing a socket and connecting to the middle server
CBsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CBsocket.connect(('127.0.0.1', 5060))

print("Connected to the middle server , forwarding to private server...!")

#now we do the recieving and forwarding art
while True:
        
        middleServerMessage = CBsocket.recv(1024).decode()
        if middleServerMessage:
            print(f"Message from middle server (Client A): {middleServerMessage}")
            PSsocket.send(middleServerMessage.encode()) 
        else:
            print("Middle server closed connection")
            break

# Close sockets when done
CBsocket.close()
PSsocket.close()
