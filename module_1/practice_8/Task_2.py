from tkinter import Tk, Canvas, CENTER
new_window = Tk()
canvas = Canvas(new_window, width=1000, height=1000, bg="white", cursor="arrow")
str = input()
str = str.replace(".", "\n")
canvas.create_text(500, 100, text=str, font="Arial 24", justify=CENTER, fill="black")
canvas.pack()
new_window.mainloop()
