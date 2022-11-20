import pygame, os

class Shop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.CURRENT_PATH = os.getcwd()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(self.CURRENT_PATH, 'src', 'PythonGame', 'Assets', 'Background', 'shop.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.05), int(self.image.get_height() * 0.05)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bg = pygame.image.load(os.path.join(self.CURRENT_PATH, 'src', 'PythonGame', 'Assets', 'Background', 'white.jpg'))
    
    def update(self, scroll):
        self.rect.y += scroll
        #check if platform has gone off
        if self.rect.top > 1080:
            self.kill()