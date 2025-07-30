import circleshape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS, PLAYER_SHOOT_SPEED
import pygame

class Player(circleshape.CircleShape):
    def __init__(self, x , y, Shots):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = Shots
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.position = pygame.Vector2(self.position.x, self.position.y)
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        # Keep player within screen bounds
        self.position.x = max(0, min(self.position.x, SCREEN_WIDTH))
        self.position.y = max(0, min(self.position.y, SCREEN_HEIGHT))
    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_position = self.position + forward * (self.radius + SHOT_RADIUS)
        shot_velocity = forward * PLAYER_SHOOT_SPEED
        new_shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS, shot_velocity)
        self.shots.add(new_shot)



class Shot(circleshape.CircleShape):
    containers = ()
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            width=2
        )
    def update(self, dt):
        self.position += self.velocity * dt