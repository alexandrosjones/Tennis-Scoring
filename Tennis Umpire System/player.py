import pygame as pg
import random
from settings import *
from os import path
import sys

class Player:
    def __init__(self, name, serving, sets, deuce, tiebreaker, disadvantage):
        self.name = name
        sets = sets
        self.score = int(0)
        self.games = int(0)
        self.sets = int(0)
        self.advantage = False
        self.deuce = deuce
        self.tiebreaker = tiebreaker
        self.disadvantage = disadvantage
        if serving == 1:
            self.serving = True

    def add_point(self):
        if not self.disadvantage:
            self.score += 1
            print(self.name,"score is now:",self.score)
        if self.score == 5:
            self.score = 0
            self.add_game()
        if self.score == 4 and not self.deuce:
            self.score = 0
            self.add_game()
        if self.disadvantage:
            self.score += 0

    def add_game(self):
        self.games += 1
        if int(self.games) > 1:
            print(self.name,"now has",self.games,"games")
        elif int(self.games) == 1:
            print(self.name,"now has",self.games,"game")
        if self.games == 6:
            self.games = 0
            self.add_set()


    def add_set(self):
        self.sets += 1
        if self.sets == sets:
            WINNER = self.name
