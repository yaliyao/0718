from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(12)

led.source = button.values

pause()