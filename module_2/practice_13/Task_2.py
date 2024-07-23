def sorting():
    lst = [10, 5, 6, 3, 8, 2, 1, 4, 7, 9]
    print(lst)
    for i in range(len(lst) - 1):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    print(lst)


sorting()
