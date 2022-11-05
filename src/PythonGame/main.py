import pygame
import os
from Classes import Player

pygame.init()

SIZE = WIDTH, HEIGHT = (1920, 1080)
DISPLAY = pygame.display.set_mode(SIZE)
FPS = pygame.time.Clock()
CURRENT_PATH = os.getcwd()
BG_PATH = CURRENT_PATH + "\\src\\PythonGame\\Assets\\Background"

bg_img = pygame.image.load(BG_PATH + "\\grass.jpg")
bg_img = pygame.transform.scale(bg_img,SIZE)



#Drawing the entire frame
def draw_window(display, background):
    display.blit(background,(0,0))
    pygame.display.update()

#=====INITIALIZE======

#User Events
player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    draw_window(DISPLAY,bg_img)
    FPS.tick(60)
    
