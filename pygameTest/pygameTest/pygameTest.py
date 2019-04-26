# import the pygame module
import pygame
import random

# import pygame.locals for easier access to key coordinates
from pygame.locals import *

# Define our player object and call super to give it all the properties and methods of pygame.sprite.Sprite
# The surface we draw on the screen is now a property of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('singleStrokeRoll.png').convert()
        self.image = pygame.transform.rotozoom(self.image, 0, .5)
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()

class Bar(pygame.sprite.Sprite):
    def __init__(self):
        super(Bar, self).__init__()
        self.image = pygame.image.load('bar.png').convert()
        self.image = pygame.transform.smoothscale(self.image, (5, 150))
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(219, 250))
        self.speed = 50.5

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left >729 :
            self.kill()

# initialize pygame
pygame.init()



# create the screen object
# here we pass it a size of 800x600
screen = pygame.display.set_mode((1200, 800))
background = pygame.Surface(screen.get_size())
background.fill((255, 255, 255))
# instantiate our player; right now he's just a rectangle
MOVEBAR = pygame.USEREVENT + 1
pygame.time.set_timer(MOVEBAR, 2500)
player = Player()
bar = Bar()
#bar = pygame.sprite.Group()
#all_sprites = pygame.sprite.Group()
#all_sprites.add(player)
# Variable to keep our main loop running
running = True

# Our main loop!
while running:
    # for loop through the event queue
    #bar.update()
    for event in pygame.event.get():
        screen.blit(background, (0, 0))
        
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
        elif event.type == MOVEBAR:
            #new_bar = Bar()
            #bar.add(new_bar)
            bar.update()
            
    #bar.update()
    # Draw the player to the screen
  
    screen.blit(bar.image, bar.rect)
    screen.blit(player.image, (150, 200))
    # Update the display
    pygame.display.flip()