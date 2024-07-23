from tkinter import Tk, Button
new_window = Tk()
new_window.title("Программа")
str1 = list(input("Введите слово: "))
num = 0


def func():
    str_new = ""
    for index, i in enumerate(str1):
        if index == num:
            str_new += f"[{i}]"
        else:
            str_new += i
    print(str_new)


func()


def right():
    global num
    if num < len(str1) - 1:
        num += 1
        func()


def left():
    global num
    if num > 0:
        num -= 1
        func()


Button(width=50, height=10, text="Влево", command=left).pack()
Button(width=50, height=10, text="Вправо", command=right).pack()
new_window.mainloop()
