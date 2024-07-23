from random import randint


def show_map():
    global mop
    for y in range(10):
        for x in range(10):
            print(mop[y][x], end=" ")
        print("\n")


def add_point(num):
    global mop
    for i in range(num):
        mop[randint(0, 9)][randint(0, 9)] = "[x]"


def chek_point(x, y):
    global mop
    if mop[y][x] == "[0]":
        cnt = 0
        for y_offset in range(y-1, y+2):
            for x_offset in range(x-1, x+2):
                if x_offset >= 0 and x_offset < 10 and y_offset >= 0 and y_offset < 10:
                    if mop[y_offset][x_offset] == "[x]":
                        cnt += 1
        if cnt != 0:
            mop[y][x] = f"[{cnt}]"
        else:
            mop[y][x] = f"[-]"


mop = []


def program(size, points):
    for i in range(10):
        mop.append(["[0]"] * 10)
    add_point(points)
    print("Стартовая карта")
    show_map()
    for y in range(size):
        for x in range(size):
            chek_point(x, y)
    print("Обработанная карта")
    show_map()


program(10, randint(8, 32))
