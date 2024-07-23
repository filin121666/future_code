r = int(input("Введите количество красных яблок: "))
g = int(input("Введите количество зелёных яблок: "))
bad_r = 0
bad_g = 0
count = 0
if r >= 30 and g >= 30:
    bad_r = r - 30
    bad_g = g - 30
    print(f"Яблок хватит на месяц испортяться {bad_r} красных яблок и {bad_g} зелёных")
else:
    if r + g > 60:
        if r > g:
            count = g
            bad_r = (r - g) - (30 - count)*2
            print(f"Яблок хватит на месяц испортятся {bad_r} красных яблок")
        elif g > r:
            count = r
            bad_r = (g - r) - (30 - count)*2
            print(f"Яблок хватит на месяц испортятся {bad_g} зелёных яблок")
    else:
        if r > g:
            count = g
            only_r = (r - g)//2
            print(f"Яблок хватит на {count + only_r} дней, {only_r} дней в рационе будут только красные яблоки")
        elif g > r:
            count = r
            only_g = (g - r)//2
            print(f"Яблок хватит на {count + only_g} дней, {only_g} дней в рационе будут только зелёные яблоки")
        elif g == r:
            count = (r + g)//2
            print(f"Яблок хватит на {count} дней")
