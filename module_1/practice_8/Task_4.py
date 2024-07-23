players = [["Николай"], ["Владимир"], ["Александр"], ["Екатерина"]]
for i in range(len(players)):
    players[i].append(int(input(f"Введите возраст {players[i][0]}: ")))
    players[i].append(int(input(f"Введите рейтинг {players[i][0]}: ")))
players.sort(key=lambda x: x[1])
print(f"Самый молодой участник {players[0][0]}, ему {players[0][1]} лет")
players.sort(key=lambda x: x[2], reverse=True)
print(f"Самый самый высокий рейтинг у {players[0][0]}, он составляет {players[0][2]}%")
