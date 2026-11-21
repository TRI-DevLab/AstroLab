# Main program where everything happens 

import pygame
from sys import exit 
import config


def main():

    # initialize pygame 
    pygame.init()

    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    clock = pygame.time.Clock()



    running = True
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        # Screen background
        screen.fill(config.BACKGROUND_COLOR)

        # Frame Rate per second
        clock.tick(config.FPS)     

        # Update constantly
        pygame.display.flip()     


    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
