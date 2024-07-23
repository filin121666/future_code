class Warrior:
    def __init__(self, damage: int, health: int, name: str):
        self.damage = damage
        self.health = health
        self.name = name

    def set_damage(self, damage: int):
        self.damage = damage

    def get_damage(self) -> int:
        return self.damage

    def set_health(self, health: int):
        self.health = health

    def get_health(self) -> int:
        return self.health

    def set_name(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name


artes = Warrior(damage=10, health=100, name='Artes')
