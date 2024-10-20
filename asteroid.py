import pygame
import random
from constants import *
from circleshape import CircleShape
from particle import Particle 


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT

    def split(self):
        self.spawn_explosion()
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        new_angle = random.uniform(20,50)
        asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
        asteroid_1.velocity = self.velocity.rotate(new_angle)*1.2
        asteroid_2.velocity = self.velocity.rotate(new_angle*-1)*1.2
    
    def spawn_explosion(self):
        # Explosion color (brownish-reddish)
        explosion_color = (165, 42, 42)  

        # Generate explosion particles based on asteroid size
        num_particles = int(self.radius / 5)  # More particles for larger asteroids
        for _ in range(num_particles):
            velocity = pygame.Vector2(random.uniform(-100, 100), random.uniform(-100, 100))
            radius = random.uniform(self.radius / 4, self.radius / 2)  # Particle size based on asteroid size
            particle = Particle(self.position, velocity, explosion_color, radius, 1)  # Lifespan of 1 second
            Particle.containers.add(particle)