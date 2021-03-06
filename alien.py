import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single aline in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the image and set is rect attributes
        self.image = pygame.image.load('assets/alien.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
