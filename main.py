import os
from time import sleep
from signal import pause
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime

# https://roboticadiy.com/how-to-debounce-push-button-in-raspberry-pi-4/
button1 = Button(25)
button2 = Button(8)
button3 = Button(7)
button4 = Button(1)

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 30


def set_saving_directory():
    drive_name = os.listdir("/media/pi")
    if drive_name == []:
        os.chdir("/home/pi/Desktop")
    else:
        os.chdir("/media/pi/" + drive_name[0])


def take_picture():
    date_string = datetime.now().strftime("%Y%m%d-%H%M%S")
    print(f"Image {date_string} captured")
    camera.annotate_text = ""
    set_saving_directory()
    camera.capture(f"image-{date_string}.png", use_video_port=True)
    camera.annotate_text = f"Image {date_string} saved to {os.getcwd()}!"
    sleep(0.1)


def zoom_preview():
    no_zoom = (0.0, 0.0, 1.0, 1.0)
    zoom2x = (0.25, 0.25, 0.75, 0.75)
    if camera.zoom() == no_zoom:
        camera.zoom(zoom2x)
        camera.annotate_text = "Zoom: 2x"
    else:
        camera.zoom(no_zoom)
        camera.annotate_text = "Zoom: 0x"


def exposure_lock():
    if camera.exposure_mode() == "auto":
        camera.exposure_mode("off")
    else:
        camera.exposure_mode("auto")
    camera.annotate_text = f"Exposure mode {camera.exposure_mode()}"


def stop():
    camera.stop_preview()
    camera.close()
    quit()


if __name__ == "__main__":
    camera.start_preview()
    camera.annotate_text = f"Resolution {camera.resolution}"
    button1.when_pressed = take_picture
    button2.when_pressed = zoom_preview
    # button3.when_pressed = take_picture
    button4.when_pressed = stop
