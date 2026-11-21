# Main program where everything happens 

import pygame
from sys import exit 


def main():

    # initialize pygame 
    pygame.init()

    screen = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption("AstroLab")
    clock = pygame.time.Clock()



    running = True
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        # Screen background
        screen.fill((8, 10, 20))

        # Frame Rate per second
        clock.tick(60)     

        # Update constantly
        pygame.display.flip()     


    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
