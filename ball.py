import pygame

class Ball(pygame.sprite.Sprite):
    """ A class that represents the ball. """

    velocity = 10.0
    x_pos = 0.0
    y_pos = 180.0
    ball_direction_degrees = 200
    ball_width = 10
    ball_height = 10

    def __init__(self):
        """ Constructor for the ball class. """
        super().__init__()

        # Create the ball sprite and set its color
        self.image = pygame.Surface([self.ball_width, self.ball_height])
        self.image.fill((255, 255, 255))

        # Grab the dimensions of the ball sprite
        self.rect = self.image.get_rect()

        # Grab the screen dimensions
        self.screen_height = pygame.display.get_surface().get_height()
        self.screen_width = pygame.display.get_surface().get_width()