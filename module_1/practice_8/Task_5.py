from tkinter import Tk, Checkbutton, Button
new_window = Tk()
colors = input("Введите цвета: ").split()
for i in colors:
    Checkbutton(new_window, text=i).pack()
Button(text="Выбрать цвет").pack()
new_window.mainloop()
