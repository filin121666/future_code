from tkinter import Tk, Canvas, Checkbutton, Button
new_window = Tk()
canvas = Canvas(new_window, width=1000, height=1000, bg="white", cursor="arrow")
checkbutton1 = Checkbutton(text="Red").pack()
checkbutton2 = Checkbutton(text="Green").pack()
checkbutton3 = Checkbutton(text="Blue").pack()
Button(text="Изменить").pack()
canvas.pack()
new_window.mainloop()
