num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
op = input('Введите оператор "+", "-", "/", "*": ')
if op == "+":
    result = num1 + num2
if op == "-":
    result = num1 - num2
if op == "/":
    result = num1 / num2
if op == "*":
    result = num1 * num2
print(f"{num1}{op}{num2}={result}")
