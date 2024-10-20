import pygame
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self, position, velocity, color, radius, lifespan):
        super().__init__()
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)
        self.color = color
        self.radius = radius
        self.lifespan = lifespan
        self.age = 0

    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt

        # Fade out over time (reduce radius and lifespan)
        self.age += dt
        self.radius -= dt * 50  # Adjust this value to control how fast particles shrink
        if self.radius < 0:
            self.radius = 0

        if self.age >= self.lifespan:
            self.kill()  # Remove the particle when its lifespan ends

    def draw(self, screen):
        if self.radius > 0:
            pygame.draw.circle(screen, self.color, self.position, int(self.radius))