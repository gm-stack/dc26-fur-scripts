"""Moving Diaganols"""

import dcfurs
import random

class diags:
  interval = 150
  ticks_per_sec = int(1000 / interval)
  frame = 0
  frames = [0, 0, 0, 0, 0]
  frames[0] = [[0,1,125],[0,3],[0,6,125],[0,8],[0,9],[0,11,125],[0,14],[0,16,125],[1,0,125],[1,2],[1,5,125],[1,7],[1,10],[1,12,125],[1,15],[1,17,125],[2,1],[2,4,125],[2,6],[2,11],[2,13,125],[2,16],[3,0],[3,3,125],[3,5],[3,8,125],[3,9,125],[3,12],[3,14,125],[3,17],[4,2,125],[4,4],[4,7,125],[4,10,125],[4,13],[4,15,125],[5,1,125],[5,3],[5,6,125],[5,11,125],[5,14],[5,16,125],[6,2],[6,5,125],[6,12,125],[6,15]]
  frames[1] = [[0,2,125],[0,4],[0,7,125],[0,10,125],[0,13],[0,15,125],[1,1,125],[1,3],[1,6,125],[1,8],[1,9],[1,11,125],[1,14],[1,16,125],[2,0,125],[2,2],[2,5,125],[2,7],[2,10],[2,12,125],[2,15],[2,17,125],[3,1],[3,4,125],[3,6],[3,11],[3,13,125],[3,16],[4,0],[4,3,125],[4,5],[4,8,125],[4,9,125],[4,12],[4,14,125],[4,17],[5,2,125],[5,4],[5,13],[5,15,125],[6,1,125],[6,3],[6,14],[6,16,125]]
  frames[2] = [[0,3,125],[0,5],[0,8,125],[0,9,125],[0,12],[0,14,125],[1,2,125],[1,4],[1,7,125],[1,10,125],[1,13],[1,15,125],[2,1,125],[2,3],[2,6,125],[2,8],[2,9],[2,11,125],[2,14],[2,16,125],[3,0,125],[3,2],[3,5,125],[3,7],[3,10],[3,12,125],[3,15],[3,17,125],[4,1],[4,4,125],[4,6],[4,11],[4,13,125],[4,16],[5,0],[5,3,125],[5,5],[5,12],[5,14,125],[5,17],[6,2,125],[6,4],[6,13],[6,15,125]]
  frames[3] = [[0,1],[0,4,125],[0,6],[0,11],[0,13,125],[0,16],[1,0],[1,3,125],[1,5],[1,8,125],[1,9,125],[1,12],[1,14,125],[1,17],[2,2,125],[2,4],[2,7,125],[2,10,125],[2,13],[2,15,125],[3,1,125],[3,3],[3,6,125],[3,8],[3,9],[3,11,125],[3,14],[3,16,125],[4,0,125],[4,2],[4,5,125],[4,7],[4,10],[4,12,125],[4,15],[4,17,125],[5,1],[5,4,125],[5,6],[5,11],[5,13,125],[5,16],[6,3,125],[6,5],[6,12],[6,14,125]]
  frames[4] = [[0,2],[0,5,125],[0,7],[0,10],[0,13,125],[0,15],[1,1],[1,4,125],[1,6],[1,11],[1,14,125],[1,16],[2,0],[2,3,125],[2,5],[2,8,125],[2,9,125],[2,12],[2,15,125],[2,17],[3,2,125],[3,4],[3,7,125],[3,10,125],[3,13],[3,16,125],[4,1,125],[4,3],[4,6,125],[4,8],[4,9],[4,11,125],[4,14],[4,17,125],[5,0,125],[5,2],[5,5,125],[5,12,125],[5,15],[6,1],[6,4,125],[6,13,125],[6,16]]

  def __init__(self):
    self.reset_fbuf()

  def reset_fbuf(self):
    self.fbuf = [bytearray(18),bytearray(18),bytearray(18),bytearray(18),bytearray(18),bytearray(18),bytearray(18)]

  def face(self):
    faceBuf = self.frames[self.frame]
    self.frame += 1
    if self.frame > 4:
      self.frame = 0
    self.reset_fbuf()
    for xy in range(0,len(faceBuf)):
      self.onPixel(faceBuf[xy][0],faceBuf[xy][1])

  def onPixel(self,y,x):
    self.fbuf[y][x] = 255

  def redrawDisplay(self):
    for y in range(0,len(self.fbuf)):
      row = self.fbuf[y]
      for x in range(0, len(row)):
        dcfurs.set_pixel(x, y, row[x])

  def draw(self):
    self.face()
    self.redrawDisplay()