def func():
    lst = []
    for _ in range(10):
        name = input("Введите слово: ")
        if name[0].isupper():
            lst.append(name)
    print(lst)


func()
