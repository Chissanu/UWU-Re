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

#define game variables


#define player action variables
moving_left = False
moving_right = False

#define colors
GREEN = (124,252,0)

#load images
CURRENT_PATH = os.getcwd()
#background
BG_PATH = CURRENT_PATH + "\\src\\PythonGame\\Assets\\Background"
bg_img = pygame.image.load(BG_PATH + "\\grass.jpg")
bg_img = pygame.transform.scale(bg_img,SIZE)
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


#Create player
player = Character.Character('Player', WIDTH/2, HEIGHT/2 + 100, 3, 5, screen)


#=====INITIALIZE======

running = True
while running:

    clock.tick(FPS)

    #Home
    if start_game == False:
        screen.fill(GREEN)
        # draw_window(screen, bg_img)
        if start_button.draw(screen):
            start_game = True
        if exit_button.draw(screen):
            running = False
    else:
        draw_window(screen, bg_img)
        player.draw()

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

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
                
                
    pygame.display.update()

pygame.quit()
    