from circleshape import CircleShape
import pygame
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),  # white rgb values
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            width = 2
        )
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
           
        random_angle = random.uniform(20, 50)
        rotated_velocity = self.velocity.rotate(random_angle)
        neg_rotated_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = rotated_velocity * 1.2
        new_asteroid2.velocity = neg_rotated_velocity * 1.2
        
        

        