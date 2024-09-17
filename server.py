import socket
import threading

Ipv4 = socket.AF_INET
TCP = socket.SOCK_STREAM


# first we make the sockets
ss5050 = socket.socket(Ipv4 , TCP)
ss5060 = socket.socket(Ipv4 , TCP)



# now we make the sockets bind on two different ports
ss5050.bind(('0.0.0.0', 5050))
ss5060.bind(('0.0.0.0', 5060))



# Now the server listens on the two declared ports and only accepts '1' client
ss5050.listen(1)
ss5060.listen(1)
print("server is online on port 5050 and port 5060")


#client A must connect to port 5050
client_A, addr_A = ss5050.accept()
print(f"Client A connected from {addr_A}")



#client B must connect to port 5060
client_B, addr_B = ss5060.accept()
print(f"Client B connected from {addr_B}")




# Function to handle forwarding messages from Client A to Client B and vice versa
def handle_client_A():
    while True:
        try:
            message = client_A.recv(1024).decode()  
            if message:
                print(f"Received from Client A: {message}")
                client_B.send(message.encode())  
            else:
                print("Client A disconnected")
                break  
        except:
            break  


def handle_client_B():
    while True:
        try:
            message = client_B.recv(1024).decode()
            if message:
                print(f"Received from Client B: {message}")
                client_A.send(message.encode())
            else:
                print("Client B disconnected")
                break
        except:
            break



#now to avoid ping pong chat we make the two functions work at the same time
clientAthread = threading.Thread(target=handle_client_A)
clientBthread = threading.Thread(target=handle_client_B)


#functions now start to work 
clientAthread.start()
clientBthread.start()

# here we made the two threads to join the main thread two avoid termination
clientAthread.join()
clientBthread.join()
