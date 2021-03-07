import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.      ######when workng with ships edge, use center, center x, centery
        ## when you're working with the edge of screen use, top, bottom, left, or right.
        # note = (0,0) is at the top left of screen. origin is at top left.

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's horizontal position. 
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ship's position based on movement flags."""
        # Upate the ship's x value, not the rect. 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x 
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        


