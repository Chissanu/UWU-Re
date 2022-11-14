import pygame, sys, os, random
from pygame.locals import *
from Classes.BaseClass import Character


CURRENT_PATH = os.getcwd()
#arrow


class Archer(Character):
    def __init__(self, type, x, y, scale, speed, screen, target_group, arrow_group):
        super().__init__(type, x, y, scale, speed, screen)
        self.target_group = target_group
        self.atk_cd_val = 50
        self.arrow_gruop = arrow_group
    

    def shoot(self):
        if self.attack_cooldown == 0:
            self.attack_cooldown = self.atk_cd_val
            arrow = Arrow(self.rect.centerx + (0.2 * self.rect.size[0] * self.direction), self.rect.centery, self.direction, self.arrow_gruop, self.scale, self.screen, self.flip, self.target_group)
            self.arrow_gruop.add(arrow)
            self.attacking = False


    #update character actions
    def update(self):
        self.update_animation()
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(5)#5: death
        elif self.hit == True:
            self.update_action(4)#4: hit
        elif self.in_air:
            self.update_action(2)#2: jump
        elif self.moving_left or self.moving_right:
            self.update_action(1)#1: run
        elif self.attacking and self.attack_cooldown == 0:
            self.update_action(3)#3: attack
            if self.frame_index == len(self.animation_list[self.action]) - 1:
                self.shoot()
        else:
            self.update_action(0)#0: idle
        self.move()
    

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, arrow_group, scale, screen, flip, target_group):
        pygame.sprite.Sprite.__init__(self)
        arrow_img = pygame.image.load(CURRENT_PATH + '\\src\\PythonGame\\Assets\\Character_img\\Archer\\Arrow\\0.png').convert_alpha()
        arrow_img = pygame.transform.scale(arrow_img, (int(arrow_img.get_width() * scale), int(arrow_img.get_height() * scale)))
        self.speed = 10
        self.image = arrow_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.arrow_group = arrow_group
        self.screen = screen
        self.flip = flip
        self.target_group = target_group

    def update(self, screen_width):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        self.rect.x += (self.direction * self.speed)
        attacking_rect = pygame.Rect(self.rect)
        for enemy in self.target_group:
            if attacking_rect.colliderect(enemy.hit_box):
                if enemy.alive:
                    enemy.health -= 10
                    enemy.hit = True
                    self.kill()
        if self.rect.right < 0 or self.rect.left > screen_width:
            self.kill()
