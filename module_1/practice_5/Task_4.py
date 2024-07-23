l = input("Введите 10 слов ").split()
n = []
for i in l:
    temp_l = [i, len(i)]
    n.append(temp_l)
n.sort(key=lambda x: x[-1], reverse=True)
print(len(l))
print(f'''Три самых длинных слова:
1-{n[0][0]}
2-{n[1][0]}
3-{n[2][0]}''')
