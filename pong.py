import pygame
from pygame.locals import *

# -----------------------------------------------
# Make sure you start with the wall python file!
# -----------------------------------------------

# ------------------------------
# FINISHING THE WALLS
# --------------------
#
# Step 1
# --------
#
# Import the Wall class from the wall file by typing:
#
# from wall import Wall
#
# Type it near where you make the other imports
# for neatness.
# --------
# Step 2
# --------
#
# Create two walls and add them to a list
# somewhere before the game loop, but after
# you init() pygame - by typing this:
#
# walls = []
# walls.append(Wall((10, 10), 780, 10))
# walls.append(Wall((10, 580), 780, 10))
#
# --------
# Step 3
# --------
#
# Inside the game loop, after
# blitting the background, type:
#
# for wall in walls:
#   wall.render(screen)
#
# To paste the walls on the screen.
#
# Try running this file with F5 now and you
# should see the walls
# ------------------------------------------


# ------------------------------
# FINISHING THE BATS
# --------------------
#
# Step 1
# --------
#
# Import the Bat class from the bat file by typing:
#
# from Bat import Bat
#
# Type it near where you make the other imports
# for neatness.
# --------
# Step 2
# --------
#
# Create two control schemes for our two bats by
# typing:
#
# control_scheme_1 = ControlScheme()
# control_scheme_1.up = K_w
# control_scheme_1.down = K_s
#
# control_scheme_2 = ControlScheme()
# control_scheme_2.up = K_UP
# control_scheme_2.down = K_DOWN
# --------
# Step 3
# --------
#
# Create two bats and add them to a list by typing:
#
# bats = []
# bats.append(Bat((10, 200), 10, 100, control_scheme_1 ))
# bats.append(Bat((780, 200), 10, 100, control_scheme_2 ))
#
# --------
# Step 4
# --------
# Inside the game loop update and render the bats
# by typing something like this:
#
# for bat in bats:
#   bat.update(time_delta)
#   bat.render(screen)
#
# --------
# Step 5
# --------
#
# Inside our event getting for loop we need to send the events
# to our bats so they can get key presses.
#
# Type:
#
# for bat in bats:
#     bat.process_event(event)
#
# inside the event loop.
#
# Hopefully that's everything you need to do this week!
# Try running the code with F5, if it all worked you should be
# able to move around two pong bats with the W & S keys or the
# up and down arrow keys.
#
# Well done if you made it! (You can delete all the comments in this file now)
# -------------------------------------------------------------


pygame.init()
pygame.display.set_caption('Pong')
screen = pygame.display.set_mode((800, 600))

background = pygame.Surface(screen.get_size())
background = background.convert(screen)
background.fill(pygame.Color("#000000"))

clock = pygame.time.Clock()

running = True
while running:
    time_delta = min(0.1, (clock.tick(60) / 1000.0))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
