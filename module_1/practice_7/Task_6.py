from tkinter import Tk, Canvas, Entry, Button
new_window = Tk()
canvas = Canvas(new_window, width=1000, height=1000, bg="white", cursor="arrow")
Entry().pack()
Entry(show="*").pack()
Button(text="Войти").pack()
Button(text="Изменить").pack()
canvas.pack()
new_window.mainloop()
