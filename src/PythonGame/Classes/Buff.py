import time, pygame, os

class Buff(pygame.sprite.Sprite):
    def __init__(self, x, y):
        CURRENT_PATH = os.getcwd()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(CURRENT_PATH, 'src', 'PythonGame', 'Assets', 'Buff_img', 'Jump', '1.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width()), int(self.image.get_height())))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.origiHealth = 100
        self.player = 0

    def setData(self, player):
        self.player = player
        self.origiHealth = player.health

    def update(self, scroll):
        self.rect.y += scroll
        #check if platform has gone off
        if self.rect.top > 1080:
            self.kill()

    def healthBuff(self):
        self.player.health = 100000

    def superJump(self):
        self.player.gravity = 0.1
    
    def clearBuff(self, num):
        self.rect.x = 0
        self.rect.y = 0
        if num == 1:
            self.player.health = 100
        elif num == 2:
            self.player.gravity = 0.75