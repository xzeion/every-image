

class PixelArray(object):
  def __init__(self, width, height, max_pixel):
    self.width = width
    self.height = height
    self.pixels = [0] * width * height
    self.max_pixel = max_pixel

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




def test_array():
    array = PixelArray(3, 3, 3)
    for i in range(150):
      array.inc()
      print array

if __name__ == '__main__':
  test_array()
