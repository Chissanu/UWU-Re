import pygame, random
from Classes.Enemy import Enemy


#platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, platform_img, x, y, platfrom_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_img, (platfrom_width, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen_height = screen_height

    def update(self, scroll):
        self.rect.y += scroll
        #check if platform has gone off
        if self.rect.top > self.screen_height:
            self.kill()

