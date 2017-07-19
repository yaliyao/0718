# Script to display the digits of pi in binary on leds
#
# pin# :  7   11   15   29
# gpio#:  4   17   22    5
#
#
import os
import time
import RPi.GPIO as GPIO

Led1 = 7     # Led1
Led2 = 11    # Led2
Led3 = 15    # Led3
Led4 = 29    # Led4

def setup():
    GPIO.setmode(GPIO.BOARD)      # Numbers GPIOs by physical location
    #GPIO.setwarnings(False)
    GPIO.setup(Led1,GPIO.OUT)     # Set Led's mode is output
    GPIO.setup(Led2,GPIO.OUT)
    GPIO.setup(Led3,GPIO.OUT)
    GPIO.setup(Led4,GPIO.OUT)
    GPIO.output(Led1, GPIO.LOW)  # Set Led low(0.0V) to off led
    GPIO.output(Led2, GPIO.LOW)
    GPIO.output(Led3, GPIO.LOW)
    GPIO.output(Led4, GPIO.LOW)

def loop():
    number_seq = '31415926535897932384'
    number_list = list(number_seq)

    for n in number_list:
        if n == '0':
            time.sleep(1)
        if n == '1':
            GPIO.output(Led1, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(Led1, GPIO.LOW)
        if n == '2':
            GPIO.output(Led2, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(Led2, GPIO.LOW)
        if n == '3':
            GPIO.output(Led1, GPIO.HIGH)
            GPIO.output(Led2, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(Led1, GPIO.LOW)
            GPIO.output(Led2, GPIO.LOW)
        if n == '4':
            GPIO.output(Led3, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(Led3, GPIO.LOW)
        if n == '5':
            GPIO.output(Led1, GPIO.HIGH)
            GPIO.output(Led3, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(Led1, GPIO.LOW)
            GPIO.output(Led3, GPIO.LOW)
        if n == '6':
            GPIO.output(Led2, GPIO.HIGH)
            GPIO.output(Led3, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(Led2, GPIO.LOW)
            GPIO.output(Led3, GPIO.LOW)
        if n == '7':
            GPIO.output(Led1, GPIO.HIGH)
            GPIO.output(Led2, GPIO.HIGH)
            GPIO.output(Led3, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(Led1, GPIO.LOW)
            GPIO.output(Led2, GPIO.LOW)
            GPIO.output(Led3, GPIO.LOW)
        if n == '8':
            GPIO.output(Led4, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(Led4, GPIO.LOW)
        if n == '9':
            GPIO.output(Led1, GPIO.HIGH)
            GPIO.output(Led4, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(Led1, GPIO.LOW)
            GPIO.output(Led4, GPIO.LOW)

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except:
        print('Quitting')
    finally:
        GPIO.cleanup()
