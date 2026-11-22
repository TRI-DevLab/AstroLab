# This file handles everything we will draw onto the pygame screen

import pygame
import config


class Renderer:

    def __init__(self, screen: pygame.Surface):

        self.screen = screen


    def draw_background(self):
        """Draw the Universe background."""

        # Screen background
        self.screen.fill(config.BACKGROUND_COLOR)


    def draw_body(self, body):
        """Draw individual celestial body."""

        pygame.draw.circle(
            self.screen,
            body.color,
            (int(body.x), int(body.y)),
            body.radius
        )