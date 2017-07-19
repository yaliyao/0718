import RPi.GPIO as GPIO
import time

ServoPin = 11     # pin 11(GPIO 17) connect to servo signal line(yellow wire)
                  # send PWM signal to control servo motion

def setup():
    # Set the layout for the pin declaration
	global Servo
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ServoPin, GPIO.OUT)
    Servo = GPIO.PWM(ServoPin, 50)

def loop():
    # Now we will start with a PWM signal at 50Hz 
    # 50Hz should work for many servos very will. If not you can play with the frequency if you like.
    
    # This command sets the left position of the servo
    Servo.start(3.0)

    while True:
        Servo.ChangeDutyCycle(7.5)
        time.sleep(1)

        Servo.ChangeDutyCycle(12.5)
        time.sleep(1)

        Servo.ChangeDutyCycle(3.0)
        time.sleep(1)

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        loop()
    except:
        print("Quitting")
    finally:
        Servo.stop()
        GPIO.cleanup()
