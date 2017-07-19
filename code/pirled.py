from gpiozero import LED
from gpiozero import MotionSensor

led = LED(17)
pir = MotionSensor(22)

pir.when_motion = led.on
pir.when_no_motion = led.off

pir.wait_for_motion()
print("Motion detected!")

pir.wait_for_no_motion()
print("No motion!")