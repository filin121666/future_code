from random import choice
turns = ["Вверх", "Вниз", "Влево", "Вправо"]
path = []

map_size = input("Введите размер поля в формате X,Y: ").split(",")
computer_pos = input("Введите позицию робота в формате X,Y: ").split(",")
max_steps = int(input("Введите количество ходов: "))
steps = 0

for i in range(2):
    map_size[i] = int(map_size[i])
    computer_pos[i] = int(computer_pos[i])

for i in range(max_steps):
    steps += 1
    turn = choice(turns)
    if turn == turns[0]:
        computer_pos[1] -= 1
    elif turn == turns[1]:
        computer_pos[1] += 1
    elif turn == turns[2]:
        computer_pos[0] -= 1
    elif turn == turns[3]:
        computer_pos[0] += 1
    print(f"Робот совершил ход {turn}. Его новая позиция X{computer_pos[0]},Y{computer_pos[1]}")
    if (computer_pos[0] == 0 or computer_pos[0] == map_size[0]) or (computer_pos[1] == 0 or computer_pos[1] == map_size[1]):
        print(f"Робот находится на границе карты. Координата X{computer_pos[0]},Y{computer_pos[1]}")
    elif (computer_pos[0] < 0 or computer_pos[0] > map_size[0]) or (computer_pos[1] < 0 or computer_pos[1] > map_size[1]):
        print(f"Робот вышел за границу карты. Ход номер-{steps}, координата X{computer_pos[0]},Y{computer_pos[1]}")
        break

if max_steps == steps:
    print(f"Совершив {steps} ходов, робот не покинул карты")
