import RPi.GPIO as GPIO
import bluetooth

LedPin = 11    # pin11

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedPin, GPIO.LOW) # Set LedPin low(0.0V) to off led

def loop():
    while True:
        data = client_socket.recv(1024)
        print("Received: %s" % data)

        data=data.decode('ascii')  # convert binary string to ascii string    
        if (data == "0"):    #if '0' is sent from the Android App, turn OFF the LED
            print("Pin " + str(LedPin) + " LOW, LED OFF")
            GPIO.output(LedPin, GPIO.LOW)

        if (data == "1"):    #if '1' is sent from the Android App, turn OFF the LED
            print("Pin " + str(LedPin) + " HIGH, LED ON")
            GPIO.output(LedPin, GPIO.HIGH)

        if (data == "q"):
            print("Quit")
            break

def destroy():
    GPIO.output(LedPin, GPIO.LOW)     # led off
    GPIO.cleanup()                    # Release resource
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        server_socket.bind(("",bluetooth.PORT_ANY))
        server_socket.listen(1)

        client_socket,address = server_socket.accept()
        print("Accepted connection from ",address)
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print('Quitting')
    finally:
        destroy()
