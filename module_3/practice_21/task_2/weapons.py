import random
import abc


class Weapon(abc.ABC):
    @abc.abstractmethod
    def change_damage() -> int:
        pass


class Sword(Weapon):
    def __init__(self, weapon_name: str) -> None:
        super().__init__()
        self.weapon_name = weapon_name

    def change_damage(self, crit: bool) -> int:
        if crit:
            return random.randint(75, 100)
        else:
            return random.randint(60, 75)


class Spear(Weapon):
    def __init__(self, weapon_name: str) -> None:
        super().__init__()
        self.weapon_name = weapon_name

    def change_damage(self, crit: bool) -> int:
        if crit:
            return random.randint(90, 110)
        else:
            return random.randint(70, 90)


class Bow(Weapon):
    def __init__(self, weapon_name: str) -> None:
        super().__init__()
        self.weapon_name = weapon_name

    def change_damage(self, crit: bool) -> int:
        if crit:
            return random.randint(75, 95)
        else:
            return random.randint(60, 75)


class Crossbow(Weapon):
    def __init__(self, weapon_name: str) -> None:
        super().__init__()
        self.weapon_name = weapon_name

    def change_damage(self, crit: bool) -> int:
        if crit:
            return random.randint(80, 100)
        else:
            return random.randint(65, 80)


# Я имею ввиду волшебную палочку, под названием Stick
class Stick(Weapon):
    def __init__(self, weapon_name: str) -> None:
        super().__init__()
        self.weapon_name = weapon_name

    def change_damage(self, crit: bool) -> int:
        if crit:
            return random.randint(100, 120)
        else:
            return random.randint(80, 100)

# Я имею ввиду книгу заклинаний, под названием Book


class Book(Weapon):
    def __init__(self, weapon_name: str) -> None:
        super().__init__()
        self.weapon_name = weapon_name

    def change_damage(self, crit: bool) -> int:
        if crit:
            return random.randint(95, 110)
        else:
            return random.randint(70, 85)
