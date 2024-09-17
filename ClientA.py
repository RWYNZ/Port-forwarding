import socket
#like server we made a socket
CAsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#now client A connects to server with its specified port
CAsocket.connect(('127.0.0.1',5050))

#now to send message we use infinite while loop

print("Connected to middle server, Enter your message")

while True:

    #with a input we get the client A's message
    sentMessage = input()
    #with send method we send it
    CAsocket.send(sentMessage.encode())

    #now we want answer
    respond = CAsocket.recv(1024)
    print("responde: ",respond)
