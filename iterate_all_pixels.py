
def test_print_array(width, height, pixels):
  ppixels = [ASCII_PIXELS[pixel] for pixel in pixels]
  print "|" + "".join(ppixels) + "|"

def increment_array(pixels, max_pixel, ind):
  # This won't work if there are more than 1000 pixels because recursion
  # refactor to scale.
  if pixels[ind] == max_pixel:
    pixels[ind] = 0
    increment_array(pixels, max_pixel, ind + 1)
  else:
    pixels[ind] += 1
