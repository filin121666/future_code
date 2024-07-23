from random import randint
arr1 = []
arr2 = []

num = int(input('Введите число для проверки кратности: '))
amount = int(input('Введите количество чисел: '))

for _ in range(50):
    arr1.append(randint(0, 100))

arr1 = sorted(arr1)

for i in range(50):
    if arr1[i] % num == 0:
        arr2.append(arr1[i])
        amount -= 1
        if amount == 0:
            break

print(f'Список 1: \n {arr1}')
if amount == 0:
    print(f'Список 2: \n {arr2}')
else:
    print(f'''
Для полного заполнения списка 2 не хватает {amount} значений
Список 2:
{arr2} ''')
