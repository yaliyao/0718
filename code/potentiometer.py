import RPi.GPIO as GPIO
import time

a_pin = 18
b_pin = 23

def setup():
    GPIO.setmode(GPIO.BCM)

def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, GPIO.LOW)
    time.sleep(0.05)

def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    count = 0
    GPIO.output(a_pin, GPIO.HIGH)
    while not GPIO.input(b_pin):
        count = count + 1
    return count

def analog_read():
    discharge()
    return charge_time()

def loop():
    while True:
        print(analog_read())
        time.sleep(1)

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  
        print('Quitting')
    finally:
        GPIO.cleanup()
