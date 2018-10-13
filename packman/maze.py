import pygame
from imagerect import ImageRect


class Maze:
    RED = (255, 0, 0)
    BRICK_SIZE = 3

    def __init__(self, screen, mazefile, brickfile, orangeportalfile, blueportalfile, shieldfile, pointfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        self.shields = []
        self.portals = []
        self.points = []

        sz = Maze.BRICK_SIZE
        self.brick = ImageRect(screen, brickfile, sz, sz)
        self.shield = ImageRect(screen, shieldfile, sz, sz)
        self.blueportal = ImageRect(screen, blueportalfile, 5 * sz, 15 * sz)
        self.orangeportal = ImageRect(screen, orangeportalfile, 15 * sz, 5 * sz)
        self.point = ImageRect(screen, pointfile, int(2*sz), int(2*sz))

        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        r = self.brick.rect
        rshield = self.shield.rect
        rblue = self.blueportal.rect
        rorange = self.orangeportal.rect
        rpoint = self.point.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 's':
                    self.shields.append(pygame.Rect(ncol * dx, nrow * dy, rshield.width, rshield.height))
                elif col == 'o':
                    self.orangeportal.rect = pygame.Rect(dx + 20, (nrow - 4) * dy, rorange.width, rorange.height)
                elif col == 'b':
                    self.blueportal.rect = pygame.Rect((ncol - 3) * dx, (nrow - 6) * dy, rblue.width, rblue.height)
                elif col == 'p':
                    self.points.append(pygame.Rect(ncol * dx, nrow * dy, rpoint.width, rpoint.height))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.shields:
            self.screen.blit(self.shield.image, rect)
        self.orangeportal.blit()
        self.blueportal.blit()
        for rect in self.points:
            self.screen.blit(self.point.image, rect)
