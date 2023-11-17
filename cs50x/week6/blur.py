from PIL import Image, ImageFilter

before = Image.open("images/yard2.bmp")
after = before.filter(ImageFilter.BoxBlur(1))
after.save("out.bmp")