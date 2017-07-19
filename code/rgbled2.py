import RPi.GPIO as GPIO
import random, time

ledRed = 17
ledGreen = 27
ledBlue = 22
freq = 100 #Hz

def setup():
    global RED,GREEN,BLUE

    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)

    # Set pins to output mode
    GPIO.setup(ledRed, GPIO.OUT)
    GPIO.setup(ledGreen, GPIO.OUT)
    GPIO.setup(ledBlue, GPIO.OUT)

    # Setup all the LED colors as pwm channel, 
    # with an initial duty cycle of 0 which is off
    RED = GPIO.PWM(ledRed, freq)
    RED.start(0)
    GREEN = GPIO.PWM(ledGreen, freq)
    GREEN.start(0)
    BLUE = GPIO.PWM(ledBlue, freq)
    BLUE.start(0)

def color(R, G, B, on_time):
    # Color brightness range is 0-100%
    RED.ChangeDutyCycle(R)
    GREEN.ChangeDutyCycle(G)
    BLUE.ChangeDutyCycle(B)
    time.sleep(on_time)
 
    # Turn all LEDs off after on_time seconds
    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
    BLUE.ChangeDutyCycle(0)

def loop():
    print("Light It Up!")
    print("Press CTRL + C to quit.\n")
    print("R G B\n--------")
 
    # Main loop
    while True:
        for x in range(0,2):
            for y in range(0,2):
                for z in range(0,2):
                    print(x,y,z)
                    # Slowly ramp up power percentage of each active color
                    for i in range(0,101):
                        color((x*i),(y*i),(z*i), .02)

def destroy():
    # Stop all pwm channel
    RED.stop()
    GREEN.stop()
    BLUE.stop()

    # Release resource
    GPIO.cleanup()

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        loop()
    # When 'Ctrl+C' is pressed, the child program 
    # destroy() will be  executed.
    except KeyboardInterrupt:
        print("Quitting")
    finally:
        destroy()

