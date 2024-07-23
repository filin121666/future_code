str1 = input("Введите строку 1: ").split()
str2 = input("Введите строку 2: ").split()
str3 = input("Введите строку 3: ").split()
str4 = []
str4.extend(str1)
str4.extend(str2)
str4.extend(str3)
list1 = str4[0::3]
list2 = str4[1::3]
list3 = str4[2::3]
print(f"Список 1: {list1} длина списка {len(list1)}")
print(f"Список 2: {list2} длина списка {len(list2)}")
print(f"Список 3: {list3} длина списка {len(list3)}")
