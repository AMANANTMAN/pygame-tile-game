import pygame as pg
from settings import * 

def collide_hit_rect(one,two):
  return one.hit_rect.colliderect(two.rect)

class Map:
  def __init__(self, filemane):
    self.data = []
    with open(filemane, 'rt') as f:
      for line in f:
        self.data.append(line.strip())

    self.tilewidth = len(self.data[0])
    self.tileheight = len(self.data)
    self.width = self.tilewidth * TILESIZE
    self.height = self.tileheight * TILESIZE

class Camera:
  def __init__(self, width, height):
    self.camera = pg.Rect(0,0,width,height)
    self.width = width
    self.height = height

  def apply(self,entity):
    return entity.rect.move(self.camera.topleft)

  def update(self, target):
    x = -target.rect.centerx + int(WIDTH/2)
    y = -target.rect.centery + int(HEIGHT/2)

    x = min(0,x)
    y = min(0,y)
    x= max(-(self.width - WIDTH), x)
    y = max(-(self.height - HEIGHT), y)
    self.camera = pg.Rect(x,y,self.width,self.height)
