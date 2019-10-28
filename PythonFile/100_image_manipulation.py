from PIL import Image

image = Image.open('./testjpg.jpg')
# rect = 80, 20, 1610, 1660
# image.crop(rect).show()


size = 640, 640
image.thumbnail(size)
image.show()