players = [
    [1, "Александр", "Иванов", 56],
    [2, "Елена","Сидорова", 73],
    [3, "Олег", "Кузнецов", 34],
]
print(f"Участник {players[0][0]} - {players[0][1]}")
print(f"Участник {players[1][0]} - {players[1][1]}")
print(f"Участник {players[2][0]} - {players[2][1]}")
print(f"Рейтинг {players[0][1]} {players[0][2]} равен {players[0][3]}%")
print(f"Рейтинг {players[1][1]} {players[1][2]} равен {players[1][3]}%")
print(f"Рейтинг {players[2][1]} {players[1][2]} равен {players[2][3]}%")
input_player1 = int(input("Введите номер участника для изменения рейтинга ")) - 1
value = int(input("Введите значение для изменения рейтинга "))
players[input_player1][3] = players[input_player1][3] + value
print("Результат после изменения рейтинга")
print(f"Рейтинг {players[0][1]} {players[0][2]} равен {players[0][3]}%")
print(f"Рейтинг {players[1][1]} {players[1][2]} равен {players[1][3]}%")
print(f"Рейтинг {players[2][1]} {players[2][2]} равен {players[2][3]}%")
