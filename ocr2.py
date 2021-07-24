import PIL
from PIL import ImageDraw
im = PIL.Image.open("sign.png")

import easyocr
reader = easyocr.Reader(['en'])

bounds = reader.readtext('sign.png')

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

draw_boxes(im, bounds)

for i in range(len(bounds)):
    print(bounds[i][1])
