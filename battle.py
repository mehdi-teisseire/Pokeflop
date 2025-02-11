import json
import random
import pygame
import sys
from pokemon import Pokemon
from multiplier import type_multiplier
from utils import Button, render_message



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
        if self.current_pokemon_1.hp <= 0:
            return self.current_pokemon_1.name, self.current_pokemon_2.name
        elif self.current_pokemon_2 <= 0:
            return self.current_pokemon_1.name, self.current_pokemon_2.name
        return None, None  

    # To allow the player to choose an attack
    def choose_attack(screen, self, pokemon):
        button1 = Button(pokemon.moov1, 100, 300, 200, 50) # should be changed
        button2 = Button(pokemon.moov2, 400, 300, 200, 50) # should be changed
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button1.is_clicked(mouse_pos):
                        return pokemon.moov1, pokemon.moove_type_1
                    elif button2.is_clicked(mouse_pos):
                        return pokemon.moov2, pokemon.moove_type_2
            screen.fill(Button.WHITE)
            option_text = self.font.render(f"{pokemon.name}, choose your attack:", True, self.BLUE) # Should be changed
            instruction_line1 = self.font.render("Press 1 :" + pokemon.moov1, True, self.BLUE) # Should be changed
            instruction_line2 = self.font.render("Press 2 :" + pokemon.moov2, True, self.BLUE) # Should be changed

            screen.blit(option_text, (100, 200))
            screen.blit(instruction_line1, (100, 250))
            screen.blit(instruction_line2 (100, 280))

            button1.draw(screen)
            button2.draw(screen)
            pygame.display.flip()
            
    # To calculate damage based on the attacker's chosen move
    def calculate_damage(self, attacker, defender, move_type, screen, font):
        if random.random() < 0.1:
            message = f"{attacker.name}'s attack missed!"
            render_message(screen, message, font)
            return 0  
        damage = attacker.attack
        multiplier = type_multiplier.get((move_type, defender.pkm_type), 1)
        effective_damage = damage * multiplier
        defender.take_damage(effective_damage)

        message = f"{attacker.name} dealt {effective_damage} damage!"
        render_message(screen, message, font)
        return effective_damage 

    # To display the defeat
    def display_defeat(self, pokemon, screen, font):
        message = f"{pokemon.name} has been defeated."
        render_message(screen, message, font)
        self.pokedex = [p for p in self.pokedex if p['name'] != pokemon.name]  # Retirer le Pokémon du Pokédex
        self.save_pokedex()

    # To display the victory
    def display_victory(self, pokemon, screen, font):
        message = f"{pokemon.name} is victorious!"
        render_message(screen, message, font)
        pokemon.level_up() 