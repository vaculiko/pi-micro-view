# pi-micro-view

Raspberry Pi microscope viewer - display, take images, live image processing and more.

## TODO

- [x] GPIO button input
- [x] Button press saves picture
- [x] Filename with date and time
- [x] Locate USB drive and save images there
- [x] [Auto launch after boot](https://www.itechfy.com/tech/auto-run-python-program-on-raspberry-pi-startup/)
- [ ] PySimpleGUI for folder selection, preview?
- [ ] Bash script for dependency installation
- [ ] Script to enable camera, VNC
- [ ] Welcome screen

### Welcome screen

Black background using `AWB_mode = 'off'`

| Button | Short press        | Long press |
|:------:|:------------------ |:---------- |
| 1      | Take picture       |            |
| 2      | Zoom 2x            |            |
| 3      | Exposure lock      |            |
| 4      | White balance lock |            |

### Connection
1 GND - Pin 30 (GND)
5 Button - Pin 25
