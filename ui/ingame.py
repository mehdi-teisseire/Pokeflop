import pygame

from model.battle import Battle

def display_ingame(game):
                
    display_background(game)
    #display_pokemon()
    display_attack_choice(game)

def display_background(game):
    game.background = pygame.image.load("media/ui-elements/MDPokemonBattle_Notextbox.png")
    game.background = pygame.transform.scale(game.background, (800, 450))
    
    game.screen.blit(game.background, (0, 0))

# To allow the player to choose an attack
def display_attack_choice(game):            

    game.button_moove1.draw(game)
    game.text_button_moove1.draw(game)


    # game.button_moov2.draw(game.screen)