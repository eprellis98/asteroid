import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):    
    def __init__(self, x, y, ):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface):
        pygame.draw.circle(surface, 'red', self.position, self.radius, width = 0)
        pygame.draw.circle(surface, 'yellow', self.position, self.radius, width = 2)


    def update(self, dt):
        self.position += (self.velocity * dt)