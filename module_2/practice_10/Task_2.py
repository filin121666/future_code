from math import sqrt
r = int(input("Введите радиус круга: "))
x = int(input("Введите координату X: "))
y = int(input("Введите координату Y: "))
if sqrt((0 - x)**2 + (0 - y)**2) <= r:
    print("Точка находится в круге")
else:
    print("Точка находится вне круга")
