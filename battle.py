import json



#Battle class for managing Pokémon battles
class Battle:
    def __init__(self, player_1_pokemons, player_2_pokemons):
        self.player_1_pokemons = player_1_pokemons
        self.player_2_pokemons = player_2_pokemons
        self.current_pokemon_1 = player_1_pokemons[0]
        self.current_pokemon_2 = player_2_pokemons[0]
        self.pokedex = self.load_pokedex()
    
    # To load the Pokedex
    def load_pokedex(self):
        try:
            with open('pokedex.json', 'r') as file:
                return json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            return[]

    # To save to the Pokedex
    def save_pokedex(self):
        with open('pokedex.json', 'r') as file:
            json.dump(self.pokedex, file)
    
    