import pygame, os, random
from pygame.locals import *
from Classes.BaseClass import Character

CURRENT_PATH = os.getcwd()
SOUND_PATH = os.path.join(CURRENT_PATH,"src","PythonGame","Assets","Sound")

pygame.mixer.init()

class Swordsman(Character):
    def __init__(self, type, x, y, scale, speed, screen, screen_size, target, platform_group):
        super().__init__(type, x, y, scale, speed, screen, screen_size, target, platform_group)
        self.atk_cd_val = 0
        self.atk_damage = 50
        self.health = 100

    def attack(self):
        pygame.mixer.Sound(os.path.join(SOUND_PATH,"swing.wav")).play()
        attacking_rect = pygame.Rect(self.hit_box.centerx - (2 * self.hit_box.width * self.flip), self.hit_box.y, 2 * self.hit_box.width, self.hit_box.height)
        pygame.draw.rect(self.screen, (0, 255, 0), attacking_rect)
        for enemy in self.target:
            if attacking_rect.colliderect(enemy.hit_box):
                if enemy.alive:
                    enemy.health -= self.atk_damage
                    enemy.hit = True
    
    def getAttack(self):
        return self.atk_damage
    
    def getHp(self):
        return self.health
