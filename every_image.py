#!/usr/bin/python

import sys
import pygame as py
from pygame.locals import *

py.init()

#set up the window
DISPLAYSURF = py.display.set_mode((500,400),0,32)
py.display.set_caption('Drawing')

#set up the colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#draw on the surface object
DISPLAYSURF.fill(WHITE)

pixObj = py.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

#run the game loop
while True:
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()
    py.display.update()
