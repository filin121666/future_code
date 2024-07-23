def my_sort(lst_val, lst_ind):
    ln = len(lst_ind)
    res_lst = list([0] * ln)
    for i in range(ln):
        res_lst[lst_ind[i]] = lst_val[i]
    return res_lst


l_val = input("Введите значения списка значений: ").split()
l_ind = list(map(int, input("Введите значения списка индексов: ").split()))
if len(l_val) == len(l_ind):
    print(f"Отсортированный список: {my_sort(l_val, l_ind)}")
else:
    print("Ошибка: длины списков не совпадают!")
