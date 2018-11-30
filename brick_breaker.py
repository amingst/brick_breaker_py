import pygame

def create_window(window_width, window_height, window_caption, bg_color):
    pygame.init()
    pygame.display.set_caption(window_caption)
    
    screen = pygame.display.set_mode([window_width, window_height])

    return screen;

def main():
    screen = create_window(800, 600, 'Brick Breaker', (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip

if __name__ == "__main__":
    main()