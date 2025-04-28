# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    FPS = pygame.time.Clock()
    dt = 0
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Groups for updating values
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initializations
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    astro_field = AsteroidField()

    #Infinite Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #specifies framerate maximum at 60 FPS
        dt = FPS.tick(60)/1000

        #prints background
        screen.fill(color="black")

         #updates the objects in the updateables group of sprites

        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                exit("Game over!")
            for shot in shots:
                if asteroid.check_collisions(shot):
                    asteroid.split()
                    shot.kill()

        #draws all obejcts in the drawables sprite group
        for drawable in drawables:
            drawable.draw(screen)

        #updates the display
        pygame.display.flip()



if __name__ == "__main__":
    main()
