import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11 --- led
BtnPin = 32    # pin32 --- button
BTime = 500
Led_status = 0

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.output(LedPin, GPIO.LOW) # Set LedPin high(0.0V) to off led

def my_callback(channel):
    global Led_status
    Led_status = not Led_status
    GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
    if Led_status == 0:
        print('led off...')
    else:
        print('...led on')
                                              
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