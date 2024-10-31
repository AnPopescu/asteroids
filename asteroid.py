from circleshape import *
from constants import ASTEROID_KINDS,ASTEROID_MAX_RADIUS,ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"Violet",self.position,self.radius,2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        new_angle = random.uniform(20,50)
        left_angle = self.velocity.rotate(new_angle)
        right_angle = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
        split_asteroid1.velocity = left_angle * 3
        
        split_asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
        split_asteroid2.velocity = right_angle * 3
        
    