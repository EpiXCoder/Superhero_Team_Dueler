import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        print(f'List of Team {self.name} heroes:')
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            fighting_hero = random.choice(living_heroes)
            fighting_opponent = random.choice(living_opponents)

            fighting_hero.fight(fighting_opponent)

            if not fighting_hero.is_alive():
                living_heroes.remove(fighting_hero)
            
            if not fighting_opponent.is_alive():
                living_opponents.remove(fighting_opponent)
