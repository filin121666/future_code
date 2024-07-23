list1 = ["Привет", 24, True, False, 67, "пока", 92, False, 273, True, "Python"]
list_bool = []
list_int = []
list_str = []
for i in list1:
    if type(i) == bool:
        list_bool.append(i)
    if type(i) == int:
        list_int.append(i)
    if type(i) == str:
        list_str.append(i)
list_bool = sorted(list_bool)
list_int = sorted(list_int)
list_str = sorted(list_str)
print(f"Список булевых значений {list_bool}")
print(f"Список слов (или строк) {list_str}")
print(f"Список целых положительных чисел {list_int}")
