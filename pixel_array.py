import pygame as py
from itertools import flatten

class PixelArray(object):
  def __init__(self, width, height, multiplier, max_pixel):
    self.width = width * multiplier
    self.height = height * multiplier
    self.pixels = [0] * width * height
    self.max_pixel = max_pixel
    self.multiplier = multiplier

  def __str__(self):
    ascii = " .:+&"
    ppixels = [ascii[pixel] for pixel in self.pixels]
    return "|" + "".join(ppixels) + "|"

  def _inc(self, ind):
    # This won't work if there are more than 1000 pixels because recursion
    # refactor to scale.
    if self.pixels[ind] == self.max_pixel:
      self.pixels[ind] = 0
      self._inc(ind + 1)
    else:
      self.pixels[ind] += 1

  def inc(self):
    self._inc(0)

  def _to_color(self, pix):
    val = pix * (255 / self.max_pixel)
    return (val, val, val)

  def colors(self):
    return [self._to_color(pix) for pix in self.n_times()]

  def n_times(self):
    return flatten([[pix] * self.multiplier for pix in self.pixels])

  def square_colors(self):
    colors = self.colors()
    return [colors[i:i+self.width] for i in xrange(0, len(colors), self.width)]

  def paint(self, surface):
    pix_array = py.PixelArray(surface)
    square = self.square_colors()
    for x in range(self.width):
      for y in range(self.height):
        pix_array[x][y] = square[x][y]
    del pix_array

def test_array():
    array = PixelArray(3, 3, 3)
    for i in range(150):
      array.inc()
      print array.square_colors()

if __name__ == '__main__':
  test_array()
