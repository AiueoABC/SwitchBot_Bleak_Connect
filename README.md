# Control SwitchBot using Bleak (for Windows10 compatibility)
Control SwitchBot from Windows10 using BLE library, bleak, on Python.

## Requirements
* OS Windows10, version 16299 (Fall Creators Update) or greater
* python 3.7.6 or greater
* bleak 0.7.1 or greater, `pip install bleak`
* Bluetooth support v5.0 or higher

Make sure your Window can access to bluetooth device and ready to communicate via BLE.

## Contents

- [Discover.py]: This will find bluetooth devices available. SwitchBot is shown as some special devices, take a note of that MAC address.
- [Bleak_Connect_SwitchBot.py]: Main script to control SwitchBot. Use MAC address found with above script. * [address] value need to be changed.


