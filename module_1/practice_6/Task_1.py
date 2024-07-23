word = input("Введите слово: ")
let = []
let.extend(word)
print(f"Слово: {let}")
print(f"Первая половина: {let[:len(let) // 2]}")
print(f"Вторая половина: {let[len(let) // 2:]}")
