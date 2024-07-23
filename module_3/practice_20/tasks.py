# Задача 1
import abc


class Warrior:
    damage: int
    health: int
    name: str


artes = Warrior()
artes.damage = 10
artes.health = 100
artes.name = 'Artes'

# Задача 2


class RailWayStation:
    def sell_ticket(self):
        pass


class Cashier(RailWayStation):
    def sell_ticket(self):
        return super().sell_ticket()

# Задача 3


class Warior:
    def attack(self):
        pass


class Archer:
    def attack(self):
        pass


class Arena:
    def batle(self, w1, w2):
        if isinstance(w1, Warior) and isinstance(w2, Warior):
            pass
        elif isinstance(w1, Warior) and isinstance(w2, Archer):
            pass
        elif isinstance(w1, Archer) and isinstance(w2, Archer):
            pass


# Задача 4


class Computer(abc.ABC):
    pass


class Phone(abc.ABC):
    pass


class Smartphone(abc.ABC):
    pass


class Samsung(Smartphone):
    pass

# Задача 5


class User:
    def save_user_to_db(self):
        pass

# Задача 6


class Permission:
    def get_permission(self, user):
        if user == 'staff':
            pass
        elif user == 'simple':
            pass
        elif user == 'admin':
            pass
