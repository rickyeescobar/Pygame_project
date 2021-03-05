import sys 
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        #^brought in background settings so that the game would run.

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        #^ the object assigned above is called a surface. a Surface is a part of the screen where a game element can 
        #be played.
    

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

            # Get rid of bullets that have dissapeared.
            for bullet in self.bullets.copy():                   #the copy method allows us to modify bullets inside
                if bullet in self.bullets.copy():                  # of the loop
                    if bullet.rect.bottom <= 0:
                        self.bullets.remove(bullet)
            
 

    def _check_events(self):
        """Respond to keypresses and mouse events."""       #<an event is an action that the user performs while
        # Watch for keyboard and mouse events.              #playing the game, such as pressing a key or moving
        for event in pygame.event.get():                    #the mouse.  this is called an event loop.
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)   

                 

    def _update_screen(self):
        """Update images on the screen, and flip to a new screen."""
        #redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible. gives the game the illusion of appearing 
        # like moving smoothly, animated.
        pygame.display.flip()


        
    #^ the run_game method is where the game is controlled from. 

if __name__ == '__main__':
    # make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


