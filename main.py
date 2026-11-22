# Main program where everything happens 

import pygame
from sys import exit 
import config

from renderer import Renderer
from objects.celestial_body import CelestialBody


def main():

    # initialize pygame 
    pygame.init()

    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    clock = pygame.time.Clock()

    # Celestial body
    sun = CelestialBody(500, 250, 2000, 15, (239, 142, 56))

    running = True
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        # Render
        renderer = Renderer(screen)

        #### Background ####
        renderer.draw_background()

        #### Draw Body ####
        renderer.draw_body(sun)

        # Frame Rate per second
        clock.tick(config.FPS)     

        # Update constantly
        pygame.display.flip()     


    pygame.quit()
    exit()

if __name__ == "__main__":
    main()
