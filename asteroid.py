import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, (139, 69, 19), self.position, self.radius, width=0)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        v1 = pygame.Vector2(self.velocity).rotate(angle)
        v2 = pygame.Vector2(self.velocity).rotate(angle * -1) 
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position[0], self.position[1], new_radius)
        a2 = Asteroid(self.position[0], self.position[1], new_radius)
        v1 = v1 * 1.2
        v2 = v2 * 1.2
        a1.velocity = v1
        a2.velocity = v2




