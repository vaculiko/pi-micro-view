# from main import *
# print("All libraries imported successfully!")


def test_camera():
    from time import sleep
    from picamera import PiCamera

    with PiCamera() as camera:
        camera.resolution = (3280, 2464)
        camera.start_preview()
        camera.annotate_text = f"Resolution {camera.resolution}"
        print(camera.framerate)
        sleep(2)
        camera.capture("/home/pi/Desktop/test.png")
        print("image taken")
        sleep(2)
        camera.close()


def test_buttons():
    from main import button1, button2, button3, button4

    print("Press any button:")

    def message():
        print(button1.is_active)
        print(button2.is_active)
        print(button3.is_active)
        print(button4.is_active)
        print("\n")

    button1.when_pressed = message
    button2.when_pressed = message
    button3.when_pressed = message
    button4.when_pressed = message


if __name__ == "__main__":
    test_camera()
    # test_buttons()
