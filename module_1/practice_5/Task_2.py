l = [
    ["Андрей", 5, 4, 5],
    ["Олег", 4, 5, 3],
    ["Иван", 3, 4, 3],
]
for i in l:
    i.append(round((i[1] + i[2] + i[3]) / 3, 1))
l.sort(key=lambda x: x[-1], reverse=True)
for i in l:
    print(i)
