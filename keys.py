#!/usr/bin/env python
import keybow
import time
import os

keybow.setup(keybow.MINI)

keybow.set_led(0, 0, 0, 127)
keybow.set_led(1, 0, 127, 0)
keybow.set_led(2, 127, 0, 0)


@keybow.on(index=0)
def handle_key(index, state=True):
    print("{}: Key {} has been {}".format(
        time.time(),
        index,
        'pressed' if state else 'released'))
    
    if state:
        keybow.set_led(index, 0, 0, 255)
        os.system("ssh pi@192.168.9.44 sudo systemctl restart mopidy")
    else:
        keybow.set_led(index, 0, 0, 127)

@keybow.on(index=1)
def handle_key(index, state):
    print("{}: Key {} has been {}".format(
        time.time(),
        index,
        'pressed' if state else 'released'))

    if state:
        keybow.set_led(index, 0, 255, 0)
        os.system("mpc -h 192.168.9.44 clear; mpc -h 192.168.9.44 add http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p; mpc -h 192.168.9.44 play")
    else:
        keybow.set_led(index, 0, 127, 0)

@keybow.on(index=2)
def handle_key(index, state):
    print("{}: Key {} has been {}".format(
        time.time(),
        index,
        'pressed' if state else 'released'))

    if state:
        keybow.set_led(index, 255, 0, 0)
        os.system("mpc -h 192.168.9.44 clear; mpc -h 192.168.9.44 add tunein:station:s266113; mpc -h 192.168.9.44 play")
    else:
        keybow.set_led(index, 127, 0, 0)

while True:
    keybow.show()
    time.sleep(1.0 / 60.0)
