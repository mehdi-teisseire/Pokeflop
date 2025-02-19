from pygame import time

def display_ingame(game):
    display_background(game)
    display_battle_interface(game)

    match game.ingame_state:
        case "attacking":
            if game.battle.chosen_moov:
                display_attacking_text(game)
            else:
                if game.battle.turn == game.battle.enemy_name:
                    display_enemy_choosing_move(game)
                else:
                    display_attack_choice(game)
        case "mooving":
            if not game.battle.miss_check:
                game.battle.has_missed = game.battle.turn_pkmn.has_missed(game.battle.chosen_moov)
                game.battle.miss_check = True
            if game.battle.has_missed:
                display_moov_missed_text(game)
            else:
                if not game.battle.damage:
                    game.battle.damage = game.battle.turn_pkmn.attack_damage(game.battle.opponent_pkmn, game.battle.chosen_moov.type)
                display_moov_animation(game)
        case "damage":
            if not game.battle.applied_damage:
                game.battle.applied_damage = game.battle.turn_pkmn.apply_damage(game, game.battle.damage)
            display_damage_text(game, game.battle.damage)
        case "turn_finish":
            game.battle.finish_turn(game)
        case _:
            print("Error selecting an ingame state")


def display_background(game):
    game.background.draw(game.screen, size=game.screen_size, image_path="media/ui-elements/MDPokemonBattle_Notextbox.png")

def display_battle_interface(game):
    game.life_text.draw(game.screen, f"{game.battle.trainer_current_hp}/{game.trainer.pokedex[0].life}", (200,50)) #TODO change "100" to "trainer.pokemon[0].max_life"
    game.life_text.draw(game.screen, f"{game.battle.enemy_current_hp}/{game.enemy.pokedex[0].life}", (500,50)) #TODO change "100" to "enemy.pokemon[0].max_life"

# To allow the player to choose an attack
def display_attack_choice(game):
    """Show the moov buttons and allow to choose an attack"""
    game.button_moov1.draw(game.screen, game.battle.turn_pkmn.moov[0].name) #game.trainer.pokedex[0].moov[0].name
    game.button_moov2.draw(game.screen, game.battle.turn_pkmn.moov[1].name) #game.trainer.pokedex[0].moov[1].name)

    game.background_button_moov.draw(game.screen, hitbox=game.button_moov1)
    game.background_button_moov.draw(game.screen, hitbox=game.button_moov2)
    
    game.text_button_moov.draw(game.screen, game.trainer.pokedex[0].moov[0].name, hitbox=game.button_moov1)    
    game.text_button_moov.draw(game.screen, game.trainer.pokedex[0].moov[1].name, hitbox=game.button_moov2)    
    
def display_attacking_text(game):
    #TODO text for attacking text (pokemon uses move)
    game.button_battle_message.draw(game.screen)
    game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
    game.text_battle_message.draw(game.screen, f"{game.battle.turn}'s {game.battle.turn_pkmn.name} uses {game.battle.chosen_moov.name}!!" ,hitbox=game.button_battle_message)
    
    game.battle.custom_wait(game, "mooving", 1000)

def display_moov_animation(game):
    #TODO placeholder/test for animation
    game.button_battle_message.draw(game.screen)
    game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
    game.text_battle_message.draw(game.screen, f"Moooving!" ,hitbox=game.button_battle_message)
   
    game.battle.custom_wait(game, "damage", 2000)
    
def display_damage_text(game, damage):
    #TODO placeholder for damage text
    game.button_battle_message.draw(game.screen)
    game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
    game.text_battle_message.draw(game.screen, f"{game.battle.turn}'s {game.battle.turn_pkmn.name} has inflicted {damage} damage to {game.battle.opponent_pkmn.name}!" ,hitbox=game.button_battle_message)
    
    game.battle.custom_wait(game, "turn_finish", 0)

def display_moov_missed_text(game):
    #TODO placeholder for miss text
    game.button_battle_message.draw(game.screen)
    game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
    game.text_battle_message.draw(game.screen, f"{game.battle.chosen_moov.name} has missed!!" ,hitbox=game.button_battle_message)
    
    game.battle.custom_wait(game, "turn_finish", 0)

def display_enemy_choosing_move(game):
    """Display a message to let AI play without interferences"""

    game.button_battle_message.draw(game.screen)
    game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
    game.text_battle_message.draw(game.screen, f"{game.battle.enemy_name} is picking a move!" ,hitbox=game.button_battle_message)
   
    if time.get_ticks() >= game.delay:
        game.delay = time.get_ticks() + 1500
        game.ingame_state = "attacking"
        game.battle.chosen_moov = game.battle.ia_choose_moov(game)

def display_battle_end(game):                
    #TODO Summary of battle, level up and evolution + pokemon give?
    if time.get_ticks() >= game.delay:
        game.game_state = "game_menu"

