import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    game_clock = pygame.time.Clock()
    dt = 0

    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2),PLAYER_RADIUS)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        updateable.update(dt)
        for a in asteroids:
            if player.collision_check(a):
                print("Game Over!")
                sys.exit()
        for d in drawable:
            d.draw(screen, "white", 2)
        pygame.display.flip()

        dt = game_clock.tick(60) / 1000

    


if __name__ == "__main__":
    main()
