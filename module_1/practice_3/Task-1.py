from tkinter import Tk, Canvas, Label
new_window = Tk()
canvas = Canvas(new_window, width=500, height=500, bg="white", cursor="arrow")
new_window.title("Программа")
my_title = Label(new_window, text="Конкурс", font=40)
my_title.pack()
canvas.pack()
new_window.mainloop()
