from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, width =2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        random_angle = random.uniform(20,50)
        deflectCCW = self.velocity.rotate(random_angle)
        deflectCW = self.velocity.rotate(-random_angle)
        self.radius -= ASTEROID_MIN_RADIUS
        new_ast_CCW = Asteroid(self.position.x, self.position.y, self.radius)
        new_ast_CCW.velocity = deflectCCW * 1.2

        new_ast_CW = Asteroid(self.position.x, self.position.y, self.radius)
        new_ast_CW.velocity = deflectCW * 1.2
