import pygame
import os

WIDTH = 1920
HEIGHT = 1080
SCREEN = (WIDTH,HEIGHT)

CURRENT_PATH = os.getcwd()
BG_PATH = CURRENT_PATH + "\\src\\PythonGame\Assets\\Backgrounds"

def main():
    pygame.init()

    # CREATING CANVAS
    window = pygame.display.set_mode(SCREEN)
    # TITLE OF CANVAS
    pygame.display.set_caption("UWU:Re")
    bg_img = pygame.image.load(BG_PATH + "\\grass.jpg")
    bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))
    running = True
    
    while running:
        window.blit(bg_img,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        

main()