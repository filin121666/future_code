num = [-12, -11, -7, -4, -3, -1, 2, 5, 7, 9, 12, 14]
n = int(input("Введите число: "))
flag = True
for i in range(len(num)):
    for j in range(i+1, len(num)):
        res = num[i] + num[j]
        if res == n:
            print(f"Число {n} можно получить сложив {i}й и {j}й элемент списка\n{num[i]} + {num[j]} = {res}")
            flag = False
if flag:
    print(f"Невозможно получить {n} сложив 2 уникальных элемента списка: {num}")
