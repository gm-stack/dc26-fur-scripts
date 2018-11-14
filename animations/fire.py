"""Southern Lights"""
import dcfurs
import settings
import math
import random

gamma_table = [
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
    1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
    2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
    5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
    10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
    17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
    25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
    37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
    51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
    69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
    90, 92, 93, 95, 96, 98, 99,101,102,104,105,107,109,110,112,114,
    115,117,119,120,122,124,126,127,129,131,133,135,137,138,140,142,
    144,146,148,150,152,154,156,158,160,162,164,167,169,171,173,175,
    177,180,182,184,186,189,191,193,196,198,200,203,205,208,210,213,
    215,218,220,223,225,228,231,233,236,239,241,244,247,249,252,255
]


class fire:
    def __init__(self):
        self.interval = 50
        self.decay = 5

        self.fire_height = dcfurs.nrows + 1
        self.fire = [bytearray(dcfurs.ncols) for _ in range(self.fire_height)]

        self.screen = [bytearray(dcfurs.ncols) for _ in range(dcfurs.nrows)]


    def draw(self):

        # randomise bottom row
        for x in range(dcfurs.ncols):
            self.fire[self.fire_height-1][x] = random.randint(0,230)

        # draw all rows down to second to bottom row
        for y in range(0,self.fire_height-2):
            # special case left column
            self.fire[y][0] = (
                self.fire[y+1][0] +
                self.fire[y+2][0] +
                self.fire[y+1][1]
            ) // self.decay
            
            # middle set
            for x in range(1,dcfurs.ncols-1):
                self.fire[y][x] = (
                    self.fire[y+1][x-1] +
                    self.fire[y+1][x]   +
                    self.fire[y+1][x+1] +
                    self.fire[y+2][x]
                ) // self.decay

            # special case right
            self.fire[y][dcfurs.ncols-1] = (
                self.fire[y+1][dcfurs.ncols-1] +
                self.fire[y+2][dcfurs.ncols-1] +
                self.fire[y+1][dcfurs.ncols-2]
            ) // self.decay

        # write last row (considers row below only)
        y = self.fire_height-2
        
        # special case leftmost pixel
        self.fire[y][0] = (
            self.fire[y+1][0] +
            self.fire[y+1][1]
        ) // self.decay

        # second to bottom row (above random row)
        for x in range(1, dcfurs.ncols-1):
            self.fire[y][x] = (
                self.fire[y+1][x-1] +
                self.fire[y+1][x]   +
                self.fire[y+1][x+1]
            ) // self.decay

        # special case rightmost pixel
        self.fire[y][dcfurs.ncols-1] = (
            self.fire[y+1][dcfurs.ncols-2] +
            self.fire[y+1][dcfurs.ncols-1]
        ) // self.decay


        # copy gamma-shifted version
        # minus bottom random row into screen buffer
        for x in range(dcfurs.ncols):
            for y in range(dcfurs.nrows):
                self.screen[y][x] = gamma_table[self.fire[y][x]]

        dcfurs.set_frame(self.screen)