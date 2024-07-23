names = []
names.extend(input("Введите список имён: ").split())
name = input("Введите имя для проверки: ")
if name in names:
    print(f"Имя {name} присутствует в списке под номером {names.index(name)+1}")
else:
    print(f"Имя {name} отсутствует в списке")
