from random import randint, choice
from model.multiplier import type_multiplier
from model.TrainerClass import Trainer
from model.EnemyTrainerClass import EnemyTrainer
from model.pokemon import Pokemon
# from utils import Button



#Battle class for managing Pokémon battles
class Battle:
    def __init__(self, trainer, enemy):
        self.trainer_name = trainer.name
        self.enemy_name = enemy.name
        self.trainer_pokemon = trainer.pokedex[0]
        self.enemy_pokemon = enemy.pokedex[0]

        self.turn = self.trainer_name
        self.opponent = self.enemy_name
        self.turn_pkmn = self.trainer_pokemon
        self.opponent_pkmn = self.enemy_pokemon

        self.chosen_move = "" #would be a return from the button with the move name
        

    def change_turn(self):
        if self.turn == self.trainer_name:
            self.turn = self.enemy_name
            self.turn_pkmn = self.enemy_pokemon
        else:
            self.turn = self.trainer_name
            self.turn_pkmn = self.trainer_pokemon
    
    def choose_move(self, move):
        if self.turn == self.enemy_name:
            return choice([self.turn_pkmn.moove1, self.turn_pkmn.moove2]) 
        else:
            return move     

    # To check if Pokemon is alive or not
    def check_health_points(self):
        if self.turn_pkmn.life <= 0:
            return False
        return True
    



            

