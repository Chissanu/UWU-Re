import pygame, sys, os, random
from pygame.locals import *

CURRENT_PATH = os.getcwd()
PLAYER_PATH = CURRENT_PATH + "\\src\\PythonGame\\Assets\\Character_img\\Player\\Standing.png"


#class for all character
class Character(pygame.sprite.Sprite):
    def __init__(self, type, x, y, scale, speed, screen):
        super().__init__()
        self.char_type = type
        self.direction = 1 #1 is 'right', 0 is 'left'
        self.step_count = 0
        self.speed = speed
        self.flip = False
        img = pygame.image.load(PLAYER_PATH)
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen

    def move(self, moving_left, moving_right):
        #reset movement variables
        dx = 0
        dy = 0

        #assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1


        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy


    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)