import pygame, sys, os, random
from pygame.locals import *
from Character import Character

class Swordsman(Character):
    def __init__(self, type, x, y, scale, speed, screen, target):
        super().__init__(type, x, y, scale, speed, screen)
        self.target = target