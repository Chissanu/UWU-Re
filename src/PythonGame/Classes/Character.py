import pygame, sys, os, random
from pygame.locals import *

class Character(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.walk_anim = [
            pygame.image.load(os.path.join("Assets", type, f"{type}_Standing.png")).convert_alpha(),
            pygame.image.load(os.path.join("Assets", type, f"{type}_L_Step.png")).convert_alpha(),
            pygame.image.load(os.path.join("Assets", type, f"{type}_Standing.png")).convert_alpha(),
            pygame.image.load(os.path.join("Assets", type, f"{type}_R_Step.png")).convert_alpha(),
        ]
        self.surface = pygame.Surface((100,150))
        self.direction = 1 #1 is 'right', 0 is 'left'
        self.step_count = 0
        