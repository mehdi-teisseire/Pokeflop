from pygame import time
class Battle:
    """Battle class for managing Pokémon battles"""
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
        self.damage = 0
        self.applied_damage = False
        self.miss_check = False
        self.has_missed = False

        
    def finish_turn(self, game):  
        self.chosen_moov = ''
        self.damage = 0
        self.applied_damage = False
        self.miss_check = False

        if self.opponent_pokemon_ko():
            self.custom_wait(game, "pokemon_ko", 2000)
        else:
            self.custom_wait(game, "attacking", 1500)
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
    

    def opponent_pokemon_ko(self):
        """To check if Pokemon is alive or not"""
        if self.enemy_current_hp <= 0 or self.trainer_current_hp <= 0:
            return True
        return False
    
    def end_results(self, game):
        if self.trainer_current_hp <= 0:
            self.has_won = False

            game.button_battle_message.draw(game.screen)
            game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
            game.text_battle_message.draw(game.screen, f"Too bad, {self.trainer_name}'s {self.trainer_pokemon} had been defeated by {self.enemy_name}'s {self.enemy_pokemon}!!" ,hitbox=game.button_battle_message)
    
            game.enemy.remove_pokemon()
        else:
            self.has_won = True

            game.button_battle_message.draw(game.screen)
            game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
            game.text_battle_message.draw(game.screen, f"Good job, {self.trainer_name}'s {self.trainer_pokemon} had defeated {self.enemy_name}'s {self.enemy_pokemon}!!" ,hitbox=game.button_battle_message)
    
            self.gave_pokemon = game.enemy.give_pokemon(game.trainer)

        game.battle_start = False

        game.delay = time.get_ticks() + 5000
        game.game_state = "battle_end"

    def custom_wait(self, game, state, wait_time = 1000):
        if time.get_ticks() >= game.delay:
            game.delay = time.get_ticks() + wait_time
            game.ingame_state = state
