import pygame as pg 
import random
import sys
from os import path
from settings import *

#Game class
class Game:
    #Init function to start the game variables
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500,100)
        #self.screen_scenario = WELCOME
        self.load_data()
        self.P1_Score = int(0)
        self.P2_Score = int(0)
        self.P1_Games = int(0)
        self.P2_Games = int(0)
        self.P1_Sets = int(0)
        self.P2_Sets = int(0)
        self.Game_Deuce = False
        self.Game_Advantage = False
        self.Game_Tiebreaker = False
        #self.Game_Winner = False
        self.sets = DEFAULT_SETS

    #Draw text function that takes: Text to display, Font of text, Size of text, Colour of text, x coord, y coord, alignment within text box
    def draw_text(self, text, font_name, size, colour, x, y, align = "nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    #Path for all the files required for the game
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "img")
        music_folder = path.join(game_folder, "music")
        fonts_folder = path.join(game_folder, "fonts")

        self.title_font = path.join(fonts_folder, "LemonMilk.otf")
        self.hud_font = path.join(fonts_folder, "Impacted2.0.ttf")
        self.text_font = path.join(fonts_folder, "CaviarDreams_Bold.ttf")
        self.points_font = path.join(fonts_folder, "scoreboard.ttf")
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()

    #Function to start a new game
    def new(self):
        self.paused = False
        self.screen.fill(DARKGREEN)

    def end_game(self):
        self.P1_Score = 0
        self.P2_Score = 0

    #Checks whether to enter a deuce or advantage mode
    def check_state(self):
        if self.P1_Score == 3 and self.P2_Score == 3:
            self.Game_Deuce = True
            self.Game_Advantage = False
        if (self.P1_Score == 4 and self.P2_Score == 3) or (self.P1_Score == 3 and self.P2_Score == 4):
            self.Game_Deuce = False
            self.Game_Advantage = True
        if (self.P1_Score == 5 and self.P2_Score == 3) or (self.P1_Score == 3 and self.P2_Score == 5):
            self.Game_Deuce = False
            self.Game_Advantage = False
        if (self.P1_Score == 4 and self.P2_Score == 4):
            self.P1_Score = 3
            self.P2_Score = 3
            self.Game_Advantage = False
            self.Game_Deuce = True

    #Functions for adding/removing points to a player
    def add_point_1(self):
        if self.P1_Score < 4 and self.Game_Deuce == False:
            self.P1_Score = self.P1_Score + 1
        print("P1 score is now:", self.P1_Score)

    def add_point_2(self):
        if self.P2_Score < 4:
            self.P2_Score = self.P2_Score + 1
        print("P2 score is now:", self.P2_Score)

    def remove_point_1(self):
        if int(self.P1_Score) > 0:
            self.P1_Score = self.P1_Score - 1
            print("1 point removed added from P1")
        print("P1 score is now:", self.P1_Score)

    def remove_point_2(self):
        if int(self.P2_Score) > 0:
            self.P2_Score = self.P2_Score - 1
            print("1 point removed added from P2")
        print("P1 score is now:", self.P2_Score)

    def add_game_1(self):
        if self.P1_Score >= 4 and self.P2_Score <= self.P1_Score - 2:
            print("P1 just won a game")
            self.end_game()
            self.P1_Games = self.P1_Games + 1
            print("P1 now has",self.P1_Games,"game(s)")

    def add_game_2(self):
        if self.P2_Score >= 4 and self.P1_Score <= self.P2_Score - 2:
            print("P2 just won a game")
            self.end_game()
            self.P2_Games = self.P2_Games + 1
            print("P2 now has",self.P2_Games,"game(s)")

    def add_set_1(self):
        pass

    def add_set_2(self):
        pass

    def deuce(self):
        print("Deuce")

    def tiebreaker(self):
        pass

    #Function to run the scoreboard
    def run(self):
        self.playing = True
        #pg.mixer.music.play(loops=-1)
        #pg.mixer.music.set_volume(BG_MUSIC_VOLUME)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            if not self.paused:
                self.update()
            self.draw()

    #Quit function
    def quit(self):
        pg.quit()
        sys.exit()

    #Update function that gets called in a loop to then call all the other functions that need to be run
    def update(self):
        #Check scoring to update and reset games
        self.add_game_1()
        self.add_game_2()
        self.add_set_1()
        self.add_set_2()
        self.deuce()
        self.tiebreaker()
        self.check_state()
        
        #print(self.P1_Games)

    #Draw function to blit all the text and scores onto the screen
    def draw(self):
        #Points box No.1
        pg.draw.rect(self.screen, BLACK, (POINTS_BOX_X_1, POINTS_BOX_Y_1, POINTS_BOX_WIDTH, POINTS_BOX_HEIGHT))
        #Points box No.2
        pg.draw.rect(self.screen, BLACK, (POINTS_BOX_X_2, POINTS_BOX_Y_2, POINTS_BOX_WIDTH, POINTS_BOX_HEIGHT))
        
        #If for how many sets there are:
        if self.sets == 5:
            #Sets box No.1
            pg.draw.rect(self.screen, BLACK, (SETS_BOX_X, SETS_BOX_Y, SETS_BOX_WIDTH, SETS_BOX_HEIGHT))  
            #Sets box No.2
            pg.draw.rect(self.screen, BLACK, (SETS_BOX_X, SETS_BOX_Y - SETS_BOX_HEIGHT - SETS_BOX_OFFSET, SETS_BOX_WIDTH, SETS_BOX_HEIGHT))       

        #Text
        self.draw_text("The National Championships", self.text_font, 80, WHITE, WIDTH/2, 55, align = "center")
        self.draw_text("Points", self.text_font, 40, WHITE, POINTS_BOX_X_1, POINTS_BOX_Y_2 - (5*POINTS_BOX_OFFSET), align="w")

        #Points
        self.draw_text(str(self.P1_Score*15), self.points_font, 180, YELLOW, POINTS_BOX_X_2, POINTS_BOX_Y_2)
        self.draw_text(str(self.P2_Score*15), self.points_font, 180, YELLOW, POINTS_BOX_X_1, POINTS_BOX_Y_1)

        #Update the screen
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.type == KILL_PROGRAM:
                    self.quit()
                if event.key == PAUSE:
                    self.paused = not self.paused
                if event.key == ADD_POINT_P1:
                    self.add_point_1()
                if event.key == ADD_POINT_P2:
                    self.add_point_2()
                if event.key == REMOVE_POINT_P1:
                    self.remove_point_1()
                if event.key == REMOVE_POINT_P2:
                    self.remove_point_2()

    def show_start_screen(self):
        self.screen.blit(MAIN_MENU_IMG, (0,0))
        self.draw_text("Welcome to the National Championships", self.title_font, 60, WHITE, WIDTH/2, HEIGHT/2, align="center")
        self.draw_text("Press any key to start setup process", self.text_font, 45, WHITE, WIDTH/2, HEIGHT/2 + 120, align="center")
        pg.display.flip()
        self.wait_for_key()

    def show_setup_screen(self):
        self.screen.blit(SETUP_IMG, (0,0))
        pg.display.flip()
        self.wait.for_key()

    def wait_for_key(self):
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False

#Create game object
g = Game()
g.show_start_screen()

while True:
    g.new()
    g.run()