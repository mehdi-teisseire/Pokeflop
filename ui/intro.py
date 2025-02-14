import pygame
from ui.ui import UIElement

def display_intro(game):
    game.background = pygame.image.load("media/ui-elements/background.png")
    game.background = pygame.transform.scale(game.background, (800, 450))

    game.img = pygame.image.load("media/ui-elements/Press-space-to-start-2-12-2025.png")
    game.img = pygame.transform.scale(game.img, (579,88 ))
    
    game.screen.blit(game.background, (0, 0))
    game.screen.blit(game.img, (120, 200))

    game.button_intro.draw(game.screen)
    