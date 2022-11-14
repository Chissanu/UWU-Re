import pygame, sys, os, random
from pygame.locals import *
from Classes.BaseClass import Character

#define game variables

class Enemy(Character):
    def __init__(self, type, x, y, scale, speed, screen):
        super().__init__(type, x, y, scale, speed, screen)
        self.health = 100
        self.move_counter = 0
        self.idling = False
        self.idling_counter = 0
        self.vision = pygame.Rect(0, 0, 350, 20)
        self.vision_x = self.vision.x
        self.attack_box_multiplier = 1.5
        self.atk_cd_val = 50
        self.tile_size = 100
        self.original_speed = self.speed
        self.increase_speed = 5

    
    def move(self, moving_left, moving_right):
        #reset movement variables
        dx = 0
        dy = 0

        #assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

		#jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -15
            self.jump = False
            self.in_air = True

		#apply gravity
        self.vel_y += self.gravity
        dy += self.vel_y

        #check collision with floor
        if self.rect.bottom + dy > 940:
            dy = 940 - self.rect.bottom
            self.in_air = False

        #update rectangle position
        self.rect.x += dx
        self.hit_box.x += dx
        self.rect.y += dy
        self.hit_box.y += dy

    def update(self, target):
        self.update_animation(target)
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(5)#5: death
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

        elif self.attacking == True or self.attack_cooldown > 0:
            if self.attack_cooldown == 0:
                self.update_action(3)#3: attack
            else:
                self.update_action(0)
        #check if the ai in near the player
        elif self.vision.colliderect(target.hit_box) and self.attack_cooldown == 0:
            self.speed = self.increase_speed
            check_attack_rect = pygame.Rect(self.hit_box.centerx - (self.attack_box_multiplier * self.hit_box.width * self.flip),
            self.hit_box.y,
            self.attack_box_multiplier * self.hit_box.width,
            self.hit_box.height)
            pygame.draw.rect(self.screen, (0, 255, 255), check_attack_rect)
            if not check_attack_rect.colliderect(target.hit_box):
                self.trigger_vision()
            else:
                self.attacking = True
        else: 
            self.speed = self.original_speed
            if self.idling == False and random.randint(1, 200) == 1:
                self.update_action(0)#0: idle
                self.idling = True
                self.idling_counter = 50
            
            elif self.idling == False:   
                self.trigger_vision()
            else:
                self.idling_counter -= 1
                if self.idling_counter <= 0:
                    self.idling = False
        
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1


    def trigger_vision(self):
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
        if self.move_counter > self.tile_size:
            self.direction *= -1
            self.move_counter *= -1


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
                    if self.attack_cooldown == 0:
                        attacking_rect = pygame.Rect(self.hit_box.centerx - (self.attack_box_multiplier* self.hit_box.width * self.flip), 
                        self.hit_box.y, 
                        self.attack_box_multiplier * self.hit_box.width, 
                        self.hit_box.height)
                        pygame.draw.rect(self.screen, (0, 255, 0), attacking_rect)
                        if attacking_rect.colliderect(target.hit_box):
                            target.health -= 10
                            target.hit = True
                            
                    self.attacking = False
                    self.attack_cooldown = self.atk_cd_val
                #check if damage was taken
                if self.action == 4:
                    self.hit = False
                    #if the player was in the middle of an attack, then the attack is stopped
                    self.attacking = False
                    self.attack_cooldown = self.atk_cd_val

