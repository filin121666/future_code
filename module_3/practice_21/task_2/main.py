# Данный проект на ходится на моём github, вот ссылка на репозиторий https://github.com/filin121666/herous_git.git
from heroes import Create_hero
from battle import battle
from weapons import Sword, Spear, Bow, Crossbow, Stick, Book


if __name__ == '__main__':
    hero_fabric = Create_hero()

    hero1 = hero_fabric.create_warrior(
        name_hero='Вася',
        weapon=Sword("Армагидон")
    )
    hero2 = hero_fabric.create_archer(
        name_hero='Иигарь',
        weapon=Bow("Snipebow")
    )

    battle(hero1=hero1, hero2=hero2)
