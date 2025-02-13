import pygame, sys
from ui.ButtonClass import Button 

from model.TrainerClass import Trainer
from model.EnemyTrainerClass import EnemyTrainer

def display_ingame(game):
    #displaybackground()
    #display_pokemon()
    display_attack_choice(game)


# To allow the player to choose an attack
def display_attack_choice(game):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if game.button_moov1.is_clicked(mouse_pos):
                return game.turn_pkmn.moov1
            elif game.button_moov2.is_clicked(mouse_pos):
                return game.turn_pkmn.moov2
            
    game.screen.fill("white")

    option_text = game.font.render(f"{game.POKEMON_TEMPLATE[0]["name"]}, choose your attack:", True, "blue") # Should be changed

    game.screen.blit(option_text, (100, 200))
    
    game.button_moov1.draw(game.screen)
    game.button_moov2.draw(game.screen)
    
    pygame.display.flip()