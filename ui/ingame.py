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
                game.battle.pokemon_missed = game.battle.turn_pkmn.has_missed(game.battle.chosen_moov)
                game.battle.miss_check = True
            if game.battle.pokemon_missed:
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
        case "pokemon_ko":
            display_end_results(game)
        case _:
            print("Error selecting an ingame state")


def display_background(game):
    game.background.draw(game.screen, size=game.screen_size, image_path="media/ui-elements/MDPokemonBattle_Notextbox.png")

def display_battle_interface(game):
    game.trainer_pokemon.draw(game.screen, (100, 250), (300,300), f"media/Pokemons-assets/back/{game.battle.trainer_pokemon.name}_back.png")
    game.enemy_pokemon.draw(game.screen, (750,170), (300,300), f"media/Pokemons-assets/front/{game.battle.enemy_pokemon.name}_front.png")

    game.ingame_text.draw(game.screen, f"{game.battle.trainer_pokemon.name}", (80,50)) 
    game.ingame_text.draw(game.screen, f"{game.battle.enemy_pokemon.name}", (850,50)) 
    
    game.ingame_text.draw(game.screen, f"{game.battle.trainer_pokemon.level}", (350,55)) 
    game.ingame_text.draw(game.screen, f"{game.battle.enemy_pokemon.level}", (750,50)) 

    game.ingame_text.draw(game.screen, f"{game.battle.trainer_current_hp}/{game.trainer.pokedex[0].life}", (50,85)) 
    game.ingame_text.draw(game.screen, f"{game.battle.enemy_current_hp}/{game.enemy.pokedex[0].life}", (800,70)) 

# To allow the player to choose an attack
def display_attack_choice(game):
    """Show the moov buttons and allow to choose an attack"""
    game.button_battle_message.draw(game.screen)
    game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)

    game.button_moov1.draw(game.screen, game.battle.turn_pkmn.moov[0].name) #game.trainer.pokedex[0].moov[0].name
    game.button_moov2.draw(game.screen, game.battle.turn_pkmn.moov[1].name) #game.trainer.pokedex[0].moov[1].name)

    game.background_button_moov.draw(game.screen, hitbox=game.button_moov1)
    game.background_button_moov.draw(game.screen, hitbox=game.button_moov2)
    
    game.text_button_moov.draw(game.screen, game.trainer.pokedex[0].moov[0].name, hitbox=game.button_moov1)    
    game.text_button_moov.draw(game.screen, game.trainer.pokedex[0].moov[1].name, hitbox=game.button_moov2)    
    
def display_attacking_text(game):
    game.button_battle_message.draw(game.screen)
    game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
    game.text_battle_message.draw(game.screen, f"{game.battle.turn}'s {game.battle.turn_pkmn.name} uses {game.battle.chosen_moov.name}!!" ,hitbox=game.button_battle_message)
    
    custom_wait(game, "mooving", 1000)

def display_moov_animation(game):
    #TODO placeholder/test for animation
    game.button_battle_message.draw(game.screen)
    game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
    game.text_battle_message.draw(game.screen, f"Moooving!" ,hitbox=game.button_battle_message)
   
    custom_wait(game, "damage", 2000)
    
def display_damage_text(game, damage):
    game.button_battle_message.draw(game.screen)
    game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
    game.text_battle_message.draw(game.screen, f"{game.battle.turn}'s {game.battle.turn_pkmn.name} has inflicted {damage} damage to {game.battle.opponent_pkmn.name}!" ,hitbox=game.button_battle_message)
    
    custom_wait(game, "turn_finish", 0)

def display_moov_missed_text(game):
    game.button_battle_message.draw(game.screen)
    game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
    game.text_battle_message.draw(game.screen, f"{game.battle.chosen_moov.name} has missed!!" ,hitbox=game.button_battle_message)
    
    custom_wait(game, "turn_finish", 0)

def display_enemy_choosing_move(game):
    """Display a message to let AI play without interferences"""

    game.button_battle_message.draw(game.screen)
    game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
    game.text_battle_message.draw(game.screen, f"{game.battle.enemy_name} is picking a move!" ,hitbox=game.button_battle_message)
   
    if time.get_ticks() >= game.delay:
        game.delay = time.get_ticks() + 1500
        game.ingame_state = "attacking"
        game.battle.chosen_moov = game.battle.ia_choose_moov(game)

def display_end_results(game):
    if not game.battle.won:
        game.button_battle_message.draw(game.screen)
        game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
        game.text_battle_message.draw(game.screen, f"Too bad, {game.battle.trainer_name}'s {game.battle.trainer_pokemon.name} had been defeated by {game.battle.enemy_name}'s {game.battle.enemy_pokemon.name}!!" ,hitbox=game.button_battle_message)
        
    else:
        game.button_battle_message.draw(game.screen)
        game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
        game.text_battle_message.draw(game.screen, f"Good job, {game.battle.trainer_name}'s {game.battle.trainer_pokemon.name} had defeated {game.battle.enemy_name}'s {game.battle.enemy_pokemon.name}!!" ,hitbox=game.button_battle_message)
        
    if time.get_ticks() >= game.delay:
        game.delay = time.get_ticks() + 5000
        if not game.battle.won:
            print(game.trainer.pokedex, game.enemy.pokedex)
            game.enemy.remove_pokemon()
            game.trainer.remove_pokemon(game.battle.opponent_pkmn)
            print(game.trainer.pokedex, game.enemy.pokedex)
        else:
            game.battle.gave_pokemon = game.enemy.give_pokemon(game.trainer)

        game.game_state = "battle_end"
        game.mixer.music.stop()
        game.mixer.music.load('media/audio/bgm_battle_end.mp3')
        game.mixer.music.play(-1)
        game.battle_start = False
        game.battle.ingame_state = "attacking"

def custom_wait(game, state, wait_time = 1000):
    if time.get_ticks() >= game.delay:
        game.delay = time.get_ticks() + wait_time
        game.ingame_state = state

def display_battle_end(game):    
    if game.battle.won:
        if game.battle.gave_pokemon:
            game.button_battle_message.draw(game.screen)
            game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
            game.text_battle_message.draw(game.screen, f"{game.battle.enemy_name} gave you a {game.battle.enemy_pokemon.name}!! So cool!" ,hitbox=game.button_battle_message)
            
   
        else:
            game.button_battle_message.draw(game.screen)
            game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
            game.text_battle_message.draw(game.screen, f"{game.battle.enemy_name} gave you a {game.battle.enemy_pokemon.name}!! Unfortunately, you already had one..." ,hitbox=game.button_battle_message)
   
    else:
        game.button_battle_message.draw(game.screen)
        game.background_battle_message.draw(game.screen, hitbox=game.button_battle_message)
        game.text_battle_message.draw(game.screen, f"{game.battle.trainer_name}'s {game.battle.enemy_pokemon.name} is dead forever..." ,hitbox=game.button_battle_message)
   
    if time.get_ticks() >= game.delay:
        game.trainer.pokedex[0].level_up()
        display_evolve(game)
        game.delay = time.get_ticks() + 5000
        game.save_json(game.trainer.pokedex, 'pokedex')
        game.mixer.music.stop()
        game.mixer.music.load('media/audio/bgm_menu.mp3')
        game.mixer.music.play(-1)
        game.game_state = "game_menu"

def display_evolve(game):
    if game.trainer.pokedex[0].level == 6 and not game.trainer.pokedex[0].name == "Charizard":
            game.trainer.pokedex[0].evolve("Charmeleon", "fire")
    elif game.trainer.pokedex[0].level == 7:
            game.trainer.pokedex[0].evolve("Charizard", "fire")