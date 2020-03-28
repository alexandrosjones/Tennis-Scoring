import pygame as pg 
import sys
import random

Running = True

while Running:
    screen = pg.display.set_mode((600, 600))
    screen.fill((0,100,0))
    pg.draw_rect()
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

def quit():
    pg.quit()
    sys.exit()