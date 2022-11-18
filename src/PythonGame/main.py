import pygame, os, random
from Classes.Button import Button
from Classes.Swordsman import Swordsman
from Classes.Enemy import Enemy
from Classes.Archer import Archer
from Classes.Preview import Preview
from Classes.Platform import Platform

pygame.init()

SIZE = WIDTH, HEIGHT = (1920, 1080)
SCROLL_THRESHOLD = 500

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('UwU:RE')

#game variables
start_game = False
select_char_mode = False
sword_selected = True
archer_selected = False
MAX_PLATFORMS = 20
MAX_ENEMY = 10
MAX_SHOP = 1
scroll = 0 
bg_scroll = 0
score = 0
shop_open = False

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define font
font_small = pygame.font.SysFont('Lucida Sans', 50)
font_big = pygame.font.SysFont('Lucida Sans', 100)

#define player action variables
moving_left = False
moving_right = False    

#define colors
GREEN = (124,252,0)
YELLOW = (255,255,0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#load images
CURRENT_PATH = os.getcwd()
#background
BG_PATH = os.path.join(CURRENT_PATH, "src", "PythonGame", "Assets", "Background") # might have to add "" if it doesn't work
bg_img = pygame.image.load(os.path.join(BG_PATH, "lined_paper.png")).convert_alpha()
bg_img = pygame.transform.scale(bg_img,SIZE)
scale = 2
platform_img = pygame.image.load(os.path.join(BG_PATH, "pencil_HB_ready.png")).convert_alpha()
platform_img = pygame.transform.scale(platform_img, (int(platform_img.get_width() * scale), int(platform_img.get_height() * scale)))
#button images
BTN_PATH = os.path.join(CURRENT_PATH, "src", "PythonGame", "Assets", "Button_img")
start_img = pygame.image.load(os.path.join(BTN_PATH, "start_btn.png")).convert_alpha()
exit_img = pygame.image.load(os.path.join(BTN_PATH, "exit_btn.png")).convert_alpha()
swordsman_btn_img = pygame.image.load(os.path.join(BTN_PATH, "swordsman_btn.png")).convert_alpha()
archer_btn_img = pygame.image.load(os.path.join(BTN_PATH, "archer_btn.png")).convert_alpha()
accept_img = pygame.image.load(os.path.join(BTN_PATH, "accept_btn.png")).convert_alpha()

#create buttons
start_button = Button(WIDTH/4 - start_img.get_width()/2, HEIGHT/2, start_img, 1.5)
exit_button = Button(WIDTH/2 + WIDTH/4 - exit_img.get_width()/2, HEIGHT/2, exit_img, 1.5)
swordsman_button = Button(WIDTH - swordsman_btn_img.get_width()/1.5, HEIGHT/4, swordsman_btn_img, 0.5)
archer_button = Button(WIDTH -  archer_btn_img.get_width()/1.5, HEIGHT/2, archer_btn_img, 0.5)
accept_button = Button(WIDTH -  accept_img.get_width()/3.2, HEIGHT/1.3, accept_img, 0.2)


#Drawing the entire frame
def draw_window(display, background):
    display.blit(background,(0,0))

def draw_game_bg(display, background, bg_scroll):
    display.blit(background,(0,0 + bg_scroll))
    display.blit(background,(0,-500 + bg_scroll))

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

#create sprite groups
platform_group = pygame.sprite.Group() 
enemy_group = pygame.sprite.Group() 
arrow_group = pygame.sprite.Group()
shop_group = pygame.sprite.Group()

#create starting platform
platform = Platform(swordsman_btn_img, WIDTH//2 - 300, HEIGHT - 150, 500, HEIGHT)
platform_group.add(platform)


class Shop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(CURRENT_PATH, 'src', 'PythonGame', 'Assets', 'Background', 'shop.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.05), int(self.image.get_height() * 0.05)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, scroll):
        self.rect.y += scroll
        #check if platform has gone off
        if self.rect.top > HEIGHT:
            self.kill()
shop = Shop(0, 0)

# player = Archer('Archer', WIDTH/3, 800, 0.3, 10, screen, WIDTH, enemy_group, arrow_group, platform_group)

#=====INITIALIZE======  

running = True 
while running:
    clock.tick(FPS)

    #Home
    if select_char_mode == False and start_game == False:
        draw_window(screen, bg_img)        
        if start_button.draw(screen):
            #Create starting preview player
            player = Preview('Swordsman', WIDTH/3 - 100, 670, 1, 10, screen, WIDTH, enemy_group, platform_group) 
            select_char_mode = True
        if exit_button.draw(screen):
            running = False
    
    if select_char_mode == True and start_game == False:
        draw_window(screen, bg_img)
        player.draw()
        player.update()
        if swordsman_button.draw(screen):
            player = Preview('Swordsman', WIDTH/3 - 100, 670, 1, 10, screen, WIDTH, enemy_group, platform_group)
            sword_selected = True
            archer_selected = False
        if archer_button.draw(screen):
            player = Preview('Archer', WIDTH/3 - 100, 670, 1, 10, screen, WIDTH, enemy_group, platform_group)
            archer_selected = True
            sword_selected = False
        if accept_button.draw(screen) and (sword_selected or archer_selected):
            if sword_selected:
                player = Swordsman('Swordsman', WIDTH/2, 800, 0.3, 10, screen, WIDTH, enemy_group, platform_group)
            if archer_selected:
                player = Archer('Archer', WIDTH/2, 800, 0.3, 10, screen, WIDTH, enemy_group, arrow_group, platform_group)
            start_game, select_char_mode = True, False

    key = pygame.key.get_pressed()
    if shop_open:
        draw_window(screen, bg_img)  
        draw_text("shop open!!!", font_big, BLACK, WIDTH/2, HEIGHT/2)
        if accept_button.draw(screen):
            start_game = True
            shop_open = False

    if start_game:
        #draw bakground
        bg_scroll += scroll
        if bg_scroll >= 500:
            bg_scroll = 0
        draw_game_bg(screen, bg_img, bg_scroll)

        #draw player
        player.draw()
        
        #update platforms
        if len(platform_group) < MAX_PLATFORMS:
            platform_random = random.randint(0, 1)
            if platform_random == 0 and WIDTH - ( platform.rect.x + platform.rect.width) > 200:    
                platform_y = platform.rect.y
                platform_width = random.randint(100, WIDTH - (platform.rect.x + platform.rect.width + 100))
                platform_x = random.randint(platform.rect.x + platform.rect.width + 100, WIDTH - platform_width)
            else:
                platform_y = platform.rect.y - 200
                platform_width = random.randint(400, 500)
                platform_x = random.randint(0, WIDTH - platform_width - 400)
            platform = Platform(platform_img, platform_x, platform_y, platform_width, HEIGHT)
            platform_group.add(platform)

            spawn_chance = random.randint(0, 10)
            if spawn_chance == 0:
                if len(shop_group) < MAX_SHOP:
                    shop = Shop(platform_x + platform_width/2, platform.rect.y - 85)
                    shop_group.add(shop)
            if spawn_chance > 5:
                if len(enemy_group) < MAX_ENEMY:         
                    enemy = Enemy('Swordsman', platform_x + platform_width/2, platform.rect.y - 85, 0.3, 5, screen, WIDTH, player, platform_group, platform_width, HEIGHT)
                    enemy_group.add(enemy)
        
        if player.hit_box.colliderect(shop.rect) and key [pygame.K_f]:
            shop_open = True
            start_game = False
        else:
            shop_open = False
        shop_group.draw(screen)
        shop_group.update(scroll)

        platform_group.update(scroll)
        platform_group.draw(screen)


        # update enemy
        for enemy in enemy_group:
            enemy.draw_health_bar(enemy.hit_box.centerx - 50, enemy.hit_box.y -10) 
            enemy.draw()
            if enemy.update(scroll):
                score += 50


        draw_text('SCORE: ' + str(score), font_small, BLACK, 0, 0)
        #draw player health bar
        player.draw_health_bar(100, 100)
        #restart game to main menu
        if player.alive == False:
            start_game = False
            enemy_group.empty()
            arrow_group.empty()
        pygame.draw.line(screen, BLACK, (0,300),(WIDTH, 300))

        arrow_group.update()
        scroll = player.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
                running = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif player.attacking == False and player.alive:
                if event.key == pygame.K_a:
                    player.moving_left = True
                if event.key == pygame.K_d:
                    player.moving_right = True
                if event.key == pygame.K_w and player.in_air == False:
                    player.jump = True
                if event.key == pygame.K_SPACE and player.attack_cooldown == 0:
                    player.attacking = True

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.moving_left = False
            if event.key == pygame.K_d:
                player.moving_right = False
                
               
    pygame.display.update()

pygame.quit()
