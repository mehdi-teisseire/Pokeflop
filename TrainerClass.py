from JsonClass import Json


class Trainer(Json):
    """Class for trainers (player) with Pokedex list as owned pokemon, stats for stat menu"""
    def __init__(self, name):
        self.name = name
        #self.image = image
        self.victory = False
        self.pokedex = [] 
        self.stats = []

    def add_pokemon(self, pokemon):
        """To add a pokemon after a win. Also called on the first pokemon the player get"""
        self.pokedex.append(pokemon)
        self.update_json()

    def remove_pokemon(self, pokemon):
        """To remove defeated pokemon from our pokedex"""
        self.pokedex.remove(pokemon)
        self.update_json()


    def update_json(self):
        """Update the json from the pokedex list"""
        self.save_json(self.pokedex, "pokedex")

    def load_pokedex(self):
        """When loading a save, add all saved pokemon on trainer object"""
        pokedex = self.load_json("pokedex")
        for pokemon in pokedex:
            self.pokedex.append(Pokemon(pokedex["name"], pokedex["stats"]))

trainer1 = Trainer("George")

class Pokemon(Json):
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat

    def remove_pokemon(self, pokemon):
        """To remove defeated pokemon from our pokedex"""
        self.pokedex.remove(pokemon)
        self.update_json()

        
    def update_json(self, pokemon_list):
        """Update the json from the pokemon list"""
        self.save_json(pokemon_list, "pokemon")


pokemon1 = Pokemon("Bulbosaur", [1,2,3])
pokemon2 = Pokemon("Squirtle", [3,2,1])

trainer1.add_pokemon(pokemon1)
trainer1.add_pokemon(pokemon2)

print(trainer1.pokedex)

print(type(trainer1.load_json("pokedex")))
print(type(trainer1.load_json("pokedex")[0]))
print(trainer1.load_json("pokedex"))

