from gpiozero import LED
import bluetooth

GPIOPin = 17
red = LED(GPIOPin)

server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

server_socket.bind(("",bluetooth.PORT_ANY))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print("Accepted connection from ",address)

while True:
    data = client_socket.recv(1024)
    print("Received: %s" % data)

    data=data.decode('ascii')  # convert binary string to ascii string    
    if (data == "0"):    #if '0' is sent from the Android App, turn OFF the LED
        print("GPIO " + str(GPIOPin) + " LOW, LED OFF")
        red.off()

    if (data == "1"):    #if '1' is sent from the Android App, turn OFF the LED
        print("GPIO " + str(GPIOPin) + " HIGH, LED ON")
        red.on()

    if (data == "q"):
        print("Quit")
        break

client_socket.close()
server_socket.close()
