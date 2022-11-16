import pygame, os, random
from pygame.locals import *
from Classes.BaseClass import Character


CURRENT_PATH = os.getcwd()


class Archer(Character):
    def __init__(self, type, x, y, scale, speed, screen, screen_width, target_group, arrow_group, platform_group):
        super().__init__(type, x, y, scale, speed, screen, screen_width, platform_group)
        self.health = 10
        self.target_group = target_group
        self.atk_cd_val = 50
        self.atk_damage = 50
        self.arrow_gruop = arrow_group
    

    def shoot(self):
        arrow = Arrow(self.char_type,
        self.rect.centerx + (0.2 * self.rect.size[0] * self.direction), 
        self.rect.centery, 
        self.scale, 
        self.speed, 
        self.screen, 
        self.screen_width, 
        self.target_group, 
        self.arrow_gruop, 
        self.flip, 
        self.direction,
        self.platform_group)
        self.arrow_gruop.add(arrow)


    #update character actions
    def update(self):
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
        elif self.attacking:
            self.update_action(3)#3: attack
            if self.frame_index == len(self.animation_list[self.action]) - 1:
                self.shoot()
        else:
            self.update_action(0)#0: idle
        self.update_animation()
        self.scroll = self.move()
        return self.scroll


class Arrow(Archer):
    def __init__(self, type, x, y, scale, speed, screen, screen_width, target_group, arrow_group, flip, direction, platform_group):
        super().__init__(type, x, y, scale, speed, screen, screen_width, target_group, arrow_group, platform_group)
        arrow_img = pygame.image.load(CURRENT_PATH + '\\src\\PythonGame\\Assets\\Character_img\\Archer\\Arrow\\0.png').convert_alpha()
        arrow_img = pygame.transform.scale(arrow_img, (int(arrow_img.get_width() * scale), int(arrow_img.get_height() * scale)))
        self.image = arrow_img
        self.arrow_speed = 50
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.arrow_image = arrow_img
        self.flip = flip
        self.direction = direction


    def update(self):
        self.screen.blit(pygame.transform.flip(self.arrow_image, self.flip, False), self.rect)
        self.rect.x += (self.direction * self.arrow_speed)
        attacking_rect = pygame.Rect(self.rect)
        for enemy in self.target_group:
            if attacking_rect.colliderect(enemy.hit_box):
                if enemy.alive:
                    enemy.health -= self.atk_damage
                    enemy.hit = True
                    self.kill()
        if self.rect.right < 0 or self.rect.left > self.screen_width:
            self.kill()
