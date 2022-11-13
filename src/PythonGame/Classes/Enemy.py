import pygame, sys, os, random
from pygame.locals import *
from Classes.Character import Character

CURRENT_PATH = os.getcwd()

#define game variables
GRAVITY = 0.75
ATK_CD_VAL = 50
TILE_SIZE = 40

class Enemy(Character):
    def __init__(self, type, x, y, scale, speed, screen, target):
        super().__init__(type, x, y, scale, speed, screen, target)
        self.health = 100
        self.move_counter = 0
        self.idling = False
        self.idling_counter = 0
        self.vision = pygame.Rect(0, 0, 170, 20)

    
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
        self.vel_y += GRAVITY
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
        elif self.attacking == True or self.attack_cooldown > 0:
            if self.attack_cooldown == 0:
                self.update_action(3)#3: attack
            else:
                self.update_action(0)
        #check if the ai in near the player
        elif self.vision.colliderect(target.hit_box) and self.attack_cooldown == 0:
            check_attack_rect = pygame.Rect(self.hit_box.centerx - (2 * self.hit_box.width * self.flip), self.hit_box.y, 2 * self.hit_box.width, self.hit_box.height)
            pygame.draw.rect(self.screen, (0, 255, 255), check_attack_rect)
            if not check_attack_rect.colliderect(target.hit_box):
                if self.direction == 1:
                    self.moving_right = True
                else:
                    self.moving_right = False
                self.moving_left = not self.moving_right
                self.move(self.moving_left, self.moving_right)
                self.update_action(1)#1: run
                self.move_counter += 1
                #update enemy vision as its moves
                self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery +50)
                pygame.draw.rect(self.screen, (255, 0, 0), self.vision)
                if self.move_counter > TILE_SIZE:
                    self.direction *= -1
                    self.move_counter *= -1
            else:
                self.attacking = True
        else: 
            if self.idling == False and random.randint(1, 200) == 1:
                self.update_action(0)#0: idle
                self.idling = True
                self.idling_counter = 50
            
            elif self.idling == False:   
                if self.direction == 1:
                    self.moving_right = True
                else:
                    self.moving_right = False
                self.moving_left = not self.moving_right
                self.move(self.moving_left, self.moving_right)
                self.update_action(1)#1: run
                self.move_counter += 1
                #update enemy vision as its moves
                self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery +50)
                pygame.draw.rect(self.screen, (255, 0, 0), self.vision)
                if self.move_counter > TILE_SIZE:
                    self.direction *= -1
                    self.move_counter *= -1
            else:
                self.idling_counter -= 1
                if self.idling_counter <= 0:
                    self.idling = False
        
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
    
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
                        attacking_rect = pygame.Rect(self.hit_box.centerx - (2 * self.hit_box.width * self.flip), self.hit_box.y, 3 * self.hit_box.width, self.hit_box.height)
                        pygame.draw.rect(self.screen, (0, 255, 0), attacking_rect)
                        print(attacking_rect)
                        if attacking_rect.colliderect(target.hit_box):
                            target.health -= 10
                            target.hit = True
                            
                    self.attacking = False
                    self.attack_cooldown = ATK_CD_VAL
                #check if damage was taken
                if self.action == 4:
                    self.hit = False
                    #if the player was in the middle of an attack, then the attack is stopped
                    self.attacking = False
                    self.attack_cooldown = ATK_CD_VAL

        # elif self.in_air:
        #     self.update_action(2)#2: jump
        # elif self.moving_left or self.moving_right:
        #     self.update_action(1)#1: run
        # else:
        #     self.update_action(0)#0: idle


    def update_action(self, new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

