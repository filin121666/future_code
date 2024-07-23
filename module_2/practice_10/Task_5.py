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
        turnlist = [[p1+1, p2-2], [p1+2, p2-1], [p1+2, p2+1], [p1+1, p2+2], [p1-1, p2+2], [p1-2, p2+1], [p1-2, p2-1], [p1-1, p2-2]]
        turnlist = sorted(turnlist)
        print("Список доступных ходов:")
        for pos in turnlist:
            if 0 < pos[0] < 9 and 0 < pos[1] < 9:
                if pos[0] == 1:
                    pos[0] = 'A'
                elif pos[0] == 2:
                    pos[0] = 'B'
                elif pos[0] == 3:
                    pos[0] = 'C'
                elif pos[0] == 4:
                    pos[0] = 'D'
                elif pos[0] == 5:
                    pos[0] = 'E'
                elif pos[0] == 6:
                    pos[0] = 'F'
                elif pos[0] == 7:
                    pos[0] = 'G'
                elif pos[0] == 8:
                    pos[0] = 'H'
                print(pos)
