import pygame, os, random
from pygame.locals import *
from Classes.BaseClass import Character

GREEN = (124,252,0)
YELLOW = (255,255,0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Enemy(Character):
    def __init__(self, type, x, y, scale, speed, screen, screen_size, target, platform_group, platform_width):
        super().__init__(type, x, y, scale, speed, screen, screen_size, target, platform_group)
        self.health = 100
        self.move_counter = 0
        self.platform_width = platform_width
        self.idling = False
        self.idling_counter = 0
        self.vision = pygame.Rect(0, 0, 350, 20)
        self.vision_x = self.vision.x
        self.attack_box_multiplier = 1.5
        self.atk_cd_val = 50
        self.original_speed = self.speed
        self.increase_speed = 5
        self.atk_damage = 10
        self.gravity = 0.05
        self.kill_score = 50
        self.atk_cd_val = 100
        self.moving_right = True

    
    def move(self):
        #reset movement variables
        dx = 0
        if self.direction == 1:
            self.moving_right = True
        else:
            self.moving_right = False
        self.moving_left = not self.moving_right
        #assign movement variables if moving left or right
        if self.moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if self.moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
            
        if self.move_counter > self.platform_width/15:
            self.direction *= -1
            self.move_counter *= -1
        
        self.rect.x += dx
        self.hit_box.x += dx

        self.update_action(1)#1: run
        self.move_counter += 1
        #update enemy vision as its moves
        self.vision.center = (self.rect.centerx + self.vision.width/2 * self.direction, self.rect.centery +50)
        pygame.draw.rect(self.screen, (255, 0, 0), self.vision)


    def update(self, scroll):
        score = self.update_animation()
        self.rect.y += scroll
        self.hit_box.y += scroll
        if self.rect.bottom > self.screen_height:
            self.kill()
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(5)#5: death
        elif self.hit == True:
            self.update_action(4)#4: hit
            if self.target.rect.centerx > self.rect.centerx:
                if self.direction == -1:
                    self.direction *= -1
                    self.move_counter *= -1
            else:
                if self.direction == 1:
                    self.direction *= -1
                    self.move_counter *= -1

        elif self.attacking == True:
            if self.attack_cooldown == 0:
                self.update_action(3)#3: attack
            else:
                self.update_action(0)
        #check if the ai in near the player
        elif self.vision.colliderect(self.target.hit_box) and self.target.alive:
            self.speed = self.increase_speed
            check_attack_rect = pygame.Rect(self.hit_box.centerx - (self.attack_box_multiplier * self.hit_box.width * self.flip),
            self.hit_box.y,
            self.attack_box_multiplier * self.hit_box.width,
            self.hit_box.height)
            pygame.draw.rect(self.screen, (0, 255, 255), check_attack_rect)
            if not check_attack_rect.colliderect(self.target.hit_box):
                self.move()
            else:
                self.attacking = True
        else: 
            self.speed = self.original_speed
            if self.idling == False and random.randint(1, 200) == 1:
                self.update_action(0)#0: idle
                self.idling = True
                self.idling_counter = 50
            
            elif self.idling == False:   
                self.move()
            else:
                self.update_action(0)
                self.idling_counter -= 1
                if self.idling_counter <= 0:
                    self.idling = False
        
        return score


    def attack(self):
        attacking_rect = pygame.Rect(self.hit_box.centerx - (self.attack_box_multiplier* self.hit_box.width * self.flip), 
        self.hit_box.y, 
        self.attack_box_multiplier * self.hit_box.width, 
        self.hit_box.height)
        pygame.draw.rect(self.screen, (0, 255, 0), attacking_rect)
        if attacking_rect.colliderect(self.target.hit_box):
            self.target.health -= self.atk_damage
            self.target.hit = True
                

    def draw_health_bar(self, x, y):
        ratio = self.health / 100
        pygame.draw.rect(self.screen, BLACK, (x - 2, y - 2, 104, 14))
        pygame.draw.rect(self.screen, RED, (x, y, 100, 10)) 
        pygame.draw.rect(self.screen, YELLOW, (x, y, 100 * ratio, 10))

