from PIL import Image, ImageFilter

before = Image.open("images/yard2.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out2.bmp")