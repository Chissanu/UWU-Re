import pygame
import os
from Classes import Button
# from Classes import Player

pygame.init()

SIZE = WIDTH, HEIGHT = (1920, 1080)
DISPLAY = pygame.display.set_mode(SIZE)
FPS = pygame.time.Clock()
CURRENT_PATH = os.getcwd()
BG_PATH = CURRENT_PATH + "\\src\\PythonGame\\Assets\\Background"
BTN_PATH = CURRENT_PATH + "\\src\\PythonGame\\Assets\\ButtonAssets"


bg_img = pygame.image.load(BG_PATH + "\\grass.jpg")
bg_img = pygame.transform.scale(bg_img,SIZE)
start_img = pygame.image.load(BTN_PATH + "\\start_btn.png")
exit_img = pygame.image.load(BTN_PATH + "\\exit_btn.png")


start_button = Button.Button(WIDTH/4 - start_img.get_width()/2, HEIGHT/2, start_img, 1.5)
exit_button = Button.Button(WIDTH/2 + WIDTH/4 - exit_img.get_width()/2, HEIGHT/2, exit_img, 1.5)

#Drawing the entire frame
def draw_window(display, background):
    display.blit(background,(0,0))
    pygame.display.update()

#=====INITIALIZE======

#User Events
# player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    draw_window(DISPLAY,bg_img)

    if start_button.draw(bg_img):
        print('START')
    if exit_button.draw(bg_img):
        print('EXIT')

    FPS.tick(60)
    