# В данном коде я не использовал Optional, потому что я использую последнюю версию Python
# В этом коде я не реализовал вывод информации о том какой сейчас был удар (критический или обычный)

import abc
import random
from weapons import Sword, Spear, Bow, Crossbow, Stick, Book


# Атрибут chance_miss будет использоваться для того, чтобы вычислить шанс того, что по данному герою промахнутся
class Hero(abc.ABC):
    health: int
    chance_miss: list

    @abc.abstractmethod
    def attack():
        pass


class Warrior(Hero):
    health: int = 1250
    chance_miss: list = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

    def __init__(self, name: str, weapon: Sword | Spear) -> None:
        super().__init__()
        self.name = name
        self.weapon = weapon

    def attack(self, enemy) -> None:
        crit = bool(random.choice([0, 0, 0, 0, 0, 0, 0, 0, 1, 1]))
        if random.choice(enemy.chance_miss):
            print(f'{self.name} промахнулся!')
        else:
            hit: int = self.weapon.change_damage(crit)
            enemy.health -= hit
            print(f'{self.name} нанёс удар {enemy.name} и оставил ему {enemy.health}hp')


class Archer(Hero):
    health: int = 1000
    chance_miss: list = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]

    def __init__(self, name: str, weapon: Bow | Crossbow) -> None:
        super().__init__()
        self.name = name
        self.weapon = weapon

    def attack(self, enemy) -> None:
        crit = bool(random.choice([0, 0, 0, 0, 0, 0, 0, 0, 1, 1]))
        if random.choice(enemy.chance_miss):
            print(f'{self.name} промахнулся!')
        else:
            hit: int = self.weapon.change_damage(crit)
            enemy.health -= hit
            print(f'{self.name} нанёс удар {enemy.name} и оставил ему {enemy.health}hp')


class Mage(Hero):
    health: int = 800
    chance_miss: list = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

    def __init__(self, name: str, weapon: Stick | Book) -> None:
        super().__init__()
        self.name = name
        self.weapon = weapon

    def attack(self, enemy) -> None:
        crit = bool(random.choice([0, 0, 0, 0, 0, 0, 0, 0, 1, 1]))
        if random.choice(enemy.chance_miss):
            print(f'{self.name} промахнулся!')
        else:
            hit: int = self.weapon.change_damage(crit)
            enemy.health -= hit
            print(f'{self.name} нанёс удар {enemy.name} и оставил ему {enemy.health}hp')


class Create_hero:
    def create_warrior(self, name_hero: str, weapon: Sword | Spear):
        return Warrior(name=name_hero, weapon=weapon)

    def create_archer(self, name_hero: str, weapon: Bow | Crossbow):
        return Archer(name=name_hero, weapon=weapon)

    def create_mage(self, name_hero: str, weapon: Stick | Book):
        return Mage(name=name_hero, weapon=weapon)
