import pygame

WIDTH = 1920
HEIGHT = 1080
SCREEN = (WIDTH,HEIGHT)

def main():
    pygame.init()

    # CREATING CANVAS
    canvas = pygame.display.set_mode(SCREEN)
    
    # TITLE OF CANVAS
    pygame.display.set_caption("UWU:Re")
    exit = False
    
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit = True
            if event.type == pygame.QUIT:
                exit = True
        pygame.display.update()
        

main()