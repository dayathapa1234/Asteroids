import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()
	Shot.containers = (shots, updatable, drawable)

	Player.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	dt = 0
	score = 0
	lives = 3
	font = pygame.font.SysFont(None, 36)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for obj in updatable:
			obj.update(dt)

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		for asteroid in asteroids:
			if asteroid.collisions(player):
				lives -= 1
				if lives <= 0:
					print("Game Over!")
					exit(0)
				else:
					player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
			for shot in shots:
				if shot.collisions(asteroid):
					score += 100  
					shot.kill()
					asteroid.split()

		score_display = font.render(f"Score: {score}", True, (255, 255, 255))
		screen.blit(score_display, (10, 10))
		lives_display = font.render(f"Lives: {lives}", True, (255, 255, 255))
		screen.blit(lives_display, (10, 50))
		pygame.display.flip()

		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
