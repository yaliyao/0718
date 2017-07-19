import socket
import sys

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " <server ip> <port number>")
    sys.exit(2)

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set server ip/port
host = sys.argv[1]
port = int(sys.argv[2])

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
msg = s.recv(1024)
s.close()
print (msg.decode('ascii'))