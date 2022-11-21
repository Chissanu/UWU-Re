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
        self.health_lvl = 0
        self.strength_lvl = 0
        self.multiplier = 0
        self.baseCost = 500
        self.costArr = [50, 50, 100]
    
    def update(self, scroll):
        self.rect.y += scroll
        #check if platform has gone off
        if self.rect.top > 1080:
            self.kill()

    def load_upgrade(self, screen, bar_arr, color):
        for i in range(self.health_lvl):
            pygame.draw.rect(screen, color, (bar_arr[i], 210, 30, 70))
        for i in range(self.strength_lvl):
            pygame.draw.rect(screen, color, (bar_arr[i], 370, 30, 70))
        for i in range(self.multiplier):
            pygame.draw.rect(screen, color, (bar_arr[i], 600, 30, 70))

    def health_upgrade(self, coin, player):
        if coin >= self.costArr[0]:
            coin -= self.costArr[0]
            self.costArr[0] = self.costArr[0] + 100 * self.health_lvl
            player.max_health += 50
            self.health_lvl += 1
            return coin
        else:
            return -1
