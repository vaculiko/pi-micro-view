import os
from time import sleep
from signal import pause
from gpiozero import Button
from picamera import PiCamera, Color
from datetime import datetime

# https://roboticadiy.com/how-to-debounce-push-button-in-raspberry-pi-4/
button1 = Button(8)
button2 = Button(25)
button3 = Button("BOARD28")
button4 = Button(7)

camera = PiCamera(resolution=(3280, 2464))
camera.color_effects = (128, 128)


def welcome_screen():
    camera.awb_mode = "off"
    camera.annotate_text_size = 100
    camera.annotate_background = Color("black")
    camera.annotate_text = """Pi Microscope Viewer
1 - Take picture
2 - Zoom 2x
3 - Exposure lock
4 - Take 10s video
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
    camera.capture(f"image-{date_string}.png", use_video_port=False)
    camera.annotate_text = f"Image saved to {os.getcwd()}!"
    # sleep(0.2)


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


def bw_toggle():
    if camera.color_effects == (128, 128):
        camera.color_effects = None
    else:
        camera.color_effects = (128, 128)
        
        
def record_video(duration: int):
    date_string = datetime.now().strftime("%Y%m%d-%H%M%S")
    camera.annotate_text = ""
    set_saving_directory()
    camera.start_recording(f'video-{date_string}.mjpeg')
    camera.wait_recording(duration)
    camera.stop_recording()
    camera.annotate_text = f"Video saved to {os.getcwd()}!"


def record_10s():
    record_video(10)

def stop():
    camera.stop_preview()
    camera.close()
    quit()


def reboot():
    os.system("sudo reboot")


if __name__ == "__main__":
    camera.start_preview()
    welcome_screen()
    camera.annotate_text = f"Resolution {camera.resolution}"
    try:
        while True:
            button1.when_pressed = take_picture
            button2.when_pressed = zoom_preview
            button3.when_pressed = exposure_lock
            button4.when_pressed = record_10s

            button1.when_held = None
            button2.when_held = None
            button3.when_held = None
            button4.when_held = stop
    except KeyboardInterrupt:
        pass