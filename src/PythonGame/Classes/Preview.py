import pygame, os, random
from pygame.locals import *
from Classes.BaseClass import Character

class Preview(Character):
    def __init__(self, type, x, y, scale, speed, screen, screen_size, target, platform_group):
        super().__init__(type, x, y, scale, speed, screen, screen_size, target, platform_group)
        self.gravity = 0.10

    def move(self):
        #reset movement variables
        dx = 0
        dy = 0

        #assign movement variables if moving left or right
        if self.moving_left:
            self.flip = True
            self.direction = -1
        if self.moving_right:
            self.flip = False
            self.direction = 1

		#jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -1
            self.jump = False
            self.in_air = True

		#apply gravity
        self.vel_y += self.gravity
        dy += self.vel_y

        #check collision with floor
        if self.rect.bottom + dy > 940:
            dy = 940 - self.rect.bottom
            self.in_air = False

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        #update rectangle position
        self.rect.x += dx
        self.hit_box.x += dx
        self.rect.y += dy
        self.hit_box.y += dy


    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)