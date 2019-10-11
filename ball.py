# -------------------
# Creating the Ball
# -------------------

import pygame
import math
import random

# ---------------------------------------------------------
# Step 1
# --------
#
# I've done the necessary imports for you this time, so
# Step 1 is just to make an empty class called Ball.
# ---------------------------------------------------------

# ---------------------------------------------------------
# Step 2
# --------
#
# Create an __init__ function for our Ball class that takes
# 'self' and 'start_position' as it's parameters.
# ---------------------------------------------------------


# ---------------------------------------------------------
# Step 3
# --------
#
# Just as with the Wall and Bat classes we need our Ball
# to have a pygame.Rect and a pygame.Color so that we can
# draw it on the screen.
# Write these lines into our new __init__() function
# to set that up:
#
# self.rect = pygame.Rect(start_position, (10, 10))
# self.colour = pygame.Color(255, 255, 255
# ---------------------------------------------------------


# ---------------------------------------------------------
# Step 4
# --------
#
# Finally, we need to setup some extra variables to describe
# the position & movement of the ball, and whether it has collided
# with our Bats or the Walls.
#
# Write this into the __init__() function:
#
# self.position = [float(start_position[0]),float(start_position[1])]
# self.start_position = [self.position[0], self.position[1]]
# self.ball_speed = 350.0
# self.max_bat_bounce_angle = 5.0 * math.pi/12.0
# self.collided = False
# ---------------------------------------------------------

# ---------------------------------------------------------
# Step 5
# --------
#
# Create a render function for our Ball class. It should be
# basically the same as the one's for our Bats and Walls
# with this:
#
# pygame.draw.rect(screen, self.colour, self.rect)
#
# in it.
# -----------------------------------------------------------

# ---------------------------------------------------------
# Step 6
# --------
#
# The next function we need is one that sets up a random
# starting direction for our ball to move in when it first
# appears.
#
# Create a new function for our Ball called 'create_random_start_vector'
# and have it take only 'self' as a parameter.
# -----------------------------------------------------------

# ---------------------------------------------------------
# Step 7
# --------
#
# There are lots of ways to create a random starting vector
# but I wrote the inside of the function like this:
#
# y_random = random.uniform(-0.5, 0.5)
# x_random = 1.0 - abs(y_random)
# if random.randint(0, 1) == 1:
#     x_random = x_random * -1.0
# self.velocity = [x_random * self.ball_speed, y_random * self.ball_speed]
#
# The idea being that a normalised Y vector value of 1.0 is straight downward, and -1.0
# is straight upward - so vector values that have a y value between 0.5 and -0.5 should be angles in
# 90, degree cones to the sides. We then generate an appropriate normalised x value
# to match our random y value and use the random library again to flip it 50% of the time
# so that balls go both left and right.
#
# Don't worry if you don't understand that! Vectors take a while to get used to!
#
# The main thing you should know is that the 'length' of the vector here has to initially add up to
# 1.0 so that when we multiply it's values by the ball speed it really does travel at that speed.
#
# (You can just cut and paste the five lines of code above into your function)
# -------------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Step 8
# --------
#
# A random starting vector function isn't much use if we don't ever call it.
#
# Call your create_random_start_vector() function at the bottom of your __init__
# function.
#
# You'll need to start your call with the self. keyword just as if we were
# creating another class variable.
# ----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Step 9
# --------
#
# Once our Ball has gone off-screen we need to reset it to the centre again. This
# is why we've kept hold of a copy of the Ball's starting position and made the
# starting vector code into a function.
#
# Create a new function in our Ball class called 'reset' that just takes 'self'
# as a parameter.
#
# Inside it write this:
#
# self.position = [self.start_position[0], self.start_position[1]]
# self.create_random_start_vector()
#
# You may recognise this code from the __init__ function. That's because we are basically
# redoing that part of our game program each time the ball goes off the screen!
# ------------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Step 10
# --------
#
# OK! Last function for the Ball class is the update function, just like we had
# with the Bat class but we need to do a few more tricky things in this one.
#
# - Create a new function called 'update' for our ball that takes 'self', 'dt'
#   and two new parameters called 'bats' and 'walls' that will represent our
#   lists of bats and walls from the pong file.
#
# - Write this code inside the update function to move the ball each frame,
#   based on the parameters we set out in our __init__ function:
#
#   self.position[0] += self.velocity[0] * dt
#   self.position[1] += self.velocity[1] * dt
#   self.rect.x = self.position[0]
#   self.rect.y = self.position[1]
# ------------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Step 11
# ---------
#
# The other bit of code we need to add to the update function is the collision
# code. This is a long bit of code that took me a bit of trial and error to work out.
#
# There are two parts, first collision with the walls which looks like this:
#
# collided_this_frame = False
# for wall in walls:
#     if self.rect.colliderect(wall.rect):
#         collided_this_frame = True
#         if not self.collided:
#             self.collided = True
#             self.velocity[1] = self.velocity[1] * -1
#
# Here we check to see if our Ball has collided with a Wall and, if it has change
# the vertical direction of the ball. This works because we know the walls are
# straight lines at the top and bottom of the screen. We also check that we
# haven't somehow collided with two things ( a wall and a bat for example) at
# the same time because if we have it could be possible to get stuck in a silly
# loop constantly flipping the direction of the ball.
#
# The next part is collision with the bats and it looks like this:
#
# for bat in bats:
#     if self.rect.colliderect(bat.rect):
#         collided_this_frame = True
#         if not self.collided:
#             self.collided = True
#             bat_y_centre = bat.position[1] + (bat.length/2)
#             ball_y_centre = self.position[1] + 5
#             relative_intersect_y = bat_y_centre - ball_y_centre # should be in 'bat space' between -50 and +50
#             normalized_relative_intersect_y = relative_intersect_y/(bat.length/2)
#             bounce_angle = normalized_relative_intersect_y * self.max_bat_bounce_angle
#
#             self.velocity[0] = self.velocity[0] * -1
#             self.velocity[1] = self.ball_speed * -math.sin(bounce_angle)
#
# if not collided_this_frame:
#     self.collided = False
#
# It's roughly the same idea except the code we use to calculate the angle we bounce the
# ball off the bat is more complicated. Instead of just reflecting the ball in the X axis
# we also try to alter the bounce angle to be more diagonal the closer the ball collides
# to the top and bottom of the bat.
#
# (Just cut and paste it all into your function!)
#
# Once you are done you can head over to the 'pong' file to finish off adding the ball
# to the game!
# ------------------------------------------------------------------------------
