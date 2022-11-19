import pygame, os, sys, random, pygame_gui, time
from Classes.Button import Button
from Classes.Swordsman import Swordsman
from Classes.Enemy import Enemy
from Classes.Archer import Archer
from Classes.Preview import Preview
from Classes.Platform import Platform
from Classes.Buff import Buff

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
manager = pygame_gui.UIManager((WIDTH, HEIGHT))
text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (900, 50)), manager=manager,
                                               object_id='#main_text_entry')

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
start_button = Button((WIDTH/4 - start_img.get_width()/2, HEIGHT/2), start_img, 1.5, "start", font_big, BLACK, WHITE)
exit_button = Button((WIDTH/2 + WIDTH/4 - exit_img.get_width()/2, HEIGHT/2), exit_img, 1.5, "exit", font_big, BLACK, WHITE)
swordsman_button = Button((WIDTH - swordsman_btn_img.get_width()/1.5, HEIGHT/4), swordsman_btn_img, 0.5, "Swordsman", font_big, BLACK, WHITE)
archer_button = Button((WIDTH -  archer_btn_img.get_width()/1.5, HEIGHT/2), archer_btn_img, 0.5, "Archer", font_big, BLACK, WHITE)
accept_button = Button((WIDTH -  accept_img.get_width()/3.2, HEIGHT/1.3), accept_img, 0.2, "Accept", font_big, BLACK, WHITE)


platform_group = pygame.sprite.Group() 
enemy_group = pygame.sprite.Group() 
arrow_group = pygame.sprite.Group()

#Drawing the entire frame
def draw_window(display, background):
    display.blit(background,(0,0))

def draw_game_bg(display, background, bg_scroll):
    display.blit(background,(0,0 + bg_scroll))
    display.blit(background,(0,-500 + bg_scroll))

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


def get_user_name():
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                return event.text
            
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        screen.fill("white")

        manager.draw_ui(screen)

        pygame.display.update()

def start_game(player_seleted):
    MAX_PLATFORMS = 20
    MAX_ENEMY = 10
    MAX_SHOP = 1
    MAX_BUFF = 1
    scroll = 0 
    bg_scroll = 0
    score = 0
    shop_open = False
    buff_hit = False
    timerArr = []
    shop = Shop(0, 0)
    buff = Buff(0, 0)

    #create sprite groups
    platform_group = pygame.sprite.Group() 
    enemy_group = pygame.sprite.Group() 
    arrow_group = pygame.sprite.Group()
    shop_group = pygame.sprite.Group()
    buff_group = pygame.sprite.Group()

    #create starting platform
    platform = Platform(swordsman_btn_img, WIDTH//2 - 300, HEIGHT - 150, 500, HEIGHT)
    platform_group.add(platform)
    if player_seleted == "Swordsman":
        player = Swordsman('Swordsman', WIDTH/2, 800, 0.3, 10, screen, WIDTH, enemy_group, platform_group)
    else:
        player = Archer('Archer', WIDTH/2, 800, 0.3, 10, screen, WIDTH, enemy_group, arrow_group, platform_group)
        
    while True:
        clock.tick(FPS)
        #draw bakground
        bg_scroll += scroll
        if bg_scroll >= 500:
            bg_scroll = 0
        draw_game_bg(screen, bg_img, bg_scroll)
        #draw name 
        # draw_text(name, font_big, BLACK, 1500, 0)
        
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

            spawn_chance = random.randint(0, 100)
            if spawn_chance == 0:
                if len(shop_group) < MAX_SHOP:
                    shop = Shop(platform_x + platform_width/2, platform.rect.y - 85)
                    shop_group.add(shop)
            if spawn_chance > 60:
                if len(enemy_group) < MAX_ENEMY:         
                    enemy = Enemy('Swordsman', platform_x + platform_width/2, platform.rect.y - 85, 0.3, 5, screen, WIDTH, player, platform_group, platform_width, HEIGHT)
                    enemy_group.add(enemy)
            if spawn_chance < 20:
                if len(buff_group) < MAX_BUFF:
                    buff = Buff(platform_x + platform_width/2, platform.rect.y - 85)
                    buff_group.add(buff)
        
        if player.hit_box.colliderect(shop.rect) and key [pygame.K_f]:
            shop_open = True
        else:
            shop_open = False

        if player.hit_box.colliderect(buff.rect):
            buff_hit = True

        key = pygame.key.get_pressed()

        if shop_open:
            draw_window(screen, bg_img)  
            draw_text("shop open!!!", font_big, BLACK, WIDTH/2, HEIGHT/2)
            if accept_button.draw():
                shop_open = False

        if buff_hit:
            buff_group.remove(buff)
            buff.healthBuff(player)
            tick = pygame.time.get_ticks()
            timerArr.append(tick)
            timer = round((timerArr[-1] - timerArr[0])/1000)
            if timer > 5:
                buff.clearBuff(player)
                timerArr = []
                buff_hit = False

        # update enemy
        for enemy in enemy_group:
            enemy.draw_health_bar(enemy.hit_box.centerx - 50, enemy.hit_box.y -10) 
            enemy.draw()
            if enemy.update(scroll):
                score += 50

        shop_group.draw(screen)
        shop_group.update(scroll)
        buff_group.draw(screen)
        buff_group.update(scroll)
        arrow_group.update()
        #draw player
        player.draw()
        scroll = player.update()
        player.draw_health_bar(100, 100)
        platform_group.update(scroll)
        platform_group.draw(screen)

        pygame.draw.line(screen, BLACK, (0,300),(WIDTH, 300))

        draw_text('SCORE: ' + str(score), font_small, BLACK, 0, 0)
        
        #restart game to main menu
        if player.alive == False:
            enemy_group.empty()
            arrow_group.empty()
            main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                    pygame.quit()
                    sys.exit()
            #keyboard presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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


def select_char_mode():
    # global sword_selected
    # global archer_selected
    # global platform_group
    player = Preview('Swordsman', WIDTH/3 - 100, 670, 1, 10, screen, WIDTH, enemy_group, platform_group)
    while True:
        clock.tick(FPS)
        
        draw_window(screen, bg_img)
        mouse_get_pos = pygame.mouse.get_pos()
        player.draw()
        player.update()

        for button in (swordsman_button, archer_button, accept_button):
            button.changeColor(mouse_get_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if swordsman_button.checkForInput(mouse_get_pos):
                    player = Preview('Swordsman', WIDTH/3 - 100, 670, 1, 10, screen, WIDTH, enemy_group, platform_group)
                    sword_selected = True
                    archer_selected = not sword_selected
                if archer_button.checkForInput(mouse_get_pos):
                    player = Preview('Archer', WIDTH/3 - 100, 670, 1, 10, screen, WIDTH, enemy_group, platform_group)
                    archer_selected = True
                    sword_selected = not archer_selected
                if accept_button.checkForInput(mouse_get_pos) and (sword_selected or archer_selected):
                    if sword_selected:
                        player_selected = "Swordsman"
                    if archer_selected:
                        player_selected = "Archer"
                    start_game(player_selected)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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

def main_menu(): 
    run = True
    while run:
        draw_window(screen, bg_img)
        mouse_get_pos = pygame.mouse.get_pos()
        for button in (start_button, exit_button):
            button.changeColor(mouse_get_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.checkForInput(mouse_get_pos):
                    # get_user_name()
                    select_char_mode()
                # if exit_button.checkForInput(mouse_get_pos):
                #     pass
                if exit_button.checkForInput(mouse_get_pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        pygame.display.update()


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

main_menu()
