from tkinter import Tk, Canvas
new_window = Tk()
canvas = Canvas(new_window, width=1000, height=1000, bg="white", cursor="arrow")
x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))
r = int(input("Введите радиус: "))
canvas.create_oval(x-r, y-r, x+r, y+r, width=5, fill="red")
canvas.pack()
new_window.mainloop()
