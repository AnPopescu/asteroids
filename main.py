#allow us to use code from lyibrary
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    
    #Presentation
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    #Grpups 
    updatable_grp = pygame.sprite.Group()
    drawable_grp = pygame.sprite.Group()
    Player.containers = (updatable_grp,drawable_grp)
    
    asteroid_grp = pygame.sprite.Group()
    Asteroid.containers = (asteroid_grp,updatable_grp,drawable_grp)
    
    shots_grp = pygame.sprite.Group()
    Shot.containers = shots_grp,updatable_grp,drawable_grp
    
    AsteroidField.containers = updatable_grp
    
    astero_field1 = AsteroidField()
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    aster_player = Player(x ,y)
    
    clock_py = pygame.time.Clock()
    dt = 0
    
   
    
    
    #Game Loop
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable_grp:
            obj.update(dt) 
        
        
        #Check Collisions
        for asteroid in asteroid_grp:
            if(asteroid.CheckCollision(aster_player)):
                print("GAME OVER!")
                return
            for bullet in shots_grp:
                if(bullet.CheckCollision(asteroid)):
                    asteroid.split()
                    bullet.kill()
        
        screen.fill("black")
        
        for obj in drawable_grp:
            obj.draw(screen) 
            
        
        
        pygame.display.flip()
        
        time_passed = clock_py.tick(60)
        dt = time_passed / 1000
    
    
if __name__ == "__main__":
    main()
