import pygame
from pygame.locals import *

# -----------------------
# CREATING THE SCORE
# -----------------------

# -------------------------------------------------------
# Step 1
# -----------
#
# Create a new class called 'Score'.
# -------------------------------------------------------


# -------------------------------------------------------
# Step 2
# -----------
#
# Add an __init__ function to the Score class that takes
# 'self' and 'font' as parameters.
# -------------------------------------------------------

# -------------------------------------------------------
# Step 3
# -----------
#
# Next we need some class variables to represent the
# scores of the two players and store the font we will
# use.
#
# Inside your __init__ function write:
#
# self.player_1_score = 0
# self.player_2_score = 0
# self.font = font
#
# -------------------------------------------------------

# -------------------------------------------------------
# Step 4
# -----------
#
# Now we need a function to setup and update the text on
# the screen. Create a new function in your Score class
# called 'update_score_text' that takes 'self' as a parameter.
#
# Then write this inside the function:
#
# self.score_string = str(self.player_1_score) + " - " + str(self.player_2_score)
# self.score_text_render = self.font.render(self.score_string, True, pygame.Color(200, 200, 200))
# -------------------------------------------------------

# -------------------------------------------------------
# Step 5
# -----------
#
# No use having the function if we don't call it. Inside
# your __init__ function write:
#
# self.update_score_text()
# -------------------------------------------------------

# -------------------------------------------------------
# Step 6
# -----------
#
# Next we need a render function to actually paste our
# text on the screen. Create a 'render' function for our
# Score class that takes 'self' and 'screen' as parameters.
#
# Inside the render function write:
#
# screen.blit(self.score_text_render, self.score_text_render.get_rect(centerx=400, centery=50))
# -------------------------------------------------------


# -------------------------------------------------------
# Step 7
# -----------
#
# Finally we need some functions to increase our player's
# scores. Create two functions called 'increase_player_1_score'
# and 'increase_player_2_score' that take 'self' as a parameter.
#
# Inside each of them, increase the respective player score
# class variable by one with += and then call our
# update_score_text function.
#
# That's it for this file, head back to the 'pong' python
# file to finish the score.
# -------------------------------------------------------
