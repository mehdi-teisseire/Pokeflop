from pygame import time
class Battle:
    """Battle class for managing Pokémon battles"""
    def __init__(self, trainer, enemy):
        self.trainer_name = trainer.name
        self.trainer_pokemon = trainer.pokedex[0]
        # self.trainer_current_hp = self.trainer_pokemon.life

        self.enemy_name = enemy.name
        self.enemy_pokemon = enemy.pokedex[0]
        # self.enemy_current_hp = self.enemy_pokemon.life

        self.turn = self.trainer_name
        self.turn_pkmn = self.trainer_pokemon

        self.opponent = self.enemy_name
        self.opponent_pkmn = self.enemy_pokemon

        self.chosen_moov = ""
        self.damage = 0
        self.applied_damage = False
        self.miss_check = False
        self.pokemon_missed = False

        
    def finish_turn(self, game):  
        self.chosen_moov = ''
        self.damage = 0
        self.applied_damage = False
        self.miss_check = False
        self.pokemon_ko = self.is_pokemon_ko()

        game.rival.draw(game.screen, (1050,150), (85,150), "media/ui-elements/Rival_stand.png")

        game.button_battle_message.draw(game.screen)
        game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
    

        if self.pokemon_ko:
            # if time.get_ticks() >= game.delay:
            game.delay = time.get_ticks() + 2000
            game.ingame_state = "pokemon_ko"
        else:
            # if time.get_ticks() >= game.delay:
            game.delay = time.get_ticks() + 1500
            game.ingame_state = "attacking"
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
    

    def is_pokemon_ko(self):
        """To check if Pokemon is alive or not"""
        if self.enemy_pokemon.current_health <= 0:
            self.won = True
            return self.enemy_name
        elif self.trainer_pokemon.current_health <= 0:        # elif self.trainer_current_hp <= 0:
            self.won = False
            return self.trainer_name
        else:
            return False
    

