lst1 = input("Введите значения списка 1 через запятую: ").split(",")
lst2 = input("Введите значения списка 2 через запятую: ").split(",")
print(f"Список 1: {lst1}")
print(f"Список 2: {lst2}")
lst3 = lst1.copy()
lst1 = lst2
lst2 = lst3
print(f"Список 1: {lst1}")
print(f"Список 2: {lst2}")
