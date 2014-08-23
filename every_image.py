#!/usr/bin/python

import sys
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
  DISPLAYSURF.fill(WHITE)
  array.paint(DISPLAYSURF)
  array.inc()

#run the game loop
while True:
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()
    py.display.update()
