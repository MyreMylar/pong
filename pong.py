import pygame
from pygame.locals import *

from game.wall import Wall
from game.bat import Bat, ControlScheme


# from ball import Ball
# from score import Score

# -----------------------------------------
# FINISHING THE BALL
# -------------------
# Step 1
# --------
#
# import the Ball class we just made from the ball code file.
# You can do this by uncommenting the correct import line above.
#
# Step 2
# --------
# Create the Ball class we just made and
# assign it to a variable called 'ball'.
# Set the start position to the middle of
# the screen in pixels.
#
# Step 3
# --------
#
# Call your new ball's update function
# in roughly the same place we update all the bats.
#
# Step 4
# --------
# Call the ball's render function in roughly
# the same place we call the bat's render functions.
#
# Step 5
# --------
# Also somewhere in the game loop we need to check
# when our ball has gone off either side of the screen
# so we can reset it's position with the ball's reset()
# function.
#
# Create two if statements that check if the ball's
# x axis position is:
#   1. less than zero or;
#   2. Greater than 800
# And if it is, call the ball's reset function.
#
# Step 6
# --------
# Test it out to see if it works, then clean up
# your code to remove the completed step by step comments
# and move on to the 'score' python file to finish up the game.
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# FINISHING THE SCORE
# -------------------
# Step 1
# --------
#
# First import the Score class from the score python file.
# there is a commented out line above that does just that.
#
# Step 2
# --------
# Create our score from the class we just made like this:
#
# score = Score(font)
#
# Add it near where we create all our other classes.
#
# Step 3
# --------
#
# Next we need to call the score's render function. Like so:
#
# score.render(screen)
#
# Add it inside our game loop, but some point after we blit the background.
#
# Step 4
# --------
#
# Finally we need to call our functions to increase the correct player's
# score. If you've already finished adding the Ball class you
# should already have the if statements in the game loop that reset the
# ball when it goes off the screen. This is also the time to increment the player's
# scores.
#
# Inside each if statement write:
#
# score.increase_player_1_score()
#
# or:
#
# score.increase_player_2_score()
#
# Depending on which side we are heading off.
# That's it! Try running the game now and if you've
# done it all right you should see the score and get points
# when the ball goes off the screen on the other side
# from the bat you are controlling.
# ---------------------------------------------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pong')

    background = pygame.Surface(screen.get_size())  # make a background surface
    background = background.convert(screen)
    background.fill((0, 0, 0))

    font = pygame.font.Font(None, 50)  # load the default font at size 30 for text rendering

    walls = [Wall((10, 10), (790, 20)),
             Wall((10, 580), (790, 590))]

    bats = []

    control_scheme_1 = ControlScheme()
    control_scheme_1.up = K_w
    control_scheme_1.down = K_s

    control_scheme_2 = ControlScheme()
    control_scheme_2.up = K_UP
    control_scheme_2.down = K_DOWN

    bats.append(Bat((10, 200), control_scheme_1))
    bats.append(Bat((780, 200), control_scheme_2))

    clock = pygame.time.Clock()

    running = True
    while running:

        frame_time = clock.tick(60)
        time_delta = frame_time / 1000.0

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            for bat in bats:
                bat.process_event(event)

        screen.blit(background, (0, 0))  # draw the background surface to our screen

        for wall in walls:
            wall.render(screen)

        for bat in bats:
            bat.update(time_delta)
            bat.render(screen)

        pygame.display.flip()  # flip all our drawn stuff onto the screen

    pygame.quit()  # exited game loop so quit pygame


if __name__ == '__main__':
    main()
