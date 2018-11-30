import pygame

def create_window(window_width, window_height, window_caption, bg_color):
    """ Method that initializes a pygame window
    @param: window_width Specifies the width of the pygame window
    @param: window_height Specifies the height of the pygame window
    @param: window_caption Specifies the title at the top of the pygame window
    @param: bg_color Specifies the background color of the pygame window
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
    screen = create_window(800, 600, 'Brick Breaker', (0, 0, 0))

    # Start the main game loop
    while True:
        # Watch for event to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Redraw the game screen
        pygame.display.flip

if __name__ == "__main__":
    main()