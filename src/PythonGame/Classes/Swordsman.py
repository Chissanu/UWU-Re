import pygame, os, random
from pygame.locals import *
from Classes.BaseClass import Character


class Swordsman(Character):
    def __init__(self, type, x, y, scale, speed, screen, screen_width, target_group, platform_group):
        super().__init__(type, x, y, scale, speed, screen, screen_width, platform_group)
        self.atk_cd_val = 30 
        self.atk_damage = 50
        self.health = 100
        self.target_group = target_group


    def attack(self):
        attacking_rect = pygame.Rect(self.hit_box.centerx - (2 * self.hit_box.width * self.flip), self.hit_box.y, 2 * self.hit_box.width, self.hit_box.height)
        pygame.draw.rect(self.screen, (0, 255, 0), attacking_rect)
        for enemy in self.target_group:
            if attacking_rect.colliderect(enemy.hit_box):
                if enemy.alive:
                    enemy.health -= self.atk_damage
                    enemy.hit = True