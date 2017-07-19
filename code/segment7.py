import RPi.GPIO as GPIO
import time

SDI   = 11   # serial data input
RCLK  = 12   # memory clock input(STCP)
SRCLK = 13   # shift register clock input(SHCP)

segCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]

def print_msg():
    print('Program is running...')
    print('Please press Ctrl+C to end the program...')

def setup():
    GPIO.setmode(GPIO.BOARD)    #Number GPIOs by its physical location
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.output(SDI, GPIO.LOW)
    GPIO.output(RCLK, GPIO.LOW)
    GPIO.output(SRCLK, GPIO.LOW)

def hc595_shift(dat):
    for bit in range(0, 8):	
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

def loop():
    while True:
        for i in range(0, len(segCode)):
            hc595_shift(segCode[i])
            time.sleep(0.5)

# If run this script directly, do:
if __name__ == '__main__':
    print_msg()
    setup()
    try:
        loop()
    except:
        print("Quitting")
    finally:
        hc595_shift(0x00)
        GPIO.cleanup()
