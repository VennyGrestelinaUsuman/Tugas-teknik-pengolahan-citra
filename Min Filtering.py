from PIL import Image, ImageFilter
im1 = Image.open(r"C:\Users\Acer\PycharmProjects\pythonProject\lena.jpg")
im2 = im1.filter (ImageFilter.MinFilter (size=3))
im2.show()