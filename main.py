import pygame
from constants import *
from player import *
from asteroid import *
from asteroid_field import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  
    Shots = pygame.sprite.Group()
    Score = 0
    player_obj = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, Shots)
    # Sprite groups for updating and drawing
    updatable = pygame.sprite.Group(player_obj)
    drawable = pygame.sprite.Group(player_obj)
    #Asteroid objects
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    #--------------------------------------------------------
    Shots.containers = (Shots, updatable, drawable)
    while True:
        
        dt = clock.tick(60) / 1000.0
        screen.fill((0, 0, 0))  
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player_obj):
                print("Game over!")
                print("Final Score:", Score)
                pygame.quit()
                return
        
        Shots.update(dt)
        for shot in Shots:
            shot.draw(screen)
        
        for sprite in drawable:
            sprite.draw(screen)
        
        for asteroid in asteroids:
            for shot in Shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    Score += 100
                    break
        
        pygame.display.flip()
        
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    


if __name__ == "__main__":
    main()
