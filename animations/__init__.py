## Load the python animations
## Dynamically import all the python files we can find.
import os
import sys

import dcfurs
import ujson
from animations.cylon import cylon
from animations.dgol import dgol
from animations.dogjump import dogjump
from animations.fur import fur
from animations.life import life
from animations.maze import maze
from animations.pong import pong
from animations.rain import rain
from animations.scroll import scroll
from animations.worm import worm


## Template class for JSON-encoded animations
class _jsonanim:
    def __init__(self):
        fh = open(self.path, "r")
        self.framenum = 0
        self.js = ujson.load(fh)
        self.intensity = bytearray(
            [0, 2, 3, 4, 6, 9, 12, 17, 24, 34, 47, 66, 92, 130, 182, 255]
        )
        fh.close()
        self.draw()

    def drawframe(self, frame):
        self.interval = int(frame["interval"])
        x = 0
        y = 0
        for ch in frame["frame"]:
            if ch == ":":
                x = 0
                y = y + 1
            else:
                dcfurs.set_pixel(x, y, self.intensity[int(ch, 16)])
                x = x + 1

    def draw(self):
        self.drawframe(self.js[self.framenum])
        self.framenum = (self.framenum + 1) % len(self.js)


## Dynamically generate animation classes from JSON files.
files = os.listdir("/flash/animations")
for filename in files:
    if filename[1] != "_" and filename[-5:] == ".json":
        classname = filename[:-5]
        try:
            globals()[classname] = type(
                classname, (_jsonanim,), {"path", "/flash/animations/" + filename}
            )
        except TypeError as e:
            print(classname, filename, e)


## Return a list of all animation classes
def all():
    results = []
    module = sys.modules["animations"]
    for name in dir(module):
        x = getattr(module, name)
        if isinstance(x, type) and name[1] != "_":
            results.append(x)
    return sorted(results, key=lambda m: m.__name__.lower())
