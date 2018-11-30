import pygame

class Paddle(pygame.sprite.Sprite):
    """ A class that represents the paddle that the player controls """

    def __init__(self):
        """ Constructor for the paddle class """
        super().__init__()

        # Set the paddle width and height
        self.paddle_width = 75
        self.paddle_height = 15

        # Create the paddle sprite and set the color
        self.image = pygame.Surface([self.paddle_width, self.paddle_height])
        self.image.fill((255, 51, 153))
        
        # Grab the dimensions of the paddle sprite and get the width and height of the screen
        self.rect = self.image.get_rect()
        self.screen_height = pygame.display.get_surface().get_height()
        self.screen_width = pygame.display.get_surface().get_width()

        # Set the position of the paddle
        self.rect.x = 0
        self.rect.y = self.screen_height - self.paddle_height
    
    def update(self):
        """ The update method for the paddle class which handles movement """
        # Grab the mouse position on the screen
        mouse_pos = pygame.mouse.get_pos()

        # Set the position of the paddle to the mouse
        self.rect.x = mouse_pos[0]

        # Set screen bounds
        if self.rect.x > self.screen_width - self.paddle_width:
            self.rect.x = self.screen_width - self.paddle_width



