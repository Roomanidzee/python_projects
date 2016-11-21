
from PIL import Image, ImageDraw
import random
import time

# This program changing the color effects at a picture
def mumator(m, a):
    res = 0
    if(m == 0):
        matr = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        for i in range(3):
            for j in range(3):
                res += a[i][j] * matr[i][j]
        res /= 9
    if(m == 1):
        matr = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
        for i in range(3):
            for j in range(3):
                res += a[i][j] * matr[i][j]
        res /= 9
    if(m == 2):
        matr = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
        for i in range(3):
            for j in range(3):
                res += a[i][j] * matr[i][j]
        res /= 9
    if (m == 3):
        matr = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
        for i in range(3):
            for j in range(3):
                res += a[i][j] * matr[i][j]
        res /= 9
    if (m == 4):
        matr = [[1, 1, 1], [1, -2, 1], [-1, -1, -1]]
        for i in range(3):
            for j in range(3):
                res += a[i][j] * matr[i][j]
        res /= 9

    return int(res)


mode = int(input("Режим: "))
image = Image.open("Koala1.jpg")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

if (mode == 0):
    t1 = time.time()
    for i in range(width):
        for j in range(height):
            r = pix[i, j][0]
            g = pix[i, j][1]
            b = pix[i, j][2]
            s = (r + g + b)//3
            draw.point((i, j), (s, s, s))
    image.save("gray1.jpg")
    t2 = time.time()
    t = round(t2 - t1, 2)
    print("Время работы программы : \%s " % t + "с")
if(mode == 1):
    t1 = time.time()
    for i in range(width):
        for j in range(height):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            draw.point((i, j), (r, g, b))
    image.save("random.jpg")
    t2 = time.time()
    t = round(t2 - t1, 2)
    print("Время работы программы : \%s " % t + "с")
if(mode == 2):
    t1 = time.time()
    for i in range(width):
        for j in range(height):
            fact = 300
            r = random.randint(-fact, fact)
            g = random.randint(-fact, fact)
            b = random.randint(-fact, fact)
            a = pix[i, j][0] + r
            b = pix[i, j][1] + g
            c = pix[i, j][2] + b
            if(a < 0):
                a = 0
            elif(a > 255):
                a = 255
            if(b < 0):
                b = 0
            elif(b > 255):
                b = 255
            if (c < 0):
                c = 0
            elif(c > 255):
                c = 255
            draw.point([i, j],(a, b, c)) 
    image.save("gradi.jpg")
    t2 = time.time()
    t = round(t2 - t1, 2)
    print("Время работы программы : \%s " % t + "с")
if(mode == 3):
    t1 = time.time()
    fact = int(input("Fact: "))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            s = a+b+c
            if(s > (255 + fact)//2*3):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    image.save("chern.jpg")
    t2 = time.time()
    t = round(t2 - t1, 2)
    print("Время работы программы : \%s " % t + "с")
if (mode == 4):
     t1 = time.time()
     for i in range(width):
        for j in range(height):
          a = pix[i, j][0]
          b = pix[i, j][1]
          c = pix[i, j][2]
          draw.point((i, j),(255 - a,255 - b,255 - c))
     image.save("chern1.jpg")
     t2 = time.time()
     t = round(t2 - t1, 2)
     print("Время работы программы : \%s " % t + "с")

if(mode == 5):
    l = int(input("Режим матрицы: "))
    t1 = time.time()
    for i in range(1, width-1):
        for j in range(1, height - 1):
            r = 0
            g = 0
            b = 0
            cur_matr = [[0]*3 for n in range(3)]
            for k in range(3):
                for m in range(0, 3):
                    for m2 in range(0, 3):
                        cur_matr[m][m2] = pix[i-1 + m, j-1 + m2][k]
                if(k == 0):
                    r = mumator(l, cur_matr)
                elif(k == 1):
                    g = mumator(l, cur_matr)
                elif(k == 2):
                    b = mumator(l, cur_matr)

            draw.point((i, j), (r, g, b))
    image.save("razm3 " + str(l) + ".jpg")
    t2 = time.time()
    t = round(t2 - t1, 2)
    print("Время работы программы : \%s " % t + "с")
