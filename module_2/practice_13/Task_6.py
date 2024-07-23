from random import randint

lst = []
for _ in range(10):
    lst.append(input("Введите слово: ").lower())


def func():
    sl_1 = randint(0, 9)
    print(f"Отгадай загаданное слово из представленных:\n{lst}")
    print(f"Подсказка: в загаданном слове {lst[sl_1].count("а")} буквы 'а' и {lst[sl_1].count("о")} буквы 'о'")
    letter1 = lst[sl_1 - 1][randint(0, len(lst[sl_1 - 1]))]
    letter2 = lst[sl_1 - 1][randint(0, len(lst[sl_1 - 1]))]
    if sl_1 - 1 > 0:
        print(f"Подсказка: в слове слева от загаданного есть буква '{letter1}' и '{letter2}'")
    if sl_1 + 1 < 9:
        if len(lst[sl_1+1]) > len([sl_1]):
            print(f"Подсказка: слово правее загаданного длиннее, чем загаданное слово")
        elif len(lst[sl_1+1]) < len([sl_1]):
            print(f"Подсказка: слово правее загаданного длиннее, чем загаданное слово")
        else:
            print(f"Подсказка: слово правее загаданного длиннее и загаданное слово имеют одинаковую длину")
    word = input("Введите слово (не допускайте ошибки): ").lower()
    if word not in lst:
        print("Слово введено не корректно (с ошибкой)")
    else:
        if word == lst[sl_1]:
            print("Вы угадали!")
        else:
            print("Вы не угадали!")


func()
