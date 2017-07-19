import socket 
import threading
import sys

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # Create a socket object
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host,self.port))

    def listen(self):
        # Now wait for client connection.
        print('Server started!')
        print('Waiting for clients...')

        try:
            self.sock.listen(5)
            while True:
                clientsocket,addr = self.sock.accept()
                print('Got connection from', addr)

                threading.Thread(target=self.on_new_client,args=(clientsocket,addr)).start()   
        finally:
            self.sock.close()

    def on_new_client(self,clientsocket,addr):
        while True:
            msg = clientsocket.recv(1024)
            msg = msg.decode("UTF-8")

            # Exit if msg is 'break'
            if msg == 'break':
                break
            
            print(addr, ' >> ', msg)
            # Convert msg to UPPER and send back to client
            msg=msg.upper() 
            clientsocket.send(bytes(msg,"UTF-8"))
        
        clientsocket.close()
        print(addr, "is disconnected!")

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: " + sys.argv[0] + " <port number>")
        sys.exit(2)

    port = int(sys.argv[1])

    ThreadedServer('',port).listen()
