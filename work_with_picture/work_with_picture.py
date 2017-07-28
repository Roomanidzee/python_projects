from PIL import Image, ImageDraw
import os.path

from functions import picture_functions


file_path = input("Введите путь до преобразуемой картинки, пожалуйста: ")
print()

mode = int(input("Режим преобразования: "))
print()

image = Image.open(os.path.abspath(file_path))
(dir_name, file_name) = os.path.split(file_path)
(file_base_name, file_extension) = os.path.splitext(file_name)
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

mode_switch = picture_functions.get_switch()

picture_functions.change_picture(mode, mode_switch, image, file_base_name, draw, width, height, pix)
