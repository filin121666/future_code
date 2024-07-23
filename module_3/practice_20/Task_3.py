import abc


class Player(abc.ABC):
    @abc.abstractmethod
    def attack(self):
        pass


class Warrior(Player):
    pass


class Archer(Player):
    pass


class Arena_players:
    def __init__(self, w1, w2) -> None:
        self.w1 = w1
        self.w2 = w2


class War_ws_war(Arena_players):
    def battle(self, *args):
        pass


class War_ws_arch(Arena_players):
    def battle(self, *args):
        pass


class Arch_ws_arch(Arena_players):
    def battle(self, *args):
        pass
