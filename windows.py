import tkinter as tk
import random

# generate word
word_list = ['which', 'their', 'would', 'there', 'could', 'other', 'about', 'great', 'these', 'after', 'first', 'never', 'where', 'those', 'shall', 'being', 'might', 'every', 'think', 'under', 'found', 'still', 'while', 'again', 'place', 'young', 'years', 'three', 'right', 'house', 'whole', 'world', 'thing', 'night', 'going', 'heard', 'heart', 'among', 'asked', 'small', 'woman', 'whose', 'quite', 'words', 'given', 'taken', 'hands', 'until', 'since', 'light']
answer = random.choice(word_list)

def create_window():
    win.mainloop()

# windows(win) basic info
win = tk.Tk()
win.title("Wordle Game")
win.geometry('370x500')
win.attributes("-topmost", 1)
win.resizable(False, False)

# windows(win) elements
block = tk.Label(win,
                 text="W O R D L E",
                 font=('Arial Black', 20),
                 width=30,
                 height=2
                 )
block.pack()

x_x = 40
y_y = 70
for i in range(0, 6):
    x_x = 40
    for j in range(0, 5):
        globals()[f'button{i}{j}'] = tk.Button(
            win, width=5, height=3, text=f'{i}{j}', state=tk.DISABLED).place(x=x_x, y=y_y)
        x_x += 60
    y_y += 60

# entry part

e0 = tk.Entry(win)
e0.pack()


def check():
    var = e0.get()
    count = 0
    for i in var:
        if(i == answer[count]):
            # green
            pass
        elif(i in answer):
            # yellow
            pass
        else:
            # grey
            pass

b0 = tk.Button(win,
               text='enter!',
               command=check,
               )
b0.pack()