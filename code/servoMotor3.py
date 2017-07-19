import RPi.GPIO as GPIO
import time
import os

ServoPin = 11     # pin 11(GPIO 17) connect to servo signal line(yellow wire)
                  # send PWM signal to control servo motion

# You can play with the values.
# 7.5 is in most cases the middle position
# 12.5 is the value for a 180 degree move to the right
# 3.0 is the value for a -90 degree move to the left
RightDC = 12.5
MiddleDC = 7.5
LeftDC = 3.0


def setup():
    # Set the layout for the pin declaration
    global Servo
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ServoPin, GPIO.OUT)

    # Now we will start with a PWM signal at 50Hz 
    # 50Hz should work for many servos very will. If not you can play with the frequency if you like.
    Servo = GPIO.PWM(ServoPin, 50)


def loop():
    # This command sets the left position of the servo
    Servo.start(LeftDC)

    while True:
        # menu info
        print("l = move to the left")
        print("r = move to the right")
        print("m = move to the middle")
        print("t = test sequence")
        print("q = stop and exit")

        # Now the program asks for the direction the servo should turn.
        ans = input("Selection: ") 

        if(ans == "t"):
            print("move to the center position:")
            Servo.ChangeDutyCycle(MiddleDC)
            time.sleep(1)
            print("move to the right position:")
            Servo.ChangeDutyCycle(RightDC)
            time.sleep(1)
            print("move to the left position:")
            Servo.ChangeDutyCycle(LeftDC)
            time.sleep(1)
            continue

        # direction right
        if(ans == "r"):
            # how many steps should the move take.
            steps = input("steps (1 - 10): ") 
            print(steps, "steps to the right")
            stepslength = (RightDC - LeftDC) / int(steps)
            for Counter in range(int(steps)):
                dc = round(LeftDC + stepslength * (Counter + 1),1)
                Servo.ChangeDutyCycle(dc)
                print(dc)
                time.sleep(0.5)

            time.sleep(1)
            
        # move to the center position
        elif(ans == "m"):
            print("Move back to the center position.")
            Servo.start(MiddleDC)
            time.sleep(1)
            
        # move to the left
        elif(ans == "l"):
            print("Move to the max right position and then to the left position.")
            Servo.start(RightDC)
            # how many steps...
            steps = input("steps (1 - 10): ") 
            print(steps, "steps to the left")
            stepslength = (RightDC - LeftDC) / int(steps)
            for Counter in range(int(steps)):
                dc = round(RightDC - (stepslength * (Counter + 1)),1)
                Servo.ChangeDutyCycle(dc)
                print(dc)
                time.sleep(0.5)

            time.sleep(1)

        # close program
        elif(ans == "q"):
            print("stop the program and exit......")
            break

        # input not valid
        else:
            print("input not valid!")

        print("Move back to start position.")
        Servo.ChangeDutyCycle(LeftDC)

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
