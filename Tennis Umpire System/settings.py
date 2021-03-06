import pygame as pg 
import random
pg.init()
#Colour RGB values
WHITE = (255,255,255)
BLACK = (0,0,0)
DARKGREY = (40,40,40)
LIGHTGREY = (100,100,100)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
BROWN = (106,55,5)
CYAN = (0,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
DARKGREEN = (0,125,0)

#Players
PLAYER1 = "Player 1"
PLAYER2 = "Player 2"
POINTS = [0, 15, 30, 40, "AD"]

#Game startup settings
WIDTH = 1600
HEIGHT = 760
FPS = 120
TITLE = "Umpire Tennis Scoreboard"
BGCOLOUR = BROWN
DEFAULT_SETS = 5
WINNER = "Null"
FONT = pg.font.Font(None, 32)

#Various GUI image locations
MAIN_MENU_IMG = pg.transform.scale(pg.image.load("img/tilemap/mainmenu.png"), (WIDTH, HEIGHT))
SERVER_IMG = pg.transform.scale(pg.image.load("img/tilemap/server.png"),(30,30))

#Music settings
BG_MUSIC_VOLUME = 0.2

#Variables for the size and positioning of the point boxes
POINTS_BOX_WIDTH = WIDTH/8
POINTS_BOX_HEIGHT = POINTS_BOX_WIDTH
POINTS_BOX_OFFSET = 5
POINTS_BOX_X_1 = 35
POINTS_BOX_Y_1 = HEIGHT - POINTS_BOX_HEIGHT - POINTS_BOX_X_1
POINTS_BOX_X_2 = POINTS_BOX_X_1
POINTS_BOX_Y_2 = POINTS_BOX_Y_1 - POINTS_BOX_OFFSET - POINTS_BOX_HEIGHT

SETS_BOX_WIDTH = POINTS_BOX_WIDTH * (DEFAULT_SETS)
SETS_BOX_HEIGHT = POINTS_BOX_HEIGHT
SETS_BOX_X = WIDTH-SETS_BOX_WIDTH - POINTS_BOX_X_1
SETS_BOX_Y = HEIGHT - SETS_BOX_HEIGHT - POINTS_BOX_X_1
SETS_BOX_OFFSET = POINTS_BOX_OFFSET

#Controls
ADD_POINT_P1 = pg.K_1
ADD_POINT_P2 = pg.K_2
REMOVE_POINT_P1 = pg.K_3
REMOVE_POINT_P2 = pg.K_4
PAUSE = pg.K_p
KILL_PROGRAM = pg.K_ESCAPE