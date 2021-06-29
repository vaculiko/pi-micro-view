import os
import datetime as dt
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 30

drive_name = os.listdir('/media/pi')[0]
os.chdir('/media/pi/' + drive_name)
print('Saving files to', os.getcwd())

def button_callback(channel):
    date_string = dt.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    print(f'Image {date_string} captured')
    camera.capture(f'image-{date_string}.jpg', use_video_port=True)
    camera.annotate_text = f'Image {date_string} saved!'
    sleep(2)
    camera.annotate_text = ''
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback, bouncetime=100)

camera.start_preview()
message = input('Press enter to quit\n\n')
camera.stop_preview()
camera.close()
GPIO.cleanup()