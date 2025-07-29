import pygame
from constants import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock().tick(60)
    dt = 0
    while True:
        screen.fill((0, 0, 0))  
        pygame.display.flip()
        dt += 60 / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()
