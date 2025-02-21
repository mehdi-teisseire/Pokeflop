from model.pokemon import Pokemon
from model.JsonClass import Json

class Trainer(Json):
    """Class for trainers (player) with Pokedex list as owned pokemon, stats for stat menu"""
    def __init__(self, name):
        self.name = name
        #self.image = image
        self.pokemon = [] # List of possible pokemon enemy can choose from 
        self.pokedex = [] # Only contain Objects
        self.stats = []

    def give_first_pokemon(self, pokemon):
        if not self.pokedex:
            self.add_pokemon(self.convert_pokemon_to_obj(pokemon))

    def add_pokemon(self, pokemon):
        """To add a pokemon when player doesn't have one."""
        self.pokedex.append(pokemon)
        self.update_json()

    def remove_pokemon(self, pokemon):
        """To remove defeated pokemon from our pokedex. pokemon is an object.
        Won't remove if it's the last pokemon."""
           
        self.pokedex.remove(pokemon)
        self.update_json()

    def convert_pokemon_to_obj(self, pokemon):
        return Pokemon(name=pokemon["name"], type=pokemon["type"],
                       attack=pokemon["attack"], defence=pokemon["defence"],
                       moov=pokemon["moov"], level=pokemon["level"],
                       life=pokemon["life"], ingame=pokemon['ingame'],
                       evolve_data=pokemon["evolve_data"])

    def update_json(self):
        """Update the json from the pokedex list"""
        self.save_json(self.pokedex, "pokedex")

    def load_pokedex(self):
        """When loading a save, add all saved pokemon on trainer object"""
        pokedex = self.load_json("pokedex")
        for pokemon in pokedex:
            self.pokedex.append(self.convert_pokemon_to_obj(pokemon))

    def already_owned(self, pokemon):
        for pokemon_pokedex in self.pokedex:
            if pokemon_pokedex.name == pokemon.name:
                return True
        return False


