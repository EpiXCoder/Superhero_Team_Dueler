import random
from ability import Ability
from armor import Armor


class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    # def fight(self, opponent):
    #     duelers=[self.name, opponent.name]
    #     winner = random.choice(duelers)
    #     duelers.remove(winner)
    #     loser = duelers[0]    
    #     print(f'{winner} defeats {loser}!')

    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)
    
    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        protection = self.defend()
        damage_impact = damage - protection
        if damage_impact > 0:
            self.current_health -= damage_impact

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        if not self.abilities and not opponent.abilities:
            print('Draw')
            return
        
        while self.is_alive() and opponent.is_alive():
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())

            if self.is_alive() and not opponent.is_alive():
                print(f'{self.name} defeats {opponent.name}!')
            elif not self.is_alive() and opponent.is_alive():
                print(f'{opponent.name} defeats {self.name}!')
            elif not self.is_alive() and not opponent.is_alive():
                print(f'Both duelers succumb to fatal injuries!')



if __name__ == "__main__":
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # hero1.fight(hero2)
    # ability = Ability("Great Debugging", 50)
    # ability2 = Ability("Fast Coding", 100)
    # armor = Armor("Firewall", 100)
    # armor2 = Armor("Pythonic", 70)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(ability2)
    # hero.add_armor(armor)
    # hero.add_armor(armor2)
    # print(hero.attack())
    # print(hero.defend())
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 500)
    ability4 = Ability("Wizard Beard", 200)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
