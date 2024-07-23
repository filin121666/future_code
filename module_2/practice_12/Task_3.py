from random import uniform
lst1 = []
lst2 = []
length = int(input("Введите длину списков: "))
for _ in range(length):
    num = uniform(-100, 100)
    lst1.append(num)
    lst2.append(round(num))
print(lst1)
print(lst2)
