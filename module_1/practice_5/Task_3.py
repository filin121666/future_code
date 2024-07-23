l = input("Введите слова ").split()
n = []
for i in l:
    n.append(len(i))
max_n = max(n)
max1 = n.index(max_n)
max2 = l[max1]
print(f"Самое длинное слово {max2}, {max_n}-букв")
print(f"список слов {l}")
print(f"список длин слов {n}")
