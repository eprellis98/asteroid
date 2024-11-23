import sys
import pygame
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

score = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)  # Font size 36, or adjust as needed


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print(f"Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    global score
                    score += 10

        screen.fill((4, 16, 36))  # Ensure this is before drawing

        # Draw all objects
        for obj in drawable:
            obj.draw(screen)

        # Render and draw the score AFTER filling the screen
        text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(text, (10, 10))  # Position the score at (10, 10)

        pygame.display.flip()  # Ensure this updates all drawings on the screen

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
