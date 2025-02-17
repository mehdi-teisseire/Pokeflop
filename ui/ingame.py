def display_ingame(game):
    display_background(game)
    display_battle_interface(game)
    if game.battle.mooving:
        display_attacking_text(game)
        if game.battle.moov_missed:
            display_moov_animation(game)
            display_damage_text(game)
        else:
            display_moov_missed_text(game)
    else:
        if game.battle.turn == game.enemy.name:
            display_enemy_choosing_move(game)
        else:
            display_attack_choice(game)

def display_background(game):
    game.background.image_path = "media/ui-elements/MDPokemonBattle_Notextbox.png"
    game.background.draw(game)

def display_battle_interface(game):
    game.life_trainer_text.draw(game, f"{game.trainer.pokedex[0].life} / 100") #TODO change "100" to "trainer.pokemon[0].max_life"
    game.life_opponent_text.draw(game, f"{game.enemy.pokedex[0].life} / 100") #TODO change "100" to "enemy.pokemon[0].max_life"

def display_enemy_choosing_move(game):
    """Display a message to let AI play without interferences"""
    display_attack_choice(game) #TODO placeholder for enemy message when acting 

# To allow the player to choose an attack
def display_attack_choice(game):
    """Show the moov buttons and allow to choose an attack"""
    game.background_button_moov1.draw(game)
    game.background_button_moov2.draw(game)

    game.text_button_moov1.draw(game, game.trainer.pokedex[0].moov1, game.background_button_moov1)    
    game.text_button_moov2.draw(game, game.trainer.pokedex[0].moov2, game.background_button_moov2)

    game.button_moov1.draw(game.screen, game.background_button_moov1)
    game.button_moov2.draw(game.screen, game.background_button_moov2)


def display_attacking_text(game):
    game.text_attacking()


def display_moov_animation(game):
    #TODO placeholder/test for animation
    print("Mooving!")
    from pygame.time import wait
    wait(1000)
    print("Finished mooving!")
    
def display_damage_text(game):
    #TODO placeholder 
    print(f"{game.battle.turn_pkmn.name} has inflicted {game.battle.moov_damage} damage to {game.battle.opponent_pkmn.name}!"
)

def display_moov_missed_text(game):
    print("UI: Show missed message!")
