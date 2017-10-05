import PIL
from PIL import Image
import os

width = 300

for filename in os.listdir('images'):
    image = Image.open('images/%s' % filename)
    width_percent = (width/float(image.size[0]))
    height = int((float(image.size[1]) * float(width_percent)))
    image = image.resize((width, height), PIL.Image.ANTIALIAS)
    image.save('output/%s' % filename.replace(" ", ""))
    