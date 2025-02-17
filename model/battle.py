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
        self.turn_pkmn = self.trainer_pokemon

        self.opponent = self.enemy_name
        self.opponent_pkmn = self.enemy_pokemon

        self.chosen_moov = ""
        
    def finish_turn(self, game):        

        #TODO make it so the display can keep up (should check after the display)
        if self.opponent_pokemon_ko():
            print("Battle Finished! Return to main menu")
            game.enemy.give_pokemon(game.trainer)
            # pygame.time.wait(1000)
            game.battle_start = False
            game.game_state = "game_menu"
        
        #TODO make it so the display can keep up (change turn should happen after the display, not here)
        
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
        if self.opponent_pkmn.life <= 0:
            return True
        return False
    



            

