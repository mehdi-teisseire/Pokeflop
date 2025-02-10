from JsonClass import Json


class Trainers(Json):
    """Class for trainers (player and foes) with Pokedex list as owned pokemon, stats for stat menu"""
    def __init__(self, name):
        self.name = name
        #self.image = image
        self.victory = False
        self.pokedex = [] 
        self.stats = []

    def add_pokemon(self, pokemon):
        """To add a pokemon after a win. Also called on the first pokemon the player get"""
        self.pokedex.append(pokemon)
        self.update_pokedex_json()

    def remove_pokemon(self, pokemon):
        """To remove defeated pokemon from pour pokedex"""
        self.pokedex.remove(pokemon)
        self.update_pokedex_json()


    def update_pokedex_json(self):
        """Update the json and the pokedex list"""
        self.save_json(self.pokedex)
        self.pokedex = self.load_json()

trainer1 = Trainers("George")

class Pokemon:
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat

pokemon1 = Pokemon("aaaa", [1,2,3])

trainer1.add_pokemon(pokemon1)

print(trainer1.pokedex)