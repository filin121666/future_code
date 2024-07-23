from random import randint
n = int(input("Введите длину списка: "))


def func():
    global n
    lst = []
    cnt = 0
    max_cnt = 0
    for i in range(n):
        lst.append(randint(0, 1))
    print(lst)
    for i in range(n):
        if i == n - 1 and cnt >= max_cnt and lst[i] == 1:
            cnt += 1
            max_cnt = cnt
            cnt = 0
        elif lst[i] == 1:
            cnt += 1
        elif cnt > max_cnt:
            max_cnt = cnt
            cnt = 0
        else:
            cnt = 0
    print(max_cnt)


func()
