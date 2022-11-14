import pygame, sys, os, random
from pygame.locals import *
from Classes.BaseClass import Character


class Swordsman(Character):
    def __init__(self, type, x, y, scale, speed, screen, target):
        super().__init__(type, x, y, scale, speed, screen)
        self.atk_cd_val = 30 
        self.target = target

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
                        if attacking_rect.colliderect(self.target.hit_box):
                            self.target.health -= 10
                            self.target.hit = True
                            
                    self.attacking = False
                    self.attack_cooldown = self.atk_cd_val
                #check if damage was taken
                if self.action == 4:
                    self.hit = False
                    #if the player was in the middle of an attack, then the attack is stopped
                    self.attacking = False
                    self.attack_cooldown = self.atk_cd_val
                    