from PIL import Image
img = Image.open('D:\\nini.jpg')
print("初始尺寸",img.size)
img.thumbnail((400,590))
print("默认缩放NEARESET", img.size)