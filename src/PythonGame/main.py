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
MAX_PLATFORMS = 10
MAX_ENEMY = 10
scroll = 0
bg_scroll = 0

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define player action variables
moving_left = False
moving_right = False    

floor = 940
#define colors
GREEN = (124,252,0)
YELLOW = (255,255,0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#load images
CURRENT_PATH = os.getcwd()
#background
BG_PATH = CURRENT_PATH + "\\src\\PythonGame\\Assets\\Background"
bg_img = pygame.image.load(BG_PATH + "\\lined_paper.png").convert_alpha()
bg_img = pygame.transform.scale(bg_img,SIZE)
scale = 2
platform_img = pygame.image.load(BG_PATH + "\\pencil_HB_ready.png").convert_alpha()
platform_img = pygame.transform.scale(platform_img, (int(platform_img.get_width() * scale), int(platform_img.get_height() * scale)))
#button images
BTN_PATH = CURRENT_PATH + "\\src\\PythonGame\\Assets\\Button_img"
start_img = pygame.image.load(BTN_PATH + "\\start_btn.png").convert_alpha()
exit_img = pygame.image.load(BTN_PATH + "\\exit_btn.png").convert_alpha()
swordsman_btn_img = pygame.image.load(BTN_PATH + "\\swordsman_btn.png").convert_alpha()
archer_btn_img = pygame.image.load(BTN_PATH + "\\archer_btn.png").convert_alpha()
accept_img = pygame.image.load(BTN_PATH + "\\accept_btn.png").convert_alpha()

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
    display.blit(background,(0,-600 + bg_scroll))
 
#function for drawing character health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, BLACK, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30)) 
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

# def selection():
#     draw_window(screen, bg_img)
#     while True:
#         if swordsman_button.draw(screen):
#             # player.draw()
#             # player.update()
#             player = Swordsman('Swordsman', WIDTH/3, 800, 0.3, 10, screen, enemy_group)
#             selected = True
#             print("ehe")
#         if archer_button.draw(screen):
#             player = Archer('Archer', WIDTH/3, 800, 0.5, 10, screen, enemy_group, arrow_group)
#             selected = True
#         if accept_button.draw(screen) and selected:
#             return player, True, False
#         # return True

#create sprite groups
enemy_group = pygame.sprite.Group() 
arrow_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group() 

#Create starting preview player
player = Preview('Swordsman', WIDTH/3 - 100, 670, 1, 10, screen, WIDTH, platform_group)
# number_enemy = 2
# for i in range(number_enemy):
#     enemy = Enemy('Swordsman', WIDTH/(i+1), 800, 0.5, 5, screen, WIDTH, platform_group)
#     enemy_group.add(enemy)

    
#create starting platform
platform = Platform(swordsman_btn_img, WIDTH//2 - 300, HEIGHT - 150, 500, HEIGHT)
platform_group.add(platform)

#=====INITIALIZE======  

running = True 
while running:
    clock.tick(FPS)

    #Home
    if select_char_mode == False and start_game == False:
        draw_window(screen, bg_img)

        
        if start_button.draw(screen):
            select_char_mode = True
        if exit_button.draw(screen):
            running = False
    
    if select_char_mode == True and start_game == False:
        draw_window(screen, bg_img)
        player.draw()
        player.update()
        if swordsman_button.draw(screen):
            player = Preview('Swordsman', WIDTH/3 - 100, 670, 1, 10, screen, WIDTH, platform_group)
            sword_selected = True
            archer_selected = False
        if archer_button.draw(screen):
            player = Preview('Archer', WIDTH/3 - 100, 670, 1, 10, screen, WIDTH, platform_group)
            archer_selected = True
            sword_selected = False
        if accept_button.draw(screen) and (sword_selected or archer_selected):
            if sword_selected:
                player = Swordsman('Swordsman', WIDTH/3, 800, 0.3, 10, screen, WIDTH, enemy_group, platform_group)
            if archer_selected:
                player = Archer('Archer', WIDTH/3, 800, 0.3, 10, screen, WIDTH, enemy_group, arrow_group, platform_group)
                
            start_game, select_char_mode = True, False

    if start_game:
        # pygame.draw.line(screen, BLACK, (0, SCROLL_THRESHOLD), (WIDTH, SCROLL_THRESHOLD))
        #draw bakground
        scroll = player.update()
        bg_scroll += scroll
        if bg_scroll >= 600:
            bg_scroll = 0
        draw_game_bg(screen, bg_img, bg_scroll)

        #draw player
        player.draw()
        
        #update platforms
        if len(platform_group) < MAX_PLATFORMS:
            platform_width = random.randint(700, 800)
            platform_x = random.randint(0, WIDTH - platform_width)
            # platform_y = random.choice([platform.rect.y - 200, platform.rect.y])
            platform_y = platform.rect.y - 200
            platform = Platform(platform_img, platform_x, platform_y, platform_width, HEIGHT)
            platform_group.add(platform)
            if len(enemy_group) < MAX_ENEMY:
                enemy = Enemy('Swordsman', platform_x + platform_width/2, platform_y - 100, 0.3, 5, screen, WIDTH, platform_group, platform_width, HEIGHT)
                enemy_group.add(enemy)

        #update enemy
        posY = 100
        for enemy in enemy_group:
            enemy.update(player, scroll)
            enemy.draw()
            draw_health_bar(enemy.health, 1400, posY) 
            posY += 50

        platform_group.update(scroll)

        platform_group.draw(screen)

        #draw player health bar
        draw_health_bar(player.health, 100, 100)

        #restart game to main menu
        if player.alive == False:
            start_game = False
            enemy_group.empty()
            arrow_group.empty()


        arrow_group.update()

    
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
