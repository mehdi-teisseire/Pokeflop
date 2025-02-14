import pygame
from ui.ui import UIElement

def display_intro(game):
    """Display The first screen of the game"""  
    game.button_intro.draw(game.screen) #Hitbox to click for next screen

    game.background.draw(game)
    game.start_text_img.draw(game)

    