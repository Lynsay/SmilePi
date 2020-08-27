'''
    Desc: Draw a smile on a Pimoroni Unicorn pHat.

    Author: Lynsay A. Shepherd

    Date: July 2020

'''

#!/usr/bin/env python

import time
from time import sleep
import colorsys
import unicornhat as unicorn


print("Generate a smile")

spacing = 360.0 / 16.0
hue = 0

#consider the size of the unicorn pHAT
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(1)
width,height=unicorn.get_shape()

#based on the examples from https://github.com/pimoroni/unicorn-hat

def drawSmile():
    hue = int(time.time() * 100) % 360
    for y in range(height):
        
        for x in range(width):
            #cycle through colours
            offset = x * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]

            #basic smile
            #left side
            unicorn.set_pixel(0,1,r, g, b)
            unicorn.set_pixel(1,2,r, g, b)
            #bottom line
            unicorn.set_pixel(2,3,r, g, b)
            unicorn.set_pixel(3,3,r, g, b)
            unicorn.set_pixel(4,3,r, g, b)
            unicorn.set_pixel(5,3,r, g, b)
            #right side
            unicorn.set_pixel(7,1,r, g, b)
            unicorn.set_pixel(6,2,r, g, b)


            unicorn.show()
            time.sleep(0.25)

while True:
    drawSmile()
