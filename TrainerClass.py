from JsonClass import Json


class Trainer(Json):
    """Class for trainers (player) with Pokedex list as owned pokemon, stats for stat menu"""
    def __init__(self, name):
        self.name = name
        #self.image = image
        self.victory = False
        self.pokedex = [] # Only contain Objects
        self.stats = []

    def add_pokemon(self, pokemon):
        """To add a pokemon after a win. Also called on the first pokemon the player get"""
        self.pokedex.append(pokemon)
        self.update_json()

    def remove_pokemon(self, pokemon):
        """To remove defeated pokemon from our pokedex. pokemon is an object"""
        self.pokedex.remove(pokemon)
        self.update_json()


    def update_json(self):
        """Update the json from the pokedex list"""
        self.save_json(self.pokedex, "pokedex")

    def load_pokedex(self):
        """When loading a save, add all saved pokemon on trainer object"""
        pokedex = self.load_json("pokedex")
        for pokemon in pokedex:
            self.pokedex.append(Pokemon(pokemon["name"], pokemon["stat"]))

    def check_if_owned(self, pokemon):
        for pokemon_pokedex in self.pokedex:
            if pokemon_pokedex.name == pokemon.name:
                return True
        return False


class Pokemon(Json):
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat

"""
Json.save_json(pokemon_list, pokemon_list, "pokemon")
pokemon_list.append(Json.load_json(pokemon_list, "pokemon"))

print(pokemon_list)



choosed_pokemon = "Bulbosaur"



for pokemon in pokemon_list:
    try:
        if pokemon["name"] == choosed_pokemon:
            already_owned = check_if_owned(pokemon)
            if not already_owned:
                new_pokemon = Pokemon(pokemon["name"], pokemon["stats"])
                trainer1.add_pokemon(new_pokemon)
                break
    except Exception:
        print("No pokemon in the list!")



print(trainer1.pokedex)
print(trainer1.pokedex[0].name)
"""

"""
pokedex.json    ->  List[dict]  ->  object  -> pokedex_list ->  list[dict]  -> pokedex.json
                                                            ->  display(object)

pokemon.json    ->  List[dict]  ->  pokemon_list    ->  rand(pokemon)   ->  object  ->  enemytrainer_list
"""


