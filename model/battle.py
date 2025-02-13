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

        self.choosed_move = self.choose_move() #would be a return from the button with the move name
        

    def change_turn(self):
        if self.turn == self.trainer_name:
            self.turn = self.enemy_name
            self.turn_pkmn = self.enemy_pokemon
        else:
            self.turn = self.trainer_name
            self.turn_pkmn = self.trainer_pokemon
    
    def choose_move(self):
        if self.turn == self.enemy_name:
            return choice([self.turn_pkmn.moove1, self.turn_pkmn.moove2]) 
        else:
            return self.turn_pkmn.moove1


    def get_moove_accuracy(self):
        match self.choosed_move:
            case self.turn_pkmn.moove1:
                return self.turn_pkmn.accuracy_mouv1
            case self.turn_pkmn.moov2:
                return self.turn_pkmn.accuracy_mouv2

    def has_missed(self):
        '''Get the accuracy of a moove'''
        random_nb = randint(0,100)
        accuracy = self.get_moove_accuracy()
        if accuracy < random_nb:
            return True
        else:
            return False
        # return f"{self.moov1} has an accuracy of {self.accuracy_mouv1} and {self.moov2} has an accuracy of {self.accuracy_mouv2}"
    
    def attack_damage(self):
        '''Calculate the damage of an attack. Multi = multiplier for types (type weakness)'''
        multi = type_multiplier[(self.turn_pkmn.pkmn_type, self.opponent_pkmn.pkmn_type)]
        damage = (self.turn_pkmn.attack * self.turn_pkmn.level * 0.2 - self.opponent_pkmn.defence * self.opponent_pkmn.level * 0.05) * multi
        self.opponent_pkmn.life -= damage
        return damage
        # return f"{self.name} has inflicted {damage} damage to {opponent.name}!"          

    # To check if Pokemon is alive or not
    def check_health_points(self):
        if self.turn_pkmn.life <= 0:
            return False
        return True
    



            

