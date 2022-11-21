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
        self.costArr = [50, 50, 100,50]
    
    def update(self, scroll):
        self.rect.y += scroll
        #check if platform has gone off
        if self.rect.top > 1080:
            self.kill()

    def load_upgrade(self, screen, bar_arr, color, player):
        for i in range(player.health_lvl):
            pygame.draw.rect(screen, color, (bar_arr[i], 210, 30, 70))
        for i in range(player.strength_lvl):
            pygame.draw.rect(screen, color, (bar_arr[i], 360, 30, 70))
        for i in range(player.multiplier):
            pygame.draw.rect(screen, color, (bar_arr[i], 515, 30, 70))

    def health_upgrade(self, coin, player):
        if coin >= self.costArr[0]:
            coin -= self.costArr[0]
            self.costArr[0] += 100 * player.health_lvl
            player.increaseMaxHp(50)
            player.increaseHp(50)
            player.health_lvl += 1
            return coin
        else:
            return -1

    def strength_upgrade(self, coin, player):
        if coin >= self.costArr[1]:
            coin -= self.costArr[1]
            self.costArr[1] += 100 * player.strength_lvl
            player.origiAtk += 25
            player.atk_damage += 25
            player.strength_lvl += 1
            return coin
        else:
            return -1
    
    def booster(self, coin, coinRate, player):
        if coin >= self.costArr[2]:
            coin -= self.costArr[2]
            self.costArr[2] += + 100 * player.multiplier
            coinRate += 10
            player.multiplier += 1
            return coin
        else:
            return -1
        
    def heal(self,coin,player):
        print("hedsakmdsads")
        if coin >= self.costArr[3]:
            coin -= self.costArr[3]
            if player.health + 50 > player.max_health:
                player.health += player.max_health - player.health
            else:
                player.health += 50
            return coin
        else:
            return -1