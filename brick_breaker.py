import sys
import pygame

from brick import Brick
from paddle import Paddle

def create_window(window_width, window_height, window_caption):
    """ Method that initializes a pygame window
    @param: window_width Specifies the width of the pygame window
    @param: window_height Specifies the height of the pygame window
    @param: window_caption Specifies the title at the top of the pygame window
    @return: screen The screen object that game objects are drawn to
    """
    # Initialize the pygame window
    pygame.init()
    pygame.display.set_caption(window_caption)
    
    # Create the screen object
    screen = pygame.display.set_mode([window_width, window_height])

    return screen;

def main():
    """ The main function that runs the game """
    screen = create_window(800, 600, 'Brick Breaker')

    # Create lists for the game sprites
    entities_list = pygame.sprite.Group()
    brick_list = pygame.sprite.Group()

    # Instantiate the paddle and add to entities_list
    paddle = Paddle()
    entities_list.add(paddle)

    # Define the brick starting position and number of bricks
    brick_start_pos = 80
    num_bricks = 32

    # Build the brick matrix
    for x in range(5):
        for y in range(0, num_bricks):
            brick = Brick((255, 102, 0), y * (23 + 2) + 1, brick_start_pos)
            brick_list.add(brick)
            entities_list.add(brick)
        brick_start_pos += 15 + 2


    fps_clock = pygame.time.Clock()

    # Start the main game loop
    while True:
        # Set the framerate
        fps_clock.tick(60)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Watch for event to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        paddle.update()
        
        # Draw sprites to the screen
        entities_list.draw(screen)
        
        # Redraw the game screen
        pygame.display.flip()

if __name__ == "__main__":
    main()