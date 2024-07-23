names = ["Антон", "Андрей", "Пётр", "Василий"]
print(f"Игроки {names}")
print("Первое разбиение")
print(f"Команда 1: {names[:len(names)//2]}")
print(f"Команда 2: {names[len(names)//2:]}")
print("Второе разбиение")
print(f"Команда 1: {names[0::2]}")
print(f"Команда 2: {names[1::2]}")
