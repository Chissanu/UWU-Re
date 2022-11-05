import pygame, sys, os, random
from pygame.locals import *
from Classes import Character

class Player(Character):
    def __init__(self):
        Character.__init__(self, "Hero")
        self.hurt = pygame.image.load(os.path.join("Assets",  "Hero", "Hero_Hurt.png")).convert_alpha()
        self.rect = self.surface.get_rect(center = (1920/2, 1920/2))
        self.x_speed = 10
        self.y_speed = 10
        self.health = 100

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            if self.direction == 1:
                self.step_count = 0
            self.direction = 0
            self.step_count += 1
            self.rect.move_ip(-10, 0)

        if self.rect.right < 1920 and pressed_keys[K_RIGHT]:
            if self.direction == 0:
                self.step_count = 0
            self.direction = 1
            self.step_count += 1
            self.rect.move_ip(10, 0)

        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
            self.step_count += 1

        if self.rect.bottom < 1080 and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
            self.step_count += 1

        if self.step_count >= 59:
            self.step_count = 0