from tkinter import BOTH, LEFT, YES, Button, Frame, Label, mainloop
from random import randint

f1 = Frame()
f1.pack(expand=YES, fill=BOTH)
f2 = Frame()
f2.pack(expand=YES, fill=BOTH)
l = Label(f1)
l.pack(expand=YES, fill=BOTH)
l.config(text="", font="Arial 100")
b1 = Button(f2)
b1.pack(expand=YES, fill=BOTH, side=LEFT)
b2 = Button(f2)
b2.pack(expand=YES, fill=BOTH, side=LEFT)


def func(num):
    n = randint(1, num)
    l.config(text=f"{n}")


b1.config(command=lambda num=6: func(num), text="Cube 6")
b2.config(command=lambda num=20: func(num), text="Cube 20")

mainloop()
