from gpiozero import LED
from gpiozero import LightSensor

led = LED(17)
ldr = LightSensor(12,threshold=0.9)

ldr.when_dark = led.on
ldr.when_light = led.off

while True:
    ldr.wait_for_light()
    print("Light detected!")

    ldr.wait_for_dark()
    print("Light disappear!")
