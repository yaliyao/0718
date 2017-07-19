from gpiozero import LED
from gpiozero import MotionSensor
import time

led = LED(17)
pir = MotionSensor(22)

print("Waiting for PIR to settle")
pir.wait_for_no_motion()

while True:
    led.off()
    print("Ready")
    pir.wait_for_motion()
    led.on()
    print("Motion detected!")
    time.sleep(2)

