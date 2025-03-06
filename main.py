import pygame
from constants import *

def main():
    #Initialize pygame, clock, and screen size
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while(1):
        #Fills screen with color black
        pygame.Surface.fill(screen, (0,0,0))

        #Allows screen to be closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Update the screen
        pygame.display.flip()

        #Setup 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()