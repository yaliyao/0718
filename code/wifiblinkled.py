# Use termius app to ssh to RPi
# Run this program to control GPIO LED
from gpiozero import LED
from time import sleep

GPIOPin = 17
red = LED(GPIOPin)

while True:
    data = input("Control LED (0:off, 1:on, q:quit): ")
    if (data == '1'):
        print("GPIO " + str(GPIOPin) + " LOW, LED ON")
        red.on()
    
    if (data == '0'):
        print("GPIO " + str(GPIOPin) + " LOW, LED OFF")
        red.off()
    
    if (data == 'q'):
        print("Quit")
        break

