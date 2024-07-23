from tkinter import Frame, YES, BOTH, Button, LEFT, N, TOP, mainloop
import random

map = []
buttons = []
frames = []


def programm(size, points):
    global map
    global buttons
    global frames
    map = []
    for button in buttons:
        button.destroy()
    buttons = []
    for frame in frames:
        frame.destroy()
    frames = []
    for i in range(10):
        map.append(["[0]"]*size)
    add_point(points, size)
    for y in range(size):
        for x in range(size):
            chek_point(x, y, size)
    print("Обработанная карта")
    show_map(size)


def show_map(size):
    global map
    for y in range(size):
        for x in range(size):
            print(map[y][x], end=" ") 
        print("\n") 


def add_point(num, size):
    global map
    for i in range(num):
        map[random.randint(0, size-1)][random.randint(0, size-1)] = "[x]"


def chek_point(x, y, size):
    global map
    if map[y][x] == "[0]":
        count = 0
        for y_offset in range(y-1, y+2):
            for x_offset in range(x-1, x+2):
                if 0 <= x_offset < size and 0 <= y_offset < size:
                    if map[y_offset][x_offset] == "[x]":
                        count += 1
        if count != 0:
            map[y][x] = f"[{count}]"
        else:
            map[y][x] = f"[-]" 


def chek_mine(x, y, n):  # 1 задача
    if map[x][y] == "[x]":
        buttons[n].config(text="[x]", bg='red', activebackground='white')
    else:
        buttons[n].config(text=map[x][y], bg='green', activebackground='white')


def marker(n):   # 2 задача
    global buttons
    if buttons[n].cget('text') == '':
        buttons[n].config(text='X', bg='yellow', activebackground='white')
    elif buttons[n].cget('text') == 'X':
        buttons[n].config(text='', bg='gray', activebackground='white')


def start_game(size, mines):  # 3 задача
    global buttons
    global frames
    global start_game_button
    start_game_button.config(text="Restart Game")
    programm(size, mines)
    for i in range(size):
        frames += ([Frame()])
        frames[i].pack(expand=YES, fill=BOTH)
        for j in range(size):
            n = i * size + j  # Вычисляем номер кнопки для списка
            buttons += ([Button(frames[i])])
            buttons[n].pack(expand=YES, fill=BOTH, side=LEFT)
            buttons[n].config(width=4, height=2)
            buttons[n].config(text='', bg='gray', activebackground='white')
            buttons[n].config(command=lambda x=i, y=j, num=n: chek_mine(x, y, num))
            buttons[n].bind('<Button-3>', lambda event, num=n: marker(num))


frame = Frame()        
frame.pack(expand=YES, fill=BOTH, anchor=N)
start_game_button = Button(frame)
start_game_button.pack(expand=YES, fill=BOTH, side=TOP)
start_game_button.config(text="Start Game", width=8, height=2)
start_game_button.config(command=lambda size=10, mines=10: start_game(size, mines))

mainloop()
