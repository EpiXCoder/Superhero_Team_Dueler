import random

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        #1) randomly choose winner,
        # Hint: Look into random library, more specifically the choice method
        duelers=[self.name, opponent.name]
        winner = random.choice(duelers)
        duelers.remove(winner)
        loser = duelers[0]    
        print(f'{winner} defeats {loser}!')


if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    hero1.fight(hero2)
