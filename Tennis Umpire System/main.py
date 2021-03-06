import pygame as pg 
import random
import sys
from os import path
from settings import *

#TODO
#Scoring + more

#Input box class
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.colour = RED
        self.text = text
        self.text_surface = FONT.render(text, True, self.colour)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.colour = BLUE if self.active else RED
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.text_surface = FONT.render(self.text, True, self.colour)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.text_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.colour, self.rect, 2)


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
        self.Game_Advantage_P1 = False
        self.Game_Advantage_P2 = False
        self.Game_Tiebreaker = False
        #self.Game_Winner = False
        self.sets = DEFAULT_SETS
        self.serve = random.choice([1,2])

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

    """def end_game(self):
        self.P1_Score = 0
        self.P2_Score = 0
        if self.serve == 1:
            self.serve = 2
        if self.serve == 2:
            self.serve = 1"""

    #Checks whether to enter a deuce or advantage mode
    """def check_state(self):
        if not self.Game_Tiebreaker:
            if self.P1_Score == 3 and self.P2_Score == 3:
                self.Game_Deuce = True
                self.Game_Advantage_P1 = False
                self.Game_Advantage_P2 = False
            if (self.P1_Score == 4 and self.P2_Score == 3):
                self.Game_Deuce = False
                self.Game_Advantage_P1 = True
                self.Game_Advantage_P2 = False
            if (self.P1_Score == 3 and self.P2_Score == 4):
                self.Game_Deuce = False
                self.Game_Advantage_P1 = False
                self.Game_Advantage_P2 = True
            if (self.P1_Score == 5 and self.P2_Score == 3):
                self.Game_Deuce = self.Game_Advantage_P1 = self.Game_Advantage_P2 = False
                self.add_game_1()
            if self.P1_Score == 3 and self.P2_Score == 5:
                self.Game_Deuce = self.Game_Advantage_P1 = self.Game_Advantage_P2 = False
                self.add_game_2()
            if (self.P1_Score == 4 and self.P2_Score == 4):
                self.P1_Score = 3
                self.P2_Score = 3
                self.Game_Advantage_P1 = False
                self.Game_Advantage_P2 = False
                self.Game_Deuce = True"""

    #Functions for adding/removing points to a player
    """def add_point_1(self):
        if self.P1_Score < 4 and self.Game_Deuce == False and self.Game_Advantage == False and self.Game_Tiebreaker == False:
            self.P1_Score = self.P1_Score + 1
        print("P1 score is now:", self.P1_Score)

    def add_point_2(self):
        if self.P2_Score < 4 and self.Game_Deuce == False and self.Game_Advantage == False and self.Game_Tiebreaker == False:
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
        if (self.P1_Score >= 4) and (self.P2_Score <= self.P1_Score - 2):
            print("P1 just won a game")
            self.end_game()
            self.P1_Games += 1
            print("P1 now has",self.P1_Games,"game(s)")
        elif (self.P1_Score == 5):
            print("P1 just won a game")
            self.end_game()
            self.P1_Games += 1
            print("P1 now has", self.P1_Games, "game(s)")

    def add_game_2(self):
        if (self.P2_Score >= 4) and (self.P1_Score <= self.P2_Score - 2):
            print("P2 just won a game")
            self.end_game()
            self.P2_Games = self.P2_Games + 1
            print("P2 now has",self.P2_Games,"game(s)")
        elif (self.P2_Score == 5):
            print("P2 just won a game")
            self.end_game()
            self.P2_Games += 1
            print("P2 now has", self.P2_Games, "game(s)")

    def add_set_1(self):
        pass

    def add_set_2(self):
        pass

    def deuce_add_point_1(self):
        self.P1_Score += 1
        self.Game_Deuce = False
        self.Game_Advantage_P1 = True
        self.Game_Advantage_P2 = False

    def deuce_add_point_2(self):
        self.P2_Score += 1
        self.Game_Advantage_P1 = False
        self.Game_Advantage_P2 = True
        self.Game_Deuce = False

    def advantage_add_point_1(self):
        self.Game_Advantage_P1 = False
        self.add_game_1()
    
    def advantage_add_point_2(self):
        self.Game_Advantage_P2 = False
        self.add_game_2()

    def disadvantage_point_1(self):
        self.P1_Score = self.P2_Score = 3
        self.Game_Advantage_P2 = False
        self.Game_Deuce = True
    
    def disadvantage_point_2(self):
        self.Game_Advantage_P1 = False
        self.Game_Deuce = True
        self.P1_Score = self.P2_Score = 3

    def deuce(self):
        #print("deuce")
        pass

    def tiebreaker(self):
        #print("tiebreaker")
        pass

    def advantage(self):
        #print("advantage")
        pass"""

    def input_box_update(self):
        input_box1 = InputBox(100,100,140,32)
        input_box2 = InputBox(100,100,140,32)
        input_boxes = [input_box1, input_box2]
        done = False

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                for box in input_boxes:
                    box.handle_event(event)

            for box in input_boxes:
                box.update()

            self.screen.fill((30, 30, 30))
            for box in input_boxes:
                box.draw(self.screen)
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
        """self.add_game_1()
        self.add_game_2()
        self.add_set_1()
        self.add_set_2()
        if self.Game_Deuce:
            self.deuce()
        if self.Game_Tiebreaker:
            self.tiebreaker()
        if self.Game_Advantage_P1 or self.Game_Advantage_P2:
            self.advantage()
        self.check_state()"""
        
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
        self.draw_text(str(POINTS[self.P1_Score]), self.points_font, 180, YELLOW, POINTS_BOX_X_2, POINTS_BOX_Y_2)
        self.draw_text(str(POINTS[self.P2_Score]), self.points_font, 180, YELLOW, POINTS_BOX_X_1, POINTS_BOX_Y_1)

        #Names
        self.draw_text(PLAYER1, self.text_font, 40, WHITE, POINTS_BOX_X_2 + POINTS_BOX_WIDTH + POINTS_BOX_OFFSET, POINTS_BOX_Y_2 + 20, align ="w")
        self.draw_text(PLAYER2, self.text_font, 40, WHITE, POINTS_BOX_X_1 + POINTS_BOX_WIDTH + POINTS_BOX_OFFSET, POINTS_BOX_Y_1 + 20, align ="w")

        #Server
        if self.serve == 1:
            self.screen.blit(SERVER_IMG, ((POINTS_BOX_X_2 + POINTS_BOX_WIDTH + POINTS_BOX_OFFSET),(POINTS_BOX_Y_2 + 50)))
        if self.serve == 2:
            self.screen.blit(SERVER_IMG, ((POINTS_BOX_X_2 + POINTS_BOX_WIDTH + POINTS_BOX_OFFSET),(POINTS_BOX_Y_1 + 50)))

        #Update the screen
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                print("keypress")
                if event.type == KILL_PROGRAM:
                    self.quit()
                if event.key == PAUSE:
                    self.paused = not self.paused
                """if not self.Game_Deuce and not self.Game_Advantage and not self.Game_Tiebreaker:
                    if event.key == ADD_POINT_P1:
                        self.add_point_1()
                    if event.key == ADD_POINT_P2:
                        self.add_point_2()
                    if event.key == REMOVE_POINT_P1:
                        self.remove_point_1()
                    if event.key == REMOVE_POINT_P2:
                        self.remove_point_2()
                if self.Game_Deuce:
                    if event.key == ADD_POINT_P1:
                        self.deuce_add_point_1()
                    if event.key == ADD_POINT_P2:
                        self.deuce_add_point_2()
                if self.Game_Advantage_P1:
                    if event.key == ADD_POINT_P1:
                        self.advantage_add_point_1()
                        print("Advantage point to 1")
                        print("P1 score is:",self.P1_Score)
                        print("P2 score is:",self.P2_Score)
                    if event.key == ADD_POINT_P2:
                        self.disadvantage_point_1()
                        print("Disadvantage point to 2")
                        print("P1 score is:",self.P1_Score)
                        print("P2 score is:",self.P2_Score)
                if self.Game_Advantage_P2:
                    if event.key == ADD_POINT_P1:
                        self.advantage_add_point_2()
                        print("Advantage point to 2")
                        print("P1 score is:",self.P1_Score)
                        print("P2 score is:",self.P2_Score)
                    if event.key == ADD_POINT_P2:
                        self.disadvantage_point_2()
                        print("Disadvantage point to 1")
                        print("P1 score is:",self.P1_Score)
                        print("P2 score is:",self.P2_Score)"""

    def show_start_screen(self):
        self.screen.blit(MAIN_MENU_IMG, (0,0))
        self.draw_text("Welcome to the National Championships", self.title_font, 60, WHITE, WIDTH/2, 60, align="center")
        self.draw_text("Press any key to start setup process", self.text_font, 45, WHITE, WIDTH/2, HEIGHT - 50, align="center")
        pg.display.flip()
        self.wait_for_key()

    def show_setup_screen(self):
        self.screen.blit(SETUP_IMG, (0,0))
        self.draw_text("Enter names of Player 1 and Player 2", self.scoreboard_font, 60, WHITE, WIDTH/2, 60, align = "center")
        pg.display.flip()
        self.wait.for_key()
        self.input_box_update()

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