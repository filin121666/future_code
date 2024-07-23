questions = [
    "Нарвал живёт в море?",
    "Помидор - это корнеплод?",
    "Радикюль - разновидность сумочки?",
    "Кипяток - загасит огонь быстрее холодной воды?",
    "Пирсинг - это вид спорта?",
    "Полное имя Димы - Владимир?",
    "Вороны питаются только сыром?",
    "Про Каштанку написал Чехов?",
    "Уфа - это город в России?",
    'Слова "день" и "ночь" женского рода?',
]

answers = ["да", "нет", "да", "да", "нет", "нет", "нет", "да", "да", "нет"]


def main():
    for i in range(10):
        if check_question(i):
            print("Верно!")
        else:
            if input("Вы ответили не верно, начать заново? Да или нет: ").lower() == "да":
                main()
            else:
                break


def check_question(q_number):
    global answers
    print(questions[q_number])
    answer = input("Да или нет: ").lower()
    if answer == answers[q_number]:
        return True
    else:
        return False


main()
print("Игра завершена.")
