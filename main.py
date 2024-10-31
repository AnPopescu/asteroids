#allow us to use code from lyibrary
import pygame
from constants import *
from player import Player

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
        
        screen.fill("black")
        
        for obj in updatable_grp:
            obj.draw(screen) 
            
        
        
        pygame.display.flip()
        
        time_passed = clock_py.tick(60)
        dt = time_passed / 1000
    
    
if __name__ == "__main__":
    main()
