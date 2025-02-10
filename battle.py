



#Battle class for managing Pokémon battles
class Battle:
    def __init__(self, player_1_pokemons, player_2_pokemons):
        self.player_1_pokemons = player_1_pokemons
        self.player_2_pokemons = player_2_pokemons
        self.current_pokemon_1 = player_1_pokemons[0]
        self.current_pokemon_2 = player_2_pokemons[0]
        self.pokedex = self.load_pokedex()