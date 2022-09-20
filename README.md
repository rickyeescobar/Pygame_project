# Pygame_project
# Alien Invasion game

#### Video Demo Link: https://youtu.be/0XhQnw_E_00

##### must have pygame downloaded in order to play
##### run alien_invasion.py to play and press "q" to quit

In Alien Invasion, the player controls a rocket ship that appears at the bottom of the screen.
The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar.
When the game begins, a fleet of aliens fills the sky and moves across and down the screen. The player 
shoots and destroys the aliens. If the player shoots all the aliens, a new fleet appears that moves 
faster than the previous fleet. If any alien hits the player's ship or reaches the bottom of the screen,
the player loses a ship. If the player loses three ships, the game ends.




`alien_invasion.py` :
the main file. contains the AlienInvasion class. has multiple important attributes. 
The main loop of the game runs on here. The While loop calls the 
`_check_event()` (detects relevent events, ie key presses and releases), processes these events. 
`ship.update()`  updates the position of the ship.
`_update_screen()` method which redraws the screen on loop.


`settings.py`:
has an `__init__()` method
contains the Settings class. controls games appearance and ship speed.


`ship.py`:
has and `__init__()` method, `update()` method, and `blitme()` method 
contains the Ship class. has the image of the ship.
