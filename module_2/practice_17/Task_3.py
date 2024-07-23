import random


def shuffle_words(words):
    shuffled_words = []
    for word in words:
        letters = list(word)
        random.shuffle(letters)
        shuffled_word = ''.join(letters)
        shuffled_words.append(shuffled_word)
    return shuffled_words


lst = input("Введите список слов: ").split()
print(f"Итоговый список: {shuffle_words(lst)}")
