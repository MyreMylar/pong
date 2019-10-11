# -------------------
# BUILDING THE BATS
# -------------------


# --------------------------------------------
# Step 1
# --------
#
# Copy all the code you just wrote
# in the wall file over to here to start with
#
# But rename the class from 'Wall' to 'Bat'
# --------------------------------------------


# --------------------------------------------
# Step 2
# --------
#
# Create a second class above our Bat class
# called 'ControlScheme'.
# ---------------------------------------------


# -------------------------------------------------
# Step 3
# --------
#
# Create an __init__ function for our ControlScheme
# class that just takes 'self' as a parameter
#
# Add two class variables to the __init__ function
# by typing:
#
# self.up = K_UP
# self.down = K_DOWN
#
# We'll use these variables later to set the keyboard keys
# used for controlling two different bats.
# ------------------------------------------------


# -------------------------------------------------
# Step 4
# --------
#
# Moving back to our Bat class, we need to add
# an input parameter to our __init__function
# called 'control_scheme' so we can use it for our
# ControlScheme class later.
#
# store the new parameter in a class variable by
# typing:
#
# self.control_scheme = control_scheme
#
# in the __init__ function
# --------------------------------------------------


# ------------------------------------------------------------------
# Step 5
# --------
#
# Add a few more class variables to the Bat's __init__
# function that we will use later to move the Bat around - by
# typing this into the function:
#
# self.move_up = False
# self.move_down = False
# self.move_speed = 350.0
# self.position = [float(top_left_corner[0]), float(top_left_corner[1])]
#
# Depending on what you named your top left corner parameter,
# you may have to adjust that code a little
# -------------------------------------------------------------------


# ------------------------------------------------------------------
# Step 6
# --------
#
# Two more functions to go! First, we need to capture our key presses.
#
# Make a class function called 'process_event' that takes 'self' and
# 'event' as parameters.
#
# -------------------------------------------------------------------


# ------------------------------------------------------------------
# Step 7
# --------
#
# Inside our process_event function we are going to check when our
# control scheme keys are pressed down and released.
#
# To do this type:
#
# if event.type == KEYDOWN:
#    if event.key == self.control_scheme.up:
#        self.move_up = True
#    if event.key == self.control_scheme.down:
#        self.move_down = True
#
# if event.type == KEYUP:
#    if event.key == self.control_scheme.up:
#        self.move_up = False
#    if event.key == self.control_scheme.down:
#        self.move_down = False
#
# into the function. We are just setting our move_up and move_down
# variables based on what is happening with our Bat's control keys.
# ---------------------------------------------------------------------


# ------------------------------------------------------------------
# Step 8
# --------
#
# Last function!
#
# Create a class function called 'update' that takes 'self' and one
# called 'dt' as parameters. dt stands for 'delta time' which just
# means the tiny amount of time that has passed between game 'frames'
# otherwise known as how long it takes to make one loop of the game loop.
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# Step 9
# --------
#
# Inside our update function we are going to move the bat upward
# when our moveUp variable is set to True, and down when our moveDown
# variable is set to True.
#
# Moving it smoothly requires multiplying our bat's speed by the time delta
# value, otherwise changes in the frame rate would make our bat move jerkily about.
#
# We also need to stop the bat when it gets too high or too low to stop it
# going off the screen forever.
#
# To do this type:
#
# if self.move_up:
#    self.position[1] -= dt * self.move_speed
#
#    if self.position[1] < 20.0:
#        self.position[1] = 20.0
#
#    self.rect.y = self.position[1]
#
# if self.move_down:
#    self.position[1] += dt * self.move_speed
#
#    if self.position[1] > 480.0:
#        self.position[1] = 480.0
#
#    self.rect.y = self.position[1]
#
#
# That's it for the Bat file, head back over to the pong file to get the bats
# into the game. Then if you did it right you can clear out all these comments!
# ----------------------------------------------------------------------------
