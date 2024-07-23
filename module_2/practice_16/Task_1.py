from tkinter import BOTH, LEFT, YES, Button, mainloop

width = 4
height = 4
b = Button()
b.pack(expand=YES, fill=BOTH, side=LEFT)
b.config(width=width, height=height)
b.config(text=f"W={width}, H={height}")


def mouse(size):
    global height
    global width
    height += size
    width += size*2
    b.config(width=width, height=height)
    b.config(text=f"W={width}, H={height}")


b.config(command=lambda size=2: mouse(size))
b.bind('<Button-3>', lambda event, size=-2: mouse(size))

mainloop()
