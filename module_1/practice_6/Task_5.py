str1 = input("Введите список имён: ").split()
for i in range(len(str1)):
    print(f"{i}-{str1[i]}")
a = int(input("Введите номер первого имени для замены: "))
b = int(input("Введите номер второго имени для замены: "))
str1[a], str1[b] = str1[b], str1[a]
print(f"Итоговый список: {str1}")
