import pygame
from constants import *
from player import Player

def main():
    #Initialize pygame, clock, and screen size
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player_ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while(1):
        #Fills screen with color black
        pygame.Surface.fill(screen, (0,0,0))

        #Allows screen to be closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        
        for item in drawable:
            item.draw(screen)

        #Update the screen
        pygame.display.flip()

        #Setup 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()