from back_end.pokemon import Pokemon
from back_end.multiplier import type_multiplier
# from utils import Button



#Battle class for managing Pokémon battles
class Battle:
    def __init__(self, trainer, enemy):
        self.trainer_pokemon = trainer.pokedex[0]
        self.enemy_pokemon = enemy.pokedex[0]
    
    # To check if Pokemon is alive or not
    def check_health_points(self):
        if self.trainer_pokemon.hp <= 0:
            return self.trainer_pokemon.name, self.enemy_pokemon.name
        elif self.current_pokemon_2 <= 0:
            return self.trainer_pokemon.name, self.enemy_pokemon.name
        return None, None  
    



            

