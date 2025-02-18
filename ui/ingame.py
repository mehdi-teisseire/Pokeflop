def display_ingame(game):
    display_background(game)
    display_battle_interface(game)
    if game.battle.chosen_moov:
        display_attacking_text(game)
        #TODO from here, refractor to the minimum (remove "game." and keep "battle"?)
        if game.battle.turn_pkmn.has_missed(game.battle.chosen_moov):
            display_moov_missed_text(game)
        else:
            damage = game.battle.turn_pkmn.attack_damage(game.battle.opponent_pkmn, game.battle.chosen_moov.type)
            display_moov_animation(game)
            game.battle.turn_pkmn.apply_damage(game, damage)
            display_damage_text(game, damage)
        game.battle.finish_turn(game)

    else:
        if game.battle.turn == game.enemy.name:
            game.battle.chosen_moov = game.battle.ia_choose_moov(game)
            display_enemy_choosing_move(game)
        else:
            display_attack_choice(game)

def display_background(game):
    game.background.image_path = "media/ui-elements/MDPokemonBattle_Notextbox.png"
    game.background.draw(game)

def display_battle_interface(game):
    game.life_trainer_text.draw(game, f"{game.battle.trainer_current_hp}/{game.trainer.pokedex[0].life}") #TODO change "100" to "trainer.pokemon[0].max_life"
    game.life_opponent_text.draw(game, f"{game.battle.enemy_current_hp}/{game.enemy.pokedex[0].life}") #TODO change "100" to "enemy.pokemon[0].max_life"

def display_enemy_choosing_move(game):
    """Display a message to let AI play without interferences"""
    game.battle.chosen_moov = game.battle.ia_choose_moov(game)
    # print("enemy is choosing move") #TODO placeholder for enemy message when acting


# To allow the player to choose an attack
def display_attack_choice(game):
    """Show the moov buttons and allow to choose an attack"""
    game.background_button_moov1.draw(game)
    game.background_button_moov2.draw(game)

    game.text_button_moov1.draw(game, game.trainer.pokedex[0].moov[0].name, game.background_button_moov1)    
    game.text_button_moov2.draw(game, game.trainer.pokedex[0].moov[1].name, game.background_button_moov2)

    game.button_moov1.label = game.trainer.pokedex[0].moov[0].name
    game.button_moov2.label = game.trainer.pokedex[0].moov[1].name
    game.button_moov1.draw(game.screen, game.background_button_moov1)
    game.button_moov2.draw(game.screen, game.background_button_moov2)

def display_attacking_text(game):
    #TODO text for attacking text (pokemon uses move)
    print(f"{game.battle.turn}'s {game.battle.turn_pkmn.name} uses {game.battle.chosen_moov.name}!!")

def display_moov_animation(game):
    #TODO placeholder/test for animation
    print("Mooving!")
    print("Finished mooving!")
    
def display_damage_text(game, damage):
    #TODO placeholder for damage text
    print(f"{game.battle.turn}'s {game.battle.turn_pkmn.name} has inflicted {damage} damage to {game.battle.opponent_pkmn.name}!")

def display_moov_missed_text(game):
    #TODO placeholder for miss text
    print(f"{game.battle.chosen_moov.name} has missed!!")
