str1 = input("Введите слово: ")
str2 = input("Введите слово: ")
if len(str1) > len(str2):
    print(f"Слово {str1} длиннее чем {str2}")
elif len(str2) > len(str1):
    print(f"Слово {str2} длиннее чем {str1}")
else:
    print("Слова имеют одинаковую длину")
