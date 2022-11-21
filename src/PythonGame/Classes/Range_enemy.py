import pygame, os, random
from Classes.Enemy import Enemy
from Classes.Archer import Arrow

CURRENT_PATH = os.getcwd()
SOUND_PATH = os.path.join(CURRENT_PATH,"src","PythonGame","Assets","Sound")
class Range_enemy(Enemy):
    def __init__(self, type, x, y, scale, speed, screen, screen_size, target, platform_group, platform, score, arrow_group):
        super().__init__(type, x, y, scale, speed, screen, screen_size, target, platform_group, platform,score)
        self.vision = pygame.Rect(0, 0, self.screen_width, 20)
        self.arrow_gruop = arrow_group
    
    
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
            
        if self.hit_box.x + self.hit_box.width > self.platform.rect.x + self.platform.rect.width:
            self.direction *= -1
            dx *= -1
        if self.hit_box.x < self.platform.rect.x:
            self.direction *= -1
            dx *= -1
        
        elif self.vision.colliderect(self.target.hit_box) and self.target.alive:
            self.attacking = True
            if self.target.rect.centerx > self.rect.centerx:
                if self.direction == -1:
                    self.direction *= -1
            else:
                if self.direction == 1:
                    self.direction *= -1
        
        self.rect.x += dx
        self.hit_box.x += dx

        self.update_action(1)#1: run
        #update enemy vision as its moves
        self.vision.center = (self.rect.centerx + self.vision.width/2 * self.direction, self.rect.centery +50)
        pygame.draw.rect(self.screen, (255, 0, 0), self.vision)

        
    def update(self, scroll):
        pygame.draw.rect(self.screen, (255, 0, 0), self.vision)
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
            else:
                if self.direction == 1:
                    self.direction *= -1
        elif self.attacking == True:
            if self.attack_cooldown == 0:
                self.update_action(3)#3: attack
            else:
                self.update_action(0)
        else: 
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
        pygame.mixer.Sound(os.path.join(SOUND_PATH,"shoot.wav")).play()
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