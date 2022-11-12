import pygame
import os
from Classes import Button
from Classes import Character

pygame.init()

SIZE = WIDTH, HEIGHT = (1920, 1080)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('UwU:RE')
start_game = False

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define player action variables
moving_left = False
moving_right = False
attack = False

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
bg_img = pygame.image.load(BG_PATH + "\\paper.jpg")
bg_img = pygame.transform.scale(bg_img,SIZE)
scale = 2
floor_img = pygame.image.load(BG_PATH + "\\ruler20.png")
floor_img = pygame.transform.scale(floor_img, (int(floor_img.get_width() * scale), int(floor_img.get_height() * scale)))
#button images
BTN_PATH = CURRENT_PATH + "\\src\\PythonGame\\Assets\\Button_img"
start_img = pygame.image.load(BTN_PATH + "\\start_btn.png")
exit_img = pygame.image.load(BTN_PATH + "\\exit_btn.png")

#create buttons
start_button = Button.Button(WIDTH/4 - start_img.get_width()/2, HEIGHT/2, start_img, 1.5)
exit_button = Button.Button(WIDTH/2 + WIDTH/4 - exit_img.get_width()/2, HEIGHT/2, exit_img, 1.5)

#Drawing the entire frame
def draw_window(display, background):
    display.blit(background,(0,0))

#function for drawing character health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, BLACK, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

#Create player
player = Character.Character('Player', WIDTH/2, HEIGHT/2 + 100, 0.5, 5, screen)
enemy = Character.Character('Player', WIDTH/2, HEIGHT/2 + 100, 0.5, 5, screen)

#=====INITIALIZE======

running = True
while running:

    clock.tick(FPS)

    #Home
    if start_game == False:
        screen.fill(GREEN)
        if start_button.draw(screen):
            start_game = True
        if exit_button.draw(screen):
            running = False
    else:
        draw_window(screen, bg_img)
        screen.blit(floor_img,(0,725))
        draw_health_bar(enemy.health, 100, 100)

        player.update_animation()
        player.draw()
        enemy.draw()
        

        player.move(moving_left, moving_right)

    	#update player actions
        if player.alive:
            if player.in_air:
                player.update_action(2)#2: jump
            elif moving_left or moving_right:
                player.update_action(1)#1: run
            elif attack == True:
                player.update_action(3)
            else:
                player.update_action(0)#0: idle
            player.move(moving_left, moving_right)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w and player.alive:
                player.jump = True
            if event.key == pygame.K_SPACE:
                attack = True
            if event.key == pygame.K_SPACE:
                player.attack(enemy)

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                attack = False
                
               
    pygame.display.update()

pygame.quit()
