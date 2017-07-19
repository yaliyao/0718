import RPi.GPIO as GPIO
import time

LedPin = 11   # LED
PIRPin = 15   # PIR

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)        # LED output pin
    GPIO.setup(PIRPin, GPIO.IN)         # Read output from PIR motion sensor

def loop():    
    while True:
       if GPIO.input(PIRPin) == 0:            # When output from motion sensor is LOW
             print("No motion")
             GPIO.output(LedPin, GPIO.LOW)    # Turn OFF LED
             time.sleep(1)
       else:                                  # When output from motion sensor is HIGH
             print("Motion detected")
             GPIO.output(LedPin, GPIO.HIGH)   # Turn ON LED
             time.sleep(1)

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print('Quitting')
    finally:
        GPIO.cleanup()
