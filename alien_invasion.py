import sys 
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        #^brought in background settings so that the game would run.
    
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        #^ the object assigned above is called a surface. a Surface is a part of the screen where a game element can 
        #be played.

        #set the background color. 
        self.by_color = (230,230,230)
    

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.game.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #^an event is an action that the user performs while playing the game, such as pressing a key or moving
            #the mouse.  this is called an event loop.

                    #redraw the screen during each pass through the loop.
                    self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible. gives the game the illusion of appearing 
            # like moving smoothly, animated.
            pygame.display.flip()
        
    #^ the run_game method is where the game is controlled from. 

if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


