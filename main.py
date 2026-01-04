from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create a new clock object
    clock = pygame.time.Clock()

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # before player object instance is created
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable

    asteroidField = AsteroidField()

    # delta time variable set to 0
    dt = 0

    while True:
        log_state()

        # close button uses this
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # update the group not the player
        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)
        # Replace with groups
        # player.draw(screen)
        # player.update(dt)
        pygame.display.flip()

        # call the clock.tick method
        # clock.tick(60)

        # amount of time that has passed since it was last called
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
