# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Refresh the display
        pygame.display.flip() 

if __name__ == "__main__":
    main()