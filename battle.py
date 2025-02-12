import json
import random
import pygame
from pokemon import *
from multiplier import type_multiplier
from utils import *
from game_ui import GameUI



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

    # To allow the player to choose an attack
    def choose_attack(self, screen, font):
        button1 = Button(pokemon.moov1, 100, 300, 200, 50) # should be changed
        button2 = Button(pokemon.moov2, 400, 300, 200, 50) # should be changed
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button1.is_clicked(mouse_pos):
                        return pokemon.moov1, pokemon.moove_type_1
                    elif button2.is_clicked(mouse_pos):
                        return pokemon.moov2, pokemon.moove_type_2
            screen.fill(Button.WHITE)
            render_message(screen, font, f"{pokemon.name}, choose your attack!")
            render_message(screen, font, "Press 1 :" + pokemon.moov1)
            render_message(screen, font,"Press 2 :" + pokemon.moov2)

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
    
    # To change the active pokemon in the battle
    def switch_pokemon(self, new_pokemon, screen, font):
        if new_pokemon in self.player_1_pokemons:
            self.current_pokemon_1 = new_pokemon
            message = f"{self.current_pokemon_1.name} is now active for Player 1."
            render_message(screen, message, font)
        elif new_pokemon in self.player_2_pokemons:
            self.current_pokemon_2 = new_pokemon
            message = f"{self.current_pokemon_2.name} is now active for Player 2."
            render_message(screen, message, font)
        else:
            message = f"The chosen Pokémon is not part of the player's team."
            render_message(screen, message, font)  

    # A button to surrender 
    def surrender(self, screen, pokemon, font, player):
        surrender_button = Button("Surrender", 250, 300, 200, 50)
        screen.fill(Button.WHITE)
        surrender_button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if surrender_button.is_clicked(mouse_pos):
                    message = f"{pokemon.name} has surrendered !"  
                    render_message(screen, message, font)
                    winner = self.current_pokemon_2.name if player == self.current_pokemon_1 else self.current_pokemon_1.name 
                    message = f"{winner} wins by default!"
                    return         

    # To start the battle
    def start_battle(self, screen, font):
        ui = GameUI(screen)
        ui.clear_screen()
        ui.draw_text("A wild Pokémon appeared!")
        pygame.display.flip()
        pygame.time.delay(2000)
        turn = 0
        while self.current_pokemon_1.life > 0 and self.current_pokemon_2.life > 0:
            if turn % 2 == 0:
                move, move_type = self.choose_attack(screen, self.current_pokemon_1)
                damage = self.calculate_damage(self.current_pokemon_1, self.current_pokemon_2, move_type, screen, self.font)
                message = f"{self.current_pokemon_1.name} uses {move} on {self.current_pokemon_2.name} and inflicts {damage} damage."
                render_message(screen, message, font)
            else:
                move, move_type = self.choose_attack(screen, self.current_pokemon_2)
                damage = self.calculate_damage(self.current_pokemon_2, self.current_pokemon_1, move_type, screen, self.font)
                message = f" {self.current_pokemon_2.name} uses {move} on {self.current_pokemon_1.name} and inflicts {damage} damage."
                render_message(screen, message, font)

            winner_name, loser_name = self.check_health_points()
            if winner_name:
                message = f"{winner_name} won the battle against {loser_name}!"
                render_message(screen, message, font)
                self.display_victory(self.current_pokemon_1 if winner_name == self.current_pokemon_1 else self.current_pokemon_2, screen, self.font)
                return

            turn += 1                            