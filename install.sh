#!/bin/bash

echo "Enable camera"
sudo raspi-config nonint do_camera 0

echo "Increasing GPU memory to 512"
sed -i "s/^gpu_mem.*/gpu_mem=512/" /boot/config.txt

echo "Installing requirements for pi-micro-view"
pip3 install -r requirements.txt