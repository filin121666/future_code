from tkinter import Tk, Canvas, Label, LEFT

v1 = 7  # Скорость первого бегуна
v2 = 5  # Скорость второго бегуна
s = 200  # Расстояние
t = s / (v1 + v2)  # Время
otv = round(t * v1)
rast = 1000 / s * otv
new_window = Tk()
canvas = Canvas(new_window, width=1000, height=1000, bg="white", cursor="arrow")
new_window.title("Программа")
my_title = Label(new_window, text="Программа", font=40)
canvas.create_text(400, 100, text="Условие задачи:", font="Arial 24", anchor="n", justify=LEFT, fill="black")
canvas.create_text(400, 125, text="Скорость первого бегуна " + str(v1) + " км/ч", font="Arial 24", anchor="n", justify=LEFT, fill="black")
canvas.create_text(400, 150, text="Скорость второго бегуна " + str(v2) + " км/ч", font="Arial 24", anchor="n", justify=LEFT, fill="black")
canvas.create_text(400, 175, text="Дистанция" + str(s) + " км", font="Arial 24", anchor="n", justify=LEFT, fill="black")
canvas.create_text(500, 500, text="Точка пересечения " + str(otv) + " км", font="Arial 24", anchor="n", justify=LEFT, fill="black")
canvas.create_line(0, 600, 1000, 600, width=5, fill="black")
canvas.create_oval(rast-25, 575, rast+25, 625, width=5, fill="red")
my_title.pack()
canvas.pack()
new_window.mainloop()
