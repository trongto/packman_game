import pygame
import os
from pygame import gfxdraw
from eventloop import EventLoop
from maze import Maze
from expandfile import ExpandFile
#import draw_arc as da


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((420, 480))
        pygame.display.set_caption("Pacman Portal")

        self.radius = 1
        self.start = 1
        self.end = 10
        self.begin = pygame.time.get_ticks()
        self.wait = 800

        self.expandfile = ExpandFile('images/pacmanportalmaze.txt', expandBy=3)
        self.maze = Maze(self.screen, mazefile='images/pacmanportalmaze_expanded.txt',
                         brickfile='square', orangeportalfile='portal_orange', blueportalfile='portal_blue', shieldfile='shield', pointfile='powerpill')

    def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'




    def open_portal(self, x, y, color):
        for r in range(self.start, self.end):
            pygame.gfxdraw.circle(self.screen, x, y, r, color)
        now = pygame.time.get_ticks()
        if (now < self.begin + self.wait): self.inc = 1
        elif (now < self.begin + 4 * self.wait): self.inc = 0
        else: self.inc = -1
        self.start += self.inc
        self.start = max(1, self.start)
        self.end += self.inc

    def play(self):
        eloop = EventLoop(finished=False)
        while not eloop.finished:
            eloop.check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        self.open_portal(100, 100, (240, 100, 20))
        pygame.display.flip()


game = Game()
game.play()
