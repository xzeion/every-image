#!/usr/bin/python

import sys
from pixel_array import PixelArray
import pygame as py
from pygame.locals import *


width = 10
height = 10


py.init()
array = PixelArray(10, 10, 3)
#set up the window
DISPLAYSURF = py.display.set_mode((width,height),0,32)
py.display.set_caption('Drawing')


#draw on the surface object
def loop_step():
  array.paint(DISPLAYSURF)
  array.inc()

#run the game loop
while True:
    loop_step()
    py.display.update()
