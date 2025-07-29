import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  
    player_obj = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    while True:
        dt = clock.tick(60) / 1000.0
        screen.fill((0, 0, 0))  
        player_obj.update(dt)
        player_obj.draw(screen)
        
        
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    


if __name__ == "__main__":
    main()
