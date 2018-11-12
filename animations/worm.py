## Wormy animation
import random

import badge
import dcfurs


def shuffle(seq):
    l = len(seq)
    for i in range(l):
        j = random.randint(0, l - 1)
        seq[i], seq[j] = seq[j], seq[i]


class worm:
    interval = 50
    x = 1
    y = 1
    moves = frozenset([(0, 1), (1, 0), (0, -1), (-1, 0)])

    def __init__(self):
        self.fbuf = [
            bytearray(18),
            bytearray(18),
            bytearray(18),
            bytearray(18),
            bytearray(18),
            bytearray(18),
            bytearray(18),
        ]
        self.last_move = (1, 0)
        self.counter = 0

    def updatePosition(self):
        self.dimPixels()
        new_x = 0
        new_y = 0
        run_once = False
        # Let's basically just move randomly
        moves = list(self.moves) + [self.last_move]
        shuffle(moves)
        for new_x, new_y in moves:
            x = (self.x + dcfurs.ncols + new_x) % dcfurs.ncols
            y = (self.y + dcfurs.nrows + new_y) % dcfurs.nrows
            if self.fbuf[y][x] == 0 and dcfurs.has_pixel(x, y):
                self.last_move = (new_x, new_y)
                self.x = x
                self.y = y
                self.setPixel(self.x, self.y, 255)
                return
        # No valid moves
        x, y = random.randint(0, dcfurs.ncols), random.randint(0, dcfurs.nrows)
        while self.fbuf[y][x] != 0 and not dcfurs.has_pixel(x, y):
            x, y = random.randint(0, dcfurs.ncols), random.randint(0, dcfurs.nrows)
        self.last_move = None
        self.x = x
        self.y = y
        self.setPixel(self.x, self.y, 255)

    def dimPixels(self):
        for y in range(0, len(self.fbuf)):
            row = self.fbuf[y]
            for x in range(0, len(row)):
                if self.fbuf[y][x] > 4:
                    self.fbuf[y][x] = self.fbuf[y][x] // 2
                else:
                    self.fbuf[y][x] = 0

    def setPixel(self, x, y, value):
        self.fbuf[y][x] = value

    def draw(self):
        self.updatePosition()
        dcfurs.set_frame(self.fbuf)
