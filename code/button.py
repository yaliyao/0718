from gpiozero import Button

button = Button(12)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")