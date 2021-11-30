#!/bin/bash
echo "Raspberry Pi Update"
sudo apt update && sudo apt full-upgrade -y 
sudo rpi-update -y
sudo apt autoremove -y
sudo apt autoclean -y
sudo reboot
