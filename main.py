import os
from time import sleep
from signal import pause
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime

# https://roboticadiy.com/how-to-debounce-push-button-in-raspberry-pi-4/
button1 = Button(7)
button2 = Button("BOARD28")
button3 = Button(25)
button4 = Button(8)

camera = PiCamera()
camera.resolution = (1024, 768)
camera.framerate = 30


def welcome_screen():
    camera.awb_mode = "off"
    camera.annotate_text_size = 50
    # camera.annotate_text = 5*"Some very long text\n"
    camera.annotate_text = """Pi Microscope Viewer

1 - Take picture
2 - Zoom 2x
3 - Exposure lock
4 - White balance lock

Press 1 to continue."""
    button1.wait_for_press()
    camera.annotate_text_size = 40
    camera.annotate_text = ""
    camera.awb_mode = "auto"


def set_saving_directory():
    try:
        drive_name = os.listdir("/media/pi")
        os.chdir("/media/pi/" + drive_name[0])
    except:
        os.chdir("/home/pi/Desktop")


def take_picture():
    date_string = datetime.now().strftime("%Y%m%d-%H%M%S")
    print(f"Image {date_string} captured")
    camera.annotate_text = ""
    set_saving_directory()
    camera.capture(f"image-{date_string}.png")
    camera.annotate_text = f"Image {date_string} saved to {os.getcwd()}!"
    sleep(0.2)


def zoom_preview():
    no_zoom = (0.0, 0.0, 1.0, 1.0)
    zoom2x = (0.25, 0.25, 0.5, 0.5)
    if camera.zoom == no_zoom:
        camera.zoom = zoom2x
        camera.annotate_text = "Zoom: 2x"
    else:
        camera.zoom = no_zoom
        camera.annotate_text = "Zoom: 0x"
    sleep(0.2)


def exposure_lock():
    if camera.exposure_mode == "auto":
        camera.exposure_mode = "off"
    else:
        camera.exposure_mode = "auto"
    camera.annotate_text = f"Exposure mode {camera.exposure_mode}"
    sleep(0.2)


def awb_lock():
    if camera.awb_mode == "auto":
        camera.awb_mode = "tungsten"
    else:
        camera.awb_mode = "auto"
    camera.annotate_text = f"White balance {camera.awb_mode}"
    sleep(0.2)


def stop():
    camera.stop_preview()
    camera.close()
    quit()


if __name__ == "__main__":
    camera.start_preview()
    welcome_screen()
    camera.annotate_text = f"Resolution {camera.resolution}"
    button1.when_pressed = take_picture
    button2.when_pressed = zoom_preview
    button3.when_pressed = exposure_lock
    button4.when_pressed = awb_lock
