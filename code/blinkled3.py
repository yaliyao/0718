import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedPin, GPIO.LOW) # Set LedPin low(0.0V) to off led

def loop():
    while True:
        print('...led on')
        GPIO.output(LedPin, GPIO.HIGH)  # led on
        time.sleep(1)
        print('led off...')
        GPIO.output(LedPin, GPIO.LOW) # led off
        time.sleep(1)

def destroy():
    GPIO.output(LedPin, GPIO.LOW)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print('Quitting')
    finally:
        destroy()