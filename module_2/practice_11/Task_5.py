fig = ['пешка', 'конь', 'слон', 'ладья', 'ферзь', 'король']
fig_list = input('Введите через запятую фигуры:').split(',')
print(f'Список фигур {fig_list}')

for num in range(len(fig_list)):
    fig_list[num] = fig_list[num].lower()

result = 0

for i in range(len(fig_list)):
    correct_fig = False
    for index, figure in enumerate(fig):
        if figure == fig_list[i]:
            result += index+1
            correct_fig = True
            break

    if correct_fig == False:
        print(f'Компьютер не смог распознать фигуру: {fig_list[i]}')
        confirm = input('Исправим фигуру? (да/нет): ').lower()
        if confirm == 'да':
            fig_list[i] = input('Введите верное название фигуры: ').lower()
            for index, figure in enumerate(fig):
                if figure == fig_list[i]:
                    result += index+1
                    correct_fig = True
                    break
print(f'''
Фигуры: {fig_list}
Сумма фигур равна: {result}
''')
