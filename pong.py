import pygame
from pygame.locals import *

from game.wall import Wall
from game.bat import Bat, ControlScheme
from game.ball import Ball
from game.score import Score


class PongGame:
    def __init__(self, size):
        self.background = pygame.Surface(size)  # make a background surface
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        font = pygame.font.Font(None, 40)

        self.score = Score(font)

        self.walls = [Wall((10, 10), (790, 20)),
                      Wall((10, 580), (790, 590))]

        self.bats = []

        control_scheme_1 = ControlScheme()
        control_scheme_1.up = K_w
        control_scheme_1.down = K_s

        control_scheme_2 = ControlScheme()
        control_scheme_2.up = K_UP
        control_scheme_2.down = K_DOWN

        self.bats.append(Bat((10, 200), control_scheme_1))
        self.bats.append(Bat((780, 200), control_scheme_2))

        self.ball = Ball((400, 300))

    def process_event(self, event):
        for bat in self.bats:
            bat.process_event(event)

    def update(self, time_delta):
        for bat in self.bats:
            bat.update(time_delta)

        self.ball.update(time_delta, self.bats, self.walls)

        if self.ball.position[0] < 0:
            self.ball.reset()
            self.score.increase_player_2_score()
        elif self.ball.position[0] > 800:
            self.ball.reset()
            self.score.increase_player_1_score()

    def draw(self, surface):
        surface.blit(self.background, (0, 0))

        for wall in self.walls:
            wall.render(surface)

        for bat in self.bats:
            bat.render(surface)

        self.ball.render(surface)
        self.score.render(surface)


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pong')

    pong = PongGame((800, 600))

    clock = pygame.time.Clock()
    running = True
    while running:
        frame_time = clock.tick(60)
        time_delta = frame_time / 1000.0

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            pong.process_event(event)

        pong.update(time_delta)

        pong.draw(screen)

        pygame.display.flip()  # flip all our drawn stuff onto the screen
