from PIL import Image, ImageDraw

from functions import picture_functions


file_path = input("Введите путь до преобразуемой картинки, пожалуйста: ")
print()

mode = int(input("Режим преобразования: "))
print()

image = Image.open(file_path)
file_name = file_path.replace(".jpg", "")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

picture_functions.change_picture(mode, image, file_name, draw, width, height, pix)
