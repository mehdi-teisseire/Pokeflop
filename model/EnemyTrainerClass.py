from model.TrainerClass import Trainer
from model.pokemon import Pokemon

class EnemyTrainer(Trainer):
    def __init__(self, name):
        super().__init__(name)
        self.pokemon = [] # List of possible pokemon enemy can choose from 


    def add_pokemon_to_list(self, pokemon_template):
        """To add a pokemon from the template to pokemon list."""
        self.pokemon.append(pokemon_template[0])
        self.update_json()

    def remove_pokemon_to_list(self, pokemon_template):
        """To remove a pokemon from the pokemon list."""
        self.pokemon.remove(pokemon_template[0]) 
        self.update_json()
        
    def choose_pokemon(self):
        """Choose a pokemon from the pokemon_list and add it to battle"""
        pokemon = self.pokemon[0]
        self.pokedex.append(self.convert_pokemon_to_obj(pokemon)) # Will make it random

    def remove_pokemon(self):
        """To remove defeated pokemon from our pokedex. pokemon is an object"""
        self.pokedex.remove(self.pokedex[0])

# Add "if hp <= 0" and "if not already_owned" before this when you call it
    def give_pokemon(self, trainer):
        """Copy itself to trainer pokedex and get removed."""
        if not trainer.already_owned(self.pokedex[0]):
            trainer.add_pokemon(self.pokedex[0])
        self.remove_pokemon()

    def update_json(self):
        """Update the json from the pokedex list"""
        self.save_json(self.pokemon, "pokemon")

    def ia_choose_move(self, game):
        moov1_dmg = self.pokedex[0].attack_damage(game.battle.opponent_pkmn, self.pokedex[0].moov_type_1)
        moov2_dmg = self.pokedex[0].attack_damage(game.battle.opponent_pkmn, self.pokedex[0].moov_type_2)
        if moov1_dmg < moov2_dmg:
            return self.pokedex[0].moov2
        else:
            return self.pokedex[0].moov1

"""

# Pokemon pool and list will contain Dict (from there, it'll create object for pokedex)
POKEMON_DB = [{"name": "Bulbosaur", "stats": [1,2,3]}, {"name": "Squirtle", "stats": [3,2,1]}, {"name": "Charizard", "stats": [2,1,3]}]
pokemon_list = [{"name": "Squirtle", "stats": [3,2,1]}]


"""

