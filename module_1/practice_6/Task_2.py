str1 = input("Введите слова: ").split()
str2 = []
for i in str1:
    str2.extend(i * len(i))
print(str2)
print(len(str2))
