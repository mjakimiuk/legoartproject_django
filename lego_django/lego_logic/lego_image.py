import itertools
from math import sqrt
import os

from fpdf import FPDF
from fpdf.enums import XPos, YPos
from PIL import Image

from .lego_tuple import Lego_colours

COLORS = [i.RGB for i in Lego_colours]


size = (48, 48)
tpl_x = range(48)
tpl_y = range(48)


def closest_color(rgb):
    """Function returns closest matching colour from a list of given colours"""
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]


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

    def return_cubes(self):
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
            pixel = closest_color(self.resized_im.getpixel((x, y)))
            self.pix[x, y] = pixel
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

    def return_cube_total(self):
        """Function returns a list with 48x48 tuples with closest matching colour for each pixel from resized image"""
        CUBE_TOTAL = []
        for x, y in itertools.product(tpl_x, tpl_y):
            pixel = closest_color(self.resized_im.getpixel((x, y)))
            self.pix[x, y] = pixel
            CUBE_TOTAL.append(pixel)
        return CUBE_TOTAL


class PDF(FPDF):
    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(
            0,
            10,
            f"Page {self.page_no()}/{{nb}}",
            new_x=XPos.RIGHT,
            new_y=YPos.NEXT,
            align="C",
            fill="False",
        )


# pdf = PDF()

line_grid_start_x = 66.5 + 6
line_grid_start_y = 66.5 + 6
line_endpoint = 208
grid_number = [str(i) for i in range(1, 4)]
grid_letter = list("ABC")


# class LEGO_plate(object):
#     """Class generates a drawing of round LEGO part with correct colour"""

#     def __init__(self, cord_x, cord_y, colour, text):
#         self.cord_x = cord_x
#         self.cord_y = cord_y
#         self.colour = colour
#         self.text = text

#     def print_it(self):
#         R, G, B = self.colour
#         n = 2
#         pdf.set_fill_color(r=R, g=G, b=B)
#         pdf.ellipse(
#             y=9 * n + self.cord_x,
#             x=8.5 * n + self.cord_y,
#             w=3.5 * n,
#             h=2 * n,
#             style="FD",
#         )
#         pdf.ellipse(
#             y=8.5 * n + self.cord_x,
#             x=8.5 * n + self.cord_y,
#             w=3.5 * n,
#             h=2 * n,
#             style="FD",
#         )
#         pdf.ellipse(
#             y=8.30 * n + self.cord_x,
#             x=9.25 * n + self.cord_y,
#             w=2 * n,
#             h=1.5 * n,
#             style="FD",
#         )
#         pdf.ellipse(
#             y=8.2 * n + self.cord_x,
#             x=9.25 * n + self.cord_y,
#             w=2 * n,
#             h=1.5 * n,
#             style="FD",
#         )
#         pdf.set_text_color(r=0, g=0, b=0)
#         pdf.set_font("helvetica", "B", 12)
#         pdf.text(14 * n + self.cord_y, 10.2 * n + self.cord_x, self.text)


def main_page(lego_object, pdf):
    """Function generates PDF page with 48x48 pixelated image and coordinates grid"""
    pdf.add_page()
    pdf.line(
        line_grid_start_x - 64, 2, line_grid_start_x - 64, line_endpoint
    )  # vertical line
    pdf.line(line_grid_start_x, 2, line_grid_start_x, line_endpoint)  # vertical line
    pdf.line(
        line_grid_start_x + 64, 2, line_grid_start_x + 64, line_endpoint
    )  # vertical line
    pdf.line(
        line_grid_start_x + 64 * 2, 2, line_grid_start_x + 64 * 2, line_endpoint
    )  # vertical line
    pdf.line(
        2, line_grid_start_y - 64, line_endpoint, line_grid_start_y - 64
    )  # horizontal line
    pdf.line(2, line_grid_start_y, line_endpoint, line_grid_start_y)  # horizontal line
    pdf.line(
        2, line_grid_start_y + 64, line_endpoint, line_grid_start_y + 64
    )  # horizontal line
    pdf.line(
        2, line_grid_start_y + 64 * 2, line_endpoint, line_grid_start_y + 64 * 2
    )  # horizontal line
    for n, (i, text) in itertools.product(range(2), enumerate(grid_letter)):
        pdf.set_font("helvetica", "B", 20)
        pdf.text(40 + i * 64, 7 + n * 200, text)  # horizontal grid letters
    for n, (i, text) in itertools.product(range(2), enumerate(grid_number)):
        pdf.set_font("helvetica", "B", 20)
        pdf.text(2 + n * 200, 40 + i * 64, text)  # vertical grid numbers
    for row in range(48):
        line = lego_object.return_cube_total()[0 + row * 48 : 48 + row * 48]
        for q, (n, l) in itertools.product(Lego_colours, enumerate(line)):
            if q.RGB == l:
                if q.RGB == (0, 0, 0):
                    pdf.set_text_color(r=255, g=255, b=255)
                else:
                    pdf.set_text_color(r=0, g=0, b=0)
                R, G, B = q.RGB
                pdf.set_fill_color(r=R, g=G, b=B)
                pdf.ellipse(y=9 + n * 4, x=9 + row * 4, w=3, h=3, style="FD")
                pdf.set_font("helvetica", "B", 6)
                if q.ID < 10:
                    pdf.text(9.9 + row * 4, 11.2 + n * 4, f"{q.ID}")
                else:
                    pdf.text(9.2 + row * 4, 11.2 + n * 4, f"{q.ID}")
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_fill_color(r=255, g=255, b=255)


# def part_description(pdf):
#     """Function generates PDF page with part list description"""
#     pdf.add_page()
#     for i, part in enumerate(Lego_colours):
#         lego_part = LEGO_plate(
#             140 + 8 * i,
#             0,
#             part.RGB,
#             f"{part.ID} - Part number: {part.LEGO_part_number}",
#         )  # 'i' is number of parts in Lego_colours list. '140 + 8*i' are coordinates for each part to be printed on page
#         lego_part.print_it()
#     pdf.set_text_color(r=0, g=0, b=0)
#     pdf.set_fill_color(r=255, g=255, b=255)


def pages_of_manual(lego_object, pdf):
    """Function generates a PDF with 9 pages of 16x16 cubes showing each part of pixelated image"""
    CUBES = lego_object.return_cubes()
    for cube_number, cube in enumerate(CUBES):
        # pdf.set_line_width(1)
        text = "".join(
            list(itertools.product(grid_letter, grid_number))[cube_number]
        )  # cube cordinates - for example A1, B3, C1
        pdf.add_page()
        pdf.set_text_color(r=0, g=0, b=0)
        pdf.set_font("helvetica", "B", 30)
        pdf.text(100, 9, text)

        for row in range(16):
            line = cube[0 + row * 16 : 16 + row * 16]
            for q, (n, l) in itertools.product(Lego_colours, enumerate(line)):
                if q.RGB == l:
                    if q.RGB == (0, 0, 0):
                        pdf.set_text_color(r=255, g=255, b=255)
                    else:
                        pdf.set_text_color(r=0, g=0, b=0)
                    R, G, B = q.RGB
                    pdf.set_fill_color(r=R, g=G, b=B)
                    pdf.ellipse(y=10 + n * 12, x=10 + row * 12, w=10, h=10, style="FD")
                    pdf.set_font("helvetica", "B", 18)
                    if q.ID < 10:
                        pdf.text(13.5 + row * 12, 17.5 + n * 12, f"{q.ID}")
                    else:
                        pdf.text(11 + row * 12, 17 + n * 12, f"{q.ID}")
        pdf.set_text_color(r=0, g=0, b=0)
        pdf.set_fill_color(r=255, g=255, b=255)


def save_output(pdf, filename=None):
    if filename is None:
        pdf.output("media/art/pdf/output.pdf")
    else:
        pdf.output(filename)
