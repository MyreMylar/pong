# A few helpful bits of code I worked out while cloning the game myself
# feel free to poke into here and steal code if you get stuck or want to
# jump ahead
import random
import pygame
import math


# a simple method that creates a random direction vector that
# aims at the sides of the screen - useful for respawning the ball
def make_random_start_vector(self):
    y_random = random.uniform(-0.5, 0.5)
    x_random = 1.0 - abs(y_random)
    if random.randint(0, 1) == 1:
        x_random = x_random * -1.0

    return [x_random, y_random]


# how to create a rectangle in pygame
rectangle = pygame.Rect((top_left_x, top_left_y), (width, height))


# how to change position of a rectangle
new_position = [400.0, 300.0]
rectangle.x = new_position[0]
rectangle.y = new_position[1]


# how to draw a rectangle in pygame
pygame.draw.rect(screen, colour, rectangle)


# how to test two rectangles for collision quickly:
if self.rect.colliderect(wall.rect):
    # change ball direction here


# How to test two rectangles for collision nicely -
# On a collision this bit of code checks whether we are *already* collided
# before running any collision code. Can help clear up any bugs where the ball
# appears to get stuck to a wall or bat.
collided_this_frame = False
for wall in walls:
    if self.rect.colliderect(wall.rect):
        collided_this_frame = True
        if not self.collided:
            self.collided = True

if not collided_this_frame:
    self.collided = False


# render and then draw some text to the screen
some_text_render = font.render("Wow. Such texts. Many colour.", True, pygame.Color("#FF6666"))
screen.blit(some_text_render, some_text_render.get_rect(centerx=400, centery=50))


# bit of code to calculate a more exciting new bounce angle when ball hits a bat
# changes angle of ball based on where it hits on the bat
# with self.maxBatBounceAngle = 5.0*math.pi/12.0 #75 degrees
bat_y_centre = bat.position[1] + (bat.length / 2)
ball_y_centre = self.position[1] + 5
relative_intersect_y = bat_y_centre - ball_y_centre # should be in 'bat space'
normalized_relative_intersection_y = relative_intersect_y / (bat.length / 2)
bounce_angle = normalized_relative_intersection_y * self.max_bat_bounce_angle

self.velocity[0] = self.velocity[0] * -1
self.velocity[1] = self.ball_speed * -math.sin(bounce_angle)
