import os
from time import sleep
from signal import pause
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime

# https://roboticadiy.com/how-to-debounce-push-button-in-raspberry-pi-4/
button = Button(2)
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 30


def set_saving_directory():
    drive_name = os.listdir('/media/pi')
    if drive_name == []:
        os.chdir('/home/pi/Desktop')
    else:
        os.chdir('/media/pi/' + drive_name[0])


def take_picture():
    date_string = datetime.now().strftime("%Y%m%d-%H%M%S")
    print(f'Image {date_string} captured')
    camera.annotate_text = ''
    set_saving_directory()
    camera.capture(f'image-{date_string}.png', use_video_port=True)
    camera.annotate_text = f'Image {date_string} saved to {os.getcwd()}!'
    sleep(.1)


def shutdown():
    camera.stop_preview()
    camera.close()
    quit()
    

camera.start_preview()
camera.annotate_text = f'Resolution {camera.resolution}'
button.when_held = shutdown
button.when_pressed = take_picture
pause()
