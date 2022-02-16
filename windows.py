import tkinter as tk
import os
from tkinter import messagebox
import random

# generate word
f = open("wordlist.txt", "r")
word_list = set()
for line in f.readlines():
    line = line.strip()
    if(len(line)==5):
        word_list.add(line)
f.close
word_list = list(word_list)
answer = random.choice(word_list)


def create_window():
    draw_blocks()
    win.mainloop()


def draw_blocks():
    x_x = 40
    y_y = 70
    temp = 0
    for i in range(0, 6):
        x_x = 40
        for j in range(0, 5):
            globals()[f'button{i}{j}'] = tk.Label(win, width=4, height=2, background=color[temp], foreground='white', text=guess[temp],
                                                  font=('Arial Black',)).place(x=x_x, y=y_y)
            temp += 1
            x_x += 60
        y_y += 60


def check():
    var = e0.get()
    var = var.lower()
    e0.delete("0","end")
    if(len(var) != 5):
        tk.messagebox.showerror(
            title='Error', message=f'require 5 alphabets, but received {len(var)}')
    elif(var not in word_list):
        tk.messagebox.showerror(
            title='Error', message=f'{var} is not in word list')
    else:
        global times,end
        correct = 0
        count = 0
        for i in var:
            guess[times*5+count] = i
            if(i == answer[count]):
                # green
                correct += 1
                color[times*5+count] = 'green'
            elif(i in answer):
                # yellow
                color[times*5+count] = 'orange3'
            else:
                # gray
                color[times*5+count] = 'gray'
            count += 1
        times += 1
        draw_blocks()
        if(correct == 5):
            tk.messagebox.showerror(title='Result', message=f'{times}/6')
            end = 1
            b0.config(state=tk.DISABLED)
        elif(times==6):
            tk.messagebox.showerror(title='Result', message=f'Failed!\nCorrect Answer:{answer}')
            end = 1
            b0.config(state=tk.DISABLED)


def check_button(self):
    global end
    if(end != 1):
        check()


# windows(win) basic info
win = tk.Tk()
win.title("Wordle Game")
win.geometry('370x500')
win.attributes("-topmost", 1)
win.resizable(False, False)

times = 0
end = 0
guess = [' ']*30
color = ['gray'] * 30

# windows(win) elements
block = tk.Label(win,
                 text="W O R D L E",
                 font=('Arial Black', 20),
                 )
block.place(x=100, y=20)

# entry part
e0 = tk.Entry(win)
e0.place(x=75, y=450)

b0 = tk.Button(win,
               text='enter!',
               command=check,
               )
b0.place(x=270, y=443)

win.bind('<Return>', check_button)
