import LCD1602
import time

def setup():
    LCD1602.init(0x27, 1)     # init(slave address, background light)
    LCD1602.write(0, 0, 'Greetings!!')
    LCD1602.write(1, 1, 'from iiiedu')
    time.sleep(2)

def loop():
    space = '                '
    greetings = 'Internet Of Things Course for Raspberry! ^_^'
    greetings = space + greetings
    while True:
        tmp = greetings
        for i in range(0, len(greetings)):
            LCD1602.write(0, 0, tmp)
            tmp = tmp[1:]
            time.sleep(0.5)
            LCD1602.clear()

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        loop()
    except:
        print("Quitting")
    finally:
        LCD1602.clear()

