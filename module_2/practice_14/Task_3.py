from random import randint
lst = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
print(lst)
hid_ind = randint(0, 4)


def func(val):
    global lst
    global hid_ind
    if val == hid_ind:
        print("Угадал")
        lst[hid_ind] = "[o]"
        print(lst)
        print("Вы победили")
        return True
    else:
        print("Не угадал")
        lst[val] = "[x]"
        print(lst)
        print("Вы проиграли")
        return False


for i in range(3):
    res = func(int(input("Введите номер ячейки от 1 до 5: ")) - 1)
    if res:
        break
