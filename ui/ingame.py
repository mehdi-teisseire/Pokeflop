import pygame

from model.battle import Battle

def display_ingame(game):
                
    #displaybackground()
    #display_pokemon()
    display_attack_choice(game)


# To allow the player to choose an attack
def display_attack_choice(game):            
    game.screen.fill("white")

    game.button_moove1.label = game.trainer.pokedex[0].moove1 #Change button label to move name
    game.button_moove1.draw_label(game, 0, 0)

    # game.button_moov2.draw(game.screen)