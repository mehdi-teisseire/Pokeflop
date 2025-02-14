import pygame

from model.battle import Battle

def display_ingame(game):
    display_background(game)
    #display_pokemon()
    display_attack_choice(game)

def display_background(game):
    game.background.image_path = "media/ui-elements/MDPokemonBattle_Notextbox.png"
    game.background.draw(game)

# To allow the player to choose an attack
def display_attack_choice(game):
    game.background_button_moov.draw(game)

    game.button_moov1.draw(game.screen)
    game.button_moov2.draw(game.screen)

    game.text_button_moov1.draw(game, game.trainer.pokedex[0].moove1, game.background_button_moov)    
    game.text_button_moov2.draw(game, game.trainer.pokedex[0].moove2, game.background_button_moov)


    # game.button_moov2.draw(game.screen)