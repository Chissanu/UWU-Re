import pygame, sys, os, random
from pygame.locals import *

CURRENT_PATH = os.getcwd()
PLAYER_PATH = CURRENT_PATH + "\\src\\PythonGame\\Assets\\Character_img\\Player\\Standing.png"

#define game variables
GRAVITY = 0.75

#class for all character
class Character(pygame.sprite.Sprite):
    def __init__(self, type, x, y, scale, speed, screen):
        super().__init__()
        self.char_type = type
        self.direction = 1 
        self.step_count = 0
        self.speed = speed
        self.vel_y = 0
        self.jump = False
        self.in_air = True
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
        # print(self.vel_y)

        #assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

		#jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

		#apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #check collision with floor
        print(self.rect.bottom)
        if self.rect.bottom + dy > 600:
            dy = 600 - self.rect.bottom
            self.in_air = False
            # print(dy)


        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy
        # print(self.rect.y)


    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
