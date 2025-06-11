import pygame
import sys
import time

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game_running = True

    # sounds
    pygame.mixer.init()
    explosion_sound = pygame.mixer.Sound("explosion.wav")
    gameover_explosion = pygame.mixer.Sound("gameover_explosion.wav")
    pygame.mixer.music.load("micron_by_micron.wav")
    pygame.mixer.music.play(-1)

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    AsteroidField()

    dt = 0
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                pygame.mixer.Sound.play(gameover_explosion)
                time.sleep(1)
                print("Game over!")
                sys.exit(1)
            for shot in shots:
                if asteroid.collision(shot):
                    pygame.mixer.Sound.play(explosion_sound)
                    asteroid.split()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
