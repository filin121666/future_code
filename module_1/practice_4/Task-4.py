numbers = []
numbers.extend(list(map(int, input('Введите числа: ').split())))
sum_nums = sum(numbers)
print(f"Вы ввели {numbers}")
print(f"Сумма чисел: {sum_nums}")
res = str(sum_nums % 2)
res = res.replace("0", "да")
res = res.replace("1", "нет")
print(f"Чётное? {res}")
