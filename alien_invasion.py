import sys 
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        #^brought in background settings so that the game would run.

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #^ the object assigned above is called a surface. a Surface is a part of the screen where a game element can 
        #be played.
    

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
 

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #^an event is an action that the user performs while playing the game, such as pressing a key or moving
            #the mouse.  this is called an event loop.

    def _update_screen(self):
        """Update images on the screen, and flip to a new screen."""
        #redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible. gives the game the illusion of appearing 
        # like moving smoothly, animated.
        pygame.display.flip()


        
    #^ the run_game method is where the game is controlled from. 

if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


