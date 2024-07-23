str1 = input("Введите строку: ").split()
str2 = []
for i in str1:
    tmp = int(input(f"Сколько букв в слове {i} оставить? "))
    str2.append(i[:tmp])
print(f"Итоговый список {str2}")
