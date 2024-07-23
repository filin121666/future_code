from random import choice
lst1 = ["камень", "ножницы", "бумага"]
str1 = input("Сделай выбор (1-камень, 2-ножницы, 3-бумага): ").lower()
if str1 == "1":
    str1 = "камень"
elif str1 == "2":
    str1 = "ножницы"
elif str1 == "3":
    str1 = "бумага"
print(str1)
str2 = choice(lst1)
if str2 == str1:
    print(f"Компьютер выбрал - {str2.title()}, ваш выбор - {str1.title()}. Ничья!")
elif str2 == lst1[0]:
    if str1 == lst1[1]:
        print(f"Компьютер выбрал - {str2.title()}, ваш выбор - {str1.title()}. Победил компьютер!")
    else:
        print(f"Компьютер выбрал - {str2.title()}, ваш выбор - {str1.title()}. Победил игрок!")
elif str2 == lst1[1]:
    if str1 == lst1[2]:
        print(f"Компьютер выбрал - {str2.title()}, ваш выбор - {str1.title()}. Победил компьютер!")
    else:
        print(f"Компьютер выбрал - {str2.title()}, ваш выбор - {str1.title()}. Победил игрок!")
elif str2 == lst1[2]:
    if str1 == lst1[0]:
        print(f"Компьютер выбрал - {str2.title()}, ваш выбор - {str1.title()}. Победил компьютер!")
    else:
        print(f"Компьютер выбрал - {str2.title()}, ваш выбор - {str1.title()}. Победил игрок!")
