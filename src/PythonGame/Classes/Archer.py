import pygame, os, random
from pygame.locals import *
from Classes.BaseClass import Character


CURRENT_PATH = os.getcwd()


class Archer(Character):
    def __init__(self, type, x, y, scale, speed, screen, screen_width, target, arrow_group, platform_group):
        super().__init__(type, x, y, scale, speed, screen, screen_width, target, platform_group)
        self.health = 100
        self.atk_cd_val = 0
        self.atk_damage = 100
        self.arrow_gruop = arrow_group
    
    def attack(self):
        arrow = Arrow(
        self.rect.centerx + (0.2 * self.rect.size[0] * self.direction), 
        self.rect.centery, 
        self.scale,  
        self.screen, 
        self.screen_width, 
        self.target, 
        self.arrow_gruop, 
        self.flip, 
        self.direction,
        self.atk_damage
        )
        self.arrow_gruop.add(arrow)
    
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
        elif self.attacking == True:
            self.update_action(3)#3: attack
        elif self.in_air:
            self.update_action(2)#2: jump
        elif self.moving_left or self.moving_right:
            self.update_action(1)#1: run
        else:
            self.update_action(0)#0: idle
        return self.scroll


    def update_animation(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
		#update animation
        if self.action == 3:
            ANIMATION_COOLDOWN = 30
        else:
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



class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, screen, screen_width, target_group, arrow_group, flip, direction, atk_damage):
        pygame.sprite.Sprite.__init__(self)
        arrow_img = pygame.image.load(os.path.join(CURRENT_PATH, 'src', 'PythonGame', 'Assets', 'Character_img', 'Archer', 'Arrow', '0.png')).convert_alpha()
        arrow_img = pygame.transform.scale(arrow_img, (int(arrow_img.get_width() * scale), int(arrow_img.get_height() * scale)))
        self.image = arrow_img
        self.arrow_speed = 10
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.arrow_image = arrow_img
        self.flip = flip
        self.direction = direction
        self.screen = screen
        self.screen_width = screen_width
        self.target_group = target_group
        self.arrow_group = arrow_group
        self.atk_damage = atk_damage


    def update(self, scroll):
        self.screen.blit(pygame.transform.flip(self.arrow_image, self.flip, False), self.rect)
        self.rect.y += scroll
        self.rect.x += (self.direction * self.arrow_speed)
        for enemy in self.target_group:
            if self.rect.colliderect(enemy.hit_box):
                if enemy.alive:
                    enemy.health -= self.atk_damage
                    enemy.hit = True
                    self.kill()
        if self.rect.right < 0 or self.rect.left > self.screen_width:
            self.kill()
