list1 = []
list2 = []
list1.append(int(input("Введите число: ")))
list1.append(int(input("Введите число: ")))
list1.append(int(input("Введите число: ")))
list1.append(int(input("Введите число: ")))
list1.append(int(input("Введите число: ")))
print(f"Вы ввели {list1}")
num = int(input("Введите число для проверки на кратность: "))
for i in list1:
    if i % num == 0:
        list2.append(i)
if len(list2) != 0:
    print(f"Список чисел {list2}, кратных {num}")
else:
    print(f"Кратных чисел числу {num} нет")
