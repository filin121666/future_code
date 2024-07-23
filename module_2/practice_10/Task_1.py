position = input('Введите позицию фигуры: ')
chek = True

if len(position) > 2:
    print('неверный ввод позиции')
else:
    p1 = position[0].lower()
    p2 = int(position[1])
    print(f'Фигура перемещается в позицию {p1.upper()}{p2}')
    if p1 == 'a':
        p1 = 1
    elif p1 == 'b':
        p1 = 2
    elif p1 == 'c':
        p1 = 3
    elif p1 == 'd':
        p1 = 4
    elif p1 == 'e':
        p1 = 5
    elif p1 == 'f':
        p1 = 6
    elif p1 == 'g':
        p1 = 7
    elif p1 == 'h':
        p1 = 8
    else:
        print('Неверный ввод значения 1')
        chek = False
    if p2 < 1 or p2 > 8:
        print('Неверный ввод значения 2')
        chek = False
    if chek:
        print("Фигура может быть перемещена в указанную позицию")
