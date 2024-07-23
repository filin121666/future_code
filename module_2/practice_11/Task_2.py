num = input("Введите число: ")
lst = []
for n in range(len(num)):
    lst.append(int(num[n]))
    if int(num[n]) == n:
        print(f"Число {num[n]} совпало с индексом {n}")
    else:
        print(f"Число {num[n]} не совпало с индексом {n}")
print(lst)
