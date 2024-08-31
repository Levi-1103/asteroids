import pygame
from circleshape import CircleShape
from constants import *
import random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y , radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius,2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        random_angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        small_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, small_asteroid_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, small_asteroid_radius)
        asteroid.velocity = b * 1.2
        
        
