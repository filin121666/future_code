names = ["Антон", "Андрей", "Пётр", "Василий", "Владимир"]
print(f'0 - {names[0]}')
print(f'1 - {names[1]}')
print(f'2 - {names[2]}')
print(f'3 - {names[3]}')
print(f'4 - {names[4]}')
a, b = list(map(int, input('Введите номера игроков для замены: ').split()))
names[a], names[b] = names[b], names[a]
print(f'0 - {names[0]}')
print(f'1 - {names[1]}')
print(f'2 - {names[2]}')
print(f'3 - {names[3]}')
print(f'4 - {names[4]}')