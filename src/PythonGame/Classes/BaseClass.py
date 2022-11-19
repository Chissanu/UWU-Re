import pygame, os, random
from pygame.locals import *

SCROLL_THRESHOLD = 300
#define colors
GREEN = (124,252,0)
YELLOW = (255,255,0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#class for all character
class Character(pygame.sprite.Sprite):
    def __init__(self, type, x, y, scale, speed, screen, screen_size, target, platform_group):
        super().__init__()
        CURRENT_PATH = os.getcwd()
        self.scroll = 0
        self.screen = screen
        self.screen_width = screen_size[0]
        self.screen_height = screen_size[1]
        self.platform_group = platform_group
        self.alive = True
        self.jump = False
        self.in_air = True
        self.flip = False
        self.attacking = False
        self.hit = False
        self.moving_left = False
        self.moving_right = False
        self.scale = scale
        self.char_type = type
        self.speed = speed
        self.gravity = 0.75
        self.direction = 1 
        self.vel_y = 0
        self.attack_cooldown = 0
        self.health = 100
        self.frame_index = 0
        self.action = 0
        self.animation_list = []
        self.atk_cd_val = 50
        self.update_time = pygame.time.get_ticks()
        self.target = target


        #load all images for the players
        animation_types = ['Idle', 'Run', 'Jump', 'Attack', 'Hit', 'Death']
        ANIMATION_PATH = os.path.join(CURRENT_PATH, 'src', 'PythonGame', 'Assets', 'Character_img')
        for animation in animation_types:
            #reset temporary list of images
            temp_list = []
            #count number of files in the folder
            num_of_frames = len(os.listdir(ANIMATION_PATH + "\\{}\\{}".format(self.char_type,animation)))
            for i in range(num_of_frames):
                img = pygame.image.load(ANIMATION_PATH + "\\{}\\{}\\{}".format(self.char_type,animation,i) + ".png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_box = pygame.Rect(self.rect.center, (80, 120))
        self.hit_box.center = (self.rect.centerx , self.rect.centery)
        self.hit_box.bottom = self.rect.bottom


    def move(self):
        if self.rect.top >  1080:
            self.health = 0
        #reset movement variables
        self.scroll = 0
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
        if self.jump == True:
            self.vel_y = -20
            self.jump = False
            self.in_air = True

		#apply gravity
        self.vel_y += self.gravity
        dy += self.vel_y

        #ensure player doesn't go off the edge of the screen
        if self.hit_box.left + dx < 0:
            dx = -self.hit_box.left
        if self.hit_box.right + dx > self.screen_width:
            dx = self.screen_width - self.hit_box.right
        
        #check collision with platforms
        for platform in self.platform_group:
            #collision in the y direction
            if platform.rect.colliderect(self.hit_box.x, self.hit_box.y + dy, self.hit_box.width, self.hit_box.height):
                #check if above the platform
                if self.hit_box.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.hit_box.bottom = platform.rect.top
                        self.rect.bottom = platform.rect.top
                        self.vel_y = 0
                        dy = 0
                        self.in_air = False
                        

        #check if the player has bounced to the top of the screen
        if self.hit_box.top <= SCROLL_THRESHOLD:
            #if player is jumping
            if self.vel_y < 0:
                self.scroll = int(-dy)

        #update rectangle position
        self.rect.x += dx
        self.hit_box.x += dx
        self.rect.y += dy + self.scroll
        self.hit_box.y += dy + self.scroll

        return self.scroll



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
        self.scroll = self.move()
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.update_action(5)#5: death
        elif self.hit == True:
            self.update_action(4)#4: hit
        elif self.in_air:
            self.update_action(2)#2: jump
        elif self.moving_left or self.moving_right:
            self.update_action(1)#1: run
        elif self.attacking == True:
            self.update_action(3)#3: attack
        else:
            self.update_action(0)#0: idle
        return self.scroll


    def update_animation(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
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
            #after animation death done
            if self.action == 5:
                self.frame_index = len(self.animation_list[self.action]) - 1
                self.alive = False
                self.kill()
                return True
            else:
                self.frame_index = 0
                #check if an attack was executed
                if self.action == 1 or self.action == 2:
                    self.attacking = False
                if self.action == 3:
                    self.attack()            
                    self.attacking = False
                    self.attack_cooldown = self.atk_cd_val
                #check if damage was taken
                if self.action == 4:
                    self.hit = False
                    #if the player was in the middle of an attack, then the attack is stopped
                    self.attacking = False
                    self.attack_cooldown = self.atk_cd_val
        return False

    def attack(self):
        return
        
    
    def draw_health_bar(self, x, y):
        ratio = self.health / 100
        pygame.draw.rect(self.screen, BLACK, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(self.screen, RED, (x, y, 400, 30)) 
        pygame.draw.rect(self.screen, YELLOW, (x, y, 400 * ratio, 30))


    def draw(self):
        pygame.draw.rect(self.screen, (255, 150, 100), self.hit_box)
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)