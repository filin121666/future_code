from tkinter import BOTH, LEFT, YES, Button, Frame, mainloop


def sw_color(but, color):
    but.config(bg=color)


f1 = Frame()
f1.pack(expand=YES, fill=BOTH)
f2 = Frame()
f2.pack(expand=YES, fill=BOTH)

B2 = Button(f2)
B2.pack(expand=YES, fill=BOTH, side=LEFT)
B2.config(text="Switch color", width=72, height=8, bg="gray")
B2.config(command=lambda but=B2, color="gray": sw_color(but, color))

b1 = Button(f1)
b1.pack(expand=YES, fill=BOTH, side=LEFT)
b1.config(text="Switch color", width=12, height=8, bg="red")
b1.config(command=lambda but=B2, color="red": sw_color(but, color))

b2 = Button(f1)
b2.pack(expand=YES, fill=BOTH, side=LEFT)
b2.config(text="Switch color", width=12, height=8, bg="orange")
b2.config(command=lambda but=B2, color="orange": sw_color(but, color))

b3 = Button(f1)
b3.pack(expand=YES, fill=BOTH, side=LEFT)
b3.config(text="Switch color", width=12, height=8, bg="yellow")
b3.config(command=lambda but=B2, color="yellow": sw_color(but, color))

b4 = Button(f1)
b4.pack(expand=YES, fill=BOTH, side=LEFT)
b4.config(text="Switch color", width=12, height=8, bg="green")
b4.config(command=lambda but=B2, color="green": sw_color(but, color))

b5 = Button(f1)
b5.pack(expand=YES, fill=BOTH, side=LEFT)
b5.config(text="Switch color", width=12, height=8, bg="blue")
b5.config(command=lambda but=B2, color="blue": sw_color(but, color))

b6 = Button(f1)
b6.pack(expand=YES, fill=BOTH, side=LEFT)
b6.config(text="Switch color", width=12, height=8, bg="purple")
b6.config(command=lambda but=B2, color="purple": sw_color(but, color))

mainloop()
