pilot1 = [0, 8]
pilot2 = [8, 16]
pilot3 = [16, 24]

speed = int(input('Введите скорость самолета км/ч: '))
dis = int(input('Введите дистанцию км.: '))

time = float(dis/speed)
if dis < 100 or speed < 100:
    print('Скорость самолета или дистанция введены неверно')
else:
    pilot_time = time - int(time/24)*24
    if pilot1[1] > pilot_time:
        print('Посадку осуществил пилот №1')
    elif pilot2[1] > pilot_time:
        print('Посадку осуществил пилот №2')
    else:
        print('Посадку осуществил пилот №3')
