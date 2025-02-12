from utils import *

class BattleMessages:
    def __init__(self, attacker, pokemon, current_pokemon_1, current_pokemon_2):
        self.attacker = attacker
        self.pokemon = pokemon
        self.current_pokemon_1 = current_pokemon_1
        self.current_pokemon_2 = current_pokemon_2

    def attack_missed_msg(self, screen, font):
        message = f"{self.attacker.name}'s attack missed!"
        self.render_message(screen, message, font)

    def attack_dealt_msg(self, screen, font, effective_damage):
        message = f"{self.attacker.name} dealt {effective_damage} damage!"
        self.render_message(screen, message, font)

    def display_defeat_msg(self, screen, font):
        message = f"{self.pokemon.name} has been defeated."
        self.render_message(screen, message, font)

    def display_victory_msg(self, screen, font):
        message = f"{self.pokemon.name} is victorious!"
        self.render_message(screen, message, font)

    def switch_pokemon_msg(self, screen, font):
        message = f"{self.current_pokemon_1.name} is now active for Player 1."
        self.render_message(screen, message, font)

    def switch_pokemon_msg_two(self, screen, font):
        message = f"{self.current_pokemon_2.name} is now active for Player 2."
        self.render_message(screen, message, font)

    def switch_pokemon_msg_three(self, screen, font):
        message = f"The chosen Pokémon is not part of the player's team."
        self.render_message(screen, message, font)

    def start_battle_mess_one(self, screen, font, move, damage):
        message = f"{self.current_pokemon_1.name} uses {move} on {self.current_pokemon_2.name} and inflicts {damage} damage."
        self.render_message(screen, message, font)

    def start_battle_mess_two(self, screen, font, move, damage):
        message = f"{self.current_pokemon_2.name} uses {move} on {self.current_pokemon_1.name} and inflicts {damage} damage."
        self.render_message(screen, message, font)

    def start_battle_mess_three(self, screen, font, winner_name, loser_name):
        message = f"{winner_name} won the battle against {loser_name}!"
        self.render_message(screen, message, font)

