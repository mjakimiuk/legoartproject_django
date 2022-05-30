import argparse
import itertools
from math import sqrt

from PIL import Image

from lego_tuple import Lego_colours

COLORS = [i.RGB for i in Lego_colours]
parser = argparse.ArgumentParser(description="Change an image to a LEGO ART set")
parser.add_argument(
    "-F",
    "--image_filename",
    type=str,
    metavar="",
    required=True,
    help="enter filename of an image",
)
args = parser.parse_args()


size = (48, 48)
tpl_x = range(48)
tpl_y = range(48)


class Lego_image(object):
    def __init__(self, filename):
        self.filename = filename
        self.im = Image.open(self.filename)
        self.rgb_im = self.im.convert("RGB")
        self.resized_im = self.rgb_im.resize(size)
        self.pix = self.resized_im.load()

    def save_output(self):
        for x, y in itertools.product(tpl_x, tpl_y):
            pixel = closest_color(self.resized_im.getpixel((x, y)))
            self.pix[x, y] = pixel
        self.resized_im.save("output.png")


lego_object = Lego_image(args.image_filename)


def closest_color(rgb):
    """Function returns closest matching colour from a list of given colours"""
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]


def return_cubes():
    """Function returns a list with 9 cubes. Each cubes consits of 16x16 tuples with closest matching colour for each pixel from resized image"""
    CUBE_1 = []
    CUBE_2 = []
    CUBE_3 = []
    CUBE_4 = []
    CUBE_5 = []
    CUBE_6 = []
    CUBE_7 = []
    CUBE_8 = []
    CUBE_9 = []
    for x, y in itertools.product(tpl_x, tpl_y):
        pixel = closest_color(lego_object.resized_im.getpixel((x, y)))
        lego_object.pix[x, y] = pixel
        if (x, y) in itertools.product(range(16), range(16)):
            CUBE_1.append(pixel)
        elif (x, y) in itertools.product(range(16, 32), range(16)):
            CUBE_2.append(pixel)
        elif (x, y) in itertools.product(range(32, 48), range(16)):
            CUBE_3.append(pixel)
        elif (x, y) in itertools.product(range(16), range(16, 32)):
            CUBE_4.append(pixel)
        elif (x, y) in itertools.product(range(16, 32), range(16, 32)):
            CUBE_5.append(pixel)
        elif (x, y) in itertools.product(range(32, 48), range(16, 32)):
            CUBE_6.append(pixel)
        elif (x, y) in itertools.product(range(16), range(32, 48)):
            CUBE_7.append(pixel)
        elif (x, y) in itertools.product(range(16, 32), range(32, 48)):
            CUBE_8.append(pixel)
        elif (x, y) in itertools.product(range(32, 48), range(32, 48)):
            CUBE_9.append(pixel)
    return [CUBE_1, CUBE_2, CUBE_3, CUBE_4, CUBE_5, CUBE_6, CUBE_7, CUBE_8, CUBE_9]


def return_cube_total():
    """Function returns a list with 48x48 tuples with closest matching colour for each pixel from resized image"""
    CUBE_TOTAL = []
    for x, y in itertools.product(tpl_x, tpl_y):
        pixel = closest_color(lego_object.resized_im.getpixel((x, y)))
        lego_object.pix[x, y] = pixel
        CUBE_TOTAL.append(pixel)
    return CUBE_TOTAL