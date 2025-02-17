from model.pokemon import Pokemon
from model.JsonClass import Json

class Trainer(Json):
    """Class for trainers (player) with Pokedex list as owned pokemon, stats for stat menu"""
    def __init__(self, name):
        self.name = name
        #self.image = image
        self.victory = False
        self.pokemon = [] # List of possible pokemon enemy can choose from 
        self.pokedex = [] # Only contain Objects
        self.stats = []

    def give_first_pokemon(self, pkmn_list, moov_list):
        #TODO change to adapt for first pokemon choice
        if not self.pokedex:
            self.add_pokemon(self.convert_pokemon_to_obj(pkmn_list[0], moov_list))

    def add_pokemon(self, pokemon):
        """To add a pokemon when player doesn't have one."""
        if not self.already_owned(pokemon):
            self.pokedex.append(pokemon)
            self.update_json()

    def remove_pokemon(self, pokemon):
        """To remove defeated pokemon from our pokedex. pokemon is an object"""
        self.pokedex.remove(pokemon)
        self.update_json()

    def convert_pokemon_to_obj(self, pokemon, moov_list):
        return Pokemon(name=pokemon["name"], sprite=pokemon["sprite"], type=pokemon["type"],
                       attack=pokemon["attack"], defence=pokemon["defence"],
                       moov1=pokemon["moov"][0], moov2=pokemon["moov"][1], moov_list=moov_list,
                       life=pokemon["life"])

    def update_json(self):
        """Update the json from the pokedex list"""
        self.save_json(self.pokedex, "pokedex")

    def load_pokedex(self, moov_list):
        """When loading a save, add all saved pokemon on trainer object"""
        pokedex = self.load_json("pokedex")
        for pokemon in pokedex:
            self.pokedex.append(self.convert_pokemon_to_obj(pokemon, moov_list))

    def already_owned(self, pokemon):
        for pokemon_pokedex in self.pokedex:
            if pokemon_pokedex.name == pokemon.name:
                return True
        return False

"""

#check if owned but for list (obsolete)
for pokemon in pokemon_list:
    try:
        if pokemon["name"] == chosen_pokemon:
            already_owned = check_if_owned(pokemon)
            if not already_owned:
                new_pokemon = Pokemon(pokemon["name"], pokemon["stats"])
                trainer1.add_pokemon(new_pokemon)
                break
    except Exception:
        print("No pokemon in the list!")


"""

"""
pokedex.json    ->  List[dict]  ->  object  -> pokedex_list ->  list[dict]  -> pokedex.json
                                                            ->  display(object)

pokemon.json    ->  List[dict]  ->  pokemon_list    ->  rand(pokemon)   ->  object  ->  enemytrainer_list
"""


