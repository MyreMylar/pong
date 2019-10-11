# -------------------
# BUILDING THE WALLS
# -------------------


# ---------------------------------------
# Step 1
# --------
#
# import pygame and the pygame.locals
# just as you did last week in the pong
# file:
#
# import pygame
# from pygame.locals import *
# ---------------------------------------


# ----------------------------------------
# Step 2
# --------
#
# Start defining a class called Wall
# by using the 'class' keyword followed
# by the name 'Wall' and finished with a :
#
# If you can't recall how to start defining
# a class from those hints, try looking at
# some old code from a previous week.
# ----------------------------------------


# ------------------------------------------------
# Step 3
# --------
#
# Start defining an __init__ function for our
# Wall class.
#
# Remember the first parameter of a class function
# must be the keyword 'self'.
#
# Make the function take three other parameters that
# will be;
# - the top left corner of our wall
# - the wall's width
# - and it's height
# -------------------------------------------------


# ---------------------------------------------------------
# Step 4
# --------
#
# Inside your __init__ function, type something like:
# 'self.rect = pygame.Rect(top_left_corner, (width, height))'
#
# What exactly you write will depend on what you called your
# input parameters. We are creating a pygame rectangle that
# is the size we want for our wall.
# ----------------------------------------------------------


# ---------------------------------------------------------
# Step 5
# --------
#
# Type:
#
# self.colour = pygame.Color("#CCCCCC")
#
# So we have a colour for our walls when we draw them.
# ---------------------------------------------------------


# ---------------------------------------------------------
# Step 6
# --------
#
# Create a new class function called 'render' that takes
# 'self' and 'screen' as parameters.
# ----------------------------------------------------------


# ---------------------------------------------------------
# Step 7
# --------
#
# Inside our render function type;
#
# pygame.draw.rect(screen, self.colour, self.rect)
#
# Which will draw our wall to the screen in the place, size
# and colour we have specified.
#
# Finally, delete all the comments in this file to clean it up,
# and head over to the 'pong' file to add the walls to the game.
# --------------------------------------------------------------
