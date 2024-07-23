def chek_name(name):
    err_chr = ['!', '?', '.', ',', ':', ';', '+', '*', '/', '_', '-', '%', '#', '&']
    flag = False
    if not (name == name.title()):
        flag = True
    if not flag:
        for i in range(len(name)):
            if name[i].isdigit() or name[i] in err_chr:
                flag = True
                break
    if flag:
        print("Ошибка при вводе имени.")
    else:
        print("Имя введено вверно.")


n = input("Введите имя: ")
chek_name(n)
