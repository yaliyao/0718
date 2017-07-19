from gpiozero import Button

button = Button(12)

button.wait_for_press()
print("Button was pressed")