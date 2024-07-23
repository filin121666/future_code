l1 = []
l2 = []
num1 = int(input("Введите переменную 1: "))
l1.append(num1)
num2 = int(input("Введите переменную 2: "))
l1.append(num2)
num3 = int(input("Введите переменную 3: "))
l1.append(num3)
num4 = int(input("Введите переменную 4: "))
l1.append(num4)
for i in l1:
    l2.append(i + l1[0])
print(f"Список переменных: {l1}")
print(f"Список сумм переменных: {l2}")
