import socket 
from threading import Thread
import sys

if len(sys.argv) !=2:
    print("Usage: " + sys.argv[0] + " <port number>")
    sys.exit(2)

def on_new_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024) 
        # Exit if msg is 'break'
        if msg == 'break':
            break
            
        print(addr, ' >> ', msg)
        # Convert msg to UPPER and send back to client
        msg.upper() 
        clientsocket.send(msg) 
        
    clientsocket.close()

serversocket = socket.socket(
socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object

port = int(sys.argv[1])

# bind to the port
# serversocket.bind((host, port))
serversocket.bind(('', port))

# Now wait for client connection.
print('Server started!')
print('Waiting for clients...')

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    print('Got connection from', addr)    
    Thread(target=on_new_client(clientsocket,addr)).start()    
    #Note it's (clientsocket,addr,) because second parameter is a tuple
    #that's how you pass arguments to functions when creating new threads 
    #using thread module

serversocket.close()

