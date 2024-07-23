from tkinter import Tk, Canvas
new_window = Tk()
canvas = Canvas(new_window, width=600, height=600, bg="white", cursor="arrow")
canvas.create_polygon([(100, 300), (150, 150), (300, 150), (300, 120), (200, 120), (200, 60), (300, 40), (400, 60), (400, 300), (200, 300), (200, 400), (150, 400)], width=5, fill="blue")
canvas.create_polygon([(200, 300), (400, 300), (400, 150), (450, 150), (500, 300), (450, 450), (300, 450), (300, 480), (400, 480), (400, 540), (300, 560), (200, 540)], width=5, fill="yellow")
canvas.create_oval(250, 60, 300, 110, fill="white")
canvas.create_oval(300, 540, 350, 490, fill="white")
canvas.pack()
new_window.mainloop()
