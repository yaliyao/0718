import RPi.GPIO as GPIO
import time

TRIG = 11
ECHO = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def distance():
    # Set TRIG as LOW
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.00002)
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    # Check whether the ECHO is LOW
    # Saves the last known time of LOW pulse
    while GPIO.input(ECHO) == 0:
        time1 = time.time()

    # Check whether the ECHO is HIGH
    # Saves the last known time of HIGH pulse
    while GPIO.input(ECHO) == 1:
        time2 = time.time()

    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    during = time2 - time1
    return (during * 34300) / 2 

def loop():
    while True:
        dist = distance()
        print ("Measured Distance = %.1f cm" % dist)
        time.sleep(1)

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print('Quitting')
    finally:
        GPIO.cleanup()
