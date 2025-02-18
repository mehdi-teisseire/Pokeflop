from random import randint, choice
from model.multiplier import type_multiplier
from model.TrainerClass import Trainer
from model.EnemyTrainerClass import EnemyTrainer
from model.pokemon import Pokemon

import pygame
# from utils import Button



#Battle class for managing Pokémon battles
class Battle:
    def __init__(self, trainer, enemy):
        self.trainer_name = trainer.name
        self.trainer_pokemon = trainer.pokedex[0]
        self.trainer_current_hp = trainer.pokedex[0].life

        self.enemy_name = enemy.name
        self.enemy_pokemon = enemy.pokedex[0]
        self.enemy_current_hp = enemy.pokedex[0].life

        self.turn = self.trainer_name
        self.turn_pkmn = self.trainer_pokemon

        self.opponent = self.enemy_name
        self.opponent_pkmn = self.enemy_pokemon

        self.chosen_moov = ""
        
    def finish_turn(self, game):        
        if self.opponent_pokemon_ko():
            print("Battle Finished!")
            if self.trainer_current_hp <= 0:
                print("You Lose!!")
            else:
                print("You Win!!")
                gave_pokemon = game.enemy.give_pokemon(game.trainer)
                if gave_pokemon:
                    print(f"{self.enemy_name} gave you a {self.enemy_pokemon.name}!! So cool!")
                else:
                    print(f"{self.enemy_name} gave you a {self.enemy_pokemon.name}!! Unfortunately, you already had one...")
            # pygame.time.wait(1000)
            pygame.time.get_ticks() + 1000

            game.battle_start = False
            game.game_state = "game_menu"
                
        game.battle.chosen_moov = ''
        self.change_turn()


    def change_turn(self):
        if self.turn == self.trainer_name:
            self.turn = self.enemy_name
            self.turn_pkmn = self.enemy_pokemon

            self.opponent = self.trainer_name
            self.opponent_pkmn = self.trainer_pokemon

        else:
            self.turn = self.trainer_name
            self.turn_pkmn = self.trainer_pokemon

            self.opponent = self.enemy_name
            self.opponent_pkmn = self.enemy_pokemon 
        
    def ia_choose_moov(self, game):
        moov1_dmg = self.turn_pkmn.attack_damage(game.battle.opponent_pkmn, self.turn_pkmn.moov[0].type)
        moov2_dmg = self.turn_pkmn.attack_damage(game.battle.opponent_pkmn, self.turn_pkmn.moov[1].type)
        if moov1_dmg < moov2_dmg:
            return self.turn_pkmn.moov[1]
        else:
            return self.turn_pkmn.moov[0]
    

    # To check if Pokemon is alive or not
    def opponent_pokemon_ko(self):
        if self.enemy_current_hp <= 0 or self.trainer_current_hp <= 0:
            return True
        return False
    



            

