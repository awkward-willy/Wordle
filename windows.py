import tkinter as tk

# windows(win) basic info
win = tk.Tk()
win.title("Wordle Game")
win.geometry('370x500')
win.attributes("-topmost", 1)
win.resizable(False, False)

# windows(win) elements

block = tk.Label(win,
                 text="W O R D L E",
                 font=('Arial Black',20),
                 width=30,
                 height=2
                 )
block.pack()

# generate button( to show the words )
x_x = 40
y_y = 70
for i in range(0,6):
    x_x = 40
    for j in range(0,5):
        button=tk.Button(win,width=5,height=3,state=tk.DISABLED).place(x=x_x,y=y_y)
        x_x+=60
    y_y+=60

def create_window():
    win.mainloop()
