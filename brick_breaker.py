import sys
import pygame

from brick import Brick
from paddle import Paddle
from ball import Ball

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
    ball_list = pygame.sprite.Group()

    # Instantiate the paddle and add to entities_list
    paddle = Paddle()
    entities_list.add(paddle)

    # Instantiate the ball and add to entities_list and ball_list
    ball = Ball()
    entities_list.add(ball)
    ball_list.add(ball)

    # Define the brick starting position and number of bricks
    brick_start_pos = 80
    num_bricks = 32

    # Game flags
    is_game_over = False

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
        
        # Update while failure state is not met
        if not is_game_over:
            paddle.update()
            is_game_over = ball.update()
        
        # Handle a failure state
        if is_game_over:
            sys.exit()

        # Handle collisions between the ball and paddle
        if pygame.sprite.spritecollide(paddle, ball_list, False):
            new_direction = (paddle.rect.x + paddle.paddle_width / 2) - (ball.rect.x + ball.ball_width / 2)

            ball.rect.y = screen.get_height() - paddle.rect.height - ball.rect.height - 1
            ball.bounce(new_direction)

        # Handle brick collisions
        broken_bricks = pygame.sprite.spritecollide(ball, brick_list, True)

        if len(broken_bricks) > 0:
            ball.bounce(0)

            if len(brick_list) == 0:
                is_game_over = True
        
        # Draw sprites to the screen
        entities_list.draw(screen)
        
        # Redraw the game screen
        pygame.display.flip()

if __name__ == "__main__":
    main()