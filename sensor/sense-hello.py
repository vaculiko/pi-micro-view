from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.clear()
sense.set_pixel(7, 4, 255, 0, 0)
sense.set_pixel(0, 2, 0, 0, 255)

sleep(1)
