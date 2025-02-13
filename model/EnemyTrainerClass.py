from TrainerClass import Trainer

class EnemyTrainer(Trainer):
    def __init__(self, name):
        super().__init__(name)
        self.pokemon = [] # List of possible pokemon enemy can choose from 

    def add_pokemon(self, pokemon):
        """To add a pokemon after a win. Also called on the first pokemon the player get"""
        self.pokedex.append(pokemon)

    def remove_pokemon(self, pokemon):
        """To remove defeated pokemon from our pokedex. pokemon is an object"""
        self.pokedex.remove(pokemon)

# Add "if hp <= 0" and "if not already_owned" before this when you call it
    def give_pokemon(self, trainer):
        """Copy itself to trainer pokedex and get removed."""
        already_owned = trainer.check_if_owned(self.pokedex[0])
        if not already_owned:
            trainer.add_pokemon(self.pokedex[0])
        self.remove_pokemon(self.pokedex[0])

"""
class Pokemon(Json):
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat


# Pokemon pool and list will contain Dict (from there, it'll create object for pokedex)
POKEMON_DB = [{"name": "Bulbosaur", "stats": [1,2,3]}, {"name": "Squirtle", "stats": [3,2,1]}, {"name": "Charizard", "stats": [2,1,3]}]
pokemon_list = [{"name": "Squirtle", "stats": [3,2,1]}]


trainer1 = Trainer("George")
enemy1 = EnemyTrainer("Gorgeorge")

trainer1.load_pokedex()

enemy1.add_pokemon(Pokemon(pokemon_list[0]["name"], pokemon_list[0]["stats"]))
try:
    print(f"enemy: {enemy1.pokedex}")
    print(f"player: {trainer1.pokedex}")
except Exception:
    pass
if enemy1.pokedex[0].name == "Squirtle":
    enemy1.give_pokemon(trainer1)
try:
    print(f"enemy: {enemy1.pokedex}")
    print(f"player: {trainer1.pokedex}")
except Exception:
    pass
"""

