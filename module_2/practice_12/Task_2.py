from random import randint
lst = []
length = int(input("Введите длину списка: "))
for i in range(length):
    lst.append(randint(0, 100))
print(lst)
