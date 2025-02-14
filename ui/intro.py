import pygame
from ui.ui import UIElement

def display_intro(game):
    """Display The first screen of the game"""  

    game.background.draw(game)
    game.start_text_img.draw(game)
    game.button_intro.draw(game.screen, game.background) #Hitbox to click for next screen
    