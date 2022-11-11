import pygame, sys, os, random
from pygame.locals import *

CURRENT_PATH = os.getcwd()
PLAYER_PATH = CURRENT_PATH + "\\src\\PythonGame\\Assets\\Character_img\\Player\\Standing.png"

#define game variables
GRAVITY = 0.75

#class for all character
class Character(pygame.sprite.Sprite):
    def __init__(self, type, x, y, scale, speed, screen):
        super().__init__()
        self.char_type = type
        self.direction = 1 
        self.step_count = 0
        self.speed = speed
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        #load all images for the players
        animation_types = ['Idle', 'Run', 'Jump']
        ANIMATION_PATH = 'C:\\Users\\ASUS\\Desktop\\UWU-Re\\src\\PythonGame\\Assets\\Character_img'
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
        self.screen = screen

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
            self.vel_y = -20
            self.jump = False
            self.in_air = True

		#apply gravity
        self.vel_y += GRAVITY
        # if self.vel_y > 10:
        #     self.vel_y
        dy += self.vel_y

        #check collision with floor
        if self.rect.bottom + dy > 880:
            dy = 880 - self.rect.bottom
            self.in_air = False


        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy
        # print(self.rect.y)

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
            self.frame_index = 0



    def update_action(self, new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
