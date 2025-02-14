import pygame

from model.battle import Battle
from model.pokemon import Pokemon
def display_ingame(game):
    display_background(game)
    display_attack_choice(game)

def display_background(game):
    game.background.image_path = "media/ui-elements/MDPokemonBattle_Notextbox.png"
    game.background.draw(game)

# To allow the player to choose an attack
def display_attack_choice(game):
    game.background_button_moov1.draw(game)
    game.background_button_moov2.draw(game)

    game.text_button_moov1.draw(game, game.trainer.pokedex[0].moov1, game.background_button_moov1)    
    game.text_button_moov2.draw(game, game.trainer.pokedex[0].moov2, game.background_button_moov2)

    game.button_moov1.draw(game.screen, game.background_button_moov1)
    game.button_moov2.draw(game.screen, game.background_button_moov2)

    # game.button_moov2.draw(game.screen)