import random
import time

from functions import draw_effects_functions


def make_gray(image, file_name, draw, width, height, pix):
    t1 = time.time()

    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            s = (r + g + b) // 3
            draw.point((i, j), (s, s, s))

    path_to_save = "images/{0}_gray.jpg".format(file_name)

    image.save(path_to_save)
    t2 = time.time()

    t = round(t2 - t1, 2)

    print("Время работы программы: {0} с".format(t))


def make_random(image, file_name, draw, width, height):
    t1 = time.time()

    for i in range(width):
        for j in range(height):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            draw.point((i, j), (r, g, b))

    path_to_save = "images/{0}_random.jpg".format(file_name)

    image.save(path_to_save)
    t2 = time.time()

    t = round(t2 - t1, 2)

    print("Время работы программы: {0} с".format(t))


def make_gradient(image, file_name, draw, width, height, pix):
    t1 = time.time()

    for i in range(width):
        for j in range(height):
            fact = 300

            r = random.randint(-fact, fact)
            g = random.randint(-fact, fact)
            b_color = random.randint(-fact, fact)

            a = pix[i, j][0] + r
            b = pix[i, j][1] + g
            c = pix[i, j][2] + b_color

            if a < 0:
                a = 0
            elif a > 255:
                a = 255

            if b < 0:
                b = 0
            elif b > 255:
                b = 255

            if c < 0:
                c = 0
            elif c > 255:
                c = 255

            draw.point([i, j], (a, b, c))

    path_to_save = "images/{0}_gradient.jpg".format(file_name)

    image.save(path_to_save)
    t2 = time.time()

    t = round(t2 - t1, 2)

    print("Время работы программы: {0} с".format(t))


def make_black1(image, file_name, draw, width, height, pix):
    t1 = time.time()

    fact = int(input("Фактор цвета: "))

    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            s = a + b + c

            if s > (255 + fact) // 6:
                a, b, c = 255, 255, 255

            else:
                a, b, c = 0, 0, 0

            draw.point((i, j), (a, b, c))

    path_to_save = "images/{0}_black1.jpg".format(file_name)

    image.save(path_to_save)
    t2 = time.time()

    t = round(t2 - t1, 2)

    print("Время работы программы: {0} с".format(t))


def make_black2(image, file_name, draw, width, height, pix):
    t1 = time.time()

    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))

    path_to_save = "images/{0}_black2.jpg".format(file_name)

    image.save(path_to_save)
    t2 = time.time()

    t = round(t2 - t1, 2)

    print("Время работы программы: {0} с".format(t))


def make_weird(image, file_name, draw, width, height, pix):
    l = int(input("Режим матрицы: "))

    t1 = time.time()

    matrix_type_dict = draw_effects_functions.get_matrix_dict()

    for i in range(1, width - 1):
        for j in range(1, height - 1):
            r = 0
            g = 0
            b = 0
            current_matrix = [[0] * 3 for n in range(3)]

            for k in range(3):
                for m in range(0, 3):
                    for m2 in range(0, 3):
                        current_matrix[m][m2] = pix[i - 1 + m, j - 1 + m2][k]
                if k == 0:
                    r = draw_effects_functions.change_color_effects(l, current_matrix, matrix_type_dict)
                elif k == 1:
                    g = draw_effects_functions.change_color_effects(l, current_matrix, matrix_type_dict)
                elif k == 2:
                    b = draw_effects_functions.change_color_effects(l, current_matrix, matrix_type_dict)

            draw.point((i, j), (r, g, b))

    path_to_save = "images/{0}_weird.jpg".format(file_name)

    image.save(path_to_save)
    t2 = time.time()

    t = round(t2 - t1, 2)

    print("Время работы программы: {0} с".format(t))


def change_picture(mode, image, file_name, draw, width, height, pix):
    if mode == 0:
        make_gray(image, file_name, draw, width, height, pix)
    elif mode == 1:
        make_random(image, file_name, draw, width, height)
    elif mode == 2:
        make_gradient(image, file_name, draw, width, height, pix)
    elif mode == 3:
        make_black1(image, file_name, draw, width, height, pix)
    elif mode == 4:
        make_black2(image, file_name, draw, width, height, pix)
    elif mode == 5:
        make_weird(image, file_name, draw, width, height, pix)
