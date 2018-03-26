import numpy
from PIL import Image


WIDTH, HEIGHT = 10, 20

imarray = numpy.random.rand(HEIGHT, WIDTH, 3) * 255
im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
im.save('image.png')
