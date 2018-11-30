import pygame

class Brick(pygame.sprite.Sprite):
    """ A class that represents the bricks that the player tries to break """

    # Member variables
    width = 23
    height = 15

    def __init__(self, brick_color, x_pos, y_pos):
        """ Constructor for the brick class
        @param: brick_color Specifies the color of the brick being created
        @param: x_pos Specifies the x axis position of the block
        @param: y_pos Specifies the y axis position of the block
        """
        super().__init__()

        # Create the brick sprite and set the color
        self.brick_sprite = pygame.Surface([width, height])
        self.brick_sprite.fill(brick_color)

        # Grab the dimensions of the brick sprite and move to the correct position
        self.rect = self.brick_sprite.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
