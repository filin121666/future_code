a = input("Введите число 1: ")
b = input("Введите число 2: ")
lst = []
c = int(a)*int(b)
print(a, "*", b, "=", c)
for n in str(c):
    lst.append(int(n))
lst.sort()
print("Отсортированный список: ", lst)
lst2 = []
for n in range(len(lst)-1):
    if lst[n] == lst[n+1]:
        lst2.append(n+1)
print("Индексы чисел на удаление: ", lst2)
for n in reversed(range(len(lst2))):
    lst.pop(lst2[n])
print(lst)
