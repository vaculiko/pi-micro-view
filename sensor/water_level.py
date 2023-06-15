from time import sleep
from gpiozero import DigitalInputDevice

level = DigitalInputDevice(17)

while True:
    print(level.value)
    sleep(1)
