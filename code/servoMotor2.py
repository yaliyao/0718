from gpiozero import AngularServo
from time import sleep

s = AngularServo(17, min_angle=-45, max_angle=45)

for t in range(0,45,15):
    s.angle = t
    sleep(1)

for t in range(45,0,-15):
    s.angle = t
    sleep(1)

