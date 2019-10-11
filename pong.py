# ---------------------------------------------------------------------
# MAKING PONG - week 1
# ---------------------
# This week we are going to create a version of the game
# 'Pong' from scratch.
#
# In case you don't know, Pong was a simplified 2D simulation of
# table-tennis using a few rectangles to represent the bats.
# and the ball.
# It was a huge hit back in the 1980s!
#
# We'll start out this week by getting a simple game loop up and running
# in pygame, I'll take you through it step by step to help.
# ---------------------------------------------------------------------


# ------------------------------------------------------------
# STEP 1
# --------
# import the 'pygame' library. This lets us use the pygame code in our game.
#
# You should also import the pygame 'locals' file directly which
# contains some useful definitions we will use (like the keyboard keys).
# You do that by writing:
#
# from pygame.locals import *
# ------------------------------------------------------------


# ------------------------------------------------------------
# STEP 2
# --------
# Call the pygame.init() function
#
# This just does some basic setup for pygame so we are ready to
# start using it's graphical capabilities and such like.
# ------------------------------------------------------------


# ------------------------------------------------------------
# STEP 3
# -------
# Create a 'screen' variable and assign it
# to the result of calling pygame.display.set_mode((800,600))
#
# 800 will be the window's width in pixels and 600 is the window's
# height.
#
# Calling this function will make pygame create a window into which all
# our graphics can be drawn.
# ------------------------------------------------------------


# ------------------------------------------------------------
# STEP 4
# --------
# Delete the comments for the steps you've done already
# and run the code with F5
#
# You should find that you get a window with a black background
# and the title 'pygame window'. We will now change these things!
# ---------------------------------------------------------------


# ------------------------------------------------------------
# STEP 5
# -------
# Change the window title by calling the function;
# pygame.display.set_caption('Dan's Super Cool Pong')
#
# And set the background colour by:
#
# 1. creating a new variable and calling it 'background'
# then setting it to be a pygame surface with this function:
# pygame.Surface(screen.get_size())
#
# 2. filling the background surface with a colour using the fill()
#    function. For example:
#    background.fill((100,0,0))
#
# 3. Paste the background surface onto our screen using the
#    'blit' function, like so:
#    screen.blit(background, (10,10))
#    The last variable is the top left co-ordinates of where
#    we want to start pasting down our background. You
#    probably want to start at 0,0.
#
#  4. Call pygame.display.flip() to signal that we are ready to
#     show our pygame 'screen' to the world.
# ------------------------------------------------------------


# -----------------------------------------------------------
# STEP 6
# -------
# The next thing we need to set up is the actual 'game loop'.
#
# This is just the loop that stops our program, or our game, from ending
# before we want it to and allows us to do things like move graphics
# smoothly frame by frame. Each loop of the game loop represents one 'frame'
# of our game, which is a term borrowed from film, where once upon a time
# each image in ye olde strips of film looked much like a small framed picture.
#
# We are going to use a while loop that uses a variable called
# 'running' to check if our game is still running or not.
#
# 1. Create the variable 'running' and set it to True.
#
# 2. Create a while loop which uses 'running' as it's condition.
#
# 3. Move the screen.blit(background, (0, 0)) and
#    pygame.display.flip() function calls inside your
#    while loop.
# --------------------------------------------------------------


# --------------------------------------------------------------
# STEP 7
# --------
# Clean up this code file again, removing all completed comment
# steps and run the code to check it all still works.
#
# You may have noticed that pressing the X button on your window
# to close your pygame program doesn't work. We'll fix that next.
# --------------------------------------------------------------


# --------------------------------------------------------------
# STEP 8
# -------
# We are going to create a pygame 'event' watching loop inside
# our game loop. This will let our code react to input like
# keyboard key presses and pressing the window buttons like X.
#
# 1. To start the event loop write:
#   for event in pygame.event.get():
#
# 2. A single event is generated whenever you interact with
#    your program window in some way. Each 'event' is a class object
#    that contains some information on the event that occurred which
#    we can use to decide how to react to it. To start with, every
#    event has a 'type' that indicates what type of interaction it is
#    e.g. KEYDOWN for pressing a keyboard keydown, or MOUSEBUTTONUP when
#    a mouse button is released after being held down.
#
# 3. Anyway, not much point having an event loop if we don't use it.
#    Inside our event loop, write an if statement that checks if
#    our event.type is equal to QUIT. QUIT is defined in the pygame
#    locals import so hopefully you imported that back in step 1!
#
# 4. Inside our QUIT event if statement set the 'running' variable
#    to False. This should let our code exit the game loop.
#
# 5. Finally outside of the game loop, at the bottom of our code
#    write pygame.quit(). This will close the pygame window.
# --------------------------------------------------------------


# --------------------------------------------------------------
# STEP 9
# ---------
# Check that everything works by pressing F5 and trying to close
# the window then clean up the code comments again so we are ready
# for next week when we try to get some table tennis bats into the
# game!
# --------------------------------------------------------------
