import RPi.GPIO as GPIO
import time

BtnPin = 32    # pin32
BTime = 500

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(BtnPin, GPIO.IN)    # Set BtnPin's mode is input

def my_callback(channel):                                                 
    print("Button pressed at ", time.ctime())

def loop():
    # wait for falling and set bouncetime to prevent the callback function from being called multiple times when the button is pressed
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=my_callback, bouncetime=BTime)
    while True:
        time.sleep(5)

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    finally:
        GPIO.cleanup() 