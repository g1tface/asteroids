from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen, color, width=2):
        pygame.draw.circle(screen, color, self.position, width)
    
    def update(self, dt):
        self.position += (self.velocity * dt)