import json
import random
from pokemon import *
from multiplier import type_multiplier



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
    
    # To check if Pokemon is alive or not
    def check_health_points(self):
        if self.current_pokemon_1.life <= 0:
            return self.current_pokemon_1.name, self.current_pokemon_2.name
        elif self.current_pokemon_2.life <= 0:
            return self.current_pokemon_2.name, self.current_pokemon_1.name
        return None, None  
            
    # To calculate damage based on the attacker's chosen move
    def calculate_damage(self, attacker, defender, move_type):
        if random.random() < 0.1:
            return 0  
        damage = attacker.attack
        multiplier = type_multiplier.get((move_type, defender.pkm_type), 1)
        effective_damage = damage * multiplier
        defender.take_damage(effective_damage)
        return effective_damage 

    # To display the defeat
    def display_defeat(self, pokemon):
        self.pokedex = [p for p in self.pokedex if p['name'] != pokemon.name]  # Retirer le Pokémon du Pokédex
        self.save_pokedex()

    # To display the victory
    def display_victory(self, pokemon):
        pokemon.level_up() 
    
    # To change the active pokemon in the battle
    def switch_pokemon(self, new_pokemon):
        if new_pokemon in self.player_1_pokemons:
            self.current_pokemon_1 = new_pokemon
        elif new_pokemon in self.player_2_pokemons:
            self.current_pokemon_2 = new_pokemon

    # To Start the battle
    def start_battle(self):
        turn = 0
        while self.current_pokemon_1.life > 0 and self.current_pokemon_2.life > 0:
            if turn % 2 == 0:
                attacker = self.current_pokemon_1
                defender = self.current_pokemon_2
            else:
                attacker = self.current_pokemon_2
                defender = self.current_pokemon_1

            move, move_type = self.choose_attack(attacker)
            damage = self.calculate_damage(attacker, defender, move_type)
            defender.life -= damage  

            winner_name, loser_name = self.check_health_points()
            if winner_name:
                return winner_name, move, damage, loser_name

            turn += 1