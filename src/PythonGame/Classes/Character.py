import pygame, sys, os, random
from pygame.locals import *

CURRENT_PATH = os.getcwd()

#define game variables
GRAVITY = 0.75
ATK_CD_VAL = 50
TILE_SIZE = 40

#class for all character
class Character(pygame.sprite.Sprite):
    def __init__(self, type, x, y, scale, speed, screen, target):
        super().__init__()
        self.alive = True
        self.char_type = type
        self.x_coordinate = x
        self.y_coordinate = y
        self.speed = speed
        self.direction = 1 
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_cooldown = 0
        self.hit = False
        self.health = 100
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.target = target
        self.moving_left = False
        self.moving_right = False

        #load all images for the players
        animation_types = ['Idle', 'Run', 'Jump', 'Attack','Hit', 'Death']
        ANIMATION_PATH = CURRENT_PATH + '\\src\\PythonGame\\Assets\\Character_img'
        for animation in animation_types:
            #reset temporary list of images
            temp_list = []
            #count number of files in the folder
            num_of_frames = len(os.listdir(ANIMATION_PATH + "\\{}\\{}".format(self.char_type,animation)))
            for i in range(num_of_frames):
                img = pygame.image.load(ANIMATION_PATH + "\\{}\\{}\\{}".format(self.char_type,animation,i) + ".png")
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_box = pygame.Rect((x, y, 80, 180))
        self.screen = screen


    def move(self):
        #reset movement variables
        dx = 0
        dy = 0

        #assign movement variables if moving left or right
        if self.moving_left and self.hit == False:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if self.moving_right and self.hit == False:
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

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        #update rectangle position
        self.rect.x += dx
        self.hit_box.x += dx
        self.rect.y += dy
        self.hit_box.y += dy


    def update_action(self, new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    

    #update character actions
    def update(self):
        self.update_animation()
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(5)#5: death
        elif self.hit == True:
            self.update_action(4)#4: hit
        elif self.in_air:
            self.update_action(2)#2: jump
        elif self.moving_left or self.moving_right:
            self.update_action(1)#1: run
        elif self.attacking == True and self.attack_cooldown == 0:
            self.update_action(3)#3: attack
        else:
            self.update_action(0)#0: idle
        self.move()

    def update_animation(self):
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
                        attacking_rect = pygame.Rect(self.hit_box.centerx - (2 * self.hit_box.width * self.flip), self.hit_box.y, 2 * self.hit_box.width, self.hit_box.height)
                        pygame.draw.rect(self.screen, (0, 255, 0), attacking_rect)
                        print(attacking_rect)
                        if attacking_rect.colliderect(self.target.hit_box):
                            self.target.health -= 10
                            self.target.hit = True
                            
                    self.attacking = False
                    self.attack_cooldown = ATK_CD_VAL
                #check if damage was taken
                if self.action == 4:
                    self.hit = False
                    #if the player was in the middle of an attack, then the attack is stopped
                    self.attacking = False
                    self.attack_cooldown = ATK_CD_VAL


    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(5)


    def draw(self):
        pygame.draw.rect(self.screen, (255, 150, 100), self.hit_box)
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
