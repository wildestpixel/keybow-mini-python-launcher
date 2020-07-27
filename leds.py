#!/usr/bin/env python
import keybow
import time
import colorsys
import os

keybow.setup(keybow.MINI)


colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255)
]

@keybow.on(index=0)
def handle_key(index, state=True):
    # print("{}: Key {} has been {}".format(
    #     time.time(),
    #     index,
    #     'pressed' if state else 'released'))
    
    if state:
        #keybow.set_led(index, 0, 0, 255)
        os.system("ssh pi@192.168.9.44 sudo systemctl restart mopidy")
    else:
        pass
        #keybow.set_led(index, 0, 0, 127)

@keybow.on(index=1)
def handle_key(index, state):
    # print("{}: Key {} has been {}".format(
    #     time.time(),
    #     index,
    #     'pressed' if state else 'released'))

    if state:
        #keybow.set_led(index, 0, 255, 0)
        os.system("mpc -h 192.168.9.44 clear; mpc -h 192.168.9.44 add http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p; mpc -h 192.168.9.44 play")
    else:
        pass
        #keybow.set_led(index, 0, 127, 0)

@keybow.on(index=2)
def handle_key(index, state):
    # print("{}: Key {} has been {}".format(
    #     time.time(),
    #     index,
    #     'pressed' if state else 'released'))

    if state:
        #keybow.set_led(index, 255, 0, 0)
        os.system("mpc -h 192.168.9.44 clear; mpc -h 192.168.9.44 add tunein:station:s266113; mpc -h 192.168.9.44 play")
        # os.system("mpc -h 192.168.9.44 status")
    else:
        pass
        #keybow.set_led(index, 127, 0, 0)


try:
    for x in range(len(colors) * 2):
        r, g, b = colors[0]
        for x in range(3):
            keybow.set_pixel(x, r, g, b)
        colors.append(colors.pop(0))
        keybow.show()
        time.sleep(0.5)

    while True:
        t = time.time()
        for x in range(3):
            h = t / 10.0
            h += x / 12.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            keybow.set_pixel(x, r, g, b)
        keybow.show()
        time.sleep(1.0 / 60)

except KeyboardInterrupt:
    pass