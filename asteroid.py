import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        new_angle = random.uniform(20,50)
        asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        asteroid_1.velocity = self.velocity.rotate(new_angle)*1.2
        asteroid_2.velocity = self.velocity.rotate(new_angle*-1)*1.2