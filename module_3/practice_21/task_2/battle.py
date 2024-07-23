from heroes import Warrior, Archer, Mage


def battle(hero1: Warrior | Archer | Mage = None, hero2: Warrior | Archer | Mage = None):
    print(f'В этой битве участвуют {hero1.name} и {hero2.name}\n')

    while hero1.health > 0 and hero2.health > 0:
        hero1.attack(hero2)
        hero2.attack(hero1)
        print()

    if hero1.health <= 0 and hero2.health > 0:
        print(f'{hero2.name} победил! У него осталось {hero2.health}hp')

    if hero1.health > 0 and hero2.health <= 0:
        print(f'{hero1.name} победил! У него осталось {hero1.health}hp')

    if hero1.health <= 0 and hero2.health <= 0:
        print(f'Ничья!')
