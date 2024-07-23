list_a = []
list_b = []

list_a.extend((input('Введите значения списка 1 через пробел: ')).split(' '))
list_b.extend((input('Введите значения списка 2 через пробел: ')).split(' '))


def unique(x_list):
    temp_list = []
    for i in range(len(x_list)):
        temp_list.extend(word_to_char(x_list[i]))
    # print(temp_list)
    result_list = []

    for ind, char in enumerate(temp_list):
        if char not in result_list:
            result_list.append(char)
    result_list.sort()
    print(result_list)
    return len(result_list)


def word_to_char(word):
    char_list = []
    char_list.extend(word)
    return char_list


result_a = unique(list_a)
result_b = unique(list_b)

if result_a > result_b:
    print('Список 1 имеет больше уникальных элментов')
elif result_a < result_b:
    print('Список 2 имеет больше уникальных элментов')
else:
    print('Количество уникальных элементов в списках одинаково')
