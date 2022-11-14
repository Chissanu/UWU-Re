import pygame, sys, os, random
from pygame.locals import *
from Classes.BaseClass import Character


class Archer(Character):
    def __init__(self, type, x, y, scale, speed, screen):
        super().__init__(type, x, y, scale, speed, screen)
        self.atk_cd_val = 0
    

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            #reduce ammo
            self.ammo -= 1
