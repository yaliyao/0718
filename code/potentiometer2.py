import RPi.GPIO as GPIO
import time, math

C = 0.12 # uF
R1 = 1000 # Ohms, connect to gpio

# Pin a charges the capacitor through a fixed 1k resistor
# and the pot in series
# Pin b discharges the capacitor through a fixed 1k resistor
a_pin = 18
b_pin = 23

def setup():
    GPIO.setmode(GPIO.BCM)

# Discharge the capacitor, leaving it ready to start filling up
def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, GPIO.LOW)
    time.sleep(0.05)

# Return the time taken (uS) for the voltage on the capacitor
# to count as a digital input HIGH
# which is 1.65V or higher
def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    GPIO.output(a_pin, GPIO.HIGH)
    t1 = time.time()
    while not GPIO.input(b_pin):
        pass
    t2 = time.time()
    return (t2 - t1) * 1000000

# Take an analog reading as the time taken to charge after
# first discharging the capacitor
def analog_read():
    discharge()
    t = charge_time()
    discharge()
    return t

# Convert the time taken to charge the cpacitor into a value of resistance
# To reduce errors, do it 100 times and take the average
def read_resistance():
    n = 10
    total = 0;
    for i in range(0, n):
        total += analog_read()
    t = total / float(n)
    T = t * 0.632 * 3.3
    r = (T / C) - R1     # subtract resistance connected to gpio
    # r = T / C          # will return real resistance
    return r

def loop():
    while True:
        print(read_resistance())
        time.sleep(0.5)

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  
        print('Quitting')
    finally:
        GPIO.cleanup()
