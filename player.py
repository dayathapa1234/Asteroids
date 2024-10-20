import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.acceleration = pygame.Vector2(0, 0)
        self.max_speed = PLAYER_MAX_SPEED
        self.friction = FRICTION

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Accelerate forward/backward with W/S
        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.acceleration = forward * 500  # Apply acceleration forward
        elif keys[pygame.K_s]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.acceleration = -forward * 500  # Apply acceleration backward
        else:
            self.acceleration = pygame.Vector2(0, 0)  # No acceleration if no key pressed

        # Apply rotation with A/D
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Shoot with SPACE
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Update velocity based on acceleration and apply friction
        self.velocity += self.acceleration * dt
        self.velocity *= self.friction  # Apply friction

        # Limit the velocity to max speed
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        # Update position based on velocity
        self.position += self.velocity * dt

        # Decrease shoot cooldown timer
        self.timer -= dt

        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        if not (self.timer > 0):
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1)
            shot.rotation = self.rotation
            shot.velocity = shot.velocity.rotate(shot.rotation)
            shot.velocity *= PLAYER_SHOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
