import pygame, sys, os, random
from pygame.locals import *
from Classes.BaseClass import Character


CURRENT_PATH = os.getcwd()
#arrow


class Archer(Character):
    def __init__(self, type, x, y, scale, speed, screen, target, arrow_group):
        super().__init__(type, x, y, scale, speed, screen)
        self.target = target
        self.atk_cd_val = 50
        self.arrow_gruop = arrow_group
    

    def shoot(self):
        if self.attack_cooldown == 0:
            self.attack_cooldown = self.atk_cd_val
            arrow = Arrow(self.rect.centerx + (0.2 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            self.arrow_gruop.add(arrow)

    
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
        elif self.attacking:
            self.update_action(3)#3: attack
            if self.frame_index == len(self.animation_list[self.action]) - 1:
                self.shoot()
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
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                #check if an attack was executed
                if self.action == 1 or self.action == 2:
                    self.attacking = False
                if self.action == 3:
                #     if self.attack_cooldown == 0:
                #         self.target.health -= 10
                #         self.target.hit = True
                    self.attacking = False
                    self.attack_cooldown = self.atk_cd_val
                #check if damage was taken
                if self.action == 4:
                    self.hit = False
                    #if the player was in the middle of an attack, then the attack is stopped
                    self.attacking = False
                    self.attack_cooldown = self.atk_cd_val
        


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        arrow_img = pygame.image.load(CURRENT_PATH + '\\src\\PythonGame\\Assets\\Character_img\\Archer\\Arrow\\0.png').convert_alpha()
        self.speed = 10
        self.image = arrow_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self, screen_width):
        self.rect.x += (self.direction * self.speed)
        if self.rect.right < 0 or self.rect.left > screen_width:
            self.kill()

    def draw(self, surface):
        # pygame.draw.rect(self.screen, (255, 150, 100), self.hit_box)
        print("here")
        self.screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
