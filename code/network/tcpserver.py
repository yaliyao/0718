import socket
import sys

if len(sys.argv) !=2:
    print("Usage: " + sys.argv[0] + " <port number>")
    sys.exit(2)
    
# create a socket object
serversocket = socket.socket(
socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
# host = socket.gethostname()
port = int(sys.argv[1])

# bind to the port
# serversocket.bind((host, port))
serversocket.bind(('', port))

# queue up to 5 requests
serversocket.listen(5)
while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    
    print("Got a connection from %s" % str(addr))
    msg='Thank you for connecting'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
