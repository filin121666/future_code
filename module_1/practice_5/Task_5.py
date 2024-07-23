str1 = input("Введите игроков ").split()
l = int(input("Введите время забега "))
print(len(str1))
lens = len(str1)
n = []
k = []
for i in str1:
    n.append([i.title()])
for i in range(len(lens)):
    n[i].append(int(input(f"Введите скорость {n[i][0]} ")))
    n[i].append(int(input(f"Введите затраты выносливости {n[i][0]} ")))
for i in range(lens):
    k.append([n[i][0], n[i][1] * l, 100 - (n[i][2] * l)])
k.sort(key=lambda x: x[1], reverse=True)
print(f"Лучший бегун: {k[0][0]}, пробежал {k[0][1]}")
k.sort(key=lambda x: x[2], reverse=True)
print(f"Лучший по выносливости: {k[0][0]}, осталось выносливости {k[0][2]}")
