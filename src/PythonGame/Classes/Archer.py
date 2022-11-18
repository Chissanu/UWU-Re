import pygame, os, random
from pygame.locals import *
from Classes.BaseClass import Character


CURRENT_PATH = os.getcwd()


class Archer(Character):
    def __init__(self, type, x, y, scale, speed, screen, screen_width, target, arrow_group, platform_group):
        super().__init__(type, x, y, scale, speed, screen, screen_width, target, platform_group)
        self.health = 10
        self.atk_cd_val = 0
        self.atk_damage = 10
        self.arrow_gruop = arrow_group
    
    def attack(self):
        arrow = Arrow(
        self.rect.centerx + (0.2 * self.rect.size[0] * self.direction), 
        self.rect.centery, 
        self.scale,  
        self.screen, 
        self.screen_width, 
        self.target, 
        self.arrow_gruop, 
        self.flip, 
        self.direction,
        self.atk_damage
        )
        self.arrow_gruop.add(arrow)


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, screen, screen_width, target_group, arrow_group, flip, direction, atk_damage):
        pygame.sprite.Sprite.__init__(self)
        arrow_img = pygame.image.load(CURRENT_PATH + '\\src\\PythonGame\\Assets\\Character_img\\Archer\\Arrow\\0.png').convert_alpha()
        arrow_img = pygame.transform.scale(arrow_img, (int(arrow_img.get_width() * scale), int(arrow_img.get_height() * scale)))
        self.image = arrow_img
        self.arrow_speed = 10
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.arrow_image = arrow_img
        self.flip = flip
        self.direction = direction
        self.screen = screen
        self.screen_width = screen_width
        self.target_group = target_group
        self.arrow_group = arrow_group
        self.atk_damage = atk_damage


    def update(self):
        self.screen.blit(pygame.transform.flip(self.arrow_image, self.flip, False), self.rect)
        self.rect.x += (self.direction * self.arrow_speed)
        for enemy in self.target_group:
            if self.rect.colliderect(enemy.hit_box):
                if enemy.alive:
                    enemy.health -= self.atk_damage
                    enemy.hit = True
                    self.kill()
        if self.rect.right < 0 or self.rect.left > self.screen_width:
            self.kill()
