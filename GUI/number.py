
from tkinter import *
import random

#граница диапазона
val_range = 0
#загаданное число
secret = 0
guesses = 0 #попытки
limit = 0#предел попыток

def new_game():
    global secret, guesses, val_range, limit
    val_range = 100
    msg['text'] = ' ' * 100 + \
                  '\nНовая игра, диапазон[0..{}]\n'.format(val_range)
    secret = random.randrange(0, val_range)
    guesses = 0
    limit = 5
    return

def input_guesses(event):
    global guesses
    value = int(ent.get())
    try:

       lab['text'] = "Вы ввели {}\nВведите следующее число:".format(value)
    except ValueError:
       lab['text'] = "Вы ввели {}\nВведите следующее число:".format(ent.get())
    ent.delete(0,END)
    guesses += 1
    if (value < secret):
        msg['text'] += "{} - больше\n".format(value)
    elif (value > secret):
        msg['text'] += "{} - меньше\n".format(value)
    else:
        msg['text'] += "Вы победили\n".format(value)
    if (guesses >= limit):
        msg['text'] += "Попытки кончились. Вы проиграли. Загаданное число: {} \n".format(secret)
    return

root = Tk()
root.title("Угадай число!")
root.geometry("500x500")
lab = Label(root, text = "Введите следующее число:")
lab.pack(side = TOP)
ent = Entry(root, width = 15)
ent.pack(side = TOP)
ent.focus()
ent.bind("<Return>",input_guesses)
Button(root, text = "Новая игра", command = new_game).pack(side = BOTTOM)
msg = Message(root, fg ="Black", width = 400, borderwidth = 0)
msg.pack(side = TOP)
new_game()
root.mainloop()