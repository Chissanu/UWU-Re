import pygame, os, sys, random, pygame_gui, time
from pygame import mixer
from Classes.Button import Button
from Classes.Swordsman import Swordsman
from Classes.Enemy import Enemy
from Classes.Archer import Archer
from Classes.Preview import Preview
from Classes.Platform import Platform
from Classes.Buff import Buff
from Classes.Leaderboard import Leaderboard
from Classes.Shop import Shop

pygame.init()
pygame.mixer.init()

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
font_big = pygame.font.SysFont('Lucida Sans', 70)
very_small = pygame.font.SysFont('Lucida Sans', 20)

#define player action variables
moving_left = False
moving_right = False    

#define colors
GREEN = (124,252,0)
YELLOW = (255,255,0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

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
base_img = pygame.image.load(os.path.join(BTN_PATH, "base_btn.png")).convert_alpha()
start_img = pygame.image.load(os.path.join(BTN_PATH, "start_btn.png")).convert_alpha()
exit_img = pygame.image.load(os.path.join(BTN_PATH, "exit_btn.png")).convert_alpha()
leaderBoard_img = pygame.image.load(os.path.join(BTN_PATH, "leaderBoard_btn.png")).convert_alpha()
swordsman_btn_img = pygame.image.load(os.path.join(BTN_PATH, "swordsman_btn.png")).convert_alpha()
archer_btn_img = pygame.image.load(os.path.join(BTN_PATH, "archer_btn.png")).convert_alpha()
accept_img = pygame.image.load(os.path.join(BTN_PATH, "accept_btn.png")).convert_alpha()
restart_img = pygame.image.load(os.path.join(BTN_PATH, "restart_btn.png")).convert_alpha()
#load music and sound
soundPath = os.path.join(CURRENT_PATH,"src","PythonGame", "Assets","Sound")

#create buttons
start_button = Button((WIDTH/2, HEIGHT/2 - 200), start_img, 0.3, "START", font_big, WHITE, GRAY)
exit_button = Button((WIDTH/2, HEIGHT/2 + 200), None, 0.3, "EXIT", font_big, BLACK, GRAY)
exit_button_restart = Button((WIDTH/2 + 200, HEIGHT/2 + 400), None, 0.2, "EXIT", font_small, WHITE, BLACK)
leaderBoard_button = Button((WIDTH/2, HEIGHT/2), leaderBoard_img, 0.4, "LEADER BOARD", font_big, WHITE, GRAY)
swordsman_button = Button((WIDTH/1.3, HEIGHT/4), swordsman_btn_img, 0.5, "Swordsman", font_big, WHITE, GRAY)
archer_button = Button((WIDTH/1.3 , HEIGHT/2), archer_btn_img, 0.5, "Archer", font_big, WHITE, GRAY)
accept_button = Button((WIDTH -  accept_img.get_width()/3.2, HEIGHT/1.3), accept_img, 0.3, "ACCEPT", font_big, WHITE, GRAY)
restart_button = Button((WIDTH/2, HEIGHT/2 + 250), restart_img, 0.25, "RESTART", font_small, BLACK, GRAY)
main_menu_button = Button((WIDTH/2 - 100, HEIGHT/2 + 400), exit_img, 0.25, "main menu", font_small, WHITE, GRAY)
back_button = Button((WIDTH - 200, HEIGHT-200), None, 0.25, "back", font_small, BLACK, GRAY)
search_button = Button((WIDTH - 400, HEIGHT-200), None, 0.25, "search", font_small, BLACK, GRAY)
return_button = Button((WIDTH - 200, HEIGHT-200), None, 0.25, "Return", font_small, WHITE, GRAY)

#Classes Import
scoreboard = Leaderboard()


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
 
def play_click():
    pygame.mixer.Sound(os.path.join(soundPath,"click.wav")).play()

def shopOpen(screen, shop, coins, player, coin_rate):
    returnToGame = False
    #add button
    health_add_button = Button((WIDTH/2, HEIGHT/2 - 300), None, 0.25, "X", font_big, WHITE, GRAY)
    strength_button = Button((WIDTH/2, HEIGHT/2 - 150), None, 0.25, "X", font_big, WHITE, GRAY)
    booster_button = Button((WIDTH/2, HEIGHT/2 + 15), None, 0.25, "X", font_big, WHITE, GRAY)
    while True:
        mouse_get_pos = pygame.mouse.get_pos()
        bar_arr = [350, 450, 550, 650, 750]
        screen.fill(BLACK)
        draw_text("Shop", font_big, WHITE, WIDTH/2 - 100, 50)
        currentCoin = f"Current coin: {coins}"
        draw_text(currentCoin, font_small, WHITE, WIDTH/2 + 400, 50)
        health_img = pygame.image.load(os.path.join(CURRENT_PATH, 'src', 'PythonGame', 'Assets', 'shop_img', 'healthIcon.png')).convert_alpha()
        health_img = pygame.transform.scale(health_img, (int(health_img.get_width() * 0.1), int(health_img.get_height() * 0.1)))
        strength_img = pygame.image.load(os.path.join(CURRENT_PATH, 'src', 'PythonGame', 'Assets', 'shop_img', 'strengthIcon.png')).convert_alpha()
        strength_img = pygame.transform.scale(strength_img, (int(strength_img.get_width() * 0.1), int(strength_img.get_height() * 0.1)))
        booster_img = pygame.image.load(os.path.join(CURRENT_PATH, 'src', 'PythonGame', 'Assets', 'shop_img', 'booster.png')).convert_alpha()
        booster_img = pygame.transform.scale(booster_img, (int(booster_img.get_width() * 0.05), int(booster_img.get_height() * 0.05)))
        draw_text(str(50 + 100 * player.health_lvl), font_big, WHITE, WIDTH/2 - 160, HEIGHT/2 - 320) #ยิ่งลบยิ่งขึ้น
        draw_text(str(50 + 100 * player.strength_lvl), font_big, WHITE, WIDTH/2 - 160, HEIGHT/2 - 175)
        draw_text(str(100 + 100 * player.multiplier), font_big, WHITE, WIDTH/2 - 160, HEIGHT/2 - 10)
        for i in bar_arr:
            pygame.draw.rect(screen, GRAY, (i, 210, 30, 70))
            pygame.draw.rect(screen, GRAY, (i, 360, 30, 70))
            pygame.draw.rect(screen, GRAY, (i, 515, 30, 70))
        shop.load_upgrade(screen, bar_arr, GREEN, player)
        screen.blit(health_img, (200, 200))
        screen.blit(strength_img, (200, 350))
        screen.blit(booster_img, (200, 500))
        # button
        for button in (health_add_button, strength_button, booster_button, return_button,):
            button.changeColor(mouse_get_pos)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                play_click()
                if health_add_button.checkForInput(mouse_get_pos):
                    output = shop.health_upgrade(coins, player)
                    if output < 0:
                        draw_text("Not enough coins!!", font_big, WHITE, WIDTH/2, HEIGHT/2)
                    else:
                        coins = output
                if strength_button.checkForInput(mouse_get_pos):
                    output = shop.strength_upgrade(coins, player)
                    if output < 0:
                        draw_text("Not enough coins!!", font_big, WHITE, WIDTH/2, HEIGHT/2)
                    else:
                        coins = output
                if booster_button.checkForInput(mouse_get_pos):
                    output = shop.booster(coins, coin_rate, player)
                    if output < 0:
                        draw_text("Not enough coins!!", font_big, WHITE, WIDTH/2, HEIGHT/2)
                    else:
                        coins = output
                if return_button.checkForInput(mouse_get_pos):
                    returnToGame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        if returnToGame:
            return (False, coin_rate, coins)
        #pygame.draw.rect()
        pygame.display.update()

def restart(score, player_selected, name):
    ANIMATION_PATH = os.path.join(CURRENT_PATH, 'src', 'PythonGame', 'Assets', 'Character_img')
    img = pygame.image.load(os.path.join(ANIMATION_PATH, player_selected, "Death",(str(4) + ".png"))).convert_alpha()
    img = pygame.transform.scale(img, (int(img.get_width() * 0.8), int(img.get_height() * 0.8)))
    while True:
        screen.fill(GRAY)
        mouse_get_pos = pygame.mouse.get_pos()

        draw_text("YOUR SCORE:", font_big, BLACK, WIDTH/2 - 200, 200)
        draw_text(str(name), font_big, BLACK, WIDTH/2 - 100, 100)
        draw_text(str(score), font_big, WHITE, WIDTH/2, 300)
        
        screen.blit(img, (450,200))
        
        for button in (restart_button, exit_button_restart, main_menu_button):
            button.changeColor(mouse_get_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                play_click()
                if restart_button.checkForInput(mouse_get_pos):
                    start_game(player_selected, name)
                if main_menu_button.checkForInput(mouse_get_pos):
                    main_menu()
                if exit_button_restart.checkForInput(mouse_get_pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        pygame.display.update()

def leader_board_page():
    soundPath = os.path.join(CURRENT_PATH,"src","PythonGame","Assets","Sound","menu.wav")
    pygame.mixer.Sound(soundPath).play()
    
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((WIDTH / 2 + 500, 100), (300, 50)), manager=manager,
                                               object_id='#main_text_entry')
    scoreboard = Leaderboard()
    players = scoreboard.getSortedScoreboard() 
    
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        screen.fill(WHITE)
        mouse_get_pos = pygame.mouse.get_pos()
        index = 1
        for button in (back_button, search_button):
            button.changeColor(mouse_get_pos)
            button.update(screen)

        for item in players:
            if index == 1:
                draw_text(item["name"], font_big, RED, WIDTH/2 - 200, 100)
                draw_text(str(item["score"]), font_big, RED, WIDTH/2 + 200, 100)
                draw_text(str(item["position"]), font_big, RED, WIDTH/2 - 400, 100)
            else:
                draw_text(item["name"], font_small, BLACK, WIDTH/2 - 200, 100 + 50 * index)
                draw_text(str(item["score"]), font_small, BLACK, WIDTH/2 + 200, 100 + 50 * index)
                draw_text(str(item["position"]), font_small, BLACK, WIDTH/2 -400, 100 + 50 * index)
                
            index += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                players = scoreboard.findPlayer(event.text)
            if event.type == pygame.MOUSEBUTTONDOWN:
                play_click()
                if back_button.checkForInput(mouse_get_pos):
                    main_menu()
                if search_button.checkForInput(mouse_get_pos):
                    players = scoreboard.getSortedScoreboard()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            manager.process_events(event)
        manager.update(UI_REFRESH_RATE)
        manager.draw_ui(screen)

        pygame.display.update()

def start_game(player_selected, name):
    MAX_PLATFORMS = 20
    MAX_ENEMY = 5
    MAX_SHOP = 1
    MAX_BUFF = 1
    scroll = 0 
    bg_scroll = 0
    score = 0
    coin = 0
    coin_add_rate = 20
    shop_open = False
    buff_hit = False
    buff_random = True
    timerArr = []
    clicked = True
    # shop = Shop(0, 0)
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
    if player_selected == "Swordsman":
        player = Swordsman('Swordsman', WIDTH/2, 800, 0.3, 10, screen, SIZE, enemy_group, platform_group)
    else:
        player = Archer('Archer', WIDTH/2, 800, 0.3, 10, screen, SIZE, enemy_group, arrow_group, platform_group)
        
    while True:
        clock.tick(FPS)
        #draw bakground
        bg_scroll += scroll
        if bg_scroll >= 500:
            bg_scroll = 0
        draw_game_bg(screen, bg_img, bg_scroll)
        #draw name 
        draw_text(name, font_big, BLACK, 1500, 0)
        
        #draw stats
        hp = "HP:" + str(player.getHp()) + "/" + str(player.max_health)
        atk = "ATK:" + str(player.getAttack())
        
        draw_text(hp, font_small, BLACK, 70, 310)
        draw_text(atk, font_small, BLACK, 70, 360)
        
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
            if spawn_chance > 0:
                if len(shop_group) < MAX_SHOP:
                    shop = Shop(platform_x + platform_width/2, platform.rect.y - 85)
                    shop_group.add(shop)
            if spawn_chance > 60:
                if len(enemy_group) < MAX_ENEMY:         
                    enemy = Enemy('Swordsman', platform_x + platform_width/2, platform.rect.y - 85, 0.3, 5, screen, SIZE, player, platform_group, platform, score)
                    enemy_group.add(enemy)
            if spawn_chance < 20:
                if len(buff_group) < MAX_BUFF:
                    buff = Buff(platform_x + platform_width/2, platform.rect.y - 85)
                    buff_group.add(buff)
        
        if player.hit_box.colliderect(shop.rect) and key [pygame.K_f]:
            output = shopOpen(screen, shop, coin, player, coin_add_rate)
            coin_add_rate = output[1]
            coin = output[2]

        if player.hit_box.colliderect(buff.rect):
            buff_hit = True

        key = pygame.key.get_pressed()
            
        if buff_hit:
            x_buff = 200
            y_buff = 180
            buff_group.remove(buff)
            buff.setData(player)
            if buff_random:
                mode = random.randint(1, 2)
                buff_random = False
            if mode == 1:
                buff.restore_health()
                tick = pygame.time.get_ticks()
                timerArr.append(tick)
                timer = (timerArr[-1] - timerArr[0])/1000
                if round(timer) == 0:
                    timer = 0.00001
                buff.draw_buff_bar(x_buff, y_buff, screen, timer * 60, mode)
                if timer > 5:
                    buff.clearBuff(mode)
                    timerArr = []
                    buff_hit = False
                    buff_random = True
            elif mode == 2:
                buff.superJump()
                tick = pygame.time.get_ticks()
                timerArr.append(tick)
                timer = (timerArr[-1] - timerArr[0])/1000
                if round(timer) == 0:
                    timer = 0.00001
                buff.draw_buff_bar(x_buff, y_buff, screen, timer * 60, mode)
                if timer > 5:
                    buff.clearBuff(mode)
                    timerArr = []
                    buff_hit = False
                    buff_random = True
        # update enemy
        for enemy in enemy_group:
            enemy.draw_health_bar(enemy.hit_box.centerx - 50, enemy.hit_box.y -10) 
            enemy.draw()
            if enemy.update(scroll):
                score += 50
                coin += coin_add_rate

        shop_group.draw(screen)
        shop_group.update(scroll)
        buff_group.draw(screen)
        buff_group.update(scroll)
        arrow_group.update(scroll)
        #draw player
        player.draw()
        scroll = player.update()
        player.draw_health_bar(100, 100)
        platform_group.update(scroll)
        platform_group.draw(screen)

        # pygame.draw.line(screen, BLACK, (0,300),(WIDTH, 300))

        draw_text('SCORE: ' + str(score), font_small, BLACK, 0, 0)
        draw_text('COINS: ' + str(coin), font_small, BLACK, 300, 0)
        
        #restart game to main menu
        if player.alive == False:
            enemy_group.empty()
            arrow_group.empty()
            newData = {
                "name" : name,
                "score": score
            }
            pygame.mixer.Sound(os.path.join(soundPath,"death.wav")).play()
            scoreboard.saveScore(newData)
            restart(score,player_selected, name) 

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
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((1250, 100), (500, 50)), manager=manager,
                                               object_id='#main_text_entry')
    global sword_selected
    global archer_selected
    # global platform_group
    player = Preview('Swordsman', WIDTH/3 - 100, 670, 1.5, 10, screen, SIZE, enemy_group, platform_group)
    sword_selected = True
    char_name, x = "-The Swordsman-", 350
    name = None
    show_accept = False
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        clock.tick(FPS)
        draw_window(screen, bg_img)
        # draw_text(name, font_small, BLACK, WIDTH/2 + 500, 100)
        draw_text(char_name, font_small, BLACK, x, 200)
        draw_text("Put your name here, then please press [enter]!", very_small, BLACK, 1200, 70)
        mouse_get_pos = pygame.mouse.get_pos()
        player.draw()
        player.update()

        for button in (swordsman_button, archer_button):
            button.changeColor(mouse_get_pos)
            button.update(screen)
        
        if show_accept:
            accept_button.changeColor(mouse_get_pos)
            accept_button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry') and name == None:
                name = event.text
                show_accept = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                play_click()
                if swordsman_button.checkForInput(mouse_get_pos):
                    player = Preview('Swordsman', WIDTH/3 - 100, 670, 1.5, 10, screen, SIZE, enemy_group, platform_group)
                    char_name, x = "-The Swordsman-", 350
                    sword_selected = True
                    archer_selected = not sword_selected
                if archer_button.checkForInput(mouse_get_pos):
                    player = Preview('Archer', WIDTH/3 - 100, 670, 1.5, 10, screen, SIZE, enemy_group, platform_group)
                    char_name, x = "-The Archer-", 400
                    archer_selected = True
                    sword_selected = not archer_selected
                if show_accept:
                    if accept_button.checkForInput(mouse_get_pos) and (sword_selected or archer_selected) and name != None:
                        if sword_selected:
                            player_selected = "Swordsman"
                            start_game(player_selected, name)
                        if archer_selected:
                            player_selected = "Archer"
                            start_game(player_selected, name)

            if event.type == pygame.KEYDOWN and name != None:
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
            manager.process_events(event)
        manager.update(UI_REFRESH_RATE)
        manager.draw_ui(screen)
     
        pygame.display.update() 

def main_menu():
    global name
    run = True
    while run:
        draw_window(screen, bg_img)
        mouse_get_pos = pygame.mouse.get_pos()
        for button in (start_button, exit_button, leaderBoard_button):
            button.changeColor(mouse_get_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                play_click()
                if start_button.checkForInput(mouse_get_pos):
                    select_char_mode()
                if leaderBoard_button.checkForInput(mouse_get_pos):
                    leader_board_page()
                    pass
                if exit_button.checkForInput(mouse_get_pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        pygame.display.update()

main_menu()
