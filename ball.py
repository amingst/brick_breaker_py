import math
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

    def bounce(self, new_direction):
        """ The bounce method that handles what to do when a collision is detected. """
        self.ball_direction_degrees = (180 - self.ball_direction_degrees) % 360
        self.ball_direction_degrees -= new_direction
    
    def update(self):
        """ Update method for the ball class. Updates the ball's position on the screen. """
        
        # Convert the ball's direction to radians
        ball_direction_radians = math.radians(self.ball_direction_degrees)

        # Update the ball's position
        self.x_pos += self.velocity * math.sin(ball_direction_radians)
        self.y_pos -= self.velocity * math.cos(ball_direction_radians)

        # Update the sprite location
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

        # Handle collisions with walls
        if self.y_pos <= 0:
            self.bounce(0)
            self.y_pos = 1
        
        if self.x_pos <= 0:
            self.ball_direction_degrees = (360 - self.ball_direction_degrees) % 360
            self.x_pos = 1
        
        if self.x_pos > self.screen_width - self.ball_width:
            self.ball_direction_degrees = (360 - self.ball_direction_degrees) % 360
            self.x_pos = self.screen_width - self.ball_width - 1
        
        # Check if the ball fell off the bottom of the screen
        if self.y_pos > 600:
            return True
        else:
            return False