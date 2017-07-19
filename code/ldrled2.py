import RPi.GPIO as GPIO
import time

LedPin = 11   # LED
LdrPin = 32   # Photoresistor

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)

def light_level(pin):
    level = 0
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.setup(pin, GPIO.IN)
    while (GPIO.input(pin) == GPIO.LOW):
        level += 1
    return level

def loop():
    while True:
        print(light_level(LdrPin))
        if light_level(LdrPin) > 150:
            print("High reading: Dark")
            GPIO.output(LedPin, GPIO.HIGH)
        else:
            print("Low reading: Light")
            GPIO.output(LedPin, GPIO.LOW)

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  
        print('Quitting')
    finally:
        GPIO.cleanup()
