from fpdf import FPDF
from PIL import Image


class PDF(FPDF):
    # def __init__ (self, orientation='portrait', unit='mm', format='A4', font_cache_dir='DEPRECATED'):
    # self.unit = unit
    # "Accepts a pair (width, height) in the unit specified to FPDF constructor"
    def set_dimensions(self, width_pt, height_pt):
        self._width_pt, self._height_pt = 210, 297

    # The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 22)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)


# Find PNG size and position of height
im = Image.open("shirtificate.png")
w, h = im.size
w = (w * 25.4) / 72
h = (h * 25.4) / 72
h_pos = (297 - h) / 2
w_pos = (210 - w) / 2

# Instantiation of inherited class
pdf = PDF()
pdf.add_page(orientation="P", format="A4")

# Add in image and center it horizontally
pdf.image("shirtificate.png", w=pdf.epw, y=h_pos)

# Set font, color, and center
pdf.set_font("helvetica", "B", 18)
pdf.set_text_color(255, 255, 255)
pdf.cell(60)

# Ask for name input and print name in white text
name = input("Name: ")
pdf.write(150, f"{name} took CS50")

# Produce PDF document
pdf.output("shirtificate.pdf")
