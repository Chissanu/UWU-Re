import pygame, os, random
from pygame.locals import *
from Classes.BaseClass import Character

GREEN = (124,252,0)
YELLOW = (255,255,0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Enemy(Character):
    def __init__(self, type, x, y, scale, speed, screen, screen_width, platform_group, platform_width, screen_height):
        super().__init__(type, x, y, scale, speed, screen, screen_width, platform_group)
        self.health = 100
        self.move_counter = 0
        self.platform_width = platform_width
        self.idling = False
        self.idling_counter = 0
        self.vision = pygame.Rect(0, 0, 350, 20)
        self.vision_x = self.vision.x
        self.attack_box_multiplier = 1.5
        self.atk_cd_val = 50
        self.tile_size = platform_width
        self.original_speed = self.speed
        self.increase_speed = 5
        self.atk_damage = 10
        self.gravity = 0.05
        self.screen_height = screen_height
        self.kill_score = 50

    
    def move(self, moving_left, moving_right):
        #reset movement variables
        dx = 0

        #assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        #ensure player doesn't go off the edge of the screen
        if self.hit_box.left + dx < 0:
            dx = -self.hit_box.left
            self.direction *= -1
            self.move_counter *= -1
        if self.hit_box.right + dx > self.screen_width:
            dx = self.screen_width - self.hit_box.right
            self.direction *= -1
            self.move_counter *= -1
        if self.move_counter > self.tile_size/15:
            self.direction *= -1
            self.move_counter *= -1
        
        self.rect.x += dx
        self.hit_box.x += dx

    def update(self, target, scroll):
        self.update_animation(target)
        self.rect.y += scroll
        self.hit_box.y += scroll
        if self.rect.bottom > self.screen_height:
            self.kill()
        # if self.health <= 0:
        #     self.health = 0
        #     self.alive = False
        #     self.update_action(5)#5: death
        elif self.hit == True:
            self.update_action(4)#4: hit
            if target.rect.centerx > self.rect.centerx:
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
        elif self.vision.colliderect(target.hit_box) and target.alive:
            self.speed = self.increase_speed
            check_attack_rect = pygame.Rect(self.hit_box.centerx - (self.attack_box_multiplier * self.hit_box.width * self.flip),
            self.hit_box.y,
            self.attack_box_multiplier * self.hit_box.width,
            self.hit_box.height)
            pygame.draw.rect(self.screen, (0, 255, 255), check_attack_rect)
            if not check_attack_rect.colliderect(target.hit_box):
                self.patrol()
            else:
                self.attacking = True
        else: 
            self.speed = self.original_speed
            if self.idling == False and random.randint(1, 200) == 1:
                self.update_action(0)#0: idle
                self.idling = True
                self.idling_counter = 50
            
            elif self.idling == False:   
                self.patrol()
            else:
                self.update_action(0)
                self.idling_counter -= 1
                if self.idling_counter <= 0:
                    self.idling = False
        
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        

    def patrol(self):
        if self.direction == 1:
            self.moving_right = True
        else:
            self.moving_right = False
        self.moving_left = not self.moving_right
        self.move(self.moving_left, self.moving_right)
        self.update_action(1)#1: run
        self.move_counter += 1
        #update enemy vision as its moves
        self.vision.center = (self.rect.centerx + self.vision.width/2 * self.direction, self.rect.centery +50)
        pygame.draw.rect(self.screen, (255, 0, 0), self.vision)


    def update_animation(self, target):
        #update animation
        ANIMATION_COOLDOWN = 100
        #update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
                
        #if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            #if the player is dead then end the animation
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                #check if an attack was executed
                if self.action == 1 or self.action == 2:
                    self.attacking = False
                if self.action == 3:
                    attacking_rect = pygame.Rect(self.hit_box.centerx - (self.attack_box_multiplier* self.hit_box.width * self.flip), 
                    self.hit_box.y, 
                    self.attack_box_multiplier * self.hit_box.width, 
                    self.hit_box.height)
                    pygame.draw.rect(self.screen, (0, 255, 0), attacking_rect)
                    if attacking_rect.colliderect(target.hit_box):
                        target.health -= self.atk_damage
                        target.hit = True
                            
                    self.attacking = False
                    self.attack_cooldown = self.atk_cd_val
                #check if damage was taken
                if self.action == 4:
                    self.hit = False
                    #if the player was in the middle of an attack, then the attack is stopped
                    self.attacking = False
                    self.attack_cooldown = self.atk_cd_val
    
    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(5)#5: death
            return 

    def draw_health_bar(self, x, y):
        ratio = self.health / 100
        pygame.draw.rect(self.screen, BLACK, (x - 2, y - 2, 104, 14))
        pygame.draw.rect(self.screen, RED, (x, y, 100, 10)) 
        pygame.draw.rect(self.screen, YELLOW, (x, y, 100 * ratio, 10))

